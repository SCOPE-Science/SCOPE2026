#!/usr/bin/env python3
"""Exact checks for rank-one isospectral updates over small prime fields.
No external dependencies.  Run with Python 3.9 or newer.
"""
from itertools import product, permutations
from fractions import Fraction


def poly_mul(a,b,p):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]=(c[i+j]+x*y)%p
    return c


def charpoly(M,p):
    n=len(M)
    ans=[0]*(n+1)
    for perm in permutations(range(n)):
        inv=sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n))
        term=[1]
        for i,j in enumerate(perm):
            term=poly_mul(term,[(-M[i][j])%p,1] if i==j else [(-M[i][j])%p],p)
        for j,x in enumerate(term): ans[j]=(ans[j]+(-1 if inv%2 else 1)*x)%p
    return tuple(ans)


def matvec(M,u,p):
    return tuple(sum(a*b for a,b in zip(row,u))%p for row in M)


def spanrank(cols,p):
    if not cols:return 0
    rows=[list(row) for row in zip(*cols)]
    rank=0
    for j in range(len(cols)):
        pivot=next((i for i in range(rank,len(rows)) if rows[i][j]%p),None)
        if pivot is None:continue
        rows[rank],rows[pivot]=rows[pivot],rows[rank]
        z=pow(rows[rank][j],-1,p)
        rows[rank]=[(x*z)%p for x in rows[rank]]
        for i in range(len(rows)):
            if i==rank:continue
            z=rows[i][j]
            rows[i]=[(x-z*y)%p for x,y in zip(rows[i],rows[rank])]
        rank+=1
    return rank


def krylov_degree(A,u,p):
    n=len(A)
    cols=[]
    for i in range(n):
        cols.append(u)
        u=matvec(A,u,p)
    return spanrank(cols,p)


def all_mats(p,n):
    for v in product(range(p),repeat=n*n):yield [v[i*n:(i+1)*n] for i in range(n)]


def direct_count(A,p):
    n=len(A)
    old=charpoly(A,p)
    vecs=list(product(range(p),repeat=n))
    count=0
    for u in vecs:
        for v in vecs:
            mat=[[(A[i][j]+u[i]*v[j])%p for j in range(n)] for i in range(n)]
            count += (charpoly(mat,p)==old)
    return count


def krylov_count(A,p):
    n=len(A)
    return sum(p**(n-krylov_degree(A,u,p)) for u in product(range(p),repeat=n))


def type_count(p,types):
    # types is ((irreducible polynomial degree, partition of primary multiplicity),...)
    n=sum(deg*sum(part) for deg,part in types)
    s=Fraction(1,1)
    for deg,part in types:
        L=max(part)
        ke=lambda e: p**(deg*sum(min(e,z) for z in part)) if e>=0 else 0
        s*=Fraction(sum((ke(e)-ke(e-1))*p**(deg*(L-e)) for e in range(L+1)),p**(deg*L))
    value=p**n*s
    assert value.denominator==1
    return int(value)


def jordan(parts,p,lam=0):
    n=sum(parts)
    A=[[0]*n for _ in range(n)]
    s=0
    for l in parts:
        for i in range(l):
            A[s+i][s+i]=lam%p
            if i+1<l:A[s+i][s+i+1]=1
        s+=l
    return A


def blockdiag(A,B):
    n,m=len(A),len(B)
    return [row+[0]*m for row in A]+[[0]*n+row for row in B]


def companion(coeff,p):
    # monic polynomial coeff from constant to leading, companion columns
    n=len(coeff)-1
    A=[[0]*n for _ in range(n)]
    for j in range(n-1):A[j+1][j]=1
    for j in range(n):A[j][n-1]=(-coeff[j])%p
    return A


def partitions(n,mx=None):
    if not n:
        yield ()
        return
    if mx is None:mx=n
    for j in range(min(n,mx),0,-1):
        for tail in partitions(n-j,j):yield (j,)+tail


def dominates(a,b):
    return all(sum(a[:j])>=sum(b[:j]) for j in range(1,max(len(a),len(b))+1))



def poly_divmod(a,b,p):
    a=list(a)
    while len(a)>1 and a[-1]==0:a.pop()
    while len(a)>=len(b) and any(a):
        c=a[-1]*pow(b[-1],-1,p)%p
        shift=len(a)-len(b)
        for i in range(len(b)):a[shift+i]=(a[shift+i]-c*b[i])%p
        while len(a)>1 and a[-1]==0:a.pop()
    return tuple(a)


def poly_pow(f,e,p):
    out=[1]
    for _ in range(e):out=poly_mul(out,f,p)
    return out


def type_fiber_count(p,factors,target):
    """For a prescribed monic target characteristic polynomial.
    factors is a sequence (monic irreducible polynomial coefficient list, partition).
    """
    chi=[1]
    n=0
    for f,part in factors:
        n+= (len(f)-1)*sum(part)
        chi=poly_mul(chi,poly_pow(f,sum(part),p),p)
    assert len(target)==n+1 and target[-1]==1
    h=tuple((a-b)%p for a,b in zip(chi,target))
    iszero=not any(h)
    total=Fraction(p**n,1)
    for f,part in factors:
        deg=len(f)-1
        M=sum(part)
        nu=M if iszero else 0
        if not iszero:
            x=h
            while nu<M and any(x):
                rem=poly_divmod(x,f,p)
                if any(rem):break
                # polynomial quotient: exact monic division
                quotient=[0]*(len(x)-len(f)+1)
                xx=list(x)
                while len(xx)>=len(f) and any(xx):
                    lead=xx[-1]*pow(f[-1],-1,p)%p
                    sh=len(xx)-len(f)
                    quotient[sh]=lead
                    for j,fc in enumerate(f):xx[sh+j]=(xx[sh+j]-lead*fc)%p
                    while len(xx)>1 and xx[-1]==0:xx.pop()
                x=tuple(quotient)
                nu+=1
        r=max(0,M-nu)
        L=max(part)
        if r>L:return 0
        k=lambda e:p**(deg*sum(min(e,t) for t in part)) if e>=0 else 0
        total*=sum(Fraction(k(e)-k(e-1),p**(deg*e)) for e in range(r,L+1))
    assert total.denominator==1,(p,factors,target,total)
    return int(total)


def direct_hist(A,p):
    n=len(A)
    vecs=list(product(range(p),repeat=n))
    hist={}
    for u in vecs:
        for v in vecs:
            mat=[[(A[i][j]+u[i]*v[j])%p for j in range(n)] for i in range(n)]
            k=charpoly(mat,p)
            hist[k]=hist.get(k,0)+1
    return hist


def targeted_fiber_tests():
    cases=[
        ('scalar2',3,jordan((1,1),3),(((0,1),(1,1)),)),
        ('jordan2',3,jordan((2,),3),(((0,1),(2,)),)),
        ('jordan3',2,jordan((3,),2),(((0,1),(3,)),)),
        ('jordan21',2,jordan((2,1),2),(((0,1),(2,1)),)),
        ('scalar3',2,jordan((1,1,1),2),(((0,1),(1,1,1)),)),
        ('distinct2',3,[[0,0],[0,1]],(((0,1),(1,)),((2,1),(1,)))),
        ('irred2',3,companion((1,0,1),3),(((1,0,1),(1,)),)),
        ('irred3',2,companion((1,1,0,1),2),(((1,1,0,1),(1,)),)),
        ('mixed3',2,blockdiag([[0]],companion((1,1,1),2)),(((0,1),(1,)),((1,1,1),(1,)))),
        ('twoquad',2,blockdiag(companion((1,1,1),2),companion((1,1,1),2)),(((1,1,1),(1,1)),)),
    ]
    count=0
    for name,p,A,fac in cases:
        h=direct_hist(A,p)
        n=len(A)
        for coeff in product(range(p),repeat=n):
            target=coeff+(1,)
            t=type_fiber_count(p,fac,target)
            assert t==h.get(target,0),(name,target,t,h.get(target,0))
            count+=1
        assert sum(h.values())==p**(2*n)
        print(f'TARGET_FIBERS_PASS name={name} q={p} n={n} targets={p**n} nonempty={len(h)}')
    print(f'ALL_TARGET_FIBERS_PASS targets={count}')

def main():
    runs=[(2,2,None),(3,2,None),(2,3,None),(3,3,45),(2,4,16)]
    for p,n,max_matrices in runs:
        checked=0
        for A in all_mats(p,n):
            # For large ambient sets, use evenly spaced reproducible samples.
            flat=[x for row in A for x in row]
            code=sum(x*p**i for i,x in enumerate(flat))
            total=p**(n*n)
            if max_matrices is not None and code not in {((i*total)//max_matrices) for i in range(max_matrices)}:continue
            c=direct_count(A,p)
            k=krylov_count(A,p)
            assert c==k,(p,n,A,c,k)
            assert (c-2*p**n+1)%(p-1)==0
            checked+=1
        print(f'DIRECT_CHARPOLY_KRYLOV_PASS p={p} n={n} matrices={checked}')
    examples=[
        ('scalar2',3,jordan((1,1),3,0),((1,(1,1)),)),
        ('nilpotent2',3,jordan((2,),3,0),((1,(2,)),)),
        ('nilpotent3',2,jordan((3,),2,0),((1,(3,)),)),
        ('split21',2,jordan((2,1),2,0),((1,(2,1)),)),
        ('scalar3',2,jordan((1,1,1),2,0),((1,(1,1,1)),)),
        ('distinct2',3,[[0,0],[0,1]],((1,(1,)),(1,(1,)))),
        ('irreducible2',3,companion((1,0,1),3),((2,(1,)),)),
        ('irreducible3',2,companion((1,1,0,1),2),((3,(1,)),)),
        ('mixed3',2,blockdiag([[0]],companion((1,1,1),2)),((1,(1,)),(2,(1,)))),
        ('two_quad_blocks',2,blockdiag(companion((1,1,1),2),companion((1,1,1),2)),((2,(1,1)),)),
    ]
    for name,p,A,typ in examples:
        t=type_count(p,typ)
        k=krylov_count(A,p)
        assert k==t,(name,t,k)
        if len(A)<=3:assert direct_count(A,p)==t
        print(f'PRIMARY_TYPE_PASS name={name} p={p} n={len(A)} pairs={t} rank_one_updates={(t-2*p**len(A)+1)//(p-1)}')
    comps=0
    for p in (2,3,5):
        for m in range(2,8):
            ps=list(partitions(m))
            for a in ps:
                for b in ps:
                    if dominates(a,b):
                        x,y=type_count(p,((1,a),)),type_count(p,((1,b),))
                        assert x<=y and (x<y if a!=b else x==y),(p,a,b,x,y)
                        comps+=1
    print(f'DOMINANCE_STRICT_PASS comparisons={comps}')
    print('ALL_ISOSPECTRAL_TESTS_PASS')
    targeted_fiber_tests()
    print('ALL_RANK_ONE_SPECTRAL_FIBER_CHECKS_PASS')

if __name__=='__main__':main()

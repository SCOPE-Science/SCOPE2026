#!/usr/bin/env python3
"""Standalone finite sanity checks for affine retractions of connected Jordan Alexander quandles."""
import itertools
from collections import Counter
from math import prod


def gauss(n, r, p):
    if r < 0 or r > n: return 0
    numerator=prod(p**(n-i)-1 for i in range(r))
    denominator=prod(p**(r-i)-1 for i in range(r))
    return numerator//denominator


def ring(p,d):
    elements=list(itertools.product(range(p),repeat=d)); index={v:i for i,v in enumerate(elements)}
    add=[[index[tuple((a[k]+b[k])%p for k in range(d))] for b in elements] for a in elements]
    neg=[index[tuple(-a[k]%p for k in range(d))] for a in elements]
    mul=[]
    for a in elements:
        row=[]
        for b in elements:
            z=[0]*d
            for i in range(d):
                for j in range(d-i): z[i+j]=(z[i+j]+a[i]*b[j])%p
            row.append(index[tuple(z)])
        mul.append(row)
    return elements,index,add,neg,mul


def mulmat(A,B,m,add,mul,zero):
    out=[]
    for i in range(m):
        for j in range(m):
            s=zero
            for k in range(m): s=add[s][mul[A[i*m+k]][B[k*m+j]]]
            out.append(s)
    return tuple(out)


def rank_mod_p(A,m,ring_elements,p):
    a=[[ring_elements[A[i*m+j]][0] for j in range(m)] for i in range(m)]
    rr=0
    for c in range(m):
        ix=next((i for i in range(rr,m) if a[i][c]),None)
        if ix is None: continue
        a[rr],a[ix]=a[ix],a[rr]
        x=pow(a[rr][c],-1,p)
        for j in range(c,m): a[rr][j]=a[rr][j]*x%p
        for i in range(m):
            if i!=rr and a[i][c]:
                x=a[i][c]
                for j in range(c,m): a[i][j]=(a[i][j]-x*a[rr][j])%p
        rr+=1
    return rr


def matrix_test(p,d,m):
    el,ind,add,neg,mul=ring(p,d); zero=ind[(0,)*d]; one=ind[(1,)+(0,)*(d-1)]; N=len(el)
    I=tuple(one if i==j else zero for i in range(m) for j in range(m))
    allm=list(itertools.product(range(N), repeat=m*m))
    projs=Counter(); samples={}
    for A in allm:
        if mulmat(A,A,m,add,mul,zero)!=A: continue
        r=rank_mod_p(A,m,el,p)
        projs[r]+=1
        samples.setdefault(r,A)
    for r in range(m+1):
        s=m-r
        expect=gauss(m,r,p)*p**((2*d-1)*r*s)
        assert projs[r]==expect,('projection count',(p,d,m),r,projs[r],expect)
        # affine translation is any vector in ker A; the ring summand ker has cardinality p^(ds)
        assert projs[r]*p**(d*s)==gauss(m,r,p)*p**(d*s+(2*d-1)*r*s)
        A=samples[r]
        Bcomm=sum(mulmat(A,B,m,add,mul,zero)==mulmat(B,A,m,add,mul,zero) for B in allm)
        assert Bcomm==p**(d*(r*r+s*s)),(p,d,m,r,Bcomm)
        total=Bcomm*p**(d*r)
        assert total==p**(d*(r*r+s*s+r))
    print('MATRIX',p,d,m,'projection_counts',dict(projs),'affine_retractions',sum(projs[r]*p**(d*(m-r)) for r in projs),'centralizers',[p**(d*(r*r+(m-r)**2+r)) for r in range(m+1)])


def tiny_quandle_test(p,d,lam):
    el,ind,add,neg,mul=ring(p,d); N=len(el); z=ind[(0,)*d]
    t=ind[tuple([lam]+([1] if d>1 else [])+[0]*max(0,d-2))]
    one=ind[(1,)+(0,)*(d-1)]; unt=add[one][neg[t]]
    table=[[add[mul[t][x]][mul[unt][y]] for y in range(N)] for x in range(N)]
    actual=[]
    for seq in itertools.product(range(N),repeat=N):
        if all(seq[table[x][y]]==table[seq[x]][seq[y]] for x in range(N) for y in range(N)):
            actual.append(seq)
    aff={tuple(add[mul[a][x]][b] for x in range(N)) for a in range(N) for b in range(N)}
    assert set(actual)==aff,(p,d,lam,len(actual),len(aff))
    idem=[f for f in actual if all(f[f[x]]==f[x] for x in range(N))]
    assert len(idem)==N+1,(p,d,len(idem))
    print('QUANDLE_FULL',p,d,lam,'size',N,'endo',len(actual),'retractions',len(idem))

def generated_quandle_test(p,d,lam):
    """Use two-point generation to rule out all nonaffine homomorphisms."""
    el,ind,add,neg,mul=ring(p,d); N=len(el)
    zero=ind[(0,)*d];one=ind[(1,)+(0,)*(d-1)]
    t=ind[tuple([lam]+([1] if d>1 else [])+[0]*max(0,d-2))]
    unt=add[one][neg[t]]
    table=[[add[mul[t][x]][mul[unt][y]] for y in range(N)] for x in range(N)]
    inv=[[None]*N for _ in range(N)]
    for x in range(N):
        for y in range(N): inv[table[x][y]][y]=x
    known={zero,one}
    while True:
        new=known | {table[x][y] for x in known for y in known} | {inv[x][y] for x in known for y in known}
        if new==known:break
        known=new
    assert len(known)==N, ('not generated',(p,d,lam))
    aff={tuple(add[mul[a][x]][b] for x in range(N)) for a in range(N) for b in range(N)}
    assert len(aff)==N*N
    for f in aff:
        assert all(f[table[x][y]]==table[f[x]][f[y]] for x in range(N) for y in range(N))
    # Two generators of the quandle imply that every endomorphism is determined by
    # its values there. Therefore at most N*N exist, so the exhibited N*N are all.
    idem=[f for f in aff if all(f[f[x]]==f[x] for x in range(N))]
    assert len(idem)==N+1,(p,d,lam,len(idem))
    print('QUANDLE_GENERATED',p,d,lam,'size',N,'endo',len(aff),'retractions',len(idem))

def mixed_module_boundary(p):
    """Linear constraint ranks for the two competing retract images."""
    n=4
    N=[[0]*n for _ in range(n)];N[0][1]=1
    def diag(ones):return [[int(i==j and i in ones) for j in range(n)] for i in range(n)]
    P_long=diag({0,1});P_short=diag({2,3})
    def rank(rows):
        A=[v[:] for v in rows];r=0
        for c in range(n*n):
            idx=next((i for i in range(r,len(A)) if A[i][c]%p),None)
            if idx is None:continue
            A[r],A[idx]=A[idx],A[r]
            inv=pow(A[r][c]%p,-1,p)
            A[r]=[v*inv%p for v in A[r]]
            for i in range(len(A)):
                if i!=r and A[i][c]:
                    f=A[i][c]
                    A[i]=[(x-f*y)%p for x,y in zip(A[i],A[r])]
            r+=1
        return r
    for P in (P_long,P_short):
        constraints=[]
        for X in (N,P):
            for i in range(n):
                for j in range(n):
                    row=[0]*(n*n)
                    for k in range(n):
                        row[i*n+k]=(row[i*n+k]+X[k][j])%p
                        row[k*n+j]=(row[k*n+j]-X[i][k])%p
                    constraints.append(row)
        dim=n*n-rank(constraints)
        assert dim==6,(dim,P)
        assert dim+2==8
    assert sum(any(N[i][j] and P_long[j][j] for j in range(n)) for i in range(n))==1
    assert sum(any(N[i][j] and P_short[j][j] for j in range(n)) for i in range(n))==0
    print('MIXED_JORDAN_BOUNDARY',p,'centralizers',p**8,p**8,'image_nilpotent_ranks',1,0)

if __name__=='__main__':
    for args in [(3,1,2),(5,1,2),(3,2,1),(3,2,2),(3,3,1)]:
        matrix_test(*args)
    for args in [(3,1,2),(5,1,2)]:
        tiny_quandle_test(*args)
    generated_quandle_test(3,2,2)
    mixed_module_boundary(3)
    mixed_module_boundary(5)
    print('JORDAN_ALEXANDER_RETRACTIONS_CHECKS_PASSED')

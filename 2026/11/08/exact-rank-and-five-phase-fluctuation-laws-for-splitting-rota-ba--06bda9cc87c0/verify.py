"""Independent finite checks for idempotent weight-minus-one Lie Rota--Baxter rank enumeration.
Run: python verify.py (standard library only).
"""
from itertools import combinations, product
from collections import Counter
from fractions import Fraction


def gaussian(n,k,q):
    if k<0 or k>n: return 0
    # exact integer as rational product
    f=Fraction(1)
    for i in range(k): f*=Fraction(q**(n-i)-1,q**(k-i)-1)
    assert f.denominator==1
    return f.numerator

def predicted(n,q):
    d=2*n+1
    out=[0]*(d+1)
    for s in range(n+1):
        isotropic=gaussian(n,s,q)
        for k in range(s): isotropic*=q**(n-k)+1
        ways=isotropic*q**(s*(2*n-s+1))
        out[s]=ways
        out[d-s]=ways
    return out


def canonical_spaces(d,q):
    """All q-subspaces via unique RREF pivot matrices; basis vectors are tuples."""
    for r in range(d+1):
        for piv in combinations(range(d),r):
            free=[(i,j) for i in range(r) for j in range(piv[i]+1,d) if j not in piv]
            for coeffs in product(range(q),repeat=len(free)):
                rows=[[0]*d for _ in range(r)]
                for i,j in enumerate(piv):rows[i][j]=1
                for (i,j),v in zip(free,coeffs): rows[i][j]=v
                vecs={tuple(sum(a*rows[i][j] for i,a in enumerate(ab))%q for j in range(d)) for ab in product(range(q),repeat=r)}
                assert len(vecs)==q**r
                yield r,rows,frozenset(vecs)


def symp(u,v,n,q):
    return sum(u[i]*v[n+i]-u[n+i]*v[i] for i in range(n))%q


def subalgebra(rows,vecs,n,q):
    d=2*n+1
    z=tuple([0]*(d-1)+[1])
    if z in vecs:return True
    return all(symp(u,v,n,q)==0 for u in rows for v in rows)


def count_complementary_subalgebras(n,q):
    d=2*n+1
    spaces=[(r,vecs) for r,rows,vecs in canonical_spaces(d,q) if subalgebra(rows,vecs,n,q)]
    zero=tuple([0]*d)
    ranks=Counter()
    for r,b in spaces:
        for s,c in spaces:
            if r+s==d and b.isdisjoint(c-{zero}):
                ranks[r]+=1
    return [ranks[i] for i in range(d+1)]


def mvec(A,u,q):
    return tuple(sum(A[i][j]*u[j] for j in range(len(u)))%q for i in range(len(u)))

def direct_matrix_count(q):
    d=3
    basis=[tuple(int(i==j) for i in range(d)) for j in range(d)]
    ranks=Counter()
    # With column-major basis matrix listing
    for a in product(range(q),repeat=9):
        cols=[a[3*j:3*j+3] for j in range(d)]
        P=[[cols[j][i] for j in range(d)] for i in range(d)]
        if any(mvec(P,mvec(P,u,q),q)!=mvec(P,u,q) for u in basis):continue
        def bracket(u,v):return (0,0,(u[0]*v[1]-u[1]*v[0])%q)
        good=True
        for u,v in combinations(basis,2):
            pu,pv=mvec(P,u,q),mvec(P,v,q)
            lhs=bracket(pu,pv)
            t1,t2,t3=bracket(pu,v),bracket(u,pv),bracket(u,v)
            rhs=mvec(P,tuple((t1[i]+t2[i]-t3[i])%q for i in range(d)),q)
            if lhs!=rhs:good=False;break
        if good:
            # rank via row-reduction
            M=[list(row) for row in P];rank=0
            for c in range(d):
                pi=next((r for r in range(rank,d) if M[r][c]),None)
                if pi is None:continue
                M[rank],M[pi]=M[pi],M[rank]
                inv=pow(M[rank][c],-1,q)
                M[rank]=[v*inv%q for v in M[rank]]
                for r in range(d):
                    if r!=rank and M[r][c]:
                        t=M[r][c];M[r]=[(x-t*y)%q for x,y in zip(M[r],M[rank])]
                rank+=1
            ranks[rank]+=1
    return [ranks[i] for i in range(d+1)]


def check_asymptotic():
    from math import exp,log
    # Show five subsequential discrete-Gaussian laws from exact counts.
    for t in range(5):
        n=5*12+t;q=2
        pred=predicted(n,q)
        # use exact integer ratios scaled by max to avoid overflow
        E=lambda j: ((8*t+3)*j-5*j*j)//2
        js=range(-30,31)
        weights=[q**E(j) if E(j)>=0 else 1/q**(-E(j)) for j in js]
        sm=sum(weights);lim={j:w/sm for j,w in zip(js,weights)}
        den=sum(pred[:n+1]);err=0
        for j in js:
            s=4*12+j
            err+=abs((pred[s]/den if 0<=s<=n else 0)-lim[j])
        assert err<1e-5,(t,err)
    print('five residue-class discrete-Gaussian checks: PASS')

def main():
    for n,q in [(1,2),(1,3),(2,2)]:
        expected=predicted(n,q)
        actual=count_complementary_subalgebras(n,q)
        assert actual==expected,(n,q,actual,expected)
        print('subalgebra decomposition',n,q,actual,'PASS')
    for q in [2,3]:
        actual=direct_matrix_count(q)
        expected=predicted(1,q)
        assert actual==expected,(q,actual,expected)
        print('direct idempotent Rota-Baxter matrices',q,actual,'PASS')
    check_asymptotic()
    print('VERIFY_OK')

if __name__=='__main__':main()

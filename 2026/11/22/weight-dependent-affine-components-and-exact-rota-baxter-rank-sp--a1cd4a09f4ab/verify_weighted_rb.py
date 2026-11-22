"""Exact enumeration of the weight-dependent Rota--Baxter operator locus on L_n.

The bracket is [v,u]=u, with basis (u,v,w_1,...,w_{n-2}).
Counts and rank distributions are compared independently against an explicit
finite union of affine subspaces and formulas for rectangular matrix ranks.
"""
from itertools import product
from collections import Counter
from math import prod


def matrank(A,q):
    a=[list(row) for row in A]; m=len(a); n=len(a[0]); r=0
    for j in range(n):
        i=next((t for t in range(r,m) if a[t][j]%q),None)
        if i is None: continue
        a[r],a[i]=a[i],a[r]; h=pow(a[r][j],-1,q)
        a[r]=[v*h%q for v in a[r]]
        for k in range(m):
            if k!=r and a[k][j]:
                z=a[k][j];a[k]=[(x-z*y)%q for x,y in zip(a[k],a[r])]
        r+=1
        if r==m:break
    return r

def valid(R,n,q,lam):
    for i in range(n):
        for j in range(n):
            lhs=R[1][i]*R[0][j]
            inner=R[1][i]*(j==0)+(i==1)*R[0][j]+lam*(i==1)*(j==0)
            for t in range(n):
                if ( (lhs if t==0 else 0)-inner*R[t][0])%q: return False
    return True

def classifier(R,n,q,lam):
    zero_u=all(R[i][0]==0 for i in range(n))
    neg_u=(R[0][0]+lam)%q==0 and all(R[i][0]==0 for i in range(1,n))
    a0=all(R[1][j]==0 for j in range(n))
    b0=all(R[0][j]==0 for j in range(n))
    aneg=all((R[1][j]+lam*(j==1))%q==0 for j in range(n))
    bneg=all((R[0][j]+lam*(j==0))%q==0 for j in range(n))
    if not lam:
        return (a0 and b0) or (zero_u and (a0 or b0))
    return (zero_u and (a0 or b0)) or (a0 and bneg) or (b0 and aneg) or (neg_u and (aneg or bneg))

def gauss(m,r,q):
    if r<0 or r>m:return 0
    return prod(q**(m-j)-1 for j in range(r))//prod(q**(r-j)-1 for j in range(r))

def rect(m,n,r,q):
    if r<0 or r>min(m,n):return 0
    return gauss(m,r,q)*prod(q**n-q**j for j in range(r))

def formulas(n,q,lam):
    f=lambda m,n,r:rect(m,n,r,q)
    if not lam:
        return [f(n-2,n,r)+2*f(n-1,n-1,r)-2*f(n-2,n-1,r) for r in range(n+1)]
    return [2*f(n-1,n-1,r)+2*q**(n-2)*f(n-2,n-1,r-1)
            +q**(2*n-3)*f(n-2,n-2,r-2)+f(n-1,n-1,r-1)
            -f(n-2,n-1,r)-q**(n-2)*f(n-2,n-2,r-1)
            -q**(n-2)*f(n-2,n-2,r-2)-f(n-2,n-1,r-1)
            for r in range(n+1)]

def check(n,q,lam):
    counts=Counter()
    for E in product(range(q),repeat=n*n):
        R=[E[i*n:(i+1)*n] for i in range(n)]
        v=valid(R,n,q,lam); u=classifier(R,n,q,lam)
        if v!=u:raise AssertionError((n,q,lam,R,v,u))
        if v:counts[matrank(R,q)]+=1
    v=[counts[r] for r in range(n+1)]
    theo=formulas(n,q,lam)
    if v!=theo:raise AssertionError((n,q,lam,v,theo))
    expected=q**(n*(n-2))+2*q**((n-1)**2)-2*q**((n-1)*(n-2))
    assert sum(v)==(2 if lam else 1)*expected
    print('n=%s q=%s weight=%s rank_counts=%s total=%s'%(n,q,lam,v,sum(v)))

if __name__=='__main__':
    for n,q,ls in [(2,2,[0,1]),(2,3,[0,1,2]),(2,5,[0,1,2,3,4]),(3,2,[0,1]),(3,3,[0,1,2]),(4,2,[0,1])]:
        for lam in ls:check(n,q,lam)
    print('WEIGHTED_LEIBNIZ_RB_CENSUS_VERIFIED')

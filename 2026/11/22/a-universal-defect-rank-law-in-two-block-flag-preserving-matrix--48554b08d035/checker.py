#!/usr/bin/env python3
"""Independent finite checks for two-step flag-preserving matrix monoid defect counts."""
from itertools import product
from collections import Counter
from math import prod

def rank(M,p):
    if not M: return 0
    A=[list(map(lambda x:x%p,row)) for row in M]
    m=len(A); n=len(A[0]); k=0
    for c in range(n):
        j=next((i for i in range(k,m) if A[i][c]),None)
        if j is None: continue
        A[k],A[j]=A[j],A[k]
        inv=pow(A[k][c],-1,p)
        A[k]=[(v*inv)%p for v in A[k]]
        for i in range(k+1,m):
            f=A[i][c]
            if f:A[i]=[(a-f*b)%p for a,b in zip(A[i],A[k])]
        k+=1
        if k==m:break
    return k

def gaussian(n,r,p):
    if r<0 or r>n:return 0
    top=prod(p**(n-j)-1 for j in range(r))
    bot=prod(p**(r-j)-1 for j in range(r))
    return top//bot

def nrect(a,b,r,p):
    if r<0 or r>min(a,b):return 0
    return gaussian(a,r,p)*gaussian(b,r,p)*prod(p**r-p**j for j in range(r))

def count(a,b,p,r,s,t):
    i=a-r;j=b-s
    return nrect(a,a,r,p)*nrect(b,b,s,p)*p**(a*b-i*j)*nrect(i,j,t,p)

def matrices(a,b,p):
    n=a+b
    positions=[(i,j) for i in range(n) for j in range(n) if not (i>=a and j<a)]
    for values in product(range(p),repeat=len(positions)):
        M=[[0]*n for _ in range(n)]
        for (i,j),v in zip(positions,values):M[i][j]=v
        yield M

def matmul(M,N,p):
    m=len(M)
    return [[sum(M[i][k]*N[k][j] for k in range(m))%p for j in range(m)] for i in range(m)]

def test(a,b,p):
    obs=Counter()
    all_m=list(matrices(a,b,p))
    for X in all_m:
        r=rank([row[:a] for row in X[:a]],p)
        s=rank([row[a:] for row in X[a:]],p)
        t=rank(X,p)-r-s
        assert 0<=t<=min(a-r,b-s)
        obs[r,s,t]+=1
    expected=Counter({(r,s,t):count(a,b,p,r,s,t) for r in range(a+1) for s in range(b+1) for t in range(min(a-r,b-s)+1)})
    assert obs==expected,(a,b,p,obs-expected,expected-obs)
    assert sum(expected.values())==p**(a*a+a*b+b*b)
    if a==b==1:
        for X in all_m:
            r=rank([row[:a] for row in X[:a]],p)
            s=rank([row[a:] for row in X[a:]],p)
            t=rank(X,p)-r-s
            regular=any(matmul(matmul(X,Y,p),X,p)==X for Y in all_m)
            assert regular == (t==0), (p,X,regular,t)
    print('PASS',p,a,b,'total',len(all_m),'defect_distribution',dict(sorted(Counter({t:sum(v for (r,s,k),v in obs.items() if k==t) for t in range(min(a,b)+1)}).items())))

if __name__=='__main__':
    for p,a,b in [(2,1,1),(3,1,1),(5,1,1),(2,1,2),(2,2,1),(3,1,2),(2,2,2)]:test(a,b,p)

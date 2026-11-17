#!/usr/bin/env python3
"""Standalone finite checks for the star cost-sensitive spectral design formula.
Run with Python 3; uses fractions plus NumPy (only for floating cross-checks).
The all-parameter proof is in RESULT.md; finite checks are not its replacement.
"""
from fractions import Fraction as F
from itertools import combinations,product
import math
import numpy as np

def det(M):
    n=len(M)
    if n==0:return F(1)
    A=[list(map(F,row)) for row in M]
    ans=F(1)
    for j in range(n):
        pivot=next((k for k in range(j,n) if A[k][j]),None)
        if pivot is None:return F(0)
        if pivot!=j: A[j],A[pivot]=A[pivot],A[j];ans=-ans
        q=A[j][j];ans*=q
        for k in range(j+1,n):
            v=A[k][j]/q
            for l in range(j+1,n):A[k][l]-=v*A[j][l]
            A[k][j]=F(0)
    return ans

def design(s):
    m=len(s); assert m>=2 and all(x>0 for x in s)
    n=m+1; C=sum(x*x for x in s)
    mx=max(s);delta=max(0,2*mx-sum(s));v=[F(1)]*m
    if delta:
        i=s.index(mx)
        for j in range(m):
            v[j]+= F(-delta if j==i else delta,n*s[j])
    Cstar=F(C)-F(delta*delta,n)
    assert sum(F(s[j]*s[j])*v[j] for j in range(m))==Cstar
    return v,Cstar,delta

def lap(w):
    m=len(w); n=m+1;L=[[F(0) for _ in range(n)] for _ in range(n)]
    for j,x in enumerate(w):
        L[0][0]+=x;L[j+1][j+1]+=x;L[0][j+1]-=x;L[j+1][0]-=x
    return L

def check_one(s):
    m=len(s); n=m+1
    v,C,delta=design(s)
    assert C>0 and all(x>0 for x in v)
    M=[[v[i]-1 if i==j else F(0) for j in range(m)] for i in range(m)]
    for i in range(m):
        for j in range(m):M[i][j]+=F(1,n)
    # all principal minors exactly nonnegative; singularity proves min Rayleigh quotient exactly one
    for k in range(1,m+1):
        for subset in combinations(range(m),k):
            assert det([[M[i][j] for j in subset] for i in subset])>=0,(s,subset)
    assert det(M)==0,(s,'singularity')
    L=np.asarray(lap(v),dtype=float)
    eig=np.linalg.eigvalsh(L)
    assert abs(eig[1]-1)<2e-9,(s,eig)
    # verify the projector expectation formula and normalization
    p=np.array([float(x) for x in v]);p=p/p.sum()
    proj=np.zeros((n,n))
    for j,pi in enumerate(p):
        a=np.zeros(n);a[0]=1;a[j+1]=-1
        proj+=pi*np.outer(a,a)/2
    assert np.max(np.abs(proj-np.asarray(lap([F.from_float(float(x)) for x in p]),dtype=float)/2))<1e-13
    eta=np.linalg.eigvalsh(proj)[1]/sum(s[j]*s[j]*p[j] for j in range(m))
    assert abs(eta-1/(2*float(C)))<1e-9,(s,eta,C)
    return True

def random_comparison(s,rng,k=100):
    m=len(s);v,C,_=design(s)
    etaopt=1/(2*float(C))
    for _ in range(k):
        p=rng.dirichlet(np.ones(m)*rng.choice([0.4,1,3]))
        eig=np.linalg.eigvalsh(np.asarray(lap(list(map(float,p))),dtype=float))
        ratio=eig[1]/(2*sum((s[j]**2)*p[j] for j in range(m)))
        assert ratio <= etaopt+1e-10,(s,ratio,etaopt)
    return k

def main():
    ncases=0;minors=0;comparisons=0
    rng=np.random.default_rng(27418)
    for m in range(2,6):
        for s in product(range(1,5),repeat=m):
            check_one(s);ncases+=1;minors+=(2**m-1)
            comparisons+=random_comparison(s,rng,8)
    for s in ((3,1,1),(2,1,1),(4,1,1),(8,2,1,1,1),(7,3,2,1),(1,1,1,1),(10,1,1,1,1,1)):
        check_one(s);ncases+=1;minors+=2**len(s)-1
        comparisons+=random_comparison(s,rng,300)
    print(f'VERIFY_OK exact_design_cases={ncases} principal_minors={minors} random_comparisons={comparisons}')
if __name__=='__main__':main()

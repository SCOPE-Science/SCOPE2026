#!/usr/bin/env python3
"""Exact finite-family verification for the affine orientation-word interval maps.

This tests algebraic identities at bounded lengths; the all-length theorem is proved separately.
"""
from fractions import Fraction as F
from itertools import product
from math import log,sqrt

def build(e):
    n=len(e); cuts=[F(i,n) for i in range(n+1)]
    def sides(a,b):
        if (a,b)==(-1,-1):return F(0),F(1)
        if (a,b)==(1,1):return F(1),F(0)
        if (a,b)==(-1,1):return F(0),F(1,n)
        if (a,b)==(1,-1):return F(1),F(n-1,n)
        assert False
    L=[]; R=[]
    for j in range(n):
        left=(F(1) if e[0]==-1 else F(0)) if j==0 else sides(e[j-1],e[j])[1]
        right=(F(0) if e[-1]==-1 else F(1)) if j==n-1 else sides(e[j],e[j+1])[0]
        L.append(left);R.append(right)
    M=[]; s=[]
    for j in range(n):
        a,b=min(L[j],R[j]),max(L[j],R[j]); length=(b-a)*n
        assert length.denominator==1 and length>=2
        s.append(int(length))
        M.append([int(a<=cuts[k] and cuts[k+1]<=b) for k in range(n)])
    return M,s,L,R

def test(e):
    n=len(e); k=sum(e[j-1]!=e[j] for j in range(1,n)); assert e[-2]==e[-1]
    A=sum((e[j-1],e[j])==(-1,1) for j in range(1,n))
    B=sum((e[j-1],e[j])==(1,-1) for j in range(1,n))
    w=[0]+[int(e[j-1]!=e[j]) for j in range(1,n)]
    M,s,L,R=build(e)
    assert all(s[j]==n-w[j] for j in range(n))
    assert all(M[j][h]==1 for j in range(n) for h in range(1,n-1))
    assert all(sum(M[j])==s[j] for j in range(n))
    assert all((not w[j]) or M[j][0]+M[j][-1]==1 for j in range(n))
    denominator=n*(n-1)-k
    pi=[F(n-1-A,denominator)]+[F(n-1,denominator)]*(n-2)+[F(n-1-B,denominator)]
    assert sum(pi)==1 and all(x>0 for x in pi)
    P=[[F(M[j][h],s[j]) for h in range(n)] for j in range(n)]
    assert all(sum(P[j])==1 for j in range(n))
    assert all(sum(pi[j]*P[j][h] for j in range(n))==pi[h] for h in range(n))
    alpha=F(k,n);beta=F(k,n-1)
    Q=((1-alpha,alpha),(1-beta,beta))
    assert all(sum(P[j][h] for h in range(n) if w[h]==1)==Q[w[j]][1] for j in range(n))
    p=F(k*(n-1),denominator)
    assert sum(pi[j]*w[j] for j in range(n))==p
    assert (1-p)*alpha+p*beta==p
    eigen=beta-alpha
    assert eigen==F(k,n*(n-1))
    var=p*(1-p)
    def matvec(a, matrix):return [sum(a[j]*matrix[j][h] for j in range(len(a))) for h in range(len(a))]
    # direct exact lag covariances, rather than computing them from the two-state chain
    pt=[F(x) for x in w]
    for lag in range(8):
        cov=sum(pi[j]*w[j]*pt[j] for j in range(n))-p*p
        assert cov==var*eigen**lag,(e,lag,cov,var*eigen**lag)
        pt=[sum(P[j][h]*pt[h] for h in range(n)) for j in range(n)]
    sigma=var*(1+eigen)/(1-eigen)
    assert sigma>=0
    # numerical metric/topological entropy comparison for nontrivial patterns
    hphys=(1-float(p))*log(n)+float(p)*log(n-1)
    htop=log((n+sqrt(n*n-4*k))/2)
    if k:assert htop>hphys-1e-12,(n,k,htop,hphys)
    else: assert abs(htop-hphys)<1e-12
    return n,k,p,eigen,sigma,htop-hphys

count=0;groups={}
for n in range(3,12):
    for prefix in product((-1,1),repeat=n-1):
        e=prefix+(prefix[-1],)
        res=test(e);count+=1
        # All arrangements having the same (n,k) have identical switching and entropy data
        key=res[:2]; val=res[2:]
        if key in groups:
            assert all(abs(float(a)-float(b))<1e-11 for a,b in zip(groups[key],val))
        groups[key]=val
for n in (50,100,500,1000,2000):
    k=n//2; p=k*(n-1)/(n*(n-1)-k)
    delta=log((n+sqrt(n*n-4*k))/2)-((1-p)*log(n)+p*log(n-1))
    assert abs(n*n*delta-.125)<.30/n
print(f'VERIFY_OK exact_orientation_words={count} n=3..11 distinct_n_k={len(groups)} lag_covariance_checks={count*8} entropy_asymptotic_cases=5')

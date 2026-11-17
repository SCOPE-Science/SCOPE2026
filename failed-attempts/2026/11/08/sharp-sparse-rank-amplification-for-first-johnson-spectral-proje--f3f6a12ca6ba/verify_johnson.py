#!/usr/bin/env python3
"""Exact and numerical checks for the first Johnson harmonic projector."""
from fractions import Fraction
from math import comb, factorial, exp, lgamma, sqrt, pi, log
from itertools import combinations

def probability(n,k,t):
    if not (max(0,2*k-n)<=t<=k): return Fraction(0)
    return Fraction(comb(k,t)*comb(n-k,k-t),comb(n,k))

def formula(n,k):
    j=k*k//n
    return Fraction(2*(n-1)*(k-j)**2,k*(n-k))*probability(n,k,j)

def direct(n,k):
    m=Fraction(k*k,n)
    return Fraction(n*(n-1),k*(n-k))*sum((abs(Fraction(t)-m)*probability(n,k,t) for t in range(k+1)),Fraction(0))

def check_projection(n,k):
    xs=list(map(frozenset,combinations(range(n),k)))
    count=len(xs)
    d=Fraction(n*(n-1),k*(n-k))
    matrix=[[d*(Fraction(len(a&b))-Fraction(k*k,n))/count for b in xs] for a in xs]
    # Every row must have absolute sum formula and annihilate constants.
    for row in matrix:
        assert sum(row)==0
        assert sum(map(abs,row))==formula(n,k)
    # Direct test idempotence by matrix product.
    for i in range(count):
        for j in range(count):
            assert sum(matrix[i][h]*matrix[h][j] for h in range(count))==matrix[i][j]

checks=0
for n in range(3,90):
    for k in range(1,n//2+1):
        assert formula(n,k)==direct(n,k), (n,k)
        j=k*k//n
        p=probability(n,k,j)
        z=sum(((Fraction(t)-Fraction(k*k,n))*probability(n,k,t) for t in range(j+1,k+1)),Fraction(0))
        assert z==Fraction((k-j)**2,n)*p
        checks+=1
for n in range(4,9):
    for k in range(1,min(3,n//2)+1):
        check_projection(n,k)

def logprob(n,k,j):
    return (lgamma(k+1)-lgamma(j+1)-lgamma(k-j+1)+lgamma(n-k+1)-lgamma(k-j+1)-lgamma(n-2*k+j+1)-lgamma(n+1)+lgamma(k+1)+lgamma(n-k+1))

def floatnorm(n,k):
    j=k*k//n
    return 2*(n-1)*(k-j)**2/(k*(n-k))*exp(logprob(n,k,j))
for n in (100,300,1000,3000):
    ks=range(1,n//2+1)
    opt=max(ks,key=lambda k:floatnorm(n,k))
    print('global',n,opt,'rank/sqrt(n)',opt/sqrt(n),'norm/sqrt(n)',floatnorm(n,opt)/sqrt(n))
for m in range(1,100):
    t=m+.5
    before=(m-.5)
    a=2*exp(-before)*before**(m-.5)/factorial(m-1) if m<70 else exp(log(2)-before+(m-.5)*log(before)-lgamma(m))
    b=2*exp(-t)*t**(m+.5)/factorial(m) if m<70 else exp(log(2)-t+(m+.5)*log(t)-lgamma(m+1))
    assert b<a
print('JOHNSON_EXACT_KERNEL_FLUX_IDEMPOTENCE_CHECKS_PASSED',checks)
print('JOHNSON_POISSON_PEAK_ORDER_PASSED 100')

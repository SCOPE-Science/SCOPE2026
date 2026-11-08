#!/usr/bin/env python3
"""Exact independent tests for reciprocal nearest-neighbor component-count formulas."""
from fractions import Fraction
from itertools import combinations, permutations
from math import factorial, comb

def event_moment(n,k):
    if not (0 <= k <= n//2):
        return Fraction(0)
    d=1
    for j in range(1,k+1):d*=2*n-2*j-1
    return Fraction(1,d)

def binomial_moment(n,k):
    return Fraction(factorial(n),factorial(n-2*k)*2**k*factorial(k))*event_moment(n,k)

def pmf(n):
    # Binomial inversion: P(X=r)=sum_{k>=r} (-1)^(k-r) binom(k,r) E[binom(X,k)]
    return [sum(((-1)**(k-r))*comb(k,r)*binomial_moment(n,k) for k in range(r,n//2+1)) for r in range(n//2+1)]

def enumerate_weights(n):
    es=list(combinations(range(n),2));hist=[0]*(n//2+1)
    for perm in permutations(range(len(es))):
        nearest=[-1]*n;left=n
        for ie in perm:
            u,v=es[ie]
            if nearest[u]<0:nearest[u]=v;left-=1
            if nearest[v]<0:nearest[v]=u;left-=1
            if left==0:break
        x=sum(nearest[u]==v for u,v in es if nearest[v]==u)
        hist[x]+=1
    return [Fraction(h,factorial(len(es))) for h in hist]

def run():
    checks=0
    for n in range(2,51):
        p=pmf(n)
        assert sum(p)==1;checks+=1
        assert all(x>=0 for x in p);checks+=1
        assert p[0]==0;checks+=1
        expected=sum(Fraction(r)*p[r] for r in range(len(p)))
        assert expected==Fraction(n*(n-1),2*(2*n-3));checks+=1
        var=sum(Fraction(r*r)*p[r] for r in range(len(p)))-expected**2
        if n>=3:
            assert var==Fraction(n*(n-3)*(n-2)*(n-1),2*(2*n-5)*(2*n-3)**2);checks+=1
        else:
            assert var==0;checks+=1
        for k in range(n//2+1):
            assert sum(comb(r,k)*p[r] for r in range(k,len(p)))==binomial_moment(n,k);checks+=1
    for n in range(2,6):
        brute=enumerate_weights(n)
        assert pmf(n)==brute;checks+=1
        print('Exact edge-order enumeration',n, 'permutations',factorial(n*(n-1)//2),'PMF',brute)
    print('VERIFY_OK',checks,'assertions')
if __name__=='__main__':run()

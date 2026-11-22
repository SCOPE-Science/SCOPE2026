#!/usr/bin/env python3
"""Exact rational verification of a two-quota coverage process."""
from fractions import Fraction
from math import comb
from functools import lru_cache

checks=0

def dpmean(a,b,q):
    @lru_cache(None)
    def E(i,j):
        if i==b and j==a: return Fraction(0)
        loop = (q if i==b else 0)+(1-q if j==a else 0)
        v=Fraction(1)
        if i<b: v+=q*E(i+1,j)
        if j<a: v+=(1-q)*E(i,j+1)
        return v/(1-loop)
    return E(0,0)

def finite(a,b,q):
    N=a+b
    terms=[Fraction(comb(N,x))*q**x*(1-q)**(N-x) for x in range(N+1)]
    excess=sum(terms[x]*Fraction(max(x-b,0),1)/(1-q) +terms[x]*Fraction(max(b-x,0),1)/q for x in range(N+1))
    return N+excess

def cdf_exact(a,b,q,t):
    if t<a+b: return Fraction(0)
    return sum(Fraction(comb(t,x))*q**x*(1-q)**(t-x) for x in range(b,t-a+1))

def cdf_dp(a,b,q,t):
    dist={(0,0):Fraction(1)}
    for _ in range(t):
      nextd={}
      for (i,j),v in dist.items():
       if i==b and j==a:
        nextd[i,j]=nextd.get((i,j),0)+v
       else:
        u=min(i+1,b)
        nextd[u,j]=nextd.get((u,j),0)+v*q
        w=min(j+1,a)
        nextd[i,w]=nextd.get((i,w),0)+v*(1-q)
      dist=nextd
    return dist.get((b,a),Fraction(0))

for a in range(1,8):
 for b in range(1,8):
  for q in [Fraction(1,5),Fraction(2,5),Fraction(1,2),Fraction(3,5),Fraction(4,5)]:
   assert dpmean(a,b,q)==finite(a,b,q),(a,b,q)
   checks+=1
   for t in range(a+b-1,a+b+4):
    assert cdf_exact(a,b,q,t)==cdf_dp(a,b,q,t),(a,b,q,t)
    checks+=1
print('PASS exact mean and all deadline CDF checks:',checks)

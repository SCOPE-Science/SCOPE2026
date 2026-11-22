#!/usr/bin/env python3
"""Separate exact arithmetic checks of the two-sided game's P enumerator."""
from math import comb
from functools import lru_cache

def closed(n):
    if n==0: return 1
    return 1+sum(comb(n-r-1,2*r) for r in range((n-1)//3+1))

# E(z)=z(1-z)/(1-2z+z^2-z^3) for positions starting and ending in a.
e=[0]*201
for n in range(1,201):
    e[n]=(2*e[n-1] if n>=1 else 0) - (e[n-2] if n>=2 else 0) + (e[n-3] if n>=3 else 0) + (int(n==1)-int(n==2))
for n in range(201):
    assert closed(n)==1+e[n],(n,closed(n),1+e[n])

@lru_cache(None)
def g(w):
    options=set()
    for i in range(len(w)-1):
        if w[i:i+2]=='ab': options.add(g(w[i+2:]))
        if w[i:i+2]=='ba': options.add(g(w[:i]))
    r=0
    while r in options:r+=1
    return r
for n in range(101):
    w=('ab'*((n+1)//2))[:n]
    assert g(w)==n//2,(n,g(w))
print('binomial count vs rational series: lengths 0..200 PASS')
print('alternating extremizers: lengths 0..100 PASS')
print('P counts 0..17:',[closed(n) for n in range(18)])
print('selected P count n=50:',closed(50))

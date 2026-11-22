#!/usr/bin/env python3
"""Exact arithmetic checks for quadratic-character Franel correlations modulo five."""
from functools import lru_cache
from math import comb
from fractions import Fraction
from collections import Counter

W=(1,-1,0,1,1)
D=((4,0),(0,1),(-1,0),(0,-1),(1,0))

def digit_weight(n):
    ans=1
    while n:
        n,d=divmod(n,5)
        ans*=W[d]
    return ans

@lru_cache(None)
def S(r,h):
    if r==0:
        return digit_weight(h)
    q,a=divmod(h,5)
    u,v=D[a]
    return u*S(r-1,q)+v*S(r-1,q+1)

@lru_cache(None)
def C(h):
    if h==0:return Fraction(1)
    if h==1:return Fraction(0)
    q,a=divmod(h,5)
    if a==0:return C(q)
    if a==1:return C(q+1)/4
    if a==2:return -C(q)/4
    if a==3:return -C(q+1)/4
    return C(q)/4

def direct_franel_mod5(n):
    return sum(comb(n,k)**3 for k in range(n+1))%5

def legendre_mod5(x):
    return 0 if x%5==0 else (1 if x%5 in (1,4) else -1)

# Independent direct binomial arithmetic at each input, not relying on digit proof.
for n in range(450):
    assert legendre_mod5(direct_franel_mod5(n))==digit_weight(n),n
print('direct Franel-binomial/Legendre checks: 450')

for r in range(1,6):
    n=5**r
    signs=[digit_weight(j) for j in range(n+160)]
    for h in range(0,151):
        d=sum(signs[j]*signs[j+h] for j in range(n))
        assert d==S(r,h),(r,h,d,S(r,h))
    assert S(r,0)==4**r
    assert S(r,1)==-1
    assert S(r,2)==-4**(r-1)
    assert S(r,3)==1
    assert S(r,4)==4**(r-1)
    print(f'r={r}, N={n}, checked 151 lags')

for h in range(1,2000):
    assert abs(C(h)) <= Fraction(1,4)
    if abs(C(h))==Fraction(1,4):
        y=h
        while y%5==0:y//=5
        assert y in (2,4)
        assert C(h)==Fraction(-1 if y==2 else 1,4)
    r=8
    exact=S(r,h)
    resid=exact-4**r*C(h)
    # Verify eventual constant error at one further depth.
    assert S(r+1,h)-4**(r+1)*C(h)==resid, (h,resid)
print('eventual coefficients, equality classification, and constant remainders: 1999 lags')

for r in range(1,6):
    counts=Counter(C(h) for h in range(5**r))
    predicted={Fraction(0):(5**r-1)//2, Fraction(1):1}
    for j in range(1,r+1):
        predicted[Fraction(1,4**j)]=4**(j-1)*comb(r,j)
        predicted[Fraction(-1,4**j)]=4**(j-1)*comb(r,j)
    assert counts==predicted,(r,counts,predicted)
print('complete all-shift signed spectrum: r=1..5, 3905 total shifts')

print('Examples:')
for h in (0,1,2,3,4,5,6,7,8,9,12,14,22,24,27,50,100):
    print(h,str(C(h)),S(4,h))
print('PASS')

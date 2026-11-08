#!/usr/bin/env python3
"""Exact finite checks for simplex-frame two-row Kaczmarz theorem.
The theorem for all dimensions is established by the accompanying proof, not enumeration.
"""
from fractions import Fraction
from itertools import product, combinations
from math import comb
checks=0

def ck(v):
    global checks
    checks += 1
    if not v: raise AssertionError('check '+str(checks))

def gain(x,beta):
    m=len(x)
    sq=[v*v for v in x]
    return sum(max(sq[i] for i in I) for I in combinations(range(m),beta))/Fraction(comb(m,beta))

# Exact check of the nonstandard square-Gini inequality on a bounded integer grid.
for m in (3,5,7):
    for v in product(range(-2,3), repeat=m-1):
        x=tuple(v)+(-sum(v),)
        if not any(x): continue
        s=sum(z*z for z in x)
        d=sum(abs(x[i]**2-x[j]**2) for i in range(m) for j in range(i+1,m))
        ck(d>=s)
        ck(gain(x,2)*Fraction(m-1)>=s)

# Check every finite coefficient inequality used in the analytic proof.
for k in range(1,51):
    m=2*k+1
    for i in range(1,m):
        h=i-1 if i<=k+1 else m-i
        c=(i-1)*(m-i)
        ck(0<=h<=k and c>=k*h)
    # For an extremizing signed vector: (k positives, k negatives, one zero),
    # the squared-error decrement ratio is exactly 1/(m-1) for any beta>=2.
    x=(1,)*k+(-1,)*k+(0,)
    for beta in (1,2,m-1,m):
        target=Fraction(1,m) if beta==1 else Fraction(1,m-1)
        ck(gain(x,beta)/sum(z*z for z in x)==target)

for n in range(2,24):
    m=n+1
    if n%2:
        x=(1,)*((m)//2)+(-1,)*((m)//2)
        for beta in (1,2,m-1,m):
            ck(gain(x,beta)/sum(z*z for z in x)==Fraction(1,m))
    else:
        x=(1,)*(n//2)+(-1,)*(n//2)+(0,)
        for beta in (2,m-1,m):
            ck(gain(x,beta)/sum(z*z for z in x)==Fraction(1,n))
print('PASS',checks,'exact assertions; analytic proof covers all real vectors and all dimensions')

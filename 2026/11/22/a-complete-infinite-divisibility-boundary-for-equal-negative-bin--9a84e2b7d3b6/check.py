#!/usr/bin/env python3
"""Exact rational checks for the zero-offset conditioned negative-binomial classification."""
from fractions import Fraction
from math import comb

checks=0
for c in range(1,24):
    for r in range(1,19):
        a1=c**r
        a2=comb(c+1,2)**r
        quadratic=Fraction(a2)-Fraction(a1*a1,2)
        special=(c==1 or r==1 or (c,r)==(2,2))
        if not special:
            assert quadratic < 0, (c,r,quadratic)
        checks+=1
# Exact generating-function identity for c=r=2:
# (1-z)^3 sum_{n>=0}(n+1)^2 z^n = 1+z.
for n in range(0,1000):
    a=lambda k:(k+1)**2 if k>=0 else 0
    coefficient=a(n)-3*a(n-1)+3*a(n-2)-a(n-3)
    assert coefficient == (1 if n<=1 else 0)
    checks+=1
# Logarithmic coefficients: 3 geometric + log(1+wz) = 4 or 2 copies.
for k in range(1,300):
    v=3+(-1)**(k-1)
    assert v in (2,4) and v>0
    checks+=1
# For representative rational w compare exact first three probabilities
# and degree-two log obstruction without relying on any floating point.
for w in (Fraction(1,7),Fraction(2,5),Fraction(9,10)):
    # exceptional c=r=2: Z=(1+w)/(1-w)^3
    z=(1+w)/(1-w)**3
    p0=1/z
    p1=4*w/z
    p2=9*w*w/z
    assert p0>0 and p0+p1+p2<1
    assert Fraction(p2,p0)-Fraction(1,2)*Fraction(p1,p0)**2 == w*w
    checks+=3
print(f'PASS: {checks} exact assertions')

#!/usr/bin/env python3
"""Exact finite diagnostics for the divisor-onset theorem (not an infinite proof)."""
from fractions import Fraction
from math import lcm

def multiplicity(n, y, lam):
    return sum(n % d == 0 and y < d and Fraction(d) <= lam*y
               for d in range(1, n+1))

checks=0
for lam in [Fraction(5,4),Fraction(3,2),Fraction(7,4),Fraction(2),
            Fraction(5,2),Fraction(3),Fraction(4),Fraction(7)]:
    for r in range(2,7):
        a=(r-1)*lam.denominator//(lam.numerator-lam.denominator)+1
        b=a+r-1
        L=lcm(*range(a,b+1))
        T=min(Fraction(b+1),lam*a)
        assert T>b
        for y in range(1,31):
            xlim=(T*y).numerator//(T*y).denominator
            if xlim>4500:continue
            for n in range(1,xlim+1):
                observed=multiplicity(n,y,lam)
                predicted=(n>b*y and n%L==0)
                assert (observed>=r)==predicted, (lam,r,y,n,observed)
                if predicted: assert observed==r
                checks+=1
assert checks==153292, checks
print('DIVISOR_ONSET_EXACT_OK',checks)

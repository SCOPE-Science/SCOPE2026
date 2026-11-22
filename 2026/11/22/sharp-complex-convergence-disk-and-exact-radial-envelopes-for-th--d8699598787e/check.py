#!/usr/bin/env python3
"""Numerical regressions for the centered Newton-sine basin theorem.

The infinite-domain statements rely on the proof, not on this finite test.
Only Python's standard library is required.
"""
from cmath import tan as ctan
from math import tan, pi, isfinite
from fractions import Fraction

# Check the recurrence from T'(z)=1+T(z)^2 in exact arithmetic.
c = [Fraction(1)]
for n in range(1, 13):
    c.append(sum(c[j] * c[n-1-j] for j in range(n)) / (2*n+1))
assert all(x > 0 for x in c)
assert c[:5] == [Fraction(1), Fraction(1,3), Fraction(2,15), Fraction(17,315), Fraction(62,2835)]

lo, hi = 1.1, 1.2
for _ in range(90):
    mid=(lo+hi)/2
    if tan(mid) > 2*mid: hi=mid
    else: lo=mid
R=(lo+hi)/2
assert 1.16556118520720 < R < 1.16556118520723

def A(t): return tan(t)-t
def N(z): return z-ctan(z)

checks=0
for s in (0.03, 0.125, 0.4, 0.75, 1.1, 1.16):
    assert A(s) < s
    q=A(s)/s
    for j in range(1, 151):
        theta=2*pi*j/151
        z=s*complex(__import__('math').cos(theta), __import__('math').sin(theta))
        assert abs(N(z)) <= A(s) + 2e-12
        assert abs(N(z)) <= q*abs(z) + 2e-12
        checks+=1
    z=s+0j
    a=s
    for n in range(1, 8):
        z=N(z);a=A(a)
        assert abs(abs(z)-a) < 2e-12
        checks+=1

assert abs(N(R)-(-R)) < 1e-12
assert abs(N(-R)-R) < 1e-12
# Critical circle: nonreal points enter the convergence disk in one step.
for j in range(1, 50):
    theta=pi*j/50
    z=R*complex(__import__('math').cos(theta), __import__('math').sin(theta))
    assert abs(N(z)) < R-1e-7
    checks+=1

print('PASS: %d numerical majorant/orbit checks; 13 exact tangent coefficients; R=%.15f' % (checks,R))

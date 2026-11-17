#!/usr/bin/env python3
"""Exact, dependency-free certificate for the productive 13-crown core.

This verifies integer data in the proof, not a brute-force graph construction.
The lower-bound reduction uses the published trace-norm formula.
"""
from fractions import Fraction
from math import isqrt

u = [1000, 730, 691, 653, 617, 583, 551, 520, 491, 463, 436, 410,
     386, 363, 340, 319, 298, 279, 260, 242, 224, 207, 191, 175,
     160, 145, 130, 116, 103, 89, 76, 63, 50, 38, 25, 12]
assert len(u) == 36 and all(t > 0 for t in u)
S = sum(t*t for t in u)
H = sum(u[k]*u[k+1] for k in range(1, 35))
a = (12*u[0]*u[0])**2 + 4*(u[0]*u[1])**2
b = (u[0]*u[0])**2 + 4*(u[0]*u[1])**2
assert (S, H) == (5606050, 4330856)
assert (isqrt(a), isqrt(b)) == (12088490, 1769632)
assert isqrt(a)**2 < a and isqrt(b)**2 < b
lower = Fraction(isqrt(a) + 12*isqrt(b), 13) + Fraction(1998,1000)*H
delta = lower - 2*S
assert delta == Fraction(7053468, 1625)
assert delta > 0
assert Fraction(2,1) + delta/S == Fraction(2,1) + Fraction(7053468, 1625*5606050)
print('EXACT_CERTIFICATE_OK')
print('squared sum:', S, 'tail adjacent product sum:', H)
print('integer-square floors:', isqrt(a), isqrt(b))
print('strict numerator surplus:', delta)
print('norm strictly exceeds:', Fraction(2,1)+delta/S)

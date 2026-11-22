#!/usr/bin/env python3
"""Exact finite cross-check of the odd-reciprocal distance law.

The mathematical proof is in RESULT.md; these tests do not certify infinity.
"""
from fractions import Fraction

def v2(n):
    assert n != 0
    n = abs(n)
    return (n & -n).bit_length() - 1

N = 80
O = [Fraction(0)]
for n in range(1, N + 1):
    O.append(O[-1] + Fraction(1, 2*n-1))
count = 0
congruences = 0
for a in range(N):
    for b in range(a+1, N+1):
        delta = O[b]-O[a]
        assert delta.denominator % 2 == 1
        v = v2(delta.numerator)
        assert v == v2((b-a)*(b+a)), (a,b,v)
        for r in range(1, 10):
            left = (delta.numerator % (1<<r) == 0)
            right = ((b*b-a*a) % (1<<r) == 0)
            assert left == right, (a,b,r)
            congruences += 1
        count += 1
print("VERIFY_OK", count, "exact rational pairs,", congruences, "modular equivalences")

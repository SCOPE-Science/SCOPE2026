#!/usr/bin/env python3
"""Exact rational and integer checks for a fifth-binomial-column fiber formula."""
from collections import Counter
from fractions import Fraction
from math import comb

EXPECTED_BASE = [(0,3,Fraction(1,5)), (0,1,Fraction(-1,5)),
                 (0,2,Fraction(1,15)), (0,1,Fraction(-1,5)),
                 (0,3,Fraction(1,5)), (1,1,Fraction(137,15)),
                 (6,2,Fraction(87,5)), (21,1,Fraction(459,5))]

def v2(x):
    if x == 0:
        return None
    def val(v):
        a=0
        while v % 2 == 0:
            a += 1
            v //= 2
        return a
    return val(abs(x.numerator)) - val(x.denominator)

def polynomial_coefficients(r):
    """Coefficients in t of F(r+8t), represented as exact fractions."""
    a=[Fraction(1)]
    for j in range(5):
        b=[Fraction(0)]*(len(a)+1)
        for i,c in enumerate(a):
            b[i] += c*(r-j)
            b[i+1] += 8*c
        a=b
    return [c/120 for c in a]

for r,(base,d,unit) in enumerate(EXPECTED_BASE):
    a=polynomial_coefficients(r)
    assert a[0]==base
    assert a[1]/(2**d)==unit
    assert v2(a[1])==d
    assert all(z==0 or v2(z)>=d+1 for z in a[2:])

for k in range(1,13):
    q=1<<k
    period=4*q
    counts=Counter(comb(n,5)%q for n in range(period))
    assert len(counts)==q
    for y in range(q):
        if k==1:
            expected=(6 if y==0 else 2)
        elif k==2:
            expected=[8,2,4,2][y]
        else:
            expected=2+2*(y%2==0)+8*(y%8==0)
        assert counts[y]==expected, (k,y,counts[y],expected)
    assert (comb(1+(period//2),5)-0) % q != 0
    # The identity proving full periodicity is general; spot-check it exactly.
    for n in range(45):
        assert (comb(n+period,5)-comb(n,5))%q==0

# Explicit low-column context; these are checks, not a proof of all levels.
for j in range(1,5):
    q=64
    counts=Counter(comb(n,j)%q for n in range(512))
    if j in (1,2,4):
        assert len(counts)==q and set(counts.values())=={8}
    else:
        assert all(counts[y]==(4+16*(y%4==0)) for y in range(q))

print('VERIFY_OK rational_branch_table=8; modulo_power_levels=1..12; '
      'period_and_half_period=1..12; lower_columns=1..4; exact_arithmetic=True')

#!/usr/bin/env python3
"""Exact-rational diagnostics for three-level inhibited marker detection.

The theorem is proved algebraically in RESULT.md. The finite checks here are
reproducibility diagnostics and do not certify statements for all real inputs.
Run: python3 check_identification.py
"""
from fractions import Fraction as F
from itertools import product

checks = 0
for denominator in range(2, 27):
    for numerator in range(1, denominator):
        q = F(numerator, denominator)
        for theta in (F(1, 13), F(1), F(7, 3), F(41, 2)):
            for a in (F(0), F(1, 7), F(2), F(101, 3)):
                y1, y2, y3 = [a + theta * j * q ** j for j in (1, 2, 3)]
                B = 4 * (y1 + y3) - 6 * y2
                C = 4 * y1 * y3 - 3 * y2 ** 2
                other = B - a
                assert a * a - B * a + C == 0
                assert other * other - B * other + C == 0
                assert other - a == 4 * theta * q * (1 - 3 * q + 3 * q*q)
                assert other > a >= 0
                assert y1 - other == -3 * theta * q * (2*q - 1)**2 <= 0
                recovered_q = (y2-a)/(2*(y1-a))
                recovered_theta = (y1-a)/recovered_q
                assert recovered_q == q and recovered_theta == theta
                assert 2 * theta * q*q * (3*q*q - 3*q + 1) > 0
                assert (y2 > y1) == (q > F(1,2))
                assert (y3 > y2) == (q > F(2,3))
                checks += 9

# Construct a continuum of two-level alternatives, including at zero background.
for q in [F(1,8),F(1,2),F(7,8),F(99,100)]:
    for a in [F(0), F(1)]:
        theta = F(3,2)
        y1 = a+theta*q
        y2 = a+2*theta*q*q
        found = False
        for d in [F(1,10**k) for k in range(1, 16)]:
            aa = a+d
            if aa >= min(y1,y2):
                continue
            qq=(y2-aa)/(2*(y1-aa))
            if 0 < qq < 1:
                tt=(y1-aa)/qq
                assert aa+tt*qq == y1 and aa+2*tt*qq*qq == y2
                assert (aa,tt,qq)!=(a,theta,q)
                found=True
                checks += 2
                break
        assert found
        checks += 1
print(f"PASS: {checks} exact rational diagnostic assertions")

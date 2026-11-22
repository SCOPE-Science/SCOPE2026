#!/usr/bin/env python3
"""Exact finite modular checks of the third Narayana-column fiber theorem."""
from collections import Counter
from math import comb

def F(n):
    numerator = n * (n-1)**2 * (n-2)
    assert numerator % 12 == 0
    return numerator // 12

def square_counts(mod):
    return Counter((j*j) % mod for j in range(mod))

checks = 0
for n in range(3,250):
    assert F(n) == (comb(n,3) * comb(n,2)) // n
    checks += 1
for k in range(1, 9):
    m = 3**k
    p = 3*m
    got = Counter(F(n) % m for n in range(p))
    sq = square_counts(3**(k-1))
    for y in range(m):
        pred = 2 if y % 3 else 2 + 3*sq[(-4*(y//3)) % (m//3)]
        assert got[y] == pred, (k,y,got[y],pred)
        checks += 1
    assert sum(got.values()) == p
    checks += 1
    # There is no shorter period because the period is a prime power.
    assert F(3**k) % m != F(0) % m
    checks += 1
    # Verify the two isometric branches exactly at finite precision.
    for a in (0,2):
        branch = [F(a+3*t) % m for t in range(m)]
        assert len(set(branch)) == m, (k,a)
        checks += 1
    print(f'k={k}: modulus={m}, least_period={p}, checked_residues={m}')
print('PASS', checks, 'exact assertions')

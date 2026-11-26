#!/usr/bin/env python3
"""Exact prime-square and period-union checks using Python's standard library."""
from math import gcd, lcm
from fractions import Fraction

prime_period_pairs = ((3, 6), (5, 20), (7, 21), (11, 110))
for prime, period in prime_period_pairs:
    assert pow(2, period, prime * prime) == 1, (prime, period)

L = lcm(*(period for _, period in prime_period_pairs))
assert L == 4620
baseline = set()
full = set()
for m in range(1, L + 1):
    if any(m % period == 0 for period in (6, 20, 21)):
        baseline.add(m)
    if any(m % period == 0 for period in (6, 20, 21, 110)):
        full.add(m)
assert len(baseline) == 1034
assert len(full) == 1048
new = full - baseline
assert len(new) == 14
assert new == {110 * k for k in range(1, 43) if gcd(k, 6) == 1}
assert Fraction(len(baseline), L) == Fraction(47, 210)
assert Fraction(len(full), L) == Fraction(262, 1155)
assert Fraction(len(new), L) == Fraction(1, 330)
assert Fraction(len(full), L) - Fraction(len(baseline), L) == Fraction(1, 330)
# All residue classes also have the prescribed squared prime divisor.
for m in range(1, L + 1):
    if m in full:
        assert any(pow(2, m, prime * prime) == 1 for prime, period in prime_period_pairs if m % period == 0)
print('VERIFY_OK p2_lifting_periods=3:6,5:20,7:21,11:110 lcm=4620 baseline_residues=1034 full_residues=1048 new_residues=14 density_lower=262/1155 added_density=1/330')

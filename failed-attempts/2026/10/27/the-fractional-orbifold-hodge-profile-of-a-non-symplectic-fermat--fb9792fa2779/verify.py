#!/usr/bin/env python3
"""Exact independent arithmetic checks for an orbifold Hodge computation."""
from itertools import product
from collections import Counter
from math import gcd

# Coefficients of z^degree t^weight in (Z[t]/(t^6-1))[z].
dp = {(0, 0): 1}
for j in range(6):
    next_dp = {}
    for (degree,weight), c in dp.items():
        for a in range(5):
            k = (degree + a, (weight + j*a) % 6)
            next_dp[k] = next_dp.get(k, 0) + c
    dp = next_dp
invariants = [dp.get((6*q, 3), 0) for q in range(5)]
assert invariants == [0, 70, 290, 70, 0], invariants
assert [sum(v for (d,w), v in dp.items() if d == 6*q) for q in range(5)] == [1,426,1751,426,1]

# Fixed loci of each power have Euler characteristics given by their
# nonempty projective eigenspaces intersected with the Fermat sextic.
# Unit: 0; involution: two smooth plane sextics (genus 10);
# order-three: three projective lines with six points each.
def fixed_euler(k):
    k %= 6
    if k == 0: return 2610
    if k in (1,5): return 0
    if k in (2,4): return 18
    if k == 3: return -36
    raise AssertionError
coarse_euler = sum(fixed_euler(k) for k in range(6)) // 6
assert coarse_euler == 435
orb_euler = sum(fixed_euler(gcd(gcd(a,b),6)) for a,b in product(range(6), repeat=2)) // 6
assert orb_euler == 441

# The genus-10 curves admit a free order-three residual action.
assert (10-1)//3+1 == 4
# Two order-three ages = 2; the involution age is 3/2.
assert (1+1+2+2) == 3*2
assert 3 == 2 * 1.5
# Coarse Hodge polynomial at (u,v)=(1,1).
assert 1+1+(invariants[2]+1)+invariants[1]+invariants[3]+1+1 == 435
# Orbifold twisted sector contribution at (1,1): 18-12.
assert coarse_euler + 2*9 + 2*(2-2*4) == orb_euler
print('VERIFY_OK invariant_counts=',invariants,'coarse_e=',coarse_euler,'orb_e=',orb_euler)

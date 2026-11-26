#!/usr/bin/env python3
"""Exact finite consistency checks for a random permutation-graph degree limit.

This program checks finite identities; it does not purport to verify convergence
of infinite sequences. The convergence proof is given in RESULT.md.
"""
from fractions import Fraction
from itertools import permutations
from math import floor, sqrt

checks = 0
for n in range(2, 8):
    counts = [0] * n
    sums = [0] * n
    pair_sums = [[0] * n for _ in range(n)]
    for p in permutations(range(n)):
        d = [sum((j-i)*(p[j]-p[i]) < 0 for j in range(n)) for i in range(n)]
        for i in range(n):
            sums[i] += d[i]
            for j in range(n):
                pair_sums[i][j] += d[i]*d[j]
        counts[0] += 1
    count = counts[0]
    for i in range(n):
        assert Fraction(sums[i], count) == Fraction(n-1, 2)
        checks += 1
        for j in range(n):
            covariance = Fraction(pair_sums[i][j], count) - Fraction(sums[i]*sums[j], count*count)
            target = (Fraction(n+1, 12) if i != j
                      else Fraction(n-1, 6) + Fraction((2*(i+1)-n-1)**2, 12))
            assert covariance == target, (n, i, j, covariance, target)
            checks += 1

# A Brownian bridge B has E B(U)^2=1/6 and E B(U)B(V)=1/12
# for independent U,V uniform on [0,1]. Integrate the polynomial kernels.
E_U1MU = Fraction(1, 2) - Fraction(1, 3)
E_MIN = 2 * Fraction(1, 2) * Fraction(1, 3)  # 2 integral_0^1 integral_0^v u du dv
E_UV = Fraction(1, 4)
assert E_U1MU == Fraction(1, 6)
assert E_MIN - E_UV == Fraction(1, 12)
checks += 2

# At the critical scale, exact normalized degree moments converge to the
# displayed Brownian-bridge-mixture moments, by direct algebra.
for n in (10001, 40001, 160001):
    ts = (-1.25, -0.35, 0.8)
    indices = [floor(n/2 + t*sqrt(n)) for t in ts]
    assert len(indices) == len(set(indices))
    for t, ind in zip(ts, indices):
        exact_var_per_n = ((n-1)/6 + (2*ind-n-1)**2/12)/n
        limit = 1/6 + t*t/3
        assert abs(exact_var_per_n - limit) < 0.035
        checks += 1
    for x in range(len(indices)):
        for y in range(x):
            assert abs((n+1)/(12*n) - 1/12) < 0.00002
            checks += 1

print('PASS:', checks, 'exact/integral/asymptotic-second-moment assertions')

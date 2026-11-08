"""Exact rational checks for the hypersimplex vertex-convexification theorem.

The theorem is proved algebraically in RESULT.md; these finite checks are
independent diagnostics and do not assert exhaustive real-parameter coverage.
"""
from fractions import Fraction as F
from itertools import combinations, product
from math import comb
import random

checks = 0


def brute_membership(n, k, y, lam):
    assert sum(y) == k
    assert all(0 <= x <= 1 for x in y)
    scaled = [(1 + lam) * x for x in y]
    for I in combinations(range(n), k):
        I = set(I)
        z = [(scaled[j] - int(j in I)) / lam for j in range(n)]
        if all(0 <= v <= 1 for v in z) and sum(z) == k:
            return True
    return False


def order_membership(n, k, y, lam):
    assert lam >= 1
    arr = sorted(y, reverse=True)
    return arr[k - 1] >= F(1, 1 + lam) and arr[k] <= lam / (1 + lam)


def rational_hypersimplex_grid(n, k, denominator):
    for a in product(range(denominator + 1), repeat=n):
        if sum(a) == k * denominator:
            yield tuple(F(t, denominator) for t in a)


for n in range(3, 8):
    for k in range(1, n):
        for q in (2, 3, 4):
            for y in rational_hypersimplex_grid(n, k, q):
                for lam in (F(1), F(3, 2), F(2), F(5, 2), F(3), F(4), F(6)):
                    assert brute_membership(n, k, y, lam) == order_membership(n, k, y, lam)
                    checks += 1

for n in range(3, 25):
    for k in range(1, n):
        c = max(k, n - k)
        yr = (F(k, k + 1),) * (k + 1) + (F(0),) * (n - k - 1)
        yc = (F(1),) * (k - 1) + (F(1, n - k + 1),) * (n - k + 1)
        assert sum(yr) == sum(yc) == k
        for y in (yr, yc):
            assert order_membership(n, k, y, F(c))
            checks += 1
        if k >= n - k:
            assert not order_membership(n, k, yr, F(k) - F(1, 2))
            checks += 1
        if n - k >= k:
            assert not order_membership(n, k, yc, F(n - k) - F(1, 2))
            checks += 1

random.seed(18021)
# Directly verify the two sharp witness obstructions below the rank and corank
# thresholds, also for parameters less than one where the sorted criterion
# was intentionally not asserted.
for n in range(3, 9):
    for k in range(1, n):
        yr = (F(k, k + 1),) * (k + 1) + (F(0),) * (n - k - 1)
        yc = (F(1),) * (k - 1) + (F(1, n - k + 1),) * (n - k + 1)
        for lam in (F(1, 3), F(1, 2), F(2, 3), F(1), F(3, 2), F(5, 2), F(7, 2)):
            assert brute_membership(n, k, yr, lam) == (lam >= k)
            assert brute_membership(n, k, yc, lam) == (lam >= n - k)
            checks += 2

for n in range(3, 12):
    for k in range(1, n):
        c = max(k, n - k)
        for trial in range(100):
                # extreme points and convexity of the hypersimplex give random points.
            v = [F(0)] * n
            for _ in range(n + 1):
                I = random.sample(range(n), k)
                for i in I:
                    v[i] += F(1, n + 1)
            assert sum(v) == k
            assert order_membership(n, k, v, F(c))
            checks += 1

print(f'PASS {checks} exact-rational finite membership/threshold checks')

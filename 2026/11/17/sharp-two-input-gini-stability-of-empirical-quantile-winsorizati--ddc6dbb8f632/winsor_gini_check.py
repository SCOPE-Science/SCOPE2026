"""Exact finite tests for pairwise-dispersion norms of coordinate replication and Winsorization.

Scientific scope: diagnostic enumeration only; the unrestricted result has a separate proof.
"""
from itertools import combinations, product
from fractions import Fraction as F
from random import Random


def g(v):
    return sum(abs(v[i] - v[j]) for i in range(len(v)) for j in range(i + 1, len(v)))


def w(v, a, b):
    z = sorted(v)
    return tuple(min(max(x, z[a - 1]), z[b - 1]) for x in v)


def compositions(n, k):
    if k == 1:
        yield (n,)
    else:
        for x in range(n + 1):
            for tail in compositions(n - x, k - 1):
                yield (x,) + tail


replication_checks = 0
for n in range(2, 8):
    for m in compositions(n, n):
        representatives = tuple(j for j in range(n) for _ in range(m[j]))
        expected = max(F(z * (n - z), n - 1) for z in m)
        observed = max(F(u * (n - u), s * (n - s))
                       for s in range(1, n)
                       for S in combinations(range(n), s)
                       for u in [sum(m[i] for i in S)])
        assert observed == expected, (n, m, observed, expected)
        replication_checks += 1
print('ALL_REPLICATION_MULTIPLICITIES_EXACT', replication_checks)

winsor_checks = 0
for n in range(2, 11):
    for a in range(1, n):
        for b in range(a + 1, n + 1):
            m = tuple(sum(min(max(i, a - 1), b - 1) == j for i in range(n)) for j in range(n))
            got = max(F(sum(m[i] for i in S) * (n - sum(m[i] for i in S)), s * (n - s))
                      for s in range(1, n)
                      for S in combinations(range(n), s))
            predicted = max(F(a * (n - a), n - 1),
                            F((n - b + 1) * (b - 1), n - 1))
            assert got == predicted, (n, a, b, got, predicted)
            # Strict order chamber + a single-rank perturbation supplies exact attainment.
            pivot = a - 1 if a * (n - a) >= (n - b + 1) * (b - 1) else b - 1
            z = tuple(F(10 * i) for i in range(n))
            dz = tuple(F(1, 100) if i == pivot else F(0) for i in range(n))
            v0 = w(z, a, b)
            v1 = w(tuple(z[i] + dz[i] for i in range(n)), a, b)
            assert g(tuple(v1[i] - v0[i] for i in range(n))) == predicted * g(dz)
            assert g(v0) <= g(z)
            winsor_checks += 1
print('ALL_WINSORIZED_CHAMBERS_AND_ATTAINMENT_EXACT', winsor_checks)

rng = Random(1207)
pair_checks = 0
for n in range(2, 11):
    for _ in range(1200):
        a = rng.randrange(1, n)
        b = rng.randrange(a + 1, n + 1)
        x = tuple(F(rng.randrange(-40, 41), rng.randrange(1, 5)) for _ in range(n))
        y = tuple(F(rng.randrange(-40, 41), rng.randrange(1, 5)) for _ in range(n))
        delta = tuple(x[i] - y[i] for i in range(n))
        L = max(F(a * (n - a), n - 1), F((n - b + 1) * (b - 1), n - 1))
        if g(delta):
            wx, wy = w(x, a, b), w(y, a, b)
            assert g(tuple(wx[i] - wy[i] for i in range(n))) <= L * g(delta)
        pair_checks += 1
print('EXACT_RANDOM_TWO_INPUT_INEQUALITIES', pair_checks)
print('ALL_WINSORIZED_GINI_DIAGNOSTICS_PASSED')

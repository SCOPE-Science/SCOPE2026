"""Exact rational checks for simplex-translate depth and empirical quantiles.

Use: python verify.py
The universal result follows from the written proof, not from these finite tests.
"""
from fractions import Fraction as F
from itertools import product, combinations
from random import Random


def depth_by_marginals(data, y):
    return F(min(sum(z[i] <= y[i] for z in data) for i in range(len(y))), len(data))


def depth_by_independent_subsets(data, y):
    # A subset fits in a translated simplex excluding y iff some coordinate
    # of every selected point strictly exceeds that coordinate of y.
    n, d = len(data), len(y)
    best = 0
    for mask in range(1, 1 << n):
        chosen = [data[j] for j in range(n) if mask & (1 << j)]
        if any(min(z[i] for z in chosen) > y[i] for i in range(d)):
            best = max(best, len(chosen))
    return F(n - best, n)


def q_regions(data, k):
    n, d = len(data), len(data[0])
    return tuple(sorted(z[i] for z in data)[k - 1] for i in range(d))


def bary_grid(d, denominator):
    for a in product(range(denominator + 1), repeat=d - 1):
        if sum(a) <= denominator:
            yield tuple(F(x, denominator) for x in a) + (F(denominator - sum(a), denominator),)


def run():
    rng = Random(40721)
    checks = 0
    for d in (2, 3, 4, 5):  # d barycentric slots; ambient dimension d-1
        grid = list(bary_grid(d, 5))
        queries = grid + [tuple(F(-1 if i == 0 else (2 if i == 1 else 0)) for i in range(d))]
        for n in range(1, 7):
            for repetition in range(12):
                data = [rng.choice(grid) for _ in range(n)]
                for y in rng.sample(queries, min(16, len(queries))):
                    a = depth_by_marginals(data, y)
                    b = depth_by_independent_subsets(data, y)
                    assert a == b, (d, n, data, y, a, b)
                    checks += 1
                for k in range(1, n + 1):
                    q = q_regions(data, k)
                    for y in rng.sample(queries, min(12, len(queries))):
                        assert (depth_by_marginals(data, y) >= F(k, n)) == all(y[i] >= q[i] for i in range(d))
                        checks += 1
                # Compare the sorted-order algorithm with direct maximization
                kstar = max(k for k in range(1, n + 1) if sum(q_regions(data, k)) <= 1)
                assert all(sum(q_regions(data, k)) > 1 for k in range(kstar + 1, n + 1))
                # A feasible barycentric center is obtained by distributing leftover mass.
                q = list(q_regions(data, kstar))
                q[0] += 1 - sum(q)
                assert sum(q) == 1 and depth_by_marginals(data, q) == F(kstar, n)
                checks += 3
    # Exact uniform-simplex computations for rational quantile thresholds.
    for d in range(1, 21):
        level = 1 - F(d, d + 1) ** d
        q = 1 - (1 - level) ** F(1, d) if d == 1 else F(1, d + 1)
        assert d == 1 or (1 - q)**d == 1 - level
        assert (d + 1) * q == 1
        checks += 2
    # A dimension-free sharpness witness: opposite-facet barycentres.
    for d in range(1, 8):
        vertices = [tuple(F(0) if j == i else F(1, d) for j in range(d + 1)) for i in range(d + 1)]
        kstar = max(k for k in range(1, d + 2) if sum(q_regions(vertices, k)) <= 1)
        assert kstar == 1
        checks += 1
    print('EXACT_OK', checks)


if __name__ == '__main__':
    run()

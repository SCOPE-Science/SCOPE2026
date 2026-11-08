#!/usr/bin/env python3
"""Independent finite spot checks for a hyper-permutahedron Euclidean-width theorem.
Only finite evidence; not a proof of the infinite-dimensional assertions.
"""
from math import comb, sqrt, isclose
from itertools import combinations
from random import Random


def mixed(n, k, s):
    return comb(n, k) - (comb(s, k) if s >= k else 0) - (comb(n - s, k) if n - s >= k else 0)


def cut_width(n, k, s):
    return mixed(n, k, s) * sqrt(n / (s * (n - s)))


def formula_min(n, k):
    s_best = min(range(1, n // 2 + 1), key=lambda s: cut_width(n, k, s))
    return cut_width(n, k, s_best), s_best


def actual_width(n, hyperedges, u):
    return sum(max(u[j] for j in H) - min(u[j] for j in H) for H in hyperedges)


def centered_normal(n, subset):
    s = len(subset)
    raw = [(1 if i in subset else 0) - s / n for i in range(n)]
    d = sqrt(sum(x * x for x in raw))
    return [x/d for x in raw]


def independent_mixed(n, k, s):
    return sum(0 < len(set(H).intersection(range(s))) < k for H in combinations(range(n), k))

rng = Random(20261106)
cut_checks = 0
normal_checks = 0
random_direction_checks = 0
for n in range(3, 10):
    for k in range(2, n + 1):
        hs = list(combinations(range(n), k))
        theory, _ = formula_min(n, k)
        for s in range(1, n):
            assert mixed(n, k, s) == independent_mixed(n, k, s)
            u = centered_normal(n, set(range(s)))
            assert isclose(actual_width(n, hs, u), cut_width(n, k, s), rel_tol=3e-12, abs_tol=3e-12)
            cut_checks += 1
            normal_checks += 1
        for _ in range(18):
            v = [rng.randrange(-10000, 10001) for _ in range(n)]
            mean = sum(v) / n
            u = [x - mean for x in v]
            length = sqrt(sum(x * x for x in u))
            if length < 1e-10:
                continue
            u = [x / length for x in u]
            assert actual_width(n, hs, u) >= theory - 1e-8
            random_direction_checks += 1

# All finite candidates are compared by exact squared-width cross multiplication,
# including the small values where a near-critical tie may occur.
finite_profiles = 0
interior_minima = 0
for n in range(4, 151):
    for k in range(2, n+1):
        c = [mixed(n, k, s) for s in range(1, n//2+1)]
        den = [s*(n-s) for s in range(1, n//2+1)]
        winners = [i+1 for i in range(len(c)) if all(c[i]**2*den[j] <= c[j]**2*den[i] for j in range(len(c)))]
        assert winners
        if any(s not in (1, n//2) for s in winners):
            interior_minima += 1  # empirical only: theorem does not assume this is zero
        finite_profiles += 1

# Numerical illustration of the asymptotic phase transition, away from c = 2.
asymptotic_checks = 0
for n in (400, 900, 1600, 2500):
    for ratio in (1.4, 1.6, 2.4, 2.7):
        k = max(2, round(ratio * sqrt(n)))
        c = [mixed(n, k, s) for s in range(1, n//2+1)]
        den = [s*(n-s) for s in range(1, n//2+1)]
        winner = 1
        for i in range(1,len(c)):
            if c[i]**2 * den[winner-1] < c[winner-1]**2 * den[i]:
                winner = i + 1
        assert winner == (1 if ratio < 2 else n//2), (n,k,ratio,winner)
        asymptotic_checks += 1
print('HYPERPERMUTAHEDRON_WIDTH_CHECKS_PASSED',
      'cut=',cut_checks,'normal=',normal_checks,'direction=',random_direction_checks,
      'finite_profiles=',finite_profiles,'finite_interior_minima=',interior_minima,
      'asymptotic=',asymptotic_checks)

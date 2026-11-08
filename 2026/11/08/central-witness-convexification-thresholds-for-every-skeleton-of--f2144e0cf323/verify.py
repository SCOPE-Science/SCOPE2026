#!/usr/bin/env python3
"""Exact rational spot-checks for a skeletal Minkowski convexification theorem.

All assertions are supplementary; the complete proof is analytic.
"""
from fractions import Fraction as F
from itertools import combinations, product
from math import ceil
from random import Random


def all_support_budgets(ds):
    return [(s, sum(q - 1 for q in s))
            for s in product(*(range(1, d + 2) for d in ds))]


def feasible_by_independent_support_search(blocks, k):
    # Enumerate actual coordinate-subset choices, not a closed-form ceiling test.
    options = []
    for block in blocks:
        candidates = []
        for s in range(1, len(block) + 1):
            ok = any(sum(block[j] for j in ss) >= 1
                     for ss in combinations(range(len(block)), s))
            if ok:
                candidates.append(s - 1)
        options.append(candidates)
    return any(sum(costs) <= k for costs in product(*options))


def exact_theorem_condition(ds, k, t):
    return sum(ceil(F(d + 1, 1) / (1 + t)) - 1 for d in ds) <= k


def make_block(n, t, rng):
    vals = [rng.randint(0, 9) for _ in range(n)]
    if sum(vals) == 0:
        vals[0] = 1
    return tuple((1 + t) * F(a, sum(vals)) for a in vals)


def main():
    r = Random(271828)
    checks = 0
    central = 0
    for ds in [(1,), (2,), (3,), (4,), (1, 1), (1, 2), (2, 2),
               (1, 3), (1, 1, 1), (1, 2, 2), (1, 1, 1, 1)]:
        dimension = sum(ds)
        for k in range(dimension):
            for t in [F(0), F(1, 5), F(1, 2), F(3, 4), F(1), F(3, 2),
                      F(2), F(3), F(4), F(5)]:
                center = tuple(tuple(F(1, 1) * (1 + t) / (d + 1)
                                     for _ in range(d + 1)) for d in ds)
                actual = feasible_by_independent_support_search(center, k)
                expected = exact_theorem_condition(ds, k, t)
                assert actual == expected, (ds, k, t, actual, expected)
                central += 1
                # Every block dominates its center for the sparse support test.
                if expected:
                    for _ in range(5):
                        blocks = tuple(make_block(d + 1, t, r) for d in ds)
                        assert feasible_by_independent_support_search(blocks, k)
                        checks += 1
                else:
                    # Counterexample at centroid, as claimed.
                    assert not actual
                # Closed-form minimization over all face-support allowances.
                index = min(max(F(d + 1, s) - 1 for d, s in zip(ds, ss))
                            for ss, cost in all_support_budgets(ds) if cost <= k)
                assert (index <= t) == expected
                checks += 1
    print('VERIFY_OK', checks, 'exact rational instances;', central,
          'centroid witness checks; support allocations and index minimizations')


if __name__ == '__main__':
    main()

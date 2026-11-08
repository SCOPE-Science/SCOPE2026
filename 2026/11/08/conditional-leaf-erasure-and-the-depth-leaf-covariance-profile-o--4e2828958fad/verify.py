#!/usr/bin/env python3
"""Independent exact checks for conditional leaf erasure and depth--leaf covariance.
Use only standard-library Fraction and exhaustive enumeration of recursive trees.
"""
from collections import Counter
from fractions import Fraction
from itertools import product, combinations
from math import factorial

checks = 0

def trees(n):
    for choices in product(*(range(1, t) for t in range(2, n + 1))):
        parents = [0, 0] + list(choices)
        depths = [0] * (n + 1)
        childcount = [0] * (n + 1)
        for t in range(2, n + 1):
            depths[t] = depths[parents[t]] + 1
            childcount[parents[t]] += 1
        leaves = {t for t in range(2, n + 1) if childcount[t] == 0}
        yield tuple(depths), frozenset(leaves)

# Depth distributions on smaller recursive trees, independently enumerated.
depth_dist = {}
for m in range(1, 9):
    counts = Counter()
    for depths, _ in trees(m):
        counts[depths[m]] += 1
    depth_dist[m] = counts
    assert sum(counts.values()) == factorial(m - 1)

for n in range(2, 9):
    data = list(trees(n))
    count = len(data)
    assert count == factorial(n - 1)
    for j in range(2, n + 1):
        dsum = sum(depths[j] for depths, leaves in data)
        Lsum = sum(len(leaves) for depths, leaves in data)
        dLsum = sum(depths[j] * len(leaves) for depths, leaves in data)
        observed_cov = Fraction(dLsum, count) - Fraction(dsum * Lsum, count * count)
        target_cov = Fraction(-(j - 2), 2 * (n - 1))
        assert observed_cov == target_cov, (n, j, observed_cov, target_cov)
        checks += 1
        for i in range(2, n + 1):
            isum = sum(i in leaves for depths, leaves in data)
            disum = sum(depths[j] * (i in leaves) for depths, leaves in data)
            observed = Fraction(disum, count) - Fraction(dsum * isum, count * count)
            target = Fraction(-(i - 1), (n - 1) * (j - 1)) if i < j else Fraction(0)
            assert observed == target, (n, i, j, observed, target)
            checks += 1
        # Every subset of earlier vertices: exact conditional distribution, not just mean.
        for r in range(j - 1):
            for selected in combinations(range(2, j), r):
                conditioned = Counter(depths[j] for depths, leaves in data if set(selected) <= leaves)
                N = sum(conditioned.values())
                assert N > 0
                baseline = depth_dist[j - r]
                baseN = factorial(j - r - 1)
                for h in set(conditioned) | set(baseline):
                    assert Fraction(conditioned[h], N) == Fraction(baseline[h], baseN), (n, j, selected, h)
                    checks += 1
    # Standard finite-leaf mean and variance check for n>=3.
    if n >= 3:
        Lsum = sum(len(leaves) for depths, leaves in data)
        L2sum = sum(len(leaves) ** 2 for depths, leaves in data)
        varL = Fraction(L2sum, count) - Fraction(Lsum * Lsum, count * count)
        assert varL == Fraction(n, 12), (n, varL)
        checks += 1

# Full conditional tree law: removing any specified leaves leaves a uniform
# recursive tree on the remaining birth-order labels (not only a depth law).
for n in range(2, 9):
    all_parent_lists = list(product(*(range(1, t) for t in range(2, n + 1))))
    for r in range(n):
        for chosen in combinations(range(2, n + 1), r):
            chosen = frozenset(chosen)
            rem = tuple(t for t in range(1, n + 1) if t not in chosen)
            pos = {t: k + 1 for k, t in enumerate(rem)}
            outcomes = Counter()
            for arr in all_parent_lists:
                parents = [0, 0] + list(arr)
                if any(parent in chosen for parent in arr):
                    continue
                reduced = tuple(pos[parents[t]] for t in rem if t > 1)
                outcomes[reduced] += 1
            assert sum(outcomes.values()) > 0
            assert len(outcomes) == factorial(len(rem) - 1), (n, chosen, len(outcomes))
            assert len(set(outcomes.values())) == 1, (n, chosen, outcomes)
            checks += len(outcomes)

print('PASS:' , checks, 'exact rational distribution/moment assertions; exhaustive through n=8.')

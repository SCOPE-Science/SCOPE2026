#!/usr/bin/env python3
"""Exact finite replay for the labelled-plateau inclusion theorem.

Usage: python3 verify.py   (Python standard library only).
The asymptotic limit is proved in RESULT.md; finite tests alone are not a proof.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb


def words(n, r):
    result = [()]
    for label in range(1, n + 1):
        result = [word[:gap] + (label,) * r + word[gap:]
                  for word in result for gap in range(len(word) + 1)]
    return result


def subsets(n):
    universe = range(1, n + 1)
    return [frozenset(s) for length in range(n + 1)
            for s in combinations(universe, length)]


def inclusion(n, r, selected):
    out = Fraction(1)
    for k in range(2, n + 1):
        count = sum(label < k for label in selected)
        out *= Fraction(r * (k - 1) + 1 - (r - 1) * count,
                        r * (k - 1) + 1)
    return out


def probability_label_set(word, n, r):
    return frozenset(label for label in range(1, n + 1)
                     if (label,) * r in (word[pos:pos + r]
                                        for pos in range(len(word) - r + 1)))


def pair_covariance(n, r, i, j):
    if i > j:
        i, j = j, i
    p_i = inclusion(n, r, frozenset((i,)))
    p_j = inclusion(n, r, frozenset((j,)))
    if i == j:
        return p_i * (1 - p_i)
    ratio = Fraction(1)
    for k in range(j + 1, n + 1):
        h = Fraction(r - 1, r * (k - 1) + 1)
        ratio *= (1 - 2 * h) / (1 - h) ** 2
    return p_i * p_j * (ratio - 1)


def run():
    assertions = 0
    cases = ((2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6),
             (3, 2), (3, 3), (3, 4), (4, 2), (4, 3))
    for r, n in cases:
        sample = words(n, r)
        expected_total = 1
        for k in range(1, n + 1):
            expected_total *= (r * (k - 1) + 1)
        assert len(sample) == expected_total
        assertions += 1
        masks = Counter(probability_label_set(w, n, r) for w in sample)
        all_subsets = subsets(n)
        for selected in all_subsets:
            exact = Fraction(sum(count for mask, count in masks.items()
                                 if selected.issubset(mask)), len(sample))
            assert exact == inclusion(n, r, selected), (r, n, selected)
            assertions += 1
            # Inclusion-exclusion recovers the exact point mass for this pattern.
            absent = frozenset(range(1, n + 1)) - selected
            mobius = sum(((-1) ** len(extra)) * inclusion(n, r, selected | extra)
                         for extra in subsets_of(absent))
            assert mobius == Fraction(masks[selected], len(sample))
            assertions += 1
        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                observed = (inclusion(n, r, frozenset((i, j)))
                            - inclusion(n, r, frozenset((i,)))
                            * inclusion(n, r, frozenset((j,))))
                assert observed == pair_covariance(n, r, i, j)
                assert observed <= 0
                assert (observed < 0) == (j < n)
                assertions += 3
        for A in all_subsets:
            for B in all_subsets:
                assert inclusion(n, r, A | B) * inclusion(n, r, A & B) <= (inclusion(n, r, A) * inclusion(n, r, B))
                assertions += 1
        print('exact', 'r=', r, 'n=', n, 'words=', len(sample), 'subsets=', len(all_subsets))
    # Direct rational mgf domination for multiple distinct z>=1.
    for r, n in ((2, 5), (3, 4), (4, 3)):
        masses = Counter(probability_label_set(w, n, r) for w in words(n, r))
        denom = sum(masses.values())
        for z in (1, 2, 3):
            actual = Fraction(sum(count * z ** len(mask) for mask, count in masses.items()), denom)
            independent = Fraction(1)
            for i in range(1, n + 1):
                p = inclusion(n, r, frozenset((i,)))
                independent *= 1 + (z - 1) * p
            assert actual <= independent
            assertions += 1
    # Independent numerical diagnostic of the asymptotic variance curve.
    # The asymptotic theorem is proved analytically, not by these checks.
    for r in (2, 3, 4):
        beta = (r - 1) / r
        n = 4000
        p = [0.0] * (n + 1)
        p[n] = 1.0
        for i in range(n - 1, 0, -1):
            p[i] = p[i + 1] * (1 - (r - 1) / (r * i + 1))
        ratios = [1.0] * (n + 1)
        for j in range(n - 1, 1, -1):
            h = (r - 1) / (r * j + 1)
            ratios[j] = ratios[j + 1] * (1 - 2 * h) / (1 - h)**2
        for t in (0.25, 0.5, 1.0):
            m = int(n * t)
            diagonal = sum(p[i] * (1 - p[i]) for i in range(1, m + 1))
            prefix = 0.0
            off_diagonal = 0.0
            for j in range(1, m + 1):
                off_diagonal += 2 * p[j] * (ratios[j] - 1) * prefix
                prefix += p[j]
            observed = (diagonal + off_diagonal) / n
            predicted = (t**(beta + 1) / (beta + 1)
                - (2 * beta * beta + beta + 1) * t**(2*beta + 1)
                   / ((beta + 1) * (2*beta + 1))
                + beta*beta * t**(2*beta + 2) / (beta + 1)**2)
            assert abs(observed - predicted) < 0.001, (r, t, observed, predicted)
    print('PASS', assertions, 'exact rational assertions, 9 numerical diagnostics')


def subsets_of(items):
    arr = sorted(items)
    return [frozenset(t) for size in range(len(arr) + 1)
            for t in combinations(arr, size)]


if __name__ == '__main__':
    run()

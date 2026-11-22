#!/usr/bin/env python3
"""Exact finite checks of comparison-event covariance and strict-laminar independence.

Uses rank permutations as the pivot priority orders. The infinite-size theorem
is proved separately; these enumerations check only the indicated finite sizes.
"""
from itertools import combinations, permutations
from collections import Counter
from fractions import Fraction
from math import factorial


def probability(a, b):
    return Fraction(2, b - a + 1)


def covariance(A, B):
    a, b = A
    c, d = B
    if A == B:
        p = probability(a, b)
        return p * (1 - p)
    u, v = b - a + 1, d - c + 1
    if b < c or d < a or a < c < d < b or c < a < b < d:
        return Fraction(0)
    if a == c or b == d:
        s, ell = min(u, v), max(u, v)
        return Fraction(s - 2, s * ell)
    if b == c or d == a:
        return Fraction((u - 2) * (v - 2), u * v * (u + v - 1))
    left = max(a, c)
    right = min(b, d)
    if left < right:
        w = right - left + 1
        union = max(b, d) - min(a, c) + 1
        return Fraction(-2 * (u + v - 2 * w), u * v * union)
    raise AssertionError((A, B))


def compatible(A, B):
    a, b = A
    c, d = B
    return (b < c or d < a or a < c < d < b or c < a < b < d)


def main():
    comparisons = 0
    triples_checked = 0
    for n in range(2, 9):
        intervals = list(combinations(range(n), 2))
        m = len(intervals)
        p_count = [0] * m
        joint_count = [[0] * m for _ in range(m)]
        valid_triples = [t for t in combinations(range(m), 3)
                         if all(intervals[k][1] - intervals[k][0] >= 2 for k in t)
                         and all(compatible(intervals[x], intervals[y])
                                 for x, y in combinations(t, 2))]
        triple_count = [0] * len(valid_triples)
        total = factorial(n)
        for order in permutations(range(n)):
            rank = [0] * n
            for j, label in enumerate(order):
                rank[label] = j
            active = [int(min(range(a, b + 1), key=rank.__getitem__) in (a, b))
                      for a, b in intervals]
            for i in range(m):
                if active[i]:
                    p_count[i] += 1
                    for j in range(i, m):
                        if active[j]:
                            joint_count[i][j] += 1
            for k, (i, j, ell) in enumerate(valid_triples):
                if active[i] and active[j] and active[ell]:
                    triple_count[k] += 1
        for i, A in enumerate(intervals):
            assert Fraction(p_count[i], total) == probability(*A)
            comparisons += 1
            for j in range(i, m):
                B = intervals[j]
                actual = Fraction(joint_count[i][j], total)
                expected = probability(*A) * probability(*B) + covariance(A, B)
                assert actual == expected, (n, A, B, actual, expected)
                if A != B and A[1] - A[0] >= 2 and B[1] - B[0] >= 2:
                    assert (actual == probability(*A)*probability(*B)) == compatible(A, B)
                comparisons += 1
        for k, triple in enumerate(valid_triples):
            value = Fraction(1)
            for i in triple:
                value *= probability(*intervals[i])
            assert Fraction(triple_count[k], total) == value
            triples_checked += 1
            comparisons += 1
        print('n={} priority_orders={} covariance_entries={} strict_laminar_triples={}'.format(
            n, total, m * (m + 1) // 2, len(valid_triples)))
    assert triples_checked >= 10
    print('PASS: {} exact rational assertions; {} nondegenerate strict-laminar triples; n<=8'.format(
        comparisons, triples_checked))


if __name__ == '__main__':
    main()

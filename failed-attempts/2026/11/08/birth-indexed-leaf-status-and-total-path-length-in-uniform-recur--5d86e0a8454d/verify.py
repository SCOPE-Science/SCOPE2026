#!/usr/bin/env python3
"""Exact finite checks for leaf-status/total-path-length covariance in recursive trees.

Python 3 standard library only. The proof is in RESULT.md; this checker tests finite sizes.
"""
from fractions import Fraction
from itertools import product
from math import factorial


def harmonics(n):
    h = [Fraction(0)]
    for k in range(1, n + 1):
        h.append(h[-1] + Fraction(1, k))
    return h


def predicted_cov(n, j, h):
    if j in (1, n):
        return Fraction(0)
    return -Fraction(j - 1, n - 1) * (h[n - 1] - h[j - 1])


def exhaustive(n):
    h = harmonics(n)
    ntrees = factorial(n - 1)
    count = 0
    sums = [0, 0, 0]
    by_index = [[0, 0] for _ in range(n + 1)]
    for parents in product(*(range(1, k) for k in range(2, n + 1))):
        depths = [0] * (n + 1)
        child_count = [0] * (n + 1)
        for k, p in enumerate(parents, 2):
            depths[k] = depths[p] + 1
            child_count[p] += 1
        total_length = sum(depths)
        leaf_flags = [0] + [int(child_count[j] == 0) for j in range(1, n + 1)]
        leaf_count = sum(leaf_flags)
        sums[0] += total_length
        sums[1] += leaf_count
        sums[2] += total_length * leaf_count
        for j in range(1, n + 1):
            by_index[j][0] += leaf_flags[j]
            by_index[j][1] += leaf_flags[j] * total_length
        count += 1
    assert count == ntrees
    mean_t = Fraction(sums[0], ntrees)
    mean_l = Fraction(sums[1], ntrees)
    assert mean_t == n * (h[n] - 1)
    assert mean_l == Fraction(n, 2)
    actual_global = Fraction(sums[2], ntrees) - mean_t * mean_l
    assert actual_global == -Fraction(n - 2, 4)
    assert sum((predicted_cov(n, j, h) for j in range(1, n + 1)), Fraction(0)) == actual_global
    tests = 5
    for j in range(1, n + 1):
        mean_x = Fraction(by_index[j][0], ntrees)
        joint_mean = Fraction(by_index[j][1], ntrees)
        cov = joint_mean - mean_x * mean_t
        assert cov == predicted_cov(n, j, h), (n, j, cov, predicted_cov(n, j, h))
        tests += 1
        if j == 1:
            assert mean_x == 0
        else:
            assert mean_x == Fraction(j - 1, n - 1)
        tests += 1
        if j > 1 and by_index[j][0]:
            conditional = joint_mean / mean_x
            assert conditional == mean_t - (h[n - 1] - h[j - 1])
            tests += 1
    return ntrees, tests


def recurrence(n):
    h = harmonics(n)
    tests = 0
    for j in range(2, n + 1):
        t = Fraction(j) * (h[j] - 1)
        for k in range(j, n):
            t = Fraction(k, k - 1) * t + 1 - h[j - 1] / (k - 1)
            actual = t - Fraction(k + 1) * (h[k + 1] - 1)
            expected = -(h[k] - h[j - 1])
            assert actual == expected, (j, k, actual, expected)
            tests += 1
    for j in range(2, n - 1):
        f_j = -predicted_cov(n, j, h)
        f_jp = -predicted_cov(n, j + 1, h)
        assert f_jp - f_j == Fraction(h[n - 1] - h[j - 1] - 1, n - 1)
        tests += 1
    return tests


def main():
    tests = 0
    total_trees = 0
    for n in range(2, 10):
        trees, numtests = exhaustive(n)
        total_trees += trees
        tests += numtests
        print(f"EXHAUSTIVE n={n}, parent_sequences={trees}, exact_assertions={numtests}")
    for n in range(2, 160):
        tests += recurrence(n)
    print(f"PASS: {tests} mathematical exact assertions, {total_trees} enumerated trees, n<=9 exhaustive, recurrences through n=159")


if __name__ == '__main__':
    main()

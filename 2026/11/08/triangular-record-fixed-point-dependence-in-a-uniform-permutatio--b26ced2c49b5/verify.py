#!/usr/bin/env python3
"""Exact small-size replay for record/fixed-point cross-covariance in uniform permutations.

This is a finite diagnostic, not a proof for all sizes; the analytic proof is supplied
in the accompanying mathematical note.
"""
from itertools import permutations
from fractions import Fraction
from math import comb, factorial


def cross_formula(n, i, j):
    if i == 1 or j > i:
        return Fraction(0)
    if j < i:
        return Fraction(1, n * i * (i - 1))
    return Fraction(1, n) * (Fraction(1, comb(n - 1, i - 1)) - Fraction(1, i))


def record_total_formula(n, i):
    return Fraction(0) if i == 1 else Fraction(1, n * comb(n - 1, i - 1))


def count_formula(n):
    return sum((record_total_formula(n, i) for i in range(1, n + 1)), Fraction(0))


def replay(n):
    all_count = factorial(n)
    a = [[0] * n for _ in range(n)]  # pairwise simultaneous counts
    r = [0] * n
    f = [0] * n
    rf = [0] * n
    t_rf = 0
    for p in permutations(range(1, n + 1)):
        marks = [int(p[j] == j + 1) for j in range(n)]
        fixed_total = sum(marks)
        max_seen = 0
        record_total = 0
        for i, value in enumerate(p):
            if value > max_seen:
                max_seen = value
                record_total += 1
                r[i] += 1
                rf[i] += fixed_total
                for j, fj in enumerate(marks):
                    a[i][j] += fj
        t_rf += record_total * fixed_total
        for j, fj in enumerate(marks):
            f[j] += fj
    assertions = 0
    for i in range(1, n + 1):
        assert Fraction(r[i-1], all_count) == Fraction(1, i)
        assertions += 1
        observed_rf = Fraction(rf[i-1], all_count) - Fraction(1, i)
        assert observed_rf == record_total_formula(n, i)
        assertions += 1
        for j in range(1, n + 1):
            actual = Fraction(a[i-1][j-1], all_count) - Fraction(r[i-1] * f[j-1], all_count**2)
            assert actual == cross_formula(n, i, j), (n, i, j, actual, cross_formula(n, i, j))
            assertions += 1
            assert Fraction(f[j-1], all_count) == Fraction(1, n)
            assertions += 1
    total_cov = Fraction(t_rf, all_count) - sum((Fraction(1, i) for i in range(1, n + 1)), Fraction(0))
    assert total_cov == count_formula(n)
    assertions += 1
    return assertions


def main():
    passed = 0
    for n in range(2, 9):
        count = replay(n)
        passed += count
        print(f"n={n}: {count} exact rational assertions passed")
    for n in range(2, 100):
        c = count_formula(n)
        assert c > 0
        assert c == Fraction(1, n) * sum((Fraction(1, comb(n-1,k)) for k in range(1, n)),Fraction(0))
        passed += 2
        # Diagonal and triangular sign classification
        for i in range(2, n + 1):
            for j in range(1, n + 1):
                x = cross_formula(n, i, j)
                if j < i:
                    assert x > 0
                elif j > i:
                    assert x == 0
                elif i <= n-2:
                    assert x < 0
                elif i == n-1:
                    assert x == 0
                else:
                    assert x > 0
                passed += 1
    print(f"TOTAL PASSED: {passed} exact rational assertions")


if __name__ == "__main__":
    main()

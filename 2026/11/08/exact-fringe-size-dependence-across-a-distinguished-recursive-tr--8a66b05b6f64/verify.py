"""Exact finite checks for the descendant/fringe-size covariance theorem.

Run: python verify.py
Standard library only. All arithmetic is exact.
"""
from fractions import Fraction
from itertools import product
from math import factorial


def mu(m, k):
    if m < k:
        return Fraction(0)
    if m == k:
        return Fraction(1)
    return Fraction(m, k * (k + 1))


def conditional_expectation(n, k, s):
    return mu(s, k) + mu(n - s, k) - int(n - s == k)


def sizes_for_parents(parents):
    n = len(parents) + 1
    subtree = [1] * (n + 1)
    for v in range(n, 1, -1):
        subtree[parents[v - 2]] += subtree[v]
    return subtree[1:]


def exact_exhaustive(n):
    domain = [range(1, v) for v in range(2, n + 1)]
    total = factorial(n - 1)
    mass = [0] * (n + 1)
    sum_s = 0
    sum_z = [0] * n
    sum_sz = [0] * n
    conditional_sum = [[0] * n for _ in range(n + 1)]
    actual_total = 0
    for parents in product(*domain):
        subtree = sizes_for_parents(parents)
        s = subtree[1]
        mass[s] += 1
        sum_s += s
        actual_total += 1
        cnt = [0] * (n + 1)
        for size in subtree:
            cnt[size] += 1
        for k in range(1, n):
            z = cnt[k]
            sum_z[k] += z
            sum_sz[k] += s * z
            conditional_sum[s][k] += z
    assert actual_total == total
    assert Fraction(sum_s, total) == Fraction(n, 2)
    assertions = 2
    for s in range(1, n):
        assert Fraction(mass[s], total) == Fraction(1, n - 1)
        assertions += 1
    for k in range(1, n):
        assert Fraction(sum_z[k], total) == mu(n, k)
        cov = Fraction(sum_sz[k], total) - Fraction(sum_s * sum_z[k], total * total)
        assert cov == Fraction(2 * k - n, 2 * (n - 1)), (n, k, cov)
        assertions += 2
        for s in range(1, n):
            assert Fraction(conditional_sum[s][k], mass[s]) == conditional_expectation(n, k, s), (n, k, s)
            assertions += 1
    return total, assertions


def recurrence_checks():
    checks = 0
    # The fringe-count expectation follows from the exact insertion transitions.
    for n in range(1, 121):
        expected_leaf = (Fraction(0) if n == 0 else mu(n, 1))
        assert mu(n + 1, 1) == (1 - Fraction(1, n)) * expected_leaf + 1
        checks += 1
        for k in range(2, n + 1):
            rhs = (1 - Fraction(k, n)) * mu(n, k) + Fraction(k - 1, n) * mu(n, k - 1)
            assert mu(n + 1, k) == rhs, (n, k)
            checks += 1
    # The two-colour component sizes have the Pólya transition; check uniformity.
    distribution = {1: Fraction(1)}  # n=2, S_2=1
    for n in range(2, 121):
        assert len(distribution) == n - 1
        for s in range(1, n):
            assert distribution[s] == Fraction(1, n - 1)
            checks += 1
        new = {s: Fraction(0) for s in range(1, n + 1)}
        for s, p in distribution.items():
            new[s + 1] += p * Fraction(s, n)
            new[s] += p * Fraction(n - s, n)
        distribution = new
    return checks


def main():
    checks = recurrence_checks()
    counts = []
    for n in range(2, 10):
        num, c = exact_exhaustive(n)
        counts.append((n, num))
        checks += c
    print('PASS: %d exact rational assertions' % checks)
    print('Exhaustive recursive-tree counts:', counts)
    print('Exact insertion recurrences: n <= 120; Pólya size law: n <= 120')


if __name__ == '__main__':
    main()

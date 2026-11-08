#!/usr/bin/env python3
"""Exact rational checks of fixed-point/descent covariances under Ewens laws.

Uses only the Python standard library. Enumeration checks small sample sizes;
the general theorem requires the symbolic argument in RESULT.md.
"""
from collections import defaultdict
from fractions import Fraction as Q
from itertools import permutations


def cycle_count(p):
    visited = set()
    answer = 0
    for start in range(len(p)):
        if start not in visited:
            answer += 1
            current = start
            while current not in visited:
                visited.add(current)
                current = p[current] - 1
    return answer


def moment_counts(n):
    """Unnormalised cycle-count-stratified exact integer moments."""
    totals = defaultdict(int)
    fix = [defaultdict(int) for _ in range(n)]
    desc = [defaultdict(int) for _ in range(n)]
    joint = [[defaultdict(int) for _ in range(n)] for _ in range(n)]
    for p in permutations(range(1, n + 1)):
        c = cycle_count(p)
        totals[c] += 1
        f = [int(p[j] == j + 1) for j in range(n)]
        d = [int(p[i] > p[(i + 1) % n]) for i in range(n)]
        for j in range(n):
            if f[j]:
                fix[j][c] += 1
                for i in range(n):
                    if d[i]:
                        joint[j][i][c] += 1
        for i in range(n):
            if d[i]:
                desc[i][c] += 1
    return totals, fix, desc, joint


def eval_poly(counter, theta):
    return sum((Q(v) * theta ** c for c, v in counter.items()), Q(0))


def predicted(n, theta, j, i):
    """One-indexed j (fixed point) and i (ordinary descent)."""
    assert n >= 3 and 1 <= j <= n and 1 <= i < n
    t = theta
    def q(size):
        return Q(size - 1) * (Q(size, 2) + t - 1) / ((size + t - 1) * (size + t - 2))
    if j == i:
        conditional = Q(i - 1) / (n + t - 2)
    elif j == i + 1:
        conditional = Q(n - i - 1) / (n + t - 2)
    else:
        conditional = q(n - 1)
    return t / (n + t - 1) * (conditional - q(n))


def predicted_circular_total(n, theta):
    t = theta
    return -Q(n) * t * (n - 2) * (t - 1) * (n + 2 * t - 3) / (
        (n + t - 3) * (n + t - 2) * (n + t - 1) ** 2)


def predicted_ordinary_total(n, theta):
    t = theta
    return -t * t * (n - 1) * (n * n + 2 * n * t - 4 * n - 2 * t + 2) / (
        (n + t - 3) * (n + t - 2) * (n + t - 1) ** 2)


def run():
    comparisons = 0
    for n in range(3, 9):
        totals, fix, desc, joint = moment_counts(n)
        for theta in (Q(1, 3), Q(1, 2), Q(3, 4), Q(1), Q(3, 2), Q(2), Q(5)):
            z = eval_poly(totals, theta)
            f_expect = [eval_poly(fix[j], theta) / z for j in range(n)]
            d_expect = [eval_poly(desc[i], theta) / z for i in range(n)]
            covariance = [
                [eval_poly(joint[j][i], theta) / z - f_expect[j] * d_expect[i]
                 for i in range(n)]
                for j in range(n)]
            for j in range(n):
                for i in range(n - 1):
                    assert covariance[j][i] == predicted(n, theta, j + 1, i + 1), (n, theta, j, i)
                    comparisons += 1
            ordinary = sum((covariance[j][i] for j in range(n) for i in range(n - 1)), Q(0))
            circular = ordinary + sum((covariance[j][n - 1] for j in range(n)), Q(0))
            assert ordinary == predicted_ordinary_total(n, theta), (n, theta, ordinary)
            assert circular == predicted_circular_total(n, theta), (n, theta, circular)
            comparisons += 2
            if theta == 1:
                assert circular == 0
                comparisons += 1
    print(f"PASS: {comparisons} exact rational checks; all permutations through n=8; seven theta values")


if __name__ == "__main__":
    run()

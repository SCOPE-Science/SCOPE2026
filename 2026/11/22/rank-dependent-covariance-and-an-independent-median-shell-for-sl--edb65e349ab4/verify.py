"""Exact small-width checks of change covariance at one window's separation."""

from fractions import Fraction
from itertools import permutations
from math import comb, factorial


def covariance_formula(k, j):
    p = [0] * (k + 1)
    for a in range(j, k + 1):
        for b in range(k - a + 1):
            p[a + b] += comb(k, a) * comb(k - a, b) * (-1) ** b
    mean = sum(Fraction(c, i + 1) for i, c in enumerate(p))
    square_mean = sum(Fraction(c * d, i + l + 1)
                      for i, c in enumerate(p) for l, d in enumerate(p))
    return Fraction((k + 1 - 2 * j) ** 2, k * k) * (square_mean - mean ** 2)


def covariance_by_order(k):
    ranks = range(1, k - 1)  # zero-based interior ranks
    counts = [[0, 0, 0] for _ in ranks]
    for order in permutations(range(2 * k + 1)):
        a, b = sorted(order[:k]), sorted(order[1:k + 1])
        c, d = sorted(order[k:2 * k]), sorted(order[k + 1:])
        for m, r in enumerate(ranks):
            left, right = a[r] != b[r], c[r] != d[r]
            counts[m][0] += left
            counts[m][1] += right
            counts[m][2] += left and right
    n = factorial(2 * k + 1)
    return [Fraction(n * both - left * right, n * n)
            for left, right, both in counts]


if __name__ == "__main__":
    for k in (3, 4):
        observed = covariance_by_order(k)
        expected = [covariance_formula(k, j) for j in range(2, k)]
        assert observed == expected, (k, observed, expected)
        print(f"width {k}, interior ranks: {', '.join(map(str, observed))}")

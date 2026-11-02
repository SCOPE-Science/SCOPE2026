"""Finite combinatorial and numerical checks for Haar simplex-section vertex counts.

Analytic proofs of the infinite-dimensional limit are given in RESULT.md.
"""
from itertools import combinations
from fractions import Fraction
from math import asin, erf, pi, sqrt

import numpy as np


def exact_expected_vertices(m):
    return m * (m - 1) / 4 + m * (m - 1) * asin(1 / (m - 1)) / (2 * pi)


def crossing_points(a):
    n = len(a)
    points = []
    for i, j in combinations(range(n), 2):
        if a[i] * a[j] < 0:
            lam_i = Fraction(-a[j], a[i] - a[j])
            lam_j = Fraction(a[i], a[i] - a[j])
            point = [Fraction(0) for _ in a]
            point[i], point[j] = lam_i, lam_j
            assert all(w >= 0 for w in point)
            assert sum(point) == 1
            assert sum(point[k] * a[k] for k in range(n)) == 0
            points.append(tuple(point))
    return points


def check_sign_patterns():
    pattern_count = 0
    for m in range(3, 10):
        indices = range(m)
        for k in range(1, m):
            for subset in combinations(indices, k):
                positives = set(subset)
                a = [m - k if i in positives else -k for i in indices]
                assert sum(a) == 0
                points = crossing_points(a)
                assert len(points) == k * (m - k)
                assert len(set(points)) == len(points)
                pattern_count += 1
    return pattern_count


def simulate(m, trials, rng):
    counts = []
    remaining = trials
    while remaining:
        rows = min(2000, remaining)
        z = rng.standard_normal((rows, m))
        k = np.sum(z > z.mean(axis=1, keepdims=True), axis=1)
        counts.append(k)
        remaining -= rows
    k = np.concatenate(counts)
    n = k * (m - k)
    mean = float(np.mean(n))
    expected = exact_expected_vertices(m)
    assert abs(mean - expected) < max(0.045, 0.013 * m), (m, mean, expected)
    sigma2 = 1 / 4 - 1 / (2 * pi)
    variance = float(np.var((k - m / 2) / sqrt(m)))
    if m >= 10:
        assert abs(variance - sigma2) < 0.017, (m, variance, sigma2)
    if m >= 200:
        deficit = (m * m / 4 - n) / m
        for threshold in [0.5, 1.0, 2.0]:
            observed = float(np.mean(deficit <= sigma2 * threshold))
            chi1_cdf = erf(sqrt(threshold / 2))
            assert abs(observed - chi1_cdf) < 0.035, (m, threshold, observed, chi1_cdf)
    return mean, expected, variance


def main():
    patterns = check_sign_patterns()
    assert patterns == sum(2**m - 2 for m in range(3, 10))
    assert abs(exact_expected_vertices(3) - 2) < 1e-12
    assert abs(exact_expected_vertices(4) - 3.649040687816356) < 1e-11
    rng = np.random.default_rng(1952)
    for m, trials in [(3, 20_000), (4, 40_000), (5, 40_000),
                      (10, 50_000), (50, 50_000), (250, 30_000), (1000, 15_000)]:
        mean, expected, variance = simulate(m, trials, rng)
        print(f'm={m}, draws={trials}, mean={mean:.6f}, exact_mean={expected:.6f}, normalized_sign_variance={variance:.6f}')
    print(f'exact_sign_patterns={patterns}')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""Finite sanity checks for the real scalar-sum norm-attainment trichotomy.

These computations do not prove the infinite-dimensional theorem.
"""
import math


def supdiff(x):
    return max(abs(x[i] - x[i + 1]) for i in range(len(x) - 1))


def value(x, weights, p):
    h = sum(a * xi for a, xi in zip(weights, x))
    return (supdiff(x) ** p + abs(h) ** p) ** (1.0 / p)


def run():
    total = 0
    for p in [1, 2, 3, 8, 32]:
        target = (2 ** p + 1) ** (1.0 / p)
        for n in [5, 12, 25, 50]:
            weights = [2.0 ** (-j - 1) for j in range(n + 3)]
            x = [1.0] * (n + 1) + [-1.0, 0.0]
            observed = value(x, weights, p)
            assert observed < target + 1e-12
            assert observed > (2 ** p + (1 - 3 * 2.0 ** (-n - 2)) ** p) ** (1.0 / p) - 1e-10
            total += 2
        # A weight vector with a zero coordinate has an exact bidual witness.
        weights = [0.5, 0.0, 0.5, 0.0, 0.0]
        x = [1.0, -1.0, 1.0, 1.0, 1.0]
        assert math.isclose(value(x, weights, p), target, abs_tol=1e-12)
        total += 1
        assert 1 <= 2 ** (1 / p) <= 2
        total += 1
    print('diagnostic checks passed:', total)


if __name__ == '__main__':
    run()

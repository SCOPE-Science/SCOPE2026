#!/usr/bin/env python3
"""Independent exact-rational checks for first collision versus full coverage."""
from fractions import Fraction
from math import pi, sqrt


def covariance_from_tail(m):
    """Closed form from collision-free prefix probabilities."""
    survival = Fraction(1)
    penalty = Fraction(0)
    total = Fraction(0)
    for b in range(1, m + 1):
        survival *= Fraction(m - b + 1, m)
        if b >= 2:
            penalty += Fraction(b - 1, m - b + 1)
            total -= survival * penalty
    return total


def covariance_from_independent_markov_recursion(m):
    """Recursively compute independent first-repeat/cover mixed moments.

    State r = number of distinct labels; process is collision-free so far.
    f[r] = expected remaining time to first repeat.
    t[r] = expected remaining time to full coverage.
    h[r] = expected product of those remaining times.
    """
    t = [Fraction(0) for _ in range(m + 1)]
    f = [Fraction(0) for _ in range(m + 1)]
    h = [Fraction(0) for _ in range(m + 1)]
    f[m] = Fraction(1)
    for r in range(m - 1, -1, -1):
        p = Fraction(r, m)
        s = 1 - p
        t[r] = Fraction(1, s) + t[r + 1]
        f[r] = 1 + s * f[r + 1]
        # An immediate repeat finishes first-repeat time at one step;
        # a new label continues both waiting times at state r+1.
        h[r] = p * (1 + t[r]) + s * (
            1 + f[r + 1] + t[r + 1] + h[r + 1]
        )
    return h[0] - f[0] * t[0]


def conditional_mean(m, b):
    if b == m + 1:
        return Fraction(m)
    return Fraction(b) + sum((Fraction(m, j) for j in range(1, m - b + 2)), Fraction(0))


def harmonic(m):
    return sum((Fraction(1, j) for j in range(1, m + 1)), Fraction(0))


def float_scaled_covariance(m):
    survival = 1.0
    penalty = 0.0
    total = 0.0
    for b in range(1, m + 1):
        survival *= (m - b + 1) / m
        if b >= 2:
            penalty += (b - 1) / (m - b + 1)
            total -= survival * penalty
    return total / sqrt(m)


def float_scaled_correlation(m):
    s = 1.0
    mean_b = 1.0
    second_b = 1.0
    for b in range(1, m + 1):
        s *= (m - b + 1) / m
        mean_b += s
        second_b += (2 * b + 1) * s
    var_b = second_b - mean_b * mean_b
    var_c = m * m * sum(1 / (j * j) for j in range(1, m + 1)) - m * sum(1 / j for j in range(1, m + 1))
    return m * float_scaled_covariance(m) * sqrt(m) / sqrt(var_b * var_c)


def main():
    comparisons = 0
    for m in range(2, 61):
        a = covariance_from_tail(m)
        b = covariance_from_independent_markov_recursion(m)
        assert a == b, (m, a, b)
        assert a < 0, (m, a)
        comparisons += 2
        hm = harmonic(m)
        for index in range(2, m + 1):
            expected = Fraction(m) * hm + 1 - sum(
                (Fraction(r, m - r) for r in range(1, index - 1)), Fraction(0)
            )
            assert conditional_mean(m, index) == expected, (m, index)
            comparisons += 1
        assert conditional_mean(m, m + 1) == m
        comparisons += 1
    print(f"PASS: {comparisons} exact-rational comparisons, m=2..60")
    target = -sqrt(pi / 8)
    for m in (100, 1000, 10000):
        print(f"m={m}: covariance/sqrt(m)={float_scaled_covariance(m):.10f}")
    print(f"Analytic covariance limit={target:.10f}")
    target_corr = -sqrt(3 / (2 * pi * (4 - pi)))
    for m in (100, 1000, 10000):
        print(f"m={m}: m*correlation={float_scaled_correlation(m):.10f}")
    print(f"Analytic correlation limit={target_corr:.10f}")
    print("Finite checks do not prove the limiting or all-size claims.")


if __name__ == "__main__":
    main()

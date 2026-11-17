"""Reproducible finite checks for a random interval map and reflected walk.

The infinite results are proved analytically in RESULT.md.
"""
from fractions import Fraction
from math import floor, log2, sqrt, pi
import random


def dyadic_depth(x):
    if not 0 < x < 1:
        raise ValueError("input must lie strictly between zero and one")
    depth = 0
    while x < Fraction(1, 2 ** (depth + 1)):
        depth += 1
    return depth


def exact_trajectory(seed, p, steps=230):
    rng = random.Random(seed)
    # Nondyadic rational prevents accidental exact absorption at zero.
    x = Fraction(5 + seed, 1000003 + 2 * seed)
    m = dyadic_depth(x)
    w = m
    biggest_geom = 0
    highest_gap = 0
    for _ in range(steps):
        expansion = rng.random() < p
        old = m
        if expansion:
            x = (2 * x) % 1
            sign = -1
        else:
            x = x / 2
            sign = 1
        m = dyadic_depth(x)
        w = max(0, w + sign)
        if old == 0 and expansion:
            biggest_geom = max(biggest_geom, m)
        assert 0 <= m - w <= biggest_geom, (m, w, biggest_geom)
        highest_gap = max(highest_gap, m - w)
    return highest_gap


def simulated_scaled_reflection_mean(seed, n=1200, samples=1000):
    rng = random.Random(seed)
    total = 0.0
    for _ in range(samples):
        w = 0
        for _ in range(n):
            w = max(0, w + (1 if rng.random() < 0.5 else -1))
        total += w / sqrt(n)
    return total / samples


def main():
    gaps = [exact_trajectory(seed, p) for seed in range(1, 9) for p in (0.40, 0.50, 0.70, 0.90)]
    assert min(gaps) >= 0
    empirical = simulated_scaled_reflection_mean(43)
    expected = sqrt(2 / pi)
    assert abs(empirical - expected) < 0.12, (empirical, expected)
    print("PELIKAN_OPTIMAL_LOG_COUPLING_CHECK_OK", "max_gap", max(gaps), "mean", round(empirical, 5))

if __name__ == "__main__":
    main()

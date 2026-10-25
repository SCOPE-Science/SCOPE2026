"""Supplementary finite checks for a log-weighted measure on [0,1].

The mathematical statements are established analytically in RESULT.md;
finite sampling does not prove an all-scale inequality.
"""
import math
import random


def primitive(t):
    return 0.0 if t <= 0 else 2 * t - t * math.log(t)


def mass(x, r):
    a = max(0.0, x - r)
    b = min(1.0, x + r)
    return primitive(b) - primitive(a)


def check():
    rng = random.Random(1043)
    worst_lower_slack = float("inf")
    largest_doubling = 0.0
    for _ in range(6000):
        x = rng.random()
        r = 10 ** (-10 * rng.random())
        factor = 1 + (1 / r - 1) * rng.random()
        R = r * factor
        smaller, larger = mass(x, r), mass(x, R)
        required = factor / (4 * (1 + math.log(factor)))
        slack = larger / (smaller * required)
        worst_lower_slack = min(worst_lower_slack, slack)
        assert slack >= 1 - 1e-9
        doubling = mass(x, 2 * r) / smaller
        largest_doubling = max(largest_doubling, doubling)
        assert doubling <= 8 + 1e-9
    for n in range(1, 10):
        r = 10 ** (-n)
        expected = 2 - math.log(r)
        obtained = mass(0, r) / r
        assert math.isclose(obtained, expected, rel_tol=1e-12, abs_tol=1e-12)
    print("FINITE_SAMPLE_CHECK_OK")
    print("minimal_observed_slack:", worst_lower_slack)
    print("maximal_observed_doubling:", largest_doubling)


if __name__ == "__main__":
    check()

#!/usr/bin/env python3
"""Independent-geometry numerical checks and exact fractions for a circular flowering theorem."""
from fractions import Fraction as F
import math
import random


def segments(center, length, period):
    a = (center - length / 2) % period
    b = (center + length / 2) % period
    return [(a, b)] if a <= b else [(0.0, b), (a, period)]


def intersection_geom(center1, center2, length1, length2, period):
    return sum(max(0.0, min(b, y) - max(a, x))
               for a, b in segments(center1, length1, period)
               for x, y in segments(center2, length2, period))


def intersection_formula(length1, length2, gap, period):
    u = (length1 + length2) / 2
    t = abs(length1 - length2) / 2
    return max(0.0, min(u - t, u - gap)) + max(0.0, min(u - t, u - (period - gap)))


def run():
    rng = random.Random(73)
    count = 0
    for _ in range(50000):
        period = rng.uniform(.5, 3)
        gap = period * rng.uniform(.0001, .4999)
        a = period * rng.uniform(.0001, .9999)
        b = period * rng.uniform(.0001, .9999)
        actual = intersection_geom(.12 * period, .12 * period + gap, a, b, period)
        formula = intersection_formula(a, b, gap, period)
        assert math.isclose(actual, formula, rel_tol=1e-8, abs_tol=1e-9)
        count += 1
    for _ in range(10000):
        period = rng.uniform(.2, 7)
        gap = period * rng.uniform(.0001, .4999)
        u = rng.uniform(gap, period - gap)
        max_t = min(u, period - u)
        def cov(t):
            h = min(u - t, u - gap)
            return h / period - (u * u - t * t) / (period * period)
        best = cov(gap)
        assert best > 0
        assert math.isclose(best, (u-gap)*(period-u-gap)/(period*period), abs_tol=1e-10)
        assert math.isclose(best - cov(0), (gap/period)**2, abs_tol=1e-10)
        for _ in range(10):
            assert best > cov(rng.uniform(0, max_t)) - 1e-10
        count += 1
    period = F(1)
    gap = F(3, 10)
    u = F(1, 2)
    joint = u - gap
    a = joint - u * u
    b = joint - (u + gap) * (u - gap)
    assert joint == F(1, 5)
    assert a == F(-1, 20)
    assert b == F(1, 25)
    assert b-a == F(9, 100)
    assert (period-u-gap, 2*gap, u-gap) == (F(1,5), F(3,5), F(1,5))
    print(f"PASS: {count} randomized geometry/optimization cases and exact rational witness")

if __name__ == '__main__':
    run()

#!/usr/bin/env python3
"""Supplemental, deterministic numerical checks for a fragment-survival bound.

The mathematical proof is in RESULT.md; these finite checks are not an
exhaustive or independent verification of the infinite-dimensional theorem.
"""
import math
import random

TESTS = 0


def check(predicate, message):
    global TESTS
    TESTS += 1
    if not predicate:
        raise AssertionError(message)


def info(z):
    if z <= 0.0:
        raise ValueError("z must be positive")
    return -math.log(-math.expm1(-z))


def q(d, z):
    return d * info(z) - z / math.expm1(z)


def zstar(d):
    left = 1.0e-14
    right = d
    check(q(d, left) > 0.0, "wrong left root bracket")
    check(q(d, right) < 0.0, "wrong right root bracket")
    for _ in range(90):
        center = (left + right) / 2.0
        if q(d, center) > 0.0:
            left = center
        else:
            right = center
    return (left + right) / 2.0


def bound_exponent(d, b, volume):
    z = zstar(d)
    return volume / (b ** d) * (z ** d) * info(z)


def exponent(d, b, parts):
    return sum(info(b / (v ** (1.0 / d))) for v in parts)


def equal_exponent(d, b, volume, count):
    return count * info(b * (count / volume) ** (1.0 / d))


def run():
    rng = random.Random(283410)
    check(abs(zstar(1.0) - math.log(2)) < 1e-12, "d=1 closed form")
    check(abs(zstar(2.0) - 1.8303008606800313) < 1e-12, "d=2 root")
    check(abs(zstar(3.0) - 2.917384703823087) < 1e-12, "d=3 root")

    for d in [0.25, 0.5, 1.0, 1.5, 2.0, 3.0, 5.0, 7.0]:
        z = zstar(d)
        check(0 < z < d, "root location")
        for fraction in [0.1, 0.3, 0.55, 0.8, 0.99]:
            check(q(d, z * fraction) > 0, "q sign left")
            check(q(d, z + (d + 2 - z) * fraction) < 0, "q sign right")
        check(abs(q(d, z)) < 1e-10, "root residual")
        # Sharp equality at an integer number of preferred fragments.
        for n in range(1, 8):
            b = 1.1
            vstar = (b / z) ** d
            exact = exponent(d, b, [vstar] * n)
            limit = bound_exponent(d, b, n * vstar)
            check(abs(exact - limit) < 1e-9 * max(1, exact), "equality")

    for trial in range(12000):
        d = rng.uniform(0.25, 5.0)
        b = rng.uniform(0.5, 2.0)
        n = rng.randrange(1, 20)
        # Relative sizes kept moderate for numerical stability.
        parts = [rng.uniform(0.02, 4.0) for _ in range(n)]
        total = sum(parts)
        exp_value = exponent(d, b, parts)
        upper = bound_exponent(d, b, total)
        check(exp_value <= upper + 1e-10 * max(1.0, upper), "partition bound")

    for trial in range(2500):
        d = rng.uniform(0.5, 3.0)
        b = rng.uniform(0.8, 1.7)
        v = rng.uniform(0.2, 3.0)
        real_k = v * (zstar(d) / b) ** d
        first = max(1, math.floor(real_k))
        second = max(1, math.ceil(real_k))
        predicted = max(equal_exponent(d, b, v, first),
                        equal_exponent(d, b, v, second))
        direct = max(equal_exponent(d, b, v, k) for k in range(1, 401))
        check(abs(predicted - direct) < 1e-11 * max(1.0, direct),
              "equal-size integer comparison (k <= 400)")

    print("PASS: %d finite supplemental assertions" % TESTS)
    for d in [1.0, 2.0, 3.0]:
        z = zstar(d)
        print("dimension %.0f: z*=%.12f, preferred volume/b^d=%.12f, survival at preferred volume=%.12f" %
              (d, z, z ** (-d), math.exp(-z)))


if __name__ == "__main__":
    run()

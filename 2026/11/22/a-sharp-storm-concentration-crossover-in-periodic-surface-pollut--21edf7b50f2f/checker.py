"""Supplementary deterministic checks for a periodic surface-wash-off theorem.

This script checks the algebraic steady-cycle formulas and policy comparisons.
The infinite-parameter theorem rests on the analytic proof, not on sampling.
Requires only Python 3 standard library.
"""
from math import exp, expm1, cosh, acosh, sqrt, sinh, isclose
from random import Random


def coth(x):
    assert x > 0
    return 1.0 + 2.0 / expm1(2.0 * x)


def mean_formula(rate, period, kappa, rain, power, equal):
    dose = kappa * (rain / 2.0 if equal else rain) ** power
    return rate * period * coth(dose / 2.0) / (4.0 if equal else 2.0)


def mean_recurrence(rate, period, kappa, rain, power, equal):
    # Explicit fixed point of a two-step affine recurrence, followed by
    # the two exactly integrated dry-period loads.
    h = period / 2.0
    r1, r2 = (rain / 2.0, rain / 2.0) if equal else (rain, 0.0)
    s1, s2 = exp(-kappa * r1**power), exp(-kappa * r2**power)
    q = s1 * s2
    first = rate * h * s2 * (1.0 + s1) / (1.0 - q)
    second = s1 * (first + rate * h)
    return (h * first + rate * h * h / 2.0 +
            h * second + rate * h * h / 2.0) / period


def normalized_ratio(x, power):
    c = 2.0 ** (power - 1.0)
    return coth(x / 2.0) / coth(c * x)


def solve_transition(power):
    assert power > 1.0
    lo, hi = 1e-12, 1.0
    while normalized_ratio(hi, power) > 2.0:
        hi *= 2.0
    for _ in range(90):
        m = (lo + hi) / 2
        if normalized_ratio(m, power) > 2:
            lo = m
        else:
            hi = m
    return (lo + hi) / 2


def run():
    rng = Random(314159)
    assertions = 0
    for _ in range(12000):
        rate = exp(rng.uniform(-2, 2))
        period = exp(rng.uniform(-2, 2))
        kappa = exp(rng.uniform(-2, 2))
        rain = exp(rng.uniform(-1, 1))
        power = rng.uniform(.2, 4.0)
        for equal in (True, False):
            analytic = mean_formula(rate, period, kappa, rain, power, equal)
            recurrence = mean_recurrence(rate, period, kappa, rain, power, equal)
            assert isclose(analytic, recurrence, rel_tol=2e-10, abs_tol=1e-10)
            assertions += 1
        x = kappa * (rain / 2)**power
        left = mean_formula(rate, period, kappa, rain, power, True)
        right = mean_formula(rate, period, kappa, rain, power, False)
        assert isclose(left / right, normalized_ratio(x, power) / 2, rel_tol=2e-10)
        assertions += 1
        if power <= 1:
            assert left < right
            assertions += 1
    for p in (1.001, 1.1, 1.3, 1.7, 2, 2.5, 3.5, 5, 8):
        star = solve_transition(p)
        assert abs(normalized_ratio(star, p) - 2) < 2e-10
        assert normalized_ratio(star / 2, p) > 2
        assert normalized_ratio(star * 2, p) < 2
        assertions += 3
    golden = (1.0 + sqrt(5.0)) / 2.0
    star = acosh(golden)
    assert isclose(normalized_ratio(star, 2), 2.0, rel_tol=2e-14)
    assert isclose(cosh(star)**2 - cosh(star) - 1, 0.0, abs_tol=2e-14)
    assertions += 2
    for p in (.3, .9, 1, 1.1, 2, 4):
        xs = [0.015 * (1.03**i) for i in range(170)]
        rs = [normalized_ratio(x, p) for x in xs]
        assert all(a > b for a, b in zip(rs, rs[1:]))
        assertions += 1
    print(f'PASS: {assertions} supplementary assertions; quadratic crossover x*={star:.12f}')


if __name__ == '__main__':
    run()

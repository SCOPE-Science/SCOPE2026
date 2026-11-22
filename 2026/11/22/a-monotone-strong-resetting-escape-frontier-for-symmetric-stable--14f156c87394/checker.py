#!/usr/bin/env python3
"""Finite numerical consistency tests for a stable-flight escape frontier.
Analytic monotonicity and infinite-time limits are proved in RESULT.md, not by this script.
Requires Python 3 standard library only.
"""
import math


def levy_coefficient(alpha):
    return (alpha * 2.0 ** (alpha - 1.0)
            * math.gamma((alpha + 1.0) / 2.0)
            / (math.sqrt(math.pi) * math.gamma(1.0 - alpha / 2.0)))


def direct_ratio(alpha, y):
    c = levy_coefficient(alpha)
    intensity = c / alpha * ((1.0 - y) ** (-alpha) + (1.0 + y) ** (-alpha))
    free_mean = (1.0 - y * y) ** (alpha / 2.0) / math.gamma(1.0 + alpha)
    return (1.0 / intensity) / free_mean


def closed_ratio(alpha, y):
    c = math.pi * alpha / (2.0 * math.sin(math.pi * alpha / 2.0))
    return c / math.cosh(alpha * math.atanh(y))


def frontier(alpha):
    c = math.pi * alpha / (2.0 * math.sin(math.pi * alpha / 2.0))
    return math.tanh(math.acosh(c) / alpha)


def assert_near(a, b, rel=3e-11, abs_=3e-11):
    assert math.isclose(a, b, rel_tol=rel, abs_tol=abs_), (a, b)


N = 0
for i in range(1, 199):
    alpha = i / 100.0
    for j in range(0, 19):
        y = j / 20.0
        assert_near(direct_ratio(alpha, y), closed_ratio(alpha, y))
        N += 1
    boundary = frontier(alpha)
    assert_near(closed_ratio(alpha, boundary), 1.0)
    assert closed_ratio(alpha, boundary / 2.0) > 1.0
    assert closed_ratio(alpha, (1.0 + boundary) / 2.0) < 1.0
    N += 3
for i in range(1, 1999):
    assert frontier(i / 1000.0) < frontier((i + 1) / 1000.0)
    N += 1
assert_near(frontier(1.0), math.sqrt(1.0 - 4.0 / math.pi ** 2))
N += 1
lim = math.tanh(math.pi / (2.0 * math.sqrt(3.0)))
assert abs(frontier(0.001) - lim) < 1e-5
N += 1
for eps in [1e-2, 1e-3, 1e-4]:
    assert abs((1.0 - frontier(2.0 - eps)) / eps - 0.5) < 0.03
    N += 1
print(f"PASS: {N} independent finite consistency assertions")
print(f"Cauchy-frontier check: {frontier(1.0):.12f}")
print(f"Small-index frontier limit: {lim:.12f}")
print("Analytical claims require the proof; these finite checks do not establish them.")

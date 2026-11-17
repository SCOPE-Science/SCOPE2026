"""Finite diagnostic checks for the sharp planar conic-spline constants.

Run: python3 verify.py
Only standard Python libraries are used. The universal inequalities are
proved analytically in RESULT.md; these finite tests are supplementary.
"""
import math
import random

PI = math.pi


def green_abs(h, s, t):
    return math.sin(min(s, t)) * math.sin(h - max(s, t)) / math.sin(h)


def profile(theta, alpha):
    return abs(math.sin(theta - alpha))


def conic_interpolant(theta, alpha, left, h):
    s = theta - left
    return (profile(left, alpha) * math.sin(h - s)
            + profile(left + h, alpha) * math.sin(s)) / math.sin(h)


def trapezoid(func, a, b, panels=2048):
    step = (b - a) / panels
    total = 0.5 * (func(a) + func(b))
    for j in range(1, panels):
        total += func(a + j * step)
    return step * total


def close(actual, expected, tol=3e-6):
    if abs(actual - expected) > tol * max(1.0, abs(expected)):
        raise AssertionError((actual, expected))


def run():
    rng = random.Random(261106212)
    checks = 0
    for _ in range(60):
        h = rng.uniform(0.10, 2.90)
        t = rng.uniform(0.02 * h, 0.98 * h)
        # Exact integral of the Dirichlet Green kernel.
        integral = trapezoid(lambda s: green_abs(h, s, t), 0.0, h)
        formula = math.cos(t - 0.5 * h) / math.cos(0.5 * h) - 1.0
        close(integral, formula)
        checks += 1
        assert formula <= 1.0 / math.cos(h / 2.0) - 1.0 + 1e-12
        checks += 1
        assert green_abs(h, t, t) <= 0.5 * math.tan(h / 2.0) + 1e-12
        checks += 1
    for n in range(2, 10):
        for _ in range(8):
            raw = [rng.uniform(0.6, 2.0) for __ in range(n)]
            gaps = [PI * v / sum(raw) for v in raw]
            k = max(range(n), key=lambda j: gaps[j])
            left = sum(gaps[:k]); h = gaps[k]; alpha = left + 0.5 * h
            # For the seminorm q(x)=|<x,v>|, curvature variation equals 4.
            M = 4.0
            C_inf = 0.25 * math.tan(h / 2.0)
            C_one = 1.0 / math.cos(h / 2.0) - 1.0
            peak = conic_interpolant(alpha, alpha, left, h) - profile(alpha, alpha)
            close(peak / M, C_inf, 1e-12)
            checks += 1
            one_cell = trapezoid(lambda s: abs(conic_interpolant(left+s, alpha, left, h)
                                                         - profile(left+s, alpha)), 0.0, h)
            # Exactly two antipodal cells contribute.
            close(2.0 * one_cell / M, C_one)
            checks += 1
            assert h >= PI/n - 1e-12
            checks += 1
    print('PASS: %d deterministic finite checks; exact proof in RESULT.md' % checks)


if __name__ == '__main__':
    run()

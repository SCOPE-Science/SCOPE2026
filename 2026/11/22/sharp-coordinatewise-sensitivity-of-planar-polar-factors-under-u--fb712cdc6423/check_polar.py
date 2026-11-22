"""Reproducible supplementary tests for a sharp planar polar-factor bound.

The mathematical proof is in RESULT.md; numerical tests are not a proof.
Run: python3 check_polar.py
Requires only the Python standard library.
"""
import math
import random

ROOT17 = math.sqrt(17.0)
TSTAR = (ROOT17 - 3.0) / 4.0
C = math.sqrt((71.0 + 17.0 * ROOT17) / 108.0)


def polar(a):
    u = a[0][0] + a[1][1]
    v = a[1][0] - a[0][1]
    r = math.hypot(u, v)
    assert u > 0.0
    return ((u / r, -v / r), (v / r, u / r))


def max_entry(a):
    return max(abs(z) for row in a for z in row)


def subtract(a, b):
    return tuple(tuple(a[i][j] - b[i][j] for j in range(2)) for i in range(2))


def add_scaled(a, h, t):
    return tuple(tuple(a[i][j] + t * h[i][j] for j in range(2)) for i in range(2))


def point(mu, p, q, r, skew):
    # Symmetric part = mu I + [[p],[q]] [[p,q]] + [[0],[r]] [[0,r]].
    return ((mu + p * p, p * q - skew),
            (p * q + skew, mu + q * q + r * r))


def derivative_norm(u, v):
    return 2.0 * (u + abs(v)) * max(u, abs(v)) / math.hypot(u, v) ** 3


def run():
    assertions = 0
    assert abs(2.0 * TSTAR * TSTAR + 3.0 * TSTAR - 1.0) < 2e-15
    assertions += 1
    assert abs(C * C - ((1 + TSTAR) ** 2 / (1 + TSTAR * TSTAR) ** 3)) < 2e-15
    assertions += 1

    rng = random.Random(20201125)
    # Deterministic broad grid verifies the scalar derivative envelope.
    for mu in (0.25, 0.7, 1.0, 2.0, 5.0):
        for k in range(3001):
            t = 5.0 * k / 3000.0
            v = 2.0 * mu * t
            assert derivative_norm(2.0 * mu, v) <= C / mu + 1e-12
            assertions += 1
        assert abs(derivative_norm(2.0 * mu, 2.0 * mu * TSTAR) - C / mu) < 1e-12
        assertions += 1

        # Sample arbitrary accretive operators, checking global pairwise bound.
        for _ in range(20000):
            p, q, r, skew = (rng.uniform(-3, 3), rng.uniform(-3, 3),
                              rng.uniform(-3, 3), rng.uniform(-5, 5))
            a = point(mu, p, q, r, skew)
            p, q, r, skew = (rng.uniform(-3, 3), rng.uniform(-3, 3),
                              rng.uniform(-3, 3), rng.uniform(-5, 5))
            b = point(mu, p, q, r, skew)
            lhs = max_entry(subtract(polar(a), polar(b)))
            rhs = C / mu * max_entry(subtract(a, b))
            assert lhs <= rhs + 3e-12, (lhs, rhs, a, b)
            assertions += 1

        # One-sided boundary perturbations attain the constant infinitesimally.
        a = ((mu, -mu * TSTAR), (mu * TSTAR, mu))
        h = ((1.0, 1.0), (-1.0, 1.0))
        for step in (1e-3, 1e-4, 1e-5, 1e-6):
            b = add_scaled(a, h, step)
            ratio = max_entry(subtract(polar(a), polar(b))) / step
            assert 0 < C / mu - ratio < 0.02
            assertions += 1
        b = add_scaled(a, h, 1e-7)
        ratio = max_entry(subtract(polar(a), polar(b))) / 1e-7
        assert abs(ratio - C / mu) < 2e-5
        assertions += 1
    print('PASS: {} supplementary assertions; C={:.15f}; t*={:.15f}'.format(assertions, C, TSTAR))


if __name__ == '__main__':
    run()

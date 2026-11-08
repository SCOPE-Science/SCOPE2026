#!/usr/bin/env python3
"""Independent numerical spot-checks for a two-level radial Bergman kernel.

No finite experiment establishes an eventual-in-m theorem or equidistribution.
The analytic argument is given in RESULT.md.
"""
import cmath
import math


def kernel(a, m, s, terms=220):
    # Horner evaluation for the exact monomial-norm coefficients.
    value = 0j
    for n in range(terms - 1, -1, -1):
        value = value * s + (n + 1) / (1.0 + a ** (n + 1 - m))
    return value


def winding(a, m, radius, points=1200):
    vals = [kernel(a, m, radius * cmath.exp(2j * math.pi * k / points))
            for k in range(points)]
    lower = min(abs(v) for v in vals)
    assert lower > 1e-13, (a, m, radius, lower)
    total = sum(cmath.phase(vals[(k + 1) % points] / vals[k])
                for k in range(points))
    n = round(total / (2 * math.pi))
    assert abs(total / (2 * math.pi) - n) < 1e-6
    return n


def infinite_product(a, z, terms=120):
    p = 1.0 + 0j
    for k in range(terms):
        p *= (1.0 - z * a ** k)
    return p


def phi_bilateral(a, s, terms=70):
    return sum(s ** j / (1.0 + a ** (j + 1)) for j in range(-terms, terms + 1))


def phi_product(a, s):
    p = lambda z: infinite_product(a, z)
    const = p(a) ** 2 / (p(-a) * p(-1))
    return const * p(-a * s) * p(-1 / s) / (p(s) * p(a / s))


def main():
    cases = [(0.15, 12, 0.6), (0.15, 20, 0.65),
             (0.25, 12, 0.6), (0.25, 24, 0.6),
             (0.4, 12, 0.7), (0.4, 24, 0.7)]
    for a, m, r in cases:
        found = winding(a, m, r)
        assert found == m - 1, (a, m, r, found, m - 1)
    for a, s in [(0.15, 0.4 + 0.1j), (0.25, 0.5 + 0.07j),
                 (0.4, 0.64 + 0.1j)]:
        got = phi_bilateral(a, s)
        expected = phi_product(a, s)
        assert abs(got - expected) <= 2e-8 * abs(expected), (a, got, expected)
    print('STEP_BERGMAN_CHECK_PASS argument_windings=6 product_identities=3')

if __name__ == '__main__':
    main()

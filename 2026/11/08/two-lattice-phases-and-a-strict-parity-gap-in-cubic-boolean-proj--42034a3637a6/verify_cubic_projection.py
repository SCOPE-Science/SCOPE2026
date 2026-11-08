#!/usr/bin/env python3
"""Exact small-case checks and high-precision diagnostics for cubic Walsh projection constants.

Requires Python 3.10+; the optional asymptotic diagnostics use mpmath.
The analytical asymptotic proof is in RESULT.md, not inferred from these tests.
"""
from fractions import Fraction
from itertools import product, combinations
from math import comb


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def cubic_kernel(n, s):
    assert n >= 3 and abs(s) <= n and (n - s) % 2 == 0
    assert (s ** 3 - (3 * n - 2) * s) % 6 == 0
    return (s ** 3 - (3 * n - 2) * s) // 6


def norm_direct_binomial(n):
    return Fraction(sum(choose(n, j) * abs(cubic_kernel(n, n - 2 * j))
                        for j in range(n + 1)), 2 ** n)


def d2(n, j):
    return choose(n - 3, j) - 2 * choose(n - 3, j - 1) + choose(n - 3, j - 2)


def norm_boundary(n):
    # Compare exact integers, avoiding floating square-root rounding.
    j = -1
    for k in range(n + 1):
        s = n - 2 * k
        if s > 0 and s * s > 3 * n - 2:
            j = k
        else:
            break
    j0 = (n - 1) // 2
    factor = Fraction(choose(n, 3), 2 ** n)
    return factor * (4 * d2(n, j) - 2 * d2(n, j0))


def check_small_exact():
    for n in range(3, 151):
        assert norm_direct_binomial(n) == norm_boundary(n), n
    for n in range(3, 11):
        triples = tuple(combinations(range(n), 3))
        total = 0
        for signs in product((-1, 1), repeat=n):
            direct_character = sum(signs[a] * signs[b] * signs[c]
                                   for (a, b, c) in triples)
            assert direct_character == cubic_kernel(n, sum(signs))
            total += abs(direct_character)
        assert Fraction(total, 2 ** n) == norm_boundary(n)
    print('EXACT_BINOMIAL_BOUNDARY_IDENTITIES_PASSED 148 dimensions')
    print('INDEPENDENT_WALSH_CHARACTER_ENUMERATION_PASSED 8 dimensions')


def check_phase_diagnostics():
    import mpmath as mp
    mp.mp.dps = 65
    p0 = 1 / mp.sqrt(2 * mp.pi)
    pa = p0 * mp.exp(mp.mpf(-3) / 2)
    leading = (p0 + 4 * pa) / 3

    def bernoulli2(x):
        t = mp.frac(x)
        return t * t - t + mp.mpf(1) / 6

    for n in (1000, 1001, 3000, 3001, 5000, 5001):
        exact_fraction = norm_boundary(n)
        exact = mp.mpf(exact_fraction.numerator) / exact_fraction.denominator
        epsilon = n % 2
        theta = (mp.sqrt(3 * n) - epsilon) / 2
        corrected = (-p0 * (mp.mpf(5) / 12 + 2 * bernoulli2(mp.mpf(epsilon) / 2))
                     -pa * (mp.mpf(2) / 3 + 8 * bernoulli2(theta)))
        residual = (exact - leading * n ** (mp.mpf(3) / 2)) / mp.sqrt(n)
        # This is a diagnostic tolerance, not a uniform asymptotic certificate.
        assert abs(residual - corrected) < mp.mpf('0.01'), (n, residual, corrected)
    print('HIGH_PRECISION_LATTICE_PHASE_DIAGNOSTICS_PASSED 6 dimensions')


if __name__ == '__main__':
    check_small_exact()
    check_phase_diagnostics()
    print('ALL_CUBIC_WALSH_PROJECTION_CHECKS_PASSED')

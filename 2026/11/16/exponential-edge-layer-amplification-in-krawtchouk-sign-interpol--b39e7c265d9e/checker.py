#!/usr/bin/env python3
"""Exact independent checks for the edge behaviour of symmetric sign interpolation.

Use: python3 checker.py. Standard library only; finite tests do not prove limits.
"""
from fractions import Fraction
from math import comb, gamma, log, pi, sqrt


def barycentric_sign(m, x):
    """Independent barycentric interpolant, exact rational arithmetic."""
    if x.denominator == 1 and -m <= x.numerator <= m:
        return Fraction((x.numerator > 0) - (x.numerator < 0))
    numerator = denominator = Fraction(0)
    for k in range(-m, m + 1):
        w = Fraction((-1) ** (m - k) * comb(2 * m, m + k), 1) / (x - k)
        numerator += ((k > 0) - (k < 0)) * w
        denominator += w
    return numerator / denominator


def gamma_lagrange_sign(m, x):
    """Exact rational nodal-product formula; independent factorial weights."""
    W = Fraction(1)
    for k in range(-m, m + 1):
        W *= x - k
    val = Fraction(0)
    for k in range(1, m + 1):
        den = x * x - k * k
        val += Fraction(2 * ((-1) ** (m - k)) * k, 1) / (den * (factorial(m + k) * factorial(m - k)))
    return W * val


def factorial(n):
    z = 1
    for k in range(2, n + 1):
        z *= k
    return z


def T(m, x):
    r = Fraction(1)
    total = Fraction(0)
    for k in range(1, m + 1):
        r *= Fraction(m - k + 1, m + k)
        total += (-1) ** k * k * r * x * x / (x * x - k * k)
    return total


def leading_constant(u):
    return -1 / (2 ** (u + 1) * sqrt(pi) * gamma(-u))


def run():
    count = 0
    for m in range(2, 18):
        for n in (1, 2, 3, 5, 7, 9):
            x = Fraction(m, 1) - Fraction(1, n + 1)
            v1 = barycentric_sign(m, x)
            v2 = gamma_lagrange_sign(m, x)
            assert v1 == v2, ('exact interpolation mismatch', m, x)
            for k in range(-m, m + 1):
                if k != 0:
                    assert barycentric_sign(m, Fraction(k)) == (k > 0) - (k < 0)
            count += 1
    # The alternating first moment has a closed finite identity.
    for m in range(1, 101):
        r = Fraction(1)
        s = Fraction(0)
        for k in range(1, m + 1):
            r *= Fraction(m - k + 1, m + k)
            s += (-1) ** k * k * r
        assert s == Fraction(-m, 2 * (2 * m - 1))
        count += 1
    # Normalization convergence for two rational offsets, with exact
    # finite values and floating-point evaluation only of Gamma constants.
    for u in (Fraction(1, 2), Fraction(1, 4)):
        c = leading_constant(float(u))
        errs = []
        for m in (20, 40, 80):
            v = gamma_lagrange_sign(m, Fraction(m) - u)
            coeff = float(((-1) ** m) * v) * (m ** (float(u) + 2.5)) / (4 ** m)
            errs.append(abs(coeff / c - 1))
            assert coeff > 0
            count += 1
        assert errs[2] < errs[1] < errs[0], (u, errs)
        assert errs[-1] < 0.02
    print('PASS exact checks:', count)
    print('Finite comparisons support but do not prove uniform edge limits.')

if __name__ == '__main__':
    run()

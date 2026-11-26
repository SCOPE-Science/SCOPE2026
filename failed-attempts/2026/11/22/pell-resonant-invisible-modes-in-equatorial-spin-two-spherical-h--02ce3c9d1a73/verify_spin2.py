#!/usr/bin/env python3
"""Exact arithmetic verification of equatorial spin-two zero-mode indices.

This independent finite test uses the factorial form of the Wigner small-d
matrix at pi/2, instead of the associated-Legendre differential equation.
The complete all-degree statement is proved analytically in RESULT.md.
"""
from fractions import Fraction
from math import factorial


def wigner_sum_at_equator(ell, m, spin_index=-2):
    """Nonzero positive factor omitted from d^ell_{m,spin_index}(pi/2)."""
    j, a, b = ell, m, spin_index
    result = Fraction(0)
    low = max(0, b - a)
    high = min(j + b, j - a)
    for k in range(low, high + 1):
        denominator = (factorial(j + b - k) * factorial(k)
                       * factorial(a - b + k) * factorial(j - a - k))
        result += Fraction((-1) ** (a - b + k), denominator)
    return result


def predicted_zero(ell, m):
    return (ell % 2 == 1 and m == 0) or (2 * m * m == ell * (ell + 1))


def run():
    checks = 0
    for ell in range(2, 65):
        for m in range(-ell, ell + 1):
            actual = (wigner_sum_at_equator(ell, m) == 0)
            assert actual == predicted_zero(ell, m), (ell, m, actual)
            checks += 1
    pell_pairs = [(1, 1), (8, 6), (49, 35), (288, 204)]
    for ell, m in pell_pairs[1:]:
        assert 2 * m * m == ell * (ell + 1)
        for sign in (-1, 1):
            assert wigner_sum_at_equator(ell, sign * m) == 0
            checks += 2
    for ell in (2, 3, 4, 8, 9, 49, 50):
        expected = sorted([m for m in range(-ell, ell + 1)
                           if predicted_zero(ell, m)])
        actual = sorted([m for m in range(-ell, ell + 1)
                         if wigner_sum_at_equator(ell, m) == 0])
        assert actual == expected
        checks += 1
    print(f"PASS: {checks} exact rational Wigner and Pell assertions")


if __name__ == '__main__':
    run()

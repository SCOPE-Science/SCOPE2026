#!/usr/bin/env python3
"""Exact checks and independent limiting-number checks for path unconditional polytopes.
Requires Python 3 standard library only; run `python3 checker.py`.
Finite checks are supplementary to the analytic proof.
"""
from fractions import Fraction
from math import comb, pi, fsum


def transfer(poly):
    """Polynomial T p(x) = integral_0^{1-x} p(y) dy, exact Q coefficients."""
    out = [Fraction(0) for _ in range(len(poly) + 1)]
    for k, c in enumerate(poly):
        for j in range(k + 2):
            out[j] += c * Fraction((-1) ** j * comb(k + 1, j), k + 1)
    return out


def integrate_product(p, q, degree=0):
    return sum((a * b / (i + j + degree + 1)
                for i, a in enumerate(p) for j, b in enumerate(q)), Fraction(0))


def exact_moments(max_n=24):
    polys = [[Fraction(1)]]
    for _ in range(max_n):
        polys.append(transfer(polys[-1]))
    result = {}
    for n in range(2, max_n + 1):
        volume_orthant = integrate_product(polys[n - 1], [Fraction(1)])
        assert volume_orthant > 0
        values = [integrate_product(polys[i], polys[n - 1 - i], 2) /
                  volume_orthant for i in range(n)]
        assert values == values[::-1], ('reversal failure', n)
        assert all(Fraction(0) < v < Fraction(1) for v in values)
        result[n] = values
    return result


def boundary_formula(j, terms=5000):
    v_bulk = Fraction(1, 3) - 2 / pi**2
    series = fsum(((-1.0) if ((k * (j + 1)) & 1) else 1.0) *
                   (1 / k**2 - 1 / (k + 1)**2) / (2 * k + 1)**j
                  for k in range(1, terms + 1))
    return v_bulk + 2 * series / pi**2


def main():
    vals = exact_moments(26)
    assert vals[2] == [Fraction(1, 6)] * 2
    assert vals[3] == [Fraction(1, 5), Fraction(1, 10), Fraction(1, 5)]
    assert vals[4] == [Fraction(14, 75), Fraction(3, 25), Fraction(3, 25), Fraction(14, 75)]
    assert abs(boundary_formula(1) - (1 - 8 / pi**2)) < 1e-10
    assert abs(boundary_formula(2) - (8 / pi - 24 / pi**2)) < 1e-12
    bulk = 1/3 - 2/pi**2
    for j in range(1, 12):
        v = boundary_formula(j)
        assert (v > bulk) if j % 2 == 1 else (v < bulk)
    for j in range(3, 12):
        assert (8/pi - 24/pi**2) < boundary_formula(j) < (1 - 8/pi**2)
    for j in range(1, 7):
        value = float(vals[26][j-1])
        target = boundary_formula(j)
        assert abs(value-target) < 2e-6, (j, value, target)
    for j in range(3, 8):
        gap = boundary_formula(j) - bulk
        main_term = (-1)**(j+1) / (2*pi**2*3**(j-1))
        assert abs(gap - main_term) < 10/5**j
    print('PATH_UNCONDITIONAL_COVARIANCE_CHECKS_PASS')
    print('exact dimensions 2..26; rational reversal and benchmark identities; six boundary limits')
    print('bulk',format(bulk,'.15f'))
    print('boundary1',format(boundary_formula(1),'.15f'))
    print('boundary2',format(boundary_formula(2),'.15f'))
    print('condition-limit',format((1-8/pi**2)/(8/pi-24/pi**2),'.15f'))

if __name__ == '__main__':
    main()

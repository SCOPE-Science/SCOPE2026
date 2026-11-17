#!/usr/bin/env python3
"""Finite reproducibility checks for a harmonic Bergman commutator.

The asymptotic theorems require the analytic proof; this checker verifies
finite-dimensional coefficient identities and exact unweighted moments.
"""
import math
from fractions import Fraction


def moment(beta, j):
    return math.exp(math.lgamma(beta + 1) + math.lgamma(j + 1) - math.lgamma(j + beta + 1))


def toeplitz_monomial(beta, r, signed_index):
    j = signed_index
    out = j + r
    if j >= 0:
        value = math.sqrt(moment(beta, out) / moment(beta, j))
    elif -j > r:
        value = math.sqrt(moment(beta, -j) / moment(beta, -j - r))
    else:
        value = moment(beta, r) / math.sqrt(moment(beta, -j) * moment(beta, out))
    return out, value


def direct_coefficient(beta, m, j):
    k, first = toeplitz_monomial(beta, m, j)
    out1, second = toeplitz_monomial(beta, 1, k)
    l, third = toeplitz_monomial(beta, 1, j)
    out2, fourth = toeplitz_monomial(beta, m, l)
    assert out1 == out2
    return first * second - third * fourth


def predicted_coefficient(beta, m, q):
    return (beta * moment(beta, m) * (m + 1 - 2*q) /
            ((q + beta) * (m - q + 1 + beta) *
             math.sqrt(moment(beta, q) * moment(beta, m - q + 1))))


def test():
    checks = 0
    for beta in (0.25, 0.5, 1.0, 1.5, 2.0, 3.5):
        for m in range(1, 81):
            for j in range(-m - 6, 12):
                want = predicted_coefficient(beta, m, -j) if -m <= j <= -1 else 0
                got = direct_coefficient(beta, m, j)
                assert abs(got-want) < 1e-12, (beta, m, j, got, want)
                checks += 1
    for m in range(1, 201):
        exact = sum((Fraction((m + 1 - 2*q)**2,
                              (m + 1)**2 * (q + 1) * (m - q + 2))
                     for q in range(1, m + 1)), Fraction(0))
        harmonic = sum((Fraction(1, j) for j in range(1, m + 2)), Fraction(0))
        expected = (2 * (m + 3) * (harmonic - 1) - 4*m) / (m + 1)**2
        assert exact == expected
        checks += 1
    print('PASS:', checks, 'coefficient and exact-rational assertions')
    print('Finite tests do not establish infinite-degree asymptotics.')


if __name__ == '__main__':
    test()

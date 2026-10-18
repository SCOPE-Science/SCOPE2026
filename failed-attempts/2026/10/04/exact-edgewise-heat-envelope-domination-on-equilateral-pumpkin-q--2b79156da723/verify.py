#!/usr/bin/env python3
"""Replays algebraic checks for the equilateral pumpkin heat-envelope formula."""
from fractions import Fraction
from math import exp, pi, isclose


def projection_diag(n: int):
    # Orthogonal projection in R^n onto the coefficient hyperplane sum b_j=0.
    P = [[(Fraction(1 if i == j else 0, 1) - Fraction(1, n)) for j in range(n)] for i in range(n)]
    # P^2=P and every diagonal entry is 1-1/n.
    for i in range(n):
        for j in range(n):
            lhs = sum(P[i][k] * P[k][j] for k in range(n))
            assert lhs == P[i][j]
    assert all(P[i][i] == Fraction(n-1, n) for i in range(n))
    return P


def positive_level_edge_weight(n: int, ell: Fraction) -> Fraction:
    P = projection_diag(n)
    # Symmetric cosine contribution plus the trace of the sine coefficient projection.
    cosine = Fraction(2, 1) / (n * ell)
    sine = Fraction(2, 1) / ell * P[0][0]
    return cosine + sine


def heat_envelope_direct(n: int, ell: float, t: float, cutoff: int) -> float:
    # Exact level weight 2/ell, truncated after cutoff positive levels.
    total = 1.0 / (n * ell)
    for m in range(1, cutoff + 1):
        total += (2.0 / ell) * exp(-((m*pi/ell)**2) * t)
    return total


def heat_envelope_formula(n: int, ell: float, t: float, cutoff: int) -> float:
    theta_tail = sum(exp(-((m*pi/ell)**2) * t) for m in range(1, cutoff + 1))
    return 1.0/(n*ell) + 2.0*theta_tail/ell


def neumann_edge_formula(ell: float, t: float, cutoff: int) -> float:
    theta_tail = sum(exp(-((m*pi/ell)**2) * t) for m in range(1, cutoff + 1))
    return 1.0/ell + 2.0*theta_tail/ell


def spectral_function(n: int, ell: float, E: float) -> float:
    # Robust floor at exact thresholds used below.
    mmax = int((ell * E**0.5) / pi + 1e-12)
    return 1.0/(n*ell) + 2.0*mmax/ell


def main():
    # Exact rational projector and per-positive-level edge weight checks.
    for n in range(2, 13):
        for ell in (Fraction(1, 1), Fraction(3, 2), Fraction(7, 5)):
            w = positive_level_edge_weight(n, ell)
            assert w == Fraction(2, 1) / ell

    # Truncated heat sums and the exact constant gap to the decoupled Neumann edge.
    for n in (2, 3, 5, 9):
        for ell in (0.7, 1.0, 2.3):
            for t in (0.003, 0.07, 0.8, 3.0):
                for cutoff in (20, 80):
                    a = heat_envelope_direct(n, ell, t, cutoff)
                    b = heat_envelope_formula(n, ell, t, cutoff)
                    c = neumann_edge_formula(ell, t, cutoff)
                    assert isclose(a, b, rel_tol=0.0, abs_tol=2e-14)
                    assert isclose(c-a, (n-1)/(n*ell), rel_tol=0.0, abs_tol=3e-14)

    # Finite-energy edge-sup spectral function: each positive level contributes 2/ell.
    for n in (2, 4, 7):
        ell = 1.7
        for q in (0, 1, 2, 5, 11):
            threshold = (q*pi/ell)**2
            got = spectral_function(n, ell, threshold)
            expected = 1.0/(n*ell) + 2.0*q/ell
            assert isclose(got, expected, rel_tol=0.0, abs_tol=2e-12)
            if q >= 1:
                below = spectral_function(n, ell, threshold*(1-1e-10))
                expected_below = 1.0/(n*ell) + 2.0*(q-1)/ell
                assert isclose(below, expected_below, rel_tol=0.0, abs_tol=2e-12)

    print('VERIFY_OK')


if __name__ == '__main__':
    main()

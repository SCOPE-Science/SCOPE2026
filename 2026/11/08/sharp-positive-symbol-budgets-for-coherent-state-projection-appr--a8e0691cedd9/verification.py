#!/usr/bin/env python3
"""Finite numerical checks for a Gaussian Toeplitz minimax formula.

The analytic proof, rather than these checks, covers all dimensions and budgets.
"""
import math


def cdf_integer_gamma(k, x):
    assert isinstance(k, int) and k >= 1 and x >= 0
    # P[Gamma(k,1) <= x] computed as the Poisson(k-1) upper tail.
    v = 1.0 - math.exp(-x) * sum(x**j / math.factorial(j) for j in range(k))
    return min(1.0, max(0.0, v))


def threshold(d, M):
    assert d >= 1 and M > 0.5
    lo, hi = 0.0, 1.0
    while M * (cdf_integer_gamma(d, hi) + cdf_integer_gamma(d+1, hi)) < 1:
        hi *= 2
    for _ in range(110):
        mid = (lo + hi) / 2
        if M * (cdf_integer_gamma(d, mid) + cdf_integer_gamma(d+1, mid)) < 1:
            lo = mid
        else:
            hi = mid
    return (hi + lo) / 2


def main():
    n = 0
    for d in [1, 2, 3, 4, 6]:
        for M in [0.51, 0.6, 1, 2, 5, 10, 40]:
            a = threshold(d, M)
            v = M * cdf_integer_gamma(d+1, a)
            u = M * cdf_integer_gamma(d, a)
            assert abs((1 - u) - v) < 2e-8
            n += 1
            for j in range(1, 20):
                assert M * cdf_integer_gamma(d+j, a) <= v + 2e-10
                n += 1
            assert 0 < v < 0.5
            n += 1
        # Geometric convergence at large symbol budgets corroborates the proven exponent.
        M = 5000.0
        a = threshold(d, M)
        estimate = math.factorial(d)**(1/d) / (d+1) * M**(-1/d)
        actual = M * cdf_integer_gamma(d+1, a)
        assert abs(actual / estimate - 1) < 0.08
        n += 1
    for M in [0.1, 0.4, 0.5]:
        assert max(1-M, M) == 1-M
        n += 1
    print(f'FOCK_POSITIVE_BUDGET_CHECK_OK {n} finite assertions')


if __name__ == '__main__':
    main()

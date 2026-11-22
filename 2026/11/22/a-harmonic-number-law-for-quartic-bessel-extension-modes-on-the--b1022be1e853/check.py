#!/usr/bin/env python3
"""Supplementary exact arithmetic and numerical checks of integer-order quartic Bessel moments.

Usage: python check.py
Requires Python 3 standard library; SciPy adds independent Bessel quadrature tests.
Finite experiments corroborate, but do not prove, the all-order theorem.
"""
from fractions import Fraction
from math import comb, factorial, pi, log


def odd_sum(n):
    return sum((Fraction(1, 2*j+1) for j in range(n)), Fraction(0))


def beta_integer(a, b):
    assert isinstance(a, int) and isinstance(b, int) and a >= 1 and b >= 1
    return Fraction(factorial(a-1)*factorial(b-1), factorial(a+b-1))


def via_beta(n):
    return sum((Fraction(comb(n-1, j), 2*j+1)*beta_integer(j+1, n-j)
                for j in range(n)), Fraction(0)) / n


def moment_rational_coefficient(n):
    """The exact number pi**2 times integral_0^infty J_n(r)**4 dr/r."""
    return odd_sum(n) / (n*n)


def main():
    count = 0
    expected = [Fraction(1), Fraction(1, 3), Fraction(23, 135),
                Fraction(11, 105), Fraction(563, 7875)]
    for n in range(1, 121):
        s = odd_sum(n)
        assert via_beta(n) == s / (n*n)
        count += 1
        assert moment_rational_coefficient(n) == s / (n*n)
        count += 1
        if n > 1:
            assert moment_rational_coefficient(n) < moment_rational_coefficient(n-1)
            count += 1
        if n <= 5:
            assert moment_rational_coefficient(n) == expected[n-1]
            count += 1
    # Demonstrate the higher-mode tail and its first Euler--Maclaurin correction.
    euler_gamma = 0.57721566490153286060651209
    for n in [100, 500, 2000, 10000]:
        actual = float(odd_sum(n))
        approx = 0.5*log(n)+log(2)+0.5*euler_gamma+1/(48*n*n)
        assert abs(actual-approx) < 1/(100*n**4) + 4e-15
        count += 1
    # Independent numerical quadrature is optional, never a substitute for proof.
    try:
        from scipy.integrate import quad
        from scipy.special import jv
    except ImportError:
        print('SciPy unavailable: omitted optional numerical quadrature')
    else:
        for n in range(1, 7):
            integrand = lambda x: jv(n, x)**4/x if x else 0.0
            integral = quad(integrand, 0, 400, epsabs=2e-10, limit=300)[0]
            exact = float(moment_rational_coefficient(n))/pi**2
            # Positive residual tail beyond 400 is approximately 4.75e-7.
            assert abs(integral-exact) < 1.0e-6, (n, integral, exact)
            count += 1
    print(f'PASS: {count} exact/supplementary numerical assertions')

if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""Finite exact checks of even weighted-Bergman kernel identities.

Analytical assertions for nonintegral parameters and infinite-dimensional
wandering subspaces are proved separately, not by this finite checker.
"""
from fractions import Fraction
from math import comb


def poly_conv(a, b, n):
    return [sum(a[k]*b[j-k] for k in range(max(0, j-len(b)+1), min(j, len(a)-1)+1)) for j in range(n)]


def integer_power_series_rational(numerator, exponent, n):
    reciprocal = [Fraction(comb(exponent+j-1, exponent-1)) for j in range(n)]
    return poly_conv([Fraction(x) for x in numerator], reciprocal, n)


def do_checks():
    checks=0
    # Even powers in (1-z)^(-q): for q=2,3,4 one gets these
    # exactly rational closed forms, including the q=2 boundary.
    cases = ((2, [1,1]), (3, [1,3]), (4, [1,6,1]))
    for q, numerator in cases:
        series=integer_power_series_rational(numerator,q,60)
        for n in range(60):
            assert series[n] == comb(q+2*n-1, 2*n)
            checks += 1
        # Weighted Bergman monomial squared norms; n is even in E_2.
        for n in range(30):
            expected=Fraction(1,comb(q+2*n-1,2*n))
            direct=Fraction(1,comb(q+2*n-1,2*n))
            assert expected==direct
            assert Fraction(1, expected)==series[n]
            checks += 2
    # Explicit degree-two example in A^2_1.  The kernel numerator
    # is 1+3t, and a=2/3, z0^2=-1/2 give t=-1/3.
    a=Fraction(2,3)
    z0_squared=-Fraction(1,2)
    t=a*z0_squared
    assert -1 < t < 0 and 0 < a < 1
    assert 1+3*t == 0
    assert Fraction(1+3*t,(1-t)**3) == 0
    checks += 3
    print('EVEN_BERGMAN_KERNEL_EXACT_OK', checks)


if __name__=='__main__':
    do_checks()

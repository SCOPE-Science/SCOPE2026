#!/usr/bin/env python3
"""Standalone finite cross-checks for the complex-Hermite angular selection rule.

The theorem for all indices is analytic; these tests check exact algebra and
selected independent numerical quadratures, not an infinite certificate.
"""
from fractions import Fraction as F
from math import factorial, gamma, sqrt, pi


def predicted_reduced(p, m):
    """<H_{p,1} e^{im arg z},H_{p+m,1}> divided by Gamma(p+m/2)."""
    return F(p, 1) + F(m, 2) - F(m*m, 4)


def expanded_reduced(p, m):
    """Independent expansion of the two radial Hermite factors."""
    a = F(2*p+m, 2)
    return (a+1)*a - (2*p+m)*a + p*(p+m)


def weight(p, m):
    return (float(predicted_reduced(p,m))*gamma(p + m/2)
            /sqrt(factorial(p)*factorial(p+m)))


def main():
    tests = 0
    for m in range(1, 25):
        for p in range(0, 31):
            assert expanded_reduced(p,m) == predicted_reduced(p,m)
            tests += 1
            zero = predicted_reduced(p,m) == 0
            assert zero == (m % 2 == 0 and p == m*(m-2)//4)
            tests += 1
    for m in (1,2,3,4,5,6,8,10,12):
        for p in (2,3,5,10,30,80):
            if p < 40:
                w = weight(p,m)
                assert abs(w) <= 1+1e-12
                tests += 1
    # Independent numerical integration of the original Gaussian radial moment.
    # Use mpmath only when installed; the exact rational checks above remain standalone.
    try:
        import mpmath as mp
        mp.mp.dps = 40
        for p,m in ((0,1),(0,2),(1,2),(2,4),(1,3),(6,6),(4,5),(9,7)):
            a=mp.mpf(p)+mp.mpf(m)/2
            f=lambda t: mp.exp(-t)*t**(a-1)*(t-p)*(t-p-m)
            observed=mp.quad(f,[0,1,mp.inf])
            expected=mp.gamma(a)*mp.mpf(predicted_reduced(p,m).numerator)/predicted_reduced(p,m).denominator
            assert abs(observed-expected) < mp.mpf('1e-28')*(1+abs(expected)), (p,m,observed,expected)
            tests += 1
    except ImportError:
        print('Optional numerical quadratures skipped: mpmath not installed')
    # The limit and the error coefficient are deduced by Stirling in the proof;
    # finite tests only check several representative windows.
    for m in (1,2,3,4,6):
        for p in (200,500):
            # Log-gamma avoids overflow in factorial normalization.
            from math import lgamma, exp
            a = p+m/2
            w = float(predicted_reduced(p,m))*exp(lgamma(a)-0.5*(lgamma(p+1)+lgamma(p+m+1)))
            assert abs(p*(1-w)-3*m*m/8) < 2.0*m**4/p
            tests += 1
    print('PASS',tests,'finite checks; independent analytic proof required for unbounded indices')

if __name__ == '__main__':
    main()

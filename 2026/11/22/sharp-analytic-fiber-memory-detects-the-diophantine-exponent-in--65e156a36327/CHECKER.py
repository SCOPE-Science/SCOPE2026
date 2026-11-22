"""Finite reproducibility checks for the dyadic skew-product Fourier law.

The infinite Diophantine conclusions are proved analytically, not by these tests.
"""
from fractions import Fraction
from math import comb, cos, pi, log, sqrt, isclose
import cmath


def digit_mean(alpha, n, k):
    """Direct exact binary-word average, using a rational alpha."""
    total = 0j
    for mask in range(2**n):
        s = mask.bit_count()
        total += cmath.exp(2j*pi*float(alpha*k*s))
    return total / 2**n


def characteristic(alpha, n, k):
    return ((1+cmath.exp(2j*pi*float(alpha*k)))/2)**n

checks = 0
for alpha in [Fraction(1, 3), Fraction(2, 5), Fraction(3, 7)]:
    for n in range(1, 9):
        for k in range(1, 8):
            lhs = digit_mean(alpha, n, k)
            rhs = characteristic(alpha, n, k)
            assert abs(lhs-rhs)<1e-10, (alpha, n, k, lhs, rhs)
            assert isclose(abs(rhs), abs(cos(pi*float(alpha*k)))**n,
                           rel_tol=1e-10, abs_tol=1e-10)
            checks += 1

# Direct conjugacy for dyadic points (without circle-floor roundoff).
for alpha in [Fraction(1, 3), Fraction(2, 5)]:
    for numerator in range(1, 63):
        x = Fraction(numerator, 64)
        digit = int(2*x)
        xnew = 2*x-digit
        u = Fraction(17, 31)
        unew = (u+alpha*x) % 1
        vold = (u-alpha*x) % 1
        vnew = (unew-alpha*xnew) % 1
        assert vnew == (vold+alpha*digit) % 1
        checks += 1

# Compare variational finite-frequency formula with Hilbert-diagonal action.
rho = .4
for alpha in [float((sqrt(5)-1)/2), sqrt(2)-1, 2/5]:
    for n in [1, 2, 8, 32, 128]:
        values = [(-2*rho*k+n*log(max(abs(cos(pi*k*alpha)),1e-300)))
                  for k in range(1, 300)]
        assert max(values) <= -2*rho + 1e-10
        checks += 1

print('PASS:', checks, 'finite direct-binomial, exact-conjugacy and Fourier tests.')
print('These tests do not certify asymptotic Diophantine statements.')

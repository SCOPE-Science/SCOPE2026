"""Finite reproducibility checks for generalized Cesaro Riesz-projection formulas.

All rational eigenvector and coefficient identities are exact. Floating-point
asymptotic diagnostics are finite tests, not proofs of the limiting laws.
Run with a standard Python 3 interpreter.
"""
import math
from fractions import Fraction


def right(m, n, t):
    return math.comb(n, m) * t ** (n - m) if n >= m else Fraction(0)


def left(m, n, t):
    return math.comb(m, n) * (-t) ** (m - n) if n <= m else Fraction(0)


def finite_sum(m, t):
    term = 1.0
    total = 1.0
    for k in range(1, m + 1):
        term *= ((m - k + 1) * t / k) ** 2
        total += term
    return total


def bessel_i0(z):
    term = 1.0
    total = 1.0
    for k in range(1, 1000):
        term *= (z / (2 * k)) ** 2
        nxt = total + term
        if nxt == total:
            return total
        total = nxt
    raise AssertionError('Bessel series did not converge')


def check():
    checks = 0
    for t in (Fraction(0), Fraction(1, 5), Fraction(2, 5), Fraction(3, 4)):
        for m in range(9):
            for k in range(m + 1):
                lhs = sum(t ** (n-k) * left(m, n, t) / Fraction(n+1)
                          for n in range(k, m+1))
                assert lhs == left(m, k, t) / Fraction(m+1)
                checks += 1
            for j in range(9):
                assert sum(right(j, n, t) * left(m, n, t)
                           for n in range(m+1)) == int(j == m)
                checks += 1
            for n in range(1, 31):
                lhs = sum(t ** (n-k) * right(m, k, t)
                          for k in range(n+1)) / Fraction(n+1)
                assert lhs == right(m, n, t) / Fraction(m+1)
                checks += 1
            for n in range(12):
                # Coefficient comparison for the hypergeometric norm identity.
                coef = sum(math.comb(m, k)**2 * math.comb(2*m+n-k, 2*m)
                           for k in range(min(n, m)+1))
                assert coef == math.comb(m+n, m)**2
                checks += 1
    for t in (0.1, 0.3, 0.6):
        for m in (10, 20, 40, 80, 150):
            w = finite_sum(m, t)
            exact = w / (1-t*t)**(m+0.5)
            predicted = ((1+t)/(2*math.sqrt(math.pi*m*t*(1-t*t)))
                         * ((1+t)/(1-t))**m)
            assert abs(exact/predicted - 1) < max(0.13, 3/m)
            checks += 1
    for tau in (0.0, 0.2, 1.0, 3.0):
        m = 1000
        t = tau/m
        exact = finite_sum(m, t)/(1-t*t)**(m+0.5)
        assert abs(exact/bessel_i0(2*tau)-1) < 0.03
        checks += 1
    return checks


if __name__ == '__main__':
    print('PASS:', check(), 'finite assertions')

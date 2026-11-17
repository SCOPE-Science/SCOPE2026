"""Reproducible finite checks for the mass-one stationary product-kernel shattering law.

Only verifies finite algebraic consequences of the stated recurrence; it does not
certify the Tauberian asymptotic or existence in an infinite kinetic system.
"""
from fractions import Fraction
from math import log


def exact_prefix(m=18):
    a = [Fraction(0)] * (m + 1)
    a[1] = Fraction(4, 5)
    for k in range(2, m + 1):
        a[k] = Fraction(k, 2 * (k + 4)) * sum(a[j] * a[k-j] for j in range(1, k))
        assert a[k] > 0
    # [z^k] { z(1-q)q' -4(z-q) } =0 up to degree m.
    for k in range(1, m + 1):
        a_term = k * a[k]
        conv = sum(j * a[j] * a[k-j] for j in range(1, k))
        coefficient = a_term - conv - 4 * (Fraction(1) if k == 1 else 0) + 4 * a[k]
        assert coefficient == 0, (k, coefficient)
    # The first two stationary coefficients are fixed exactly by the recurrence.
    assert a[1] == Fraction(4, 5)
    assert a[2] == Fraction(8, 75)
    return m


def large_prefix(N=6000):
    a = [0.0] * (N + 1)
    a[1] = 0.8
    for k in range(2, N+1):
        z = 0.0
        for j in range(1, k):
            z += a[j] * a[k-j]
        a[k] = k * z / (2.0 * (k+4))
        assert a[k] > 0
    mass = 0.0
    second = 0.0
    ratios = []
    for k in range(1, N+1):
        mass += a[k]
        second += k * a[k]
        if k in (100, 1000, 6000):
            ratios.append((k, round((2.0-second)*log(k), 9)))
    assert 0.99 < mass < 1.0
    assert 1.0 < second < 2.0
    assert ratios[0][1] < ratios[1][1] < ratios[2][1] < 2
    return mass, second, ratios

if __name__ == '__main__':
    exact = exact_prefix()
    mass, m2, ratios = large_prefix()
    print('VERIFY_OK exact_series_coefficients=%d finite_prefix=6000' % exact)
    print('PARTIAL_MASS %.12f PARTIAL_SECOND_MOMENT %.12f' % (mass, m2))
    print('TRUNCATION_LOG_RATIOS', ratios)
    print('FINITE_CHECK_ONLY: no claim of infinite-tail certification')

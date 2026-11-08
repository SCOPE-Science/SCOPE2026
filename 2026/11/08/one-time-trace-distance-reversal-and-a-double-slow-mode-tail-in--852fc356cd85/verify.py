"""Finite consistency tests for a pure-death Dicke ladder comparison.

The accompanying analytical proof, not these tests, covers all admissible sizes.
Requires Python 3, numpy and scipy.
"""
from fractions import Fraction
import math
import numpy as np
from scipy.linalg import expm


def cascade_matrix(n, rate=1.0):
    q = np.zeros((n + 1, n + 1))
    for k in range(1, n + 1):
        lam = rate * k * (n - k + 1)
        q[k, k] = -lam
        q[k - 1, k] = lam
    return q


def quantities(n, j, t):
    p = expm(t * cascade_matrix(n))[:, j]
    return (float(np.sum(p[1:])), float(np.dot(np.arange(n + 1), p)))


def exact_c(n, j):
    out = Fraction(1)
    for k in range(2, j + 1):
        lam = k * (n - k + 1)
        out *= Fraction(lam, lam - n)
    return out


def check():
    count = 0
    for n in range(3, 51):
        for j in range(1, n):
            assert exact_c(n, j) == Fraction(j * (n - 1), n - j)
            count += 1
    for n in (3, 4, 5, 6, 8, 12, 20):
        j = (2 * n + 2) // 3
        b = 0.5
        q = cascade_matrix(n)
        assert np.max(abs(np.sum(q, axis=0))) < 1e-12
        count += 1
        old_ratio = 1.0
        crossing_intervals = 0
        for t in np.linspace(0, 10.0 / n, 201):
            sj, ej = quantities(n, j, t)
            sn, en = quantities(n, n, t)
            assert -1e-10 <= sj <= 1.0 + 1e-10
            assert -1e-10 <= sn <= 1.0 + 1e-10
            assert 0 <= ej <= j + 1e-10
            assert 0 <= en <= n + 1e-10
            rr = sj / sn
            assert rr < old_ratio + 1e-10
            if old_ratio > b >= rr:
                crossing_intervals += 1
            old_ratio = rr
            count += 1
        assert crossing_intervals == 1, (n, crossing_intervals)
        count += 1
    # Large-time first-moment and survival ratios in a manageable scaling regime.
    for n in (3, 4, 5, 6, 8):
        j = (2 * n + 2) // 3
        t = 30 / n
        sj, ej = quantities(n, j, t)
        sn, en = quantities(n, n, t)
        # Numerical exponentials become ill-conditioned in very small tails;
        # test the predicted leading decay at moderate times, with loose bounds.
        coeff = Fraction(2 * j, n * (n - 1) * (n - j))
        assert 0.25 < (sj / (0.5 * sn)) * t / float(coeff) < 4.0
        assert 0.25 < (ej / (0.5 * en)) * t / float(coeff) < 4.0
        count += 2
    # Independent emitter sanity check: no reversal for j>b*n.
    for n in range(3, 21):
        j = (2 * n + 2) // 3
        for t in (0.05, 0.2, 0.8, 2.0, 5.0):
            q = 1 - math.exp(-t)
            sj = 1 - q ** j
            sn = 1 - q ** n
            assert sj > 0.5 * sn
            count += 1
    print('PASS', count, 'finite consistency checks')


if __name__ == '__main__':
    check()

"""Deterministic checks for Gaussian frozen-propulsion exit moments.

Run: python verify.py
Requires numpy. Numerical quadrature supplements, but does not prove, the theorem.
"""
import math
import numpy as np
from numpy.polynomial.legendre import leggauss


def exact_moments(x, L, D, sigma, order=28):
    """Gauss--Legendre integration of the exact finite-dimensional formulas."""
    assert 0 < x <= L and L > 0 and D > 0 and sigma >= 0
    a, w = leggauss(order)
    a, w = (a + 1.0) / 2.0, w / 2.0
    theta = sigma * sigma / (2.0 * D * D)
    m1 = m2 = 0.0
    for i, z in enumerate(x * a):
        wz = x * w[i]
        for j, t in enumerate(a):
            y = z + (L - z) * t
            wy = (L - z) * w[j]
            m1 += wz * wy * math.exp(theta * (y - z) ** 2) / D
            for k, ta in enumerate(a):
                aa = y * ta
                wa = y * w[k]
                bs = aa + (L - aa) * a
                core = float(np.dot(w, np.exp(theta * ((y - z) + (bs - aa)) ** 2))) * (L - aa)
                m2 += 2.0 * wz * wy * wa * core / (D * D)
    return m1, m2


def brownian_moments(x, L, D):
    m1 = x * (2 * L - x) / (2 * D)
    m2 = x * (2 * L - x) * (4 * L * L + 2 * L * x - x * x) / (12 * D * D)
    return m1, m2


def expect_close(a, b, tolerance=1e-10):
    assert math.isclose(a, b, rel_tol=tolerance, abs_tol=tolerance), (a, b)


def run():
    count = 0
    for x, L, D in [(0.15, 1, 1), (0.8, 1, 1), (1, 1, 1), (0.6, 1.3, 0.7)]:
        actual = exact_moments(x, L, D, 0)
        predicted = brownian_moments(x, L, D)
        for a, b in zip(actual, predicted):
            expect_close(a, b)
            count += 1
        slope = actual[0] ** 2 - actual[1] / 2
        closed = x * (x - 2 * L) * (5 * x * x - 10 * L * x + 4 * L * L) / (24 * D * D)
        expect_close(slope, closed)
        count += 1
    for x in [0.1, 0.5, 0.8, 1.0]:
        prev = -1
        for sigma in [0, 0.5, 1, 2, 3]:
            one, two = exact_moments(x, 1, 1, sigma)
            assert one > prev and two > 0
            prev = one
            count += 1
    x, L, D = 0.8, 1, 1
    slopes = []
    for sigma in [0, 0.5, 1, 2]:
        m1, m2 = exact_moments(x, L, D, sigma)
        slopes.append(m1 * m1 - m2 / 2)
        count += 1
    assert slopes[0] > 0 and slopes[1] > 0 and slopes[-1] < 0
    count += 1
    # The asymptotic ratios must approach 1 at sufficiently large noise.
    errs = []
    for sigma in [4, 5, 6]:
        m1, m2 = exact_moments(x, L, D, sigma, order=38)
        a1 = D**3 / (sigma**4 * L**2) * math.exp(sigma**2 * L**2 / (2 * D**2))
        a2 = D**6 / (8 * sigma**8 * L**4) * math.exp(2 * sigma**2 * L**2 / D**2)
        errs.append((abs(m1 / a1 - 1), abs(m2 / a2 - 1)))
        count += 2
    for j in range(2):
        assert errs[0][j] > errs[1][j] > errs[2][j]
        assert errs[2][j] < 0.12
        count += 1
    print(f"PASS {count} deterministic integral, sign, and asymptotic tests")
    print("Asymptotic relative errors at sigma = 4,5,6:", errs)


if __name__ == '__main__':
    run()

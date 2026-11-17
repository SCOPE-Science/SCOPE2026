#!/usr/bin/env python3
"""Exact rational checks and independent finite spectral spot checks.

The general theorem is proved analytically; this program tests its formulas
on a reproducible finite selection of fractional orders and memory lengths.
"""
from fractions import Fraction as F
from math import sqrt


def coefficients(q, M):
    g = [F(1)]
    for j in range(1, M + 1):
        g.append(g[-1] * (F(j - 1) - q) / F(j))
    return g


def descriptors(g):
    M = len(g) - 1
    b = [-g[j] for j in range(M + 1)]
    G = sum(g[1:])
    H = sum(((-1) ** (j - 1)) * g[j] for j in range(1, M + 1))
    R = F(2) + G
    r_star = 2 * R - H
    c = [sum(((-1) ** (j - k - 1)) * b[j]
             for j in range(k + 1, M + 1))
         for k in range(1, M)]
    S = F(1) - sum(((-1) ** k) * c[k - 1]
                   for k in range(1, M))
    return G, H, R, r_star, b, c, S


def poly_times_z_plus_one(Q):
    out = [F(0)] * (len(Q) + 1)
    for j, value in enumerate(Q):
        out[j] += value
        out[j + 1] += value
    return out


def exact_check(q, M):
    g = coefficients(q, M)
    G, H, R, r_star, b, c, S = descriptors(g)
    assert H < 0 and R > 0 and R - H > 0
    assert r_star > R and S > 0
    assert all(v >= 0 for v in c) and sum(c) < 1
    assert sum(c) == sum(b[j] for j in range(2, M + 1, 2))
    P = [F(1), F(1) - H - b[1]] + [-b[j] for j in range(2, M + 1)]
    Q = [F(1)] + [-v for v in c]
    assert poly_times_z_plus_one(Q) == P
    assert S == F(1) + sum(((-1) ** j) * (j - 1) * b[j]
                                for j in range(2, M + 1))
    for r in [r_star + F(1, 100), r_star + F(1, 7), r_star + 2]:
        m = (r - H) / (2 * r)
        d_sq = (r - H) * (r - r_star) / (4 * r * r)
        # Both phase equations use only the mean and the alternating part.
        assert (F(1) + G) * m == r * (m * (1 - m) - d_sq) - m
        assert H == r * (1 - 2 * m)
        assert m * m > d_sq and (1 - m) * (1 - m) > d_sq
    return g, H, R, r_star, S


def numerical_check(q, M):
    import numpy as np
    g, H, R, r_star, S = exact_check(q, M)
    gf = [float(x) for x in g]
    r0 = float(r_star)

    def jac(x, r):
        J = np.zeros((M, M))
        J[0, 0] = r * (1 - 2 * x) - 1 - gf[1]
        for j in range(2, M + 1):
            J[0, j - 1] = -gf[j]
        for j in range(1, M):
            J[j, j - 1] = 1
        return J

    x0 = 1 - float(R) / r0
    eigenvalues = np.linalg.eigvals(jac(x0, r0))
    assert sum(abs(z + 1) < 1e-6 for z in eigenvalues) == 1
    assert all(abs(z) < 1 - 1e-7 for z in eigenvalues if abs(z + 1) >= 1e-6)
    for delta in [1e-5, 1e-4, 1e-3]:
        r = r0 + delta
        m = (r - float(H)) / (2 * r)
        d = sqrt((r - float(H)) * delta) / (2 * r)
        x_plus, x_minus = m + d, m - d
        assert 0 < x_minus < x_plus < 1
        U = [x_plus if j % 2 == 0 else x_minus for j in range(M)]
        V = [x_minus if j % 2 == 0 else x_plus for j in range(M)]
        def update(X):
            return r * X[0] * (1 - X[0]) - X[0] - sum(
                gf[j] * X[j-1] for j in range(1, M+1))
        assert abs(update(U) - x_minus) < 1e-10
        assert abs(update(V) - x_plus) < 1e-10
        eig2 = np.linalg.eigvals(jac(x_minus, r) @ jac(x_plus, r))
        lead = min(eig2, key=lambda z: abs(z - 1))
        expected = 1 - 4 * delta / float(S)
        assert abs(lead - expected) < 0.06 * delta
        assert max(abs(z) for z in eig2) < 1


if __name__ == '__main__':
    orders = [F(1, 20), F(1, 4), F(1, 2), F(3, 4), F(19, 20), F(1)]
    lengths = [1, 2, 3, 4, 5, 7, 10, 16]
    for order in orders:
        for length in lengths:
            exact_check(order, length)
    for order in orders:
        for length in [1, 2, 3, 5, 8, 12]:
            numerical_check(order, length)
    print('VERIFY_OK exact_fraction_cases=48 exact_period2_instances=144 '
          'spectral_cases=36 local_multiplier_cases=108')

#!/usr/bin/env python3
"""Exact local identities and numerical checks for three-step Lanczos heat propagation.

Requirements: Python 3, SymPy, NumPy, and SciPy. Run: python3 verify.py
"""
from itertools import combinations
from sympy import Matrix, Rational, eye, factor, symbols
import numpy as np
from scipy.linalg import eigh_tridiagonal
from scipy.optimize import brentq


def laplacian(n, edges):
    L = Matrix.zeros(n)
    W = Matrix.zeros(n)
    for a, b, weight in edges:
        w = Rational(weight)
        assert a != b and w > 0 and W[a, b] == 0
        W[a, b] = W[b, a] = w
        L[a, a] += w
        L[b, b] += w
        L[a, b] -= w
        L[b, a] -= w
    return L, W


def data(L, W, r):
    n = L.rows
    e = eye(n)[:, r]
    a0 = L[r, r]
    k1 = (L - a0 * eye(n)) * e
    b02 = (k1.T * k1)[0]
    if b02 == 0:
        return None
    a1 = factor((k1.T * L * k1)[0] / b02)
    v = (L - a1 * eye(n)) * k1 - b02 * e
    vv = factor((v.T * v)[0])
    if vv == 0:
        return None
    a2 = factor((v.T * L * v)[0] / vv)
    b12 = factor(vv / b02)
    for j in range(n):
        w = W[r, j]
        if j == r:
            assert v[j] == 0
        elif w > 0:
            triangle = sum(W[j, k] * W[r, k] for k in range(n) if k != j and k != r)
            adjusted_degree = L[j, j] - triangle / w
            assert factor(v[j] + w * (adjusted_degree - a1)) == 0
        else:
            paths2 = sum(W[j, k] * W[r, k] for k in range(n))
            assert v[j] == paths2
            assert v[j] >= 0
    # The projected matrix has exactly the expected first three moments.
    assert factor((k1.T * L * k1)[0] - b02 * a1) == 0
    assert factor((v.T * L * v)[0] - vv * a2) == 0
    return a0, b02, a1, b12, a2, k1, v, vv


def heat_approx(L, r, t):
    n = L.rows
    W = Matrix.zeros(n)
    for i in range(n):
        for j in range(i + 1, n):
            W[i, j] = W[j, i] = -L[i, j]
    D = data(L, W, r)
    if D is None:
        return None
    a0, b02, a1, b12, a2, k1, v, vv = D
    off = [np.sqrt(float(b02)), np.sqrt(float(b12))]
    al = [float(a0), float(a1), float(a2)]
    theta, U = eigh_tridiagonal(al, off)
    q0 = np.zeros(n)
    q0[r] = 1
    q1 = np.array(k1, dtype=float).ravel() / np.sqrt(float(b02))
    q2 = np.array(v, dtype=float).ravel() / np.sqrt(float(vv))
    Q = np.array([q0, q1, q2]).T
    # Matrix function via diagonalized projected Jacobi matrix.
    x = Q @ U @ (np.exp(-float(t) * theta) * U[0, :])
    assert np.allclose(Q.T @ Q, np.eye(3), atol=1e-9)
    return theta, x, D


def test_small_graphs():
    test_cases = [
        (3, [(0, 1, 1), (1, 2, 3)]),
        (4, [(0, 1, 1), (1, 2, 4), (2, 3, 2)]),
        (4, [(0, 1, 2), (0, 2, 3), (0, 3, 5)]),
        (4, [(0, 1, 2), (1, 2, 3), (2, 3, 5), (3, 0, 7)]),
        (4, [(0, 1, 3), (1, 2, 2), (2, 0, 5), (2, 3, 7)]),
        (5, [(0, 1, 1), (0, 3, 4), (0, 4, 40), (1, 2, 60)]),
        (5, [(0, 1, 2), (1, 2, 3), (2, 3, 1), (3, 4, 5), (4, 0, 7)]),
        (5, [(0, 1, 2), (0, 2, 1), (1, 2, 3), (0, 3, 7), (2, 4, 5)]),
        (6, [(0, 1, 3), (1, 2, 2), (2, 3, 4), (3, 4, 2), (4, 5, 6), (5, 0, 1)]),
    ]
    tested = 0
    for n, edges in test_cases:
        L, W = laplacian(n, edges)
        for r in range(n):
            z = data(L, W, r)
            if z is None:
                continue
            a0, b02, a1, b12, a2, _, _, _ = z
            for t in (0.005, 0.07, 0.2, 1., 4.):
                theta, x, _ = heat_approx(L, r, t)
                threshold = float(a1 + a2) - theta[0]
                assert x[r] > 0
                for j in range(n):
                    if j == r:
                        continue
                    w = W[r, j]
                    paths2 = sum(W[r, k] * W[k, j] for k in range(n))
                    if w == 0:
                        if paths2 > 0:
                            assert x[j] > -1e-12
                        else:
                            assert abs(x[j]) < 1e-10
                    else:
                        triangles = sum(W[r, k] * W[j, k] for k in range(n))
                        adjusted = float(L[j, j] - triangles / w)
                        if adjusted <= threshold - 1e-7:
                            assert x[j] > -1e-9
                tested += 1
    return tested


def exact_witness():
    L, W = laplacian(5, [(0, 1, 1), (0, 3, 4), (0, 4, 40), (1, 2, 60)])
    a0, b02, a1, b12, a2, k1, v, vv = data(L, W, 0)
    assert a0 == 45
    assert b02 == 1617
    assert a1 == Rational(21375, 539)
    assert b12 == Rational(4417376, 290521)
    assert a2 == Rational(1471877080, 74405177)
    assert a1 + a2 == Rational(8205095, 138043)
    assert 61 - a1 - a2 == Rational(215528, 138043) > 0
    lam = symbols('lam')
    det_formula = factor((lam - a0) * ((lam - a1) * (lam - a2) - b12) - b02 * (lam - a2))
    assert factor(det_formula - (138043 * lam**3 - 14417030 * lam**2 + 252207736 * lam - 363098400) / 138043) == 0
    theta, x, _ = heat_approx(L, 0, 0.2)
    assert min(theta) > 0
    assert x[1] < -0.0011 and x[1] > -0.0013
    assert all(x[j] > 0 for j in [0, 2, 3, 4])
    # Numerical crossing is supplementary; exact existence and uniqueness are proved analytically.
    root = brentq(lambda t: heat_approx(L, 0, t)[1][1], .1, .2)
    assert 0.11816 < root < 0.11817
    return root, x[1]


if __name__ == '__main__':
    n = test_small_graphs()
    root, neg = exact_witness()
    print(f'PASS: {n} point/time structural and sign checks')
    print('PASS: exact rational Lanczos moments, cubic and negative witness')
    print(f'Unique-crossing illustration: t={root:.12f}, x_1(0.2)={neg:.12g}')

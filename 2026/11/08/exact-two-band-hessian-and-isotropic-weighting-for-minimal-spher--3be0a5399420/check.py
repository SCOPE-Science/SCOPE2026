#!/usr/bin/env python3
"""Separate matrix and symbolic checks for the weighted simplex moment Hessian.

Requires Python 3, NumPy, and SymPy. All dimensions tested are finite; the
all-dimensions assertion is provided by the accompanying mathematical proof.
"""
import math
import numpy as np
import sympy as sp

COUNT = 0

def confirm(condition, message):
    global COUNT
    if not bool(condition):
        raise AssertionError(message)
    COUNT += 1


def simplex(d):
    n = d + 1
    p = np.eye(n) - np.ones((n, n)) / n
    q, _ = np.linalg.qr(p[:, :d])
    u = (q * math.sqrt(n / d)).T
    confirm(np.allclose(u.T @ u, np.eye(n) * (n / d) - np.ones((n, n)) / d,
                        atol=1.e-12), f'simplex Gram d={d}')
    return u


def tangent_basis(u):
    d, n = u.shape
    basis = []
    for i in range(n):
        w, v = np.linalg.eigh(np.eye(d) - np.outer(u[:, i], u[:, i]))
        for k in range(1, d):
            h = np.zeros_like(u)
            h[:, i] = v[:, k]
            basis.append(h)
    return basis


def calculated_hessian(u, a, b):
    hs = tangent_basis(u)
    js = np.stack([np.sum(h, axis=1) for h in hs], axis=1)
    jq = np.stack([(h @ u.T + u @ h.T).reshape(-1) for h in hs], axis=1)
    return 2 * (a * (js.T @ js) + b * (jq.T @ jq))


def predicted(d, a, b):
    n = d + 1
    v = 2 * (a * (d * d - 1) / d + b * 4 * n / (d * d))
    w = 8 * b * n / d
    return sorted([0.] * (d * (d - 1) // 2) +
                  [v] * d + [w] * ((d + 1) * (d - 2) // 2))


def energy(x, a, b):
    d, n = x.shape
    s = np.sum(x, axis=1)
    q = x @ x.T - (n / d) * np.eye(d)
    return a * float(s @ s) + b * float(np.sum(q * q))


def geodesic(u, h, t):
    v = np.zeros_like(u)
    for i in range(u.shape[1]):
        m = np.linalg.norm(h[:, i])
        if m == 0:
            v[:, i] = u[:, i]
        else:
            v[:, i] = u[:, i] * math.cos(t * m) + (h[:, i] / m) * math.sin(t * m)
    return v


d = sp.symbols('d', positive=True)
a, b = sp.symbols('a b', positive=True)
v = 2 * (a * (d**2 - 1) / d + 4 * b * (d + 1) / d**2)
w = 8 * b * (d + 1) / d
confirm(sp.simplify((v-w) / (a-4*b/d) - 2*(d**2-1)/d) == 0,
        'symbolic exact crossing')
confirm(sp.simplify(v.subs(a, 4*b/d) - w) == 0,
        'equal nonzero eigenvalues at the unique optimum')

rng = np.random.default_rng(8032)
for D in range(3, 11):
    U = simplex(D)
    n = D + 1
    confirm(np.allclose(np.sum(U, axis=1), 0, atol=1.e-12), f'centroid d={D}')
    confirm(np.allclose(U @ U.T, n / D * np.eye(D), atol=1.e-12),
            f'covariance d={D}')
    for A, B in [(1, 1), (1, 3), (3, 1), (4 / D, 1), (0.14, 2)]:
        H = calculated_hessian(U, A, B)
        numeric = np.linalg.eigvalsh(H)
        exact = predicted(D, A, B)
        confirm(np.allclose(numeric, exact, atol=2.e-11, rtol=2.e-11),
                f'Hessian spectrum d={D}, a={A}, b={B}')
        confirm(abs(np.trace(H) - sum(exact)) < 1.e-9,
                f'Hessian trace d={D}, a={A}, b={B}')
    confirm(energy(U, 2, 3) < 1.e-24, f'exact zero energy d={D}')
    h = rng.normal(size=U.shape)
    h -= U * np.sum(h * U, axis=0)[None, :]
    A, B = 0.6, 1.7
    ds = np.sum(h, axis=1)
    dq = h @ U.T + U @ h.T
    analytic = A * float(ds @ ds) + B * float(np.sum(dq*dq))
    for t in [2.e-4, 1.e-4]:
        eg = energy(geodesic(U, h, t), A, B)
        confirm(abs(eg / (t*t) - analytic) < max(0.01, 8.e-4*analytic),
                f'geodesic Hessian check d={D}, t={t}')

print(f'SIMPLEX_MOMENT_CHECKS_PASS {COUNT}')

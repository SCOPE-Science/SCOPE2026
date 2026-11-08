#!/usr/bin/env python3
"""Independent finite-precision checks for the explicit Gaussian Ritz moment law.

Proof is in RESULT.md; this program checks concrete algebra and numerics.
Requires Python 3 and numpy. No network or external files are needed.
"""
import math
import numpy as np


def moments(t):
    assert 0 < t < 1
    f1 = t * (t - 1 - math.log(t)) / (1 - t) ** 2
    f2 = t * (1 + 2 * t * math.log(t) - t * t) / (1 - t) ** 3
    return f1, f2


def one_angle(eps, seed=2026):
    rng = np.random.default_rng(seed)
    d = 2 * math.sin(eps) ** 2
    b = math.sin(2 * eps)
    t = b * b
    A = np.diag([-1.0, 0.0, 1.0, 2.0]).astype(complex)
    W = np.zeros((4, 2), dtype=complex)
    W[1, 0], W[3, 0], W[2, 1] = math.cos(eps), math.sin(eps), 1
    u = np.array([0, -math.sin(eps), 0, math.cos(eps)], dtype=complex)
    assert np.max(np.abs(W.conj().T @ W - np.eye(2))) < 1e-14
    assert np.max(np.abs(A @ W[:, 0] - d * W[:, 0] - b * u)) < 1e-14
    assert np.max(np.abs(W.conj().T @ A @ W - np.diag([d, 1]))) < 1e-14
    N = 35000
    omegas = (rng.normal(size=(N, 4, 2)) + 1j * rng.normal(size=(N, 4, 2))) / math.sqrt(2)
    G = np.conjugate(np.transpose(omegas, (0, 2, 1))) @ W
    H = np.conjugate(np.transpose(omegas, (0, 2, 1))) @ (A @ W)
    Q = np.linalg.solve(G, H)
    h = np.conjugate(np.transpose(omegas, (0, 2, 1))) @ u
    U = np.linalg.solve(G, h[..., np.newaxis])[..., 0]
    assert np.max(np.abs(Q[:, 0, 0] - d - b * U[:, 0])) < 1e-9
    assert np.max(np.abs(Q[:, 1, 0] - b * U[:, 1])) < 1e-9
    assert np.max(np.abs(Q[:, :, 1] - np.array([0, 1]))) < 1e-9
    z = -b * U[:, 1] / (1 - d - b * U[:, 0])
    rho = (d + abs(z) ** 2) / (1 + abs(z) ** 2)
    R = (rho - d) / (1 - d)
    assert np.all((R >= -1e-11) & (R <= 1 + 1e-11))
    for x in (0.02, 0.1, 0.25, 0.5, 0.9):
        ecdf = np.mean(R <= x)
        exact = x / (t + (1 - t) * x)
        assert abs(ecdf - exact) < 0.018, (eps, x, ecdf, exact)
    # Direct integration of the exact density, independent of the closed formulas.
    nodes, weights = np.polynomial.legendre.leggauss(768)
    xx = (nodes + 1) / 2
    ww = weights / 2
    den = t + (1 - t) * xx
    f1_num = float(np.sum(ww * xx * t / den ** 2))
    f2_num = float(np.sum(ww * xx ** 2 * t / den ** 2))
    f1, f2 = moments(t)
    assert abs(f1 - f1_num) < 1e-10
    assert abs(f2 - f2_num) < 1e-10
    # Sample moment checks are deliberately lower precision than exact quadrature.
    assert abs(np.mean(R) - f1) < 0.015
    assert abs(np.mean(R ** 2) - f2) < 0.014
    return {'angle': eps, 'samples': N, 'cdf_points': 5, 'f1': f1, 'f2': f2}


def main():
    results = [one_angle(e, seed=2026 + k) for k, e in enumerate((0.11, 0.23, 0.37))]
    angles = (1e-2, 1e-3, 1e-5, 1e-8)
    first = []; second = []
    for e in angles:
        d, t = 2 * math.sin(e) ** 2, math.sin(2 * e) ** 2
        f1, f2 = moments(t)
        mean = d + (1 - d) * f1
        ms = d * d + 2 * d * (1 - d) * f1 + (1 - d) ** 2 * f2
        first.append(mean / (e ** 2 * math.log(1 / e)))
        second.append(math.sqrt(ms) / e)
    assert abs(first[-1] - 8) < 0.8, first
    assert abs(second[-1] - 2) < 0.08, second
    for r in results:
        print('PASS angle={angle}, samples={samples}, cdf_points={cdf_points}, F1={f1:.9g}, F2={f2:.9g}'.format(**r))
    print('PASS asymptotic mean coefficient sequence:', first)
    print('PASS asymptotic RMS coefficient sequence:', second)
    print('ALL CHECKS PASSED')


if __name__ == '__main__':
    main()

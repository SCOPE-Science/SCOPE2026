#!/usr/bin/env python3
"""Numerical finite-section checks of a geometric-weight Cesaro singular law.
Dependencies: numpy and scipy. Checks corroborate; they do not certify an infinite asymptotic.
"""
import math
import numpy as np
from scipy.linalg import eigh_tridiagonal
from scipy.special import ellipk, spence


def matrix(n, r):
    rows = np.arange(1, n + 1)[:, None]
    cols = np.arange(1, n + 1)[None, :]
    return np.where(rows >= cols, r ** np.maximum(rows - cols, 0) / rows, 0.0)


def jacobi(n, r):
    j = np.arange(1, n + 1, dtype=float)
    return j**2 + (r * (j - 1))**2, -r * j[:-1] ** 2


def coefficient(r):
    return 2.0 * ellipk(4 * r / (1 + r) ** 2) / (math.pi * (1 + r))


def main():
    checks = 0
    for n in (3, 5, 8, 12, 20):
        for r in (0.0, 0.2, 0.5, 0.8):
            a = matrix(n, r)
            b = np.diag(np.arange(1, n + 1, dtype=float))
            b -= np.diag(r * np.arange(1, n, dtype=float), -1)
            assert np.allclose(b @ a, np.eye(n), rtol=0, atol=1.0e-12)
            diag, off = jacobi(n, r)
            assert np.allclose(b @ b.T, np.diag(diag) + np.diag(off, 1) + np.diag(off, -1), atol=1e-11)
            spec = np.linalg.svd(a, compute_uv=False)
            ev = eigh_tridiagonal(diag, off, eigvals_only=True, check_finite=False)
            assert np.allclose(spec, 1 / np.sqrt(ev), rtol=3e-10, atol=1e-11)
            checks += 3
    for r in (0.25, 0.5, 0.8):
        n_max = 5500
        diag, off = jacobi(n_max, r)
        ev = eigh_tridiagonal(diag, off, select='i', select_range=(0, 499), eigvals_only=True, check_finite=False)
        c = coefficient(r)
        assert c > 1
        for k in (50, 100, 200, 350, 500):
            approx = k / math.sqrt(ev[k - 1])
            assert abs(approx - c) < (0.13 / k ** 2 + 1e-7)
            checks += 1
        print(f'r={r:.2f} singular coefficient={c:.12f}; 500*s_500={500/math.sqrt(ev[499]):.12f}')
    for r in (0.0, 0.25, 0.5, 0.8):
        z = r*r
        theoretical = (math.pi**2/6 - spence(1-z))/(1-z)
        j = np.arange(1, 10001, dtype=float)
        truncated = np.sum((1 - z**j)/(j*j*(1-z)))
        assert 0 <= theoretical-truncated <= 1/((1-z)*10000) + 1e-10
        checks += 1
    assert coefficient(0.0) == 1
    print(f'PASS: {checks + 1} finite matrix/spectral/coefficient assertions')


if __name__ == '__main__':
    main()

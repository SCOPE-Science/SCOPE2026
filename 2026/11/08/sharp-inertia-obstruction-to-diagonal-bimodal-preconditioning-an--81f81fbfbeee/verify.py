#!/usr/bin/env python3
"""Finite diagnostics for the accompanying analytic spectral theorem.
Requires Python 3 and NumPy; finite checks are not a proof of all-dimensional claims.
"""
import numpy as np

checks = 0
rng = np.random.default_rng(20260622)
for n in range(3, 18):
    J = np.ones((n, n))
    P = J / n
    for t in range(8):
        w = np.exp(rng.uniform(-1.5, 1.5, n))
        W = np.diag(w)
        A = W @ (J - np.eye(n)) @ W
        G = np.diag(np.sqrt(2 / n) / w)
        e = np.linalg.eigvalsh(G.T @ A @ G)
        value = np.mean((np.abs(e) - 1) ** 2)
        sharp = ((n - 2) / n) ** 2
        assert abs(value - sharp) < 5e-12
        checks += 1
        Q = np.eye(n) + (1 / np.sqrt(n - 1) - 1) * P
        Gr = np.diag(1 / w) @ Q
        actual = Gr.T @ A @ Gr
        assert np.max(np.abs(actual - (2 * P - np.eye(n)))) < 5e-12
        checks += 1
        for k in range(4):
            H = np.diag(np.exp(rng.uniform(-1, 1, n)) / w)
            f = np.linalg.eigvalsh(H.T @ A @ H)
            assert np.mean((np.abs(f) - 1) ** 2) >= sharp - 5e-12
            checks += 1
    for k in range(12):
        M = rng.normal(size=(n, n))
        A = (M + M.T) / 2
        np.fill_diagonal(A, 0)
        G = np.diag(np.exp(rng.uniform(-1, 1, n)))
        B = G @ A @ G
        e = np.linalg.eigvalsh(B)
        r = np.count_nonzero(e > 1e-9)
        s = np.count_nonzero(e < -1e-9)
        if r + s != n or min(r, s) < 1:
            continue
        value = np.mean((abs(e) - 1) ** 2)
        assert value >= ((r - s) / n) ** 2 - 5e-11
        checks += 1
print('PASS', checks, 'finite checks; analytic universal proof is in RESULT.md')

#!/usr/bin/env python3
"""Bounded numeric checks of the Schur-cycle theorem, including the shift sign."""
import numpy as np


def nuclear(matrix):
    return float(np.linalg.svd(matrix, compute_uv=False).sum())


def objective(mask, u, v):
    assert min(u.min(), v.min()) >= -1e-13
    return nuclear(np.sqrt(np.maximum(u, 0))[:, None] * mask * np.sqrt(np.maximum(v, 0))[None, :])


def weights(n, a, b, shift=0.0):
    angles = 2*np.pi*(np.arange(n) + shift)/n
    return (1 + a*np.cos(angles) + b*np.sin(angles))/n


dimensions = 0
boundary_vertices = 0
for n in range(3, 41):
    rows = np.arange(n)
    p = np.zeros((n, n))
    p[rows, (rows - 1) % n] = 1
    assert np.array_equal(p @ rows, (rows - 1) % n)
    mask = np.eye(n) + p
    target = 2/(n * (np.sin(np.pi/(2*n)) if n % 2 else np.tan(np.pi/(2*n))))
    assert abs(nuclear(mask)/n - target) < 1e-10
    dimensions += 1
    for a, b in [(0.0, 0.0), (0.4, 0.0), (0.15, -0.2), (-0.12, 0.23)]:
        u = weights(n, a, b)
        v = weights(n, a, b, 0.5 if n % 2 == 0 else 0.0)
        got = objective(mask, u, v)
        if n % 2 and (a or b):
            assert got < target - 1e-8
        else:
            assert abs(got - target) < 1e-10
    if n % 2 == 0:
        # Adjacent half-plane normals at spacing pi/n give all polygon vertices.
        half = np.pi/(2*n)
        for ell in range(2*n):
            phi = ell*np.pi/n + half
            a, b = -np.cos(phi)/np.cos(half), -np.sin(phi)/np.cos(half)
            u, v = weights(n, a, b), weights(n, a, b, 0.5)
            assert np.count_nonzero(np.abs(np.r_[u, v]) < 1e-12) == 2
            assert abs(objective(mask, u, v) - target) < 1e-8
            boundary_vertices += 1
    if n == 4:
        u = weights(n, 0.4, 0)
        v_reverse = weights(n, 0.4, 0, -0.5)
        assert objective(mask, u, v_reverse) < target - 0.01
        assert abs(objective(mask.T, u, v_reverse) - target) < 1e-10

print(f"CYCLE_SCHUR_CHECKS_PASS dimensions={dimensions} boundary_vertices={boundary_vertices}")

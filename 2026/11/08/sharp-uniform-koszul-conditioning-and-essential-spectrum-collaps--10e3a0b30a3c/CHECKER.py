#!/usr/bin/env python3
"""Finite-fermionic consistency checks for a normal Koszul complex.

These finite tests do not establish infinite-dimensional Fredholm statements.
"""
import numpy as np
from itertools import product

count = 0
m = 4
size = 1 << m
ann = []
for j in range(m):
    a = np.zeros((size, size), dtype=complex)
    for state in range(size):
        if (state >> j) & 1:
            dest = state ^ (1 << j)
            a[dest, state] = (-1) ** ((state & ((1 << j) - 1)).bit_count())
    ann.append(a)
I = np.eye(size, dtype=complex)
for i in range(m):
    for j in range(m):
        left = ann[i] @ ann[j].conj().T + ann[j].conj().T @ ann[i]
        assert np.allclose(left, I if i == j else np.zeros_like(I), atol=1e-12)
        count += 1
rows = [
    np.array([[0.8, 0.0, -0.3, 1.2], [-0.5, 1.1, 0.0, -0.7]], dtype=complex),
    np.array([[0.2j, 1.0, -1.0, 0.3], [0.6, -0.2j, 1.3, 0.1]], dtype=complex),
]
for z in rows:
    for lam in [np.array([0.13+0.09j, -0.11, 0.3, 0.21]), np.array([0.4, 0.7j, -0.2, 0.5])]:
        dif = z - lam[None, :]
        d = sum(np.kron(np.diag(dif[:, j]), ann[j]) for j in range(m))
        B = np.diag(np.sum(abs(dif)**2, axis=1))
        assert np.allclose(d @ d, 0, atol=1e-12)
        count += 1
        assert np.allclose(d @ d.conj().T + d.conj().T @ d, np.kron(B, I), atol=1e-12)
        count += 1
        degree_one = [1 << j for j in range(m)]
        cols = [a*size + b for a in range(z.shape[0]) for b in degree_one]
        rows0 = [a*size for a in range(z.shape[0])]
        d1 = d[np.ix_(rows0, cols)]
        sig = np.linalg.svd(d1, compute_uv=False)
        expected = np.sqrt(np.min(np.diag(B))).real
        assert np.isclose(np.min(sig), expected, rtol=1e-12)
        count += 1
        lift = d1.conj().T @ np.linalg.inv(B)
        assert np.allclose(d1 @ lift, np.eye(z.shape[0]), atol=1e-12)
        count += 1
        assert np.isclose(np.linalg.norm(lift, ord=2), 1/expected, rtol=1e-12)
        count += 1
print('NORMAL_KOSZUL_FINITE_CHECKS_OK', count)

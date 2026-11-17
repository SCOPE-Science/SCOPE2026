#!/usr/bin/env python3
"""Numerical checks for nearly flat spherical random tetrahedra.

Samples the first three surface-uniform vertices and integrates the fourth
vertex's polar coordinate analytically. This is a finite check, not proof.
"""
import math
import numpy as np


def sample(n=1_500_000, seed=211108):
    rng = np.random.default_rng(seed)
    p = rng.standard_normal((n, 3, 3))
    p /= np.linalg.norm(p, axis=2, keepdims=True)
    u, v = p[:, 1] - p[:, 0], p[:, 2] - p[:, 0]
    cross = np.cross(u, v)
    D = np.linalg.norm(cross, axis=1)
    h = np.einsum('ij,ij->i', cross, p[:, 0]) / D
    L = np.linalg.norm(u, axis=1)
    assert np.all((D > 0) & (np.abs(h) < 1 + 1e-12))
    return D, h, L


def main():
    D, h, L = sample()
    inv = float(np.mean(np.minimum(1 / D, 10000)))
    print(f'truncated_E1_over_D={inv:.8f}; exact_untruncated={math.pi/2:.8f}')
    assert abs(inv-math.pi/2) < .05
    previous = 0.
    for eps in (.01, .002, .00025, .0001):
        delta = 6 * eps / D
        prob = .5 * np.maximum(0, np.minimum(1, h + delta) - np.maximum(-1, h - delta))
        coef = float(prob.mean()/eps)
        edge_mean = float(prob.dot(L) / prob.sum())
        print(f'eps={eps:.5f}, P/eps={coef:.6f}, conditional-edge-mean={edge_mean:.6f}')
        assert coef > previous
        previous = coef
    assert abs(coef-3*math.pi) < .25
    assert abs(edge_mean-1.) < .04
    print('SPHERE_TETRA_SMALL_VOLUME_UNIFORM_CHORD_OK')


if __name__ == '__main__':
    main()

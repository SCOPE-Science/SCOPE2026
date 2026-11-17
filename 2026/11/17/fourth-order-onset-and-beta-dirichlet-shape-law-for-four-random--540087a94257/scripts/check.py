#!/usr/bin/env python3
"""Reproducibility checks for the four-cap endpoint theorem.

Requires numpy and sympy. Monte Carlo is corroboration, not proof.
"""
import math
import numpy as np
import sympy as s


def symbolic_jacobian():
    t2, t3 = s.sqrt(2), s.sqrt(3)
    a, b, k = t2 / 3, -2 * t2 / 3, 4 * t3 / 9
    z = s.zeros(1, 5)
    dot = {
        (1, 2): s.Matrix([[a, a, 0, -k, 0]]),
        (1, 3): s.Matrix([[a, 0, a, 0, k]]),
        (2, 3): s.Matrix([[0, a, a, k, -k]]),
        (1, 4): s.Matrix([[b, 0, 0, 0, 0]]),
        (2, 4): s.Matrix([[0, b, 0, 0, 0]]),
        (3, 4): s.Matrix([[0, 0, b, 0, 0]]),
    }
    rows = []
    for vertex in [1, 2, 3]:
        rows.append(sum((v for pair, v in dot.items() if vertex not in pair), z) / 3)
    rows += [(dot[1, 2] + dot[3, 4]) / 4,
             (dot[1, 3] + dot[2, 4]) / 4]
    jac = s.Matrix.vstack(*rows)
    det = s.simplify(jac.det())
    assert s.simplify(abs(det) - 64 * t2 / 19683) == 0
    sin0 = 2 * t2 / 3
    branch_density = s.simplify(sin0**3 / (32 * s.pi**2 * abs(det)))
    assert s.simplify(branch_density - 729 / (128 * s.pi**2)) == 0
    alpha, beta, delta, q = s.symbols('alpha beta delta q', real=True, positive=True)
    Q = alpha**2 + beta**2 + (alpha + beta)**2
    assert s.simplify((s.hessian(Q, (alpha, beta)) / 2).det() - 3) == 0
    volume = s.simplify(s.pi / s.sqrt(3) * s.integrate((4 * delta - 2 * q)**3 / 6, (q, 0, 2 * delta)))
    assert s.simplify(volume - 16 * s.pi * delta**4 / (3 * t3)) == 0
    C = s.simplify(2 * branch_density * volume / delta**4)
    assert s.simplify(C - 81 * t3 / (4 * s.pi)) == 0
    Cangle = s.simplify(C * (2 * t2 / 3)**4)
    assert s.simplify(Cangle - 16 * t3 / s.pi) == 0
    print('Jacobian, two branches, quartic constant, angular conversion: exact OK')
    return float(C)


def random_check(C, sample_size=1_500_000):
    rng = np.random.default_rng(921742)
    gaps = np.array([0.14, 0.10, 0.08], dtype=float)
    hits = np.zeros(len(gaps), dtype=int)
    for j in range(0, sample_size, 50000):
        n = min(50000, sample_size - j)
        points = rng.normal(size=(n, 4, 3))
        points /= np.linalg.norm(points, axis=2, keepdims=True)
        height = np.zeros((n, 4))
        origin_inside = np.ones(n, dtype=bool)
        for i in range(4):
            triple = [k for k in range(4) if k != i]
            a, b, c = (points[:, k, :] for k in triple)
            normal = np.cross(b - a, c - a)
            support = np.einsum('ij,ij->i', normal, a)
            opposite = np.einsum('ij,ij->i', normal, points[:, i, :])
            origin_inside &= (-support) * (opposite - support) > 0
            height[:, i] = np.abs(support) / np.linalg.norm(normal, axis=1)
        radius = height.min(axis=1)
        for k, gap in enumerate(gaps):
            hits[k] += np.count_nonzero(origin_inside & (radius >= 1 / 3 - gap))
    estimate = hits / sample_size / gaps**4
    print('Counts by gap:', list(zip(gaps.tolist(), hits.tolist())))
    print('Observed ratios:', estimate, 'asymptotic constant', C)
    # The sampled gaps are not asymptotically tiny, so use a loose finite-size check.
    assert np.all(estimate > C * 0.6)
    assert np.all(estimate < C * 1.5)


if __name__ == '__main__':
    C = symbolic_jacobian()
    random_check(C)
    print('FOUR_RANDOM_CAP_TETRAHEDRAL_ENDPOINT_OK')

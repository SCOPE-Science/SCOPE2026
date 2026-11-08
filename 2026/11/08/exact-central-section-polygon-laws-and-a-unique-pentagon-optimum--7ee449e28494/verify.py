#!/usr/bin/env python3
"""Independent checks of central-section polygon-type laws for a right regular triangular prism.
This script tests the mathematical formulas by direct edge intersection and high-precision quadrature.
It is not an exhaustive proof of a continuum statement.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq

THETA = 2 * np.pi * np.arange(3) / 3
PLANAR = np.stack((np.cos(THETA), np.sin(THETA)), axis=1)
EDGES = [(i, (i + 1) % 3) for i in range(3)] + [(i + 3, (i + 1) % 3 + 3) for i in range(3)] + [(i, i + 3) for i in range(3)]


def exact_probs(H):
    assert H > 0
    c = math.sqrt(1 + H * H)
    F = lambda b: math.asin(b / c)
    p3 = 1 - 6 / math.pi * F(0.5)
    p5 = 6 / math.pi * (2 * F(math.sqrt(3) / 2) - F(0.5) - F(1))
    return {3: p3, 4: 1 - p3 - p5, 5: p5}


def edge_intersections(normals, H):
    """Count crossings of the prism's nine actual edges for a centroidal plane."""
    n = normals.shape[0]
    xy = normals[:, :2] @ PLANAR.T
    z = H * normals[:, 2:3]
    sides = np.hstack((xy - z, xy + z))
    crosses = np.zeros(n, dtype=int)
    for i, j in EDGES:
        crosses += (sides[:, i] * sides[:, j] < 0)
    assert np.all((crosses >= 3) & (crosses <= 5)), 'unexpected section type'
    return crosses


def conditional_probs(H):
    """Independent angular integration of the order-statistic events."""
    t = lambda b: b / math.sqrt(H * H + b * b)
    f = lambda phi: sorted((abs(math.cos(phi - angle)) for angle in (0, 2*math.pi/3, 4*math.pi/3)))
    p3 = 6/math.pi * quad(lambda phi: 1 - t(f(phi)[2]), 0, math.pi/6, epsabs=1e-12)[0]
    p5 = 6/math.pi * quad(lambda phi: t(f(phi)[1]) - t(f(phi)[0]), 0, math.pi/6, epsabs=1e-12)[0]
    return {3:p3,4:1-p3-p5,5:p5}


def J(H):
    return math.sqrt(3)*H / math.sqrt(H*H + 0.25) - 0.5*H / math.sqrt(H*H + 0.75)


def dJ(H):
    return (math.sqrt(3)/4)/(H*H+0.25)**1.5 - (3/8)/(H*H+0.75)**1.5

rng = np.random.default_rng(20261102)
H_values = (0.12, 0.35, 0.5314695510636118, 0.8, 1.0, 2.5, 8.0)
normal_count = 180000
max_simulation_error = 0.0
for H in H_values:
    p = exact_probs(H)
    q = conditional_probs(H)
    assert abs(sum(p.values()) - 1.0) < 1e-13 and min(p.values()) > 0
    assert max(abs(p[v] - q[v]) for v in (3,4,5)) < 1e-12
    normals = rng.standard_normal((normal_count, 3))
    counts = edge_intersections(normals, H)
    freq = {v: np.mean(counts == v) for v in (3,4,5)}
    for v in (3,4,5):
        err = abs(freq[v] - p[v])
        max_simulation_error = max(max_simulation_error, err)
        # 6 sigma plus fixed slack for independent Monte-Carlo samples
        bound = 6*math.sqrt(p[v]*(1-p[v])/normal_count) + .001
        assert err < bound, (H, v, err, bound)

star = brentq(lambda H:J(H)-1, 0.001, 5.0, xtol=1e-14)
assert abs(star - 0.5314695510636118) < 1e-12
assert all(dJ(x) > 0 for x in (1e-6,.01,.1,.5,1,5,1e4))
assert exact_probs(star)[5] > max(exact_probs(star*0.99)[5],exact_probs(star*1.01)[5])
assert abs(exact_probs(star)[5] - 0.3851558056741766) < 1e-12
print(f'VERIFY_OK heights={len(H_values)} plane_normals={len(H_values)*normal_count} exact_integrals=14 ' 
      f'max_absolute_sampling_error={max_simulation_error:.6g} pentagon_optimum_H={star:.12f} '
      f'pentagon_probability={exact_probs(star)[5]:.12f}')

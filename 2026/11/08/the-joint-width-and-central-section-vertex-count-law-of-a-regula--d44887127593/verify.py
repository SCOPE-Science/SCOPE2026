#!/usr/bin/env python3
"""Reproduce the exact joint width/section-count law for a regular tetrahedron.

Requires numpy and scipy. The analytic proof is in RESULT.md; simulations
and numerical quadrature here are independent finite checks, not an infinite proof.
"""
import math
import numpy as np
from scipy.integrate import quad

PI = math.pi
DELTA = math.atan(math.sqrt(2.0))
B0 = 1 / math.sqrt(2.0)
B1 = math.sqrt(2.0 / 3.0)
B2 = math.sqrt(3.0) / 2.0

def theta(s):
    return math.acos(min(1.0, max(-1.0, s / math.sqrt(3.0 * (1.0 - s * s)))))

def density(s, n):
    if s < B0 or s > 1.0:
        return 0.0
    if n == 4:
        return 12.0 / PI * (DELTA - theta(s) if s < B2 else DELTA)
    if n == 3:
        if s < B1:
            return 0.0
        if s < B2:
            return 12.0 / PI * (PI / 2.0 - DELTA - theta(s))
        return 12.0 / PI * (PI / 2.0 - DELTA)
    raise ValueError(n)

def integ(fun, a, b):
    return quad(fun, a, b, epsabs=2e-12, epsrel=2e-12)[0]

def integral(fn):
    return sum(integ(fn, a, b) for a, b in [(B0, B1), (B1, B2), (B2, 1.0)])

mass_4 = integral(lambda s: density(s, 4))
mass_3 = integral(lambda s: density(s, 3))
assert abs(mass_4 + mass_3 - 1.0) < 1e-11
assert abs(mass_4 - (6 * math.acos(-1 / 3) / PI - 3)) < 1e-11
assert abs(integral(lambda s: s * (density(s, 3) + density(s, 4))) - 3 * math.acos(-1 / 3) / (2 * PI)) < 1e-11
assert abs(integral(lambda s: s * s * (density(s, 3) + density(s, 4))) - (1 / 3 + (3 + math.sqrt(3)) / (3 * PI))) < 1e-11
assert abs(density(B2 + 1e-6, 4) / (density(B2 + 1e-6, 4) + density(B2 + 1e-6, 3)) - 2 * DELTA / PI) < 1e-11
assert all(density(s, 3) == 0 for s in np.linspace(B0, B1-1e-8, 30))

v = np.asarray([[1, 1, 1], [1,-1,-1],[-1,1,-1],[-1,-1,1]], dtype=float)
rng = np.random.default_rng(71725)
m = 500_000
u = rng.normal(size=(m, 3))
u /= np.linalg.norm(u, axis=1)[:, None]
h = u @ v.T
w = (np.max(h, axis=1) - np.min(h, axis=1)) / (2 * math.sqrt(2))
num = np.sum(h > 0, axis=1)
n = np.where(num == 2, 4, 3)
a = np.sort(np.abs(u), axis=1)
assert np.max(np.abs(w - (a[:, 1] + a[:, 2]) / math.sqrt(2))) < 2e-15
assert np.all((n == 3) | (n == 4))
assert not np.any((w < B1 - 1e-12) & (n == 3))
max_dev = 0.0
for l, r in [(B0, B1), (B1, B2), (B2, 0.92), (0.92, 0.96), (0.96, 1.0)]:
    for k in (3, 4):
        p_expected = integ(lambda s: density(s, k), l, r)
        p_observed = np.mean((w >= l) & (w < r) & (n == k))
        max_dev = max(max_dev, abs(p_expected-p_observed))
assert max_dev < 0.004
print(f'VERIFY_OK total_probability=1 exact_moment_consistency=2 tetrahedral_width_identity={m} '
      f'joint_mass_checks=10 max_absolute_simulation_deviation={max_dev:.9f} '
      f'four_vertex_probability={mass_4:.12f} triangular_probability={mass_3:.12f}')

#!/usr/bin/env python3
"""Numerical geometry checks of an explicit axes-plus-diagonal zonotope.

Needs numpy and scipy; run `python check_zonotope.py`.
"""
import itertools
import math
import random

import numpy as np
from scipy.spatial import ConvexHull


def formula(d, b, a):
    v = math.prod(b) + a * sum(math.prod(b[j] for j in range(d) if j != i) for i in range(d))
    s = 2 * sum(math.prod(b[j] for j in range(d) if j != i) for i in range(d))
    s += 2 * math.sqrt(2) * a * sum(math.prod(b[k] for k in range(d) if k != i and k != j)
                                      for i in range(d) for j in range(i + 1, d))
    return v, s


def vertices(d, b, a):
    return np.array([[b[i] * ((mask >> i) & 1) + a * z for i in range(d)]
                     for mask in range(1 << d) for z in (0, 1)], dtype=float)


def quotient(d, b, a):
    v, s = formula(d, b, a)
    return s**d / v**(d - 1)


def check():
    rng = random.Random(20261115)
    count = 0
    for d in range(2, 7):
        for trial in range(7):
            b = [rng.uniform(0.45, 2.3) for _ in range(d)]
            a = rng.uniform(.13, 1.7)
            volume, boundary = formula(d, b, a)
            hull = ConvexHull(vertices(d, b, a))
            assert math.isclose(hull.volume, volume, rel_tol=1e-9, abs_tol=1e-9), (d, trial, 'volume')
            assert math.isclose(hull.area, boundary, rel_tol=1e-9, abs_tol=1e-9), (d, trial, 'boundary')
            count += 1

    root2 = math.sqrt(2)
    for d in range(2, 11):
        optimum = (root2 * d)**d * (1 + d * (root2 - 1))
        assert math.isclose(quotient(d, [1.] * d, root2 - 1), optimum, rel_tol=2e-12)
        for t in range(1, 10):
            b = [1.0 + (t * i) / (20. * d) for i in range(d)]
            a = (root2 - 1) * (1 + t / 30)
            assert quotient(d, b, a) > optimum, (d, t)
    print(f'AXES_DIAGONAL_ISOPERIMETRY_CHECK_PASS hull_cases={count} dimensions=2..10')


if __name__ == '__main__':
    check()

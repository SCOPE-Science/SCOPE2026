#!/usr/bin/env python3
"""Reproduce independent exact-slice quadrature and direct Euclidean geometry checks."""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import beta

C = beta(1 / 3, 3 / 2) * beta(1 / 3, 1 / 3) / (2 ** (2 / 3) * math.pi)
assert 2.68231 < C < 2.68232

def conditional_slice(length, threshold):
    delta = 2 * threshold / length
    h = math.sqrt(1 - length * length / 4)
    if delta >= 1 + h:
        return 1.0
    lower, upper = max(-1., h - delta), min(1., h + delta)
    if lower >= upper:
        return 0.0
    def integrand(u):
        ball_y2 = max(0., delta * delta - (u - h) ** 2)
        disk_y2 = max(0., 1 - u * u)
        if disk_y2 < 1.e-14:
            return .5
        return math.asin(min(1., math.sqrt(ball_y2 / disk_y2))) / math.pi
    crossover = (1 + h * h - delta * delta) / (2 * h) if h > 1.e-8 else 1.
    endpoints = [lower] + ([crossover] if lower < crossover < upper else []) + [upper]
    return sum(quad(integrand, a, b, epsabs=2e-9, epsrel=3e-7, limit=100)[0]
               for a, b in zip(endpoints, endpoints[1:]))

def exact_integral(threshold):
    scale = threshold ** (1 / 3)
    endpoints = [0., scale / 4, scale, 4 * scale, 2.]
    endpoints = sorted(set(x for x in endpoints if 0 <= x <= 2))
    def f(length):
        return (length / 2) * conditional_slice(length, threshold) if length else 0.
    return sum(quad(f, a, b, epsabs=1e-11, epsrel=3e-5, limit=160)[0]
               for a, b in zip(endpoints, endpoints[1:]))

ratios = []
for eps in (0.02, 0.005, 0.001):
    p = exact_integral(eps)
    ratio = p / (C * eps ** (5 / 3))
    ratios.append(ratio)
    print(f'exact quadrature t={eps}: probability={p:.12g}, asymptotic-ratio={ratio:.8f}')
assert 0.79 < ratios[0] < 0.82
assert 0.86 < ratios[1] < 0.89
assert 0.92 < ratios[2] < 0.94
assert ratios[0] < ratios[1] < ratios[2] < 1

rng = np.random.default_rng(20261108)
n = 1200000
points = rng.normal(size=(n, 3, 3))
points /= np.linalg.norm(points, axis=2, keepdims=True)
area = 0.5 * np.linalg.norm(np.cross(points[:, 1] - points[:, 0], points[:, 2] - points[:, 0]), axis=1)
for eps in (0.02, 0.005):
    observed = float(np.mean(area <= eps))
    expected = exact_integral(eps)
    standard_error = math.sqrt(expected * (1 - expected) / n)
    print(f'direct vectors t={eps}: frequency={observed:.9g}, exact-slice={expected:.9g}, SE={standard_error:.3g}')
    assert abs(observed - expected) < 5 * standard_error
print('SPHERE_CHORD_TRIANGLE_SMALL_AREA_CHECK_OK')

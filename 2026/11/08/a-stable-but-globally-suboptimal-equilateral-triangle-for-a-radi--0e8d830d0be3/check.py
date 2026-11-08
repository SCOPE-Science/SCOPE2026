#!/usr/bin/env python3
"""Reproducible interval and independent geometric checks for radial-power triangles."""
from math import cos, sin, pi
from mpmath import iv

P_NUM, P_DEN = 7, 4
S_NUM, S_DEN = 15, 4
N = 4096
iv.dps = 30
s = iv.mpf(S_NUM) / S_DEN


def sector_interval(a):
    """Riemann bounds for integral_0^a (cos(a)/cos(t))^s dt."""
    c = iv.cos(a)
    h = a / N
    total = iv.mpf(0)
    for j in range(N):
        total += (c / iv.cos(a * j / N)) ** s
    lower = h * total
    # The integrand is strictly increasing; endpoint difference is exact.
    upper = lower + h * (1 - c ** s)
    return lower, upper


def endpoints(x):
    return float(x.a), float(x.b)


a = sector_interval(iv.pi * 19 / 72)  # half of 95 degrees
b = sector_interval(iv.pi * 17 / 36)  # half of 170 degrees
e = sector_interval(iv.pi / 3)        # half of 120 degrees
# Integral over each sector has factor 2/(p+2).
delta_lower = (2 / s) * (2 * a[0] + b[0] - 3 * e[1])
# 2 f''(2pi/3) = (3p+2)*I(p) - sqrt(3).
hessian_upper = (iv.mpf(3) * iv.mpf(P_NUM) / P_DEN + 2) * e[1] - iv.sqrt(3)
assert delta_lower.a > 0, endpoints(delta_lower)
assert hessian_upper.b < 0, endpoints(hessian_upper)
print('Certified radial-power advantage lower:', endpoints(delta_lower))
print('Certified equilateral second-variation upper:', endpoints(hessian_upper))


def integrate_triangle(gaps, power=P_NUM / P_DEN, n=400):
    """Independent midpoint integration of |x|^power over a physical triangle."""
    angles = [0., gaps[0], gaps[0] + gaps[1]]
    vertices = [(cos(t), sin(t)) for t in angles]
    x0, y0 = vertices[0]
    dx1, dy1 = vertices[1][0] - x0, vertices[1][1] - y0
    dx2, dy2 = vertices[2][0] - x0, vertices[2][1] - y0
    determinant = abs(dx1 * dy2 - dx2 * dy1)
    total = 0.
    for i in range(n):
        u = (i + 0.5) / n
        b = 1. - u
        x_base, y_base = x0 + u * dx1, y0 + u * dy1
        for j in range(n):
            v = b * (j + 0.5) / n
            x, y = x_base + v * dx2, y_base + v * dy2
            total += b * (x * x + y * y) ** (power / 2)
    return total * determinant / (n * n)


regular = integrate_triangle([2 * pi / 3] * 3)
competitor = integrate_triangle([19 * pi / 36, 19 * pi / 36, 17 * pi / 18])
assert competitor - regular > 3e-4, (regular, competitor)
print('Independent 2D quadrature regular and competitor:', regular, competitor)
print('ALL_RADIAL_WEIGHTED_TRIANGLE_CHECKS_PASSED')

#!/usr/bin/env python3
"""Consistency checks for exact beta identities and asymptotic coefficients.

Requires only Python's standard library. Finite checks are not substitutes
for the analytic uniform-error proof accompanying the theorem.
"""
import math


def beta(a, b):
    return math.gamma(a) * math.gamma(b) / math.gamma(a + b)


def close(x, y, tol=1e-10):
    assert math.isclose(x, y, rel_tol=tol, abs_tol=tol), (x, y)


for k in range(2, 20):
    alpha = 1.0 / k
    j = beta(alpha, 0.5) / k
    v = beta(alpha, 1.5) / k
    close(v / j, k / (k + 2))
    close(beta(alpha + 1, 0.5) / beta(alpha, 0.5), 2 / (k + 2))
    close(beta(alpha + 1, 1.5) / beta(alpha, 1.5), 2 / (3 * k + 2))

for m in (4, 6, 8, 10):
    for n in range(2, m):
        jn = beta(1 / n, 0.5) / n
        jm = beta(1 / m, 0.5) / m
        vn = beta(1 / n, 1.5) / n
        vm = beta(1 / m, 1.5) / m
        close((jn / jm) / (vn / vm), m * (n + 2) / (n * (m + 2)))

# Exact one-sided harmonic/quartic example:
# U_+(r)=r^2/2, U_-(r)=r^4/4.
B12 = beta(0.25, 0.5)
B32 = beta(0.25, 1.5)
for h in (1e-4, 1e-8, 1e-12):
    t_plus = math.pi
    t_minus = B12 / 2 * h ** (-0.25)
    a_plus = math.pi * h
    a_minus = B32 * h ** 0.75
    ratio = (t_plus / (t_plus + t_minus)) / (a_plus / (a_plus + a_minus))
    assert abs(ratio - 4 / 3) <= 10 * h ** 0.25
    eps = h * 1e-6
    area_p = math.pi * (h + eps) + B32 * (h + eps) ** 0.75
    area_m = math.pi * (h - eps) + B32 * (h - eps) ** 0.75
    close((area_p - area_m) / (2 * eps), t_plus + t_minus, tol=3e-8)

# Independent inverse-derivative perturbation check:
# U(r)=a*r^k*(1+b*r). The fractional correction coefficient is 2*b/k.
a, b, k = 0.7, 0.25, 4
for u in (1e-4, 1e-6, 1e-8, 1e-10):
    lo, hi = 0.0, (2 * u / a) ** (1 / k)
    for _ in range(100):
        mid = (lo + hi) / 2
        if a * mid ** k * (1 + b * mid) < u:
            lo = mid
        else:
            hi = mid
    r = (lo + hi) / 2
    d_exact = 1 / (a * k * r ** (k - 1) * (1 + (k + 1) / k * b * r))
    alpha = 1 / k
    A = a ** (-alpha)
    d_asym = A * alpha * u ** (alpha - 1) * (1 - 2 * alpha * b * A * u ** alpha)
    relative_error = abs(d_exact / (A * alpha * u ** (alpha - 1)) - d_asym / (A * alpha * u ** (alpha - 1)))
    assert relative_error < 4 * u ** (2 * alpha)

print('DUAL_BETA_TIME_AREA_SWITCHING_CENTER_CHECK_OK')

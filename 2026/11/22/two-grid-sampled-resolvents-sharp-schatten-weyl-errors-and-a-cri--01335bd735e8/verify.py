#!/usr/bin/env python3
"""Finite diagnostics for the positive two-grid sampled-resolvent formula."""
import math


def phi(u):
    if u < 0.1:
        # Stable expansion from the power series of the hyperbolic cosecant.
        return u / 24 - 7 * u**3 / 5760 + 31 * u**5 / 967680
    return 1 / u - math.exp(-u / 2) / (1 - math.exp(-u))


def two_grid(h, a):
    x = h * a
    return h / (-math.expm1(-x / 2)) - h / (-math.expm1(-x))


def exact_formula(h, a):
    x = h * a
    return h * math.exp(-x / 2) / (-math.expm1(-x))


def interval_trace(h, n=250000, lam=1.0):
    return math.fsum(h * phi(h * (lam + (math.pi * j) ** 2)) for j in range(1, n + 1))


def main():
    count = 0
    for k in range(1, 201):
        u = 0.001 * (60 / 0.001) ** (k / 200)
        h = 0.1
        a = u / h
        assert abs(two_grid(h, a) - exact_formula(h, a)) < 1e-10
        assert 0 < phi(u) < 1 / u
        count += 2
    for u in (0.01, 0.015, 0.02, 0.03):
        assert abs(phi(u) / (u / 24) - 1) < 0.002
        count += 1
    # Dirichlet spectrum (pi*j)^2, Weyl coefficient 1/pi and exponent 1/2.
    # The exact limit constant is (sqrt(2)-1)*abs(zeta(1/2))/(2*sqrt(pi)).
    zeta_half = -1.4603545088095868
    constant = (math.sqrt(2) - 1) * abs(zeta_half) / (2 * math.sqrt(math.pi))
    for h, tol in ((0.002, 0.035), (0.001, 0.025), (0.0005, 0.018)):
        val = interval_trace(h) / math.sqrt(h)
        assert abs(val / constant - 1) < tol, (h, val, constant)
        count += 1
        print('scaled_trace', h, 'observed', f'{val:.12f}', 'limit', f'{constant:.12f}')
    print('VERIFY_OK', count)


if __name__ == '__main__':
    main()

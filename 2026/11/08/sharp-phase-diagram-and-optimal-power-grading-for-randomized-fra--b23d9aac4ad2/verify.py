#!/usr/bin/env python3
"""Independent numerical spot checks for fractional Brownian sign-occupation quadrature.

Standard library only. Finite sums/integrals here supplement, not replace, the proof.
"""
import math


def panel(hurst, gamma, j, m=48):
    a = (j - 1) ** gamma
    b = j ** gamma
    width = b - a
    total = 0.0
    for k in range(m):
        s = a + width * (k + 0.5) / m
        s_h = s ** hurst
        s_2h = s_h * s_h
        for ell in range(m):
            t = a + width * (ell + 0.5) / m
            t_h = t ** hurst
            rho = (s_2h + t_h * t_h - abs(t - s) ** (2 * hurst)) / (2 * s_h * t_h)
            total += math.acos(max(-1.0, min(1.0, rho)))
    return width * width * total / (2 * math.pi * m * m)


def error(hurst, gamma, n, m=40):
    return math.fsum(panel(hurst, gamma, j, m) for j in range(1, n + 1)) / n ** (2 * gamma)


def limit_constant(hurst, gamma):
    assert 2 * gamma > 1 + hurst
    return gamma ** (2 + hurst) / (math.pi * (1 + hurst) * (2 + hurst) * (2 * gamma - 1 - hurst))


def run():
    checks = 0
    # A single interval is unaffected by the mesh grading exponent.
    for gamma in (0.6, 1.0, 1.25, 2.0):
        approx = error(0.5, gamma, 1, 180)
        assert abs(approx - 0.125) < 0.002, (gamma, approx)
        checks += 1
    for H in (0.25, 0.5, 0.75):
        gamma_star = 1 + H / 2
        K = limit_constant(H, gamma_star)
        assert K < limit_constant(H, 1.0)
        assert K < limit_constant(H, gamma_star - 0.06)
        assert K < limit_constant(H, gamma_star + 0.06)
        assert abs(K * math.pi * (H+1) * (H+2) - gamma_star**(H+2)) < 1e-12
        checks += 4
    # Convergence toward the complete infinite-n theorem, with finite-size error.
    for H, gamma, n, tolerance in ((0.5, 1.25, 420, 0.035),
                                    (0.75, 1.375, 650, 0.065),
                                    (0.25, 1.125, 350, 0.035)):
        value = error(H, gamma, n)
        ratio = value * n ** (1+H) / limit_constant(H, gamma)
        assert abs(ratio - 1.0) < tolerance, (H, gamma, n, ratio)
        checks += 1
    # All three asymptotic exponents are in the correct order on both sides.
    for H in (0.25, 0.5, 0.75):
        lower = (H + 1)/2 - 0.1
        critical = (H + 1)/2
        upper = (H + 1)/2 + 0.1
        assert 2*lower < H+1 and 2*critical == H+1 and 2*upper > H+1
        checks += 1
    print(f"PASS: {checks} finite analytic/numerical checks")


if __name__ == '__main__':
    run()

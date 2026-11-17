"""Reproducible finite checks for a circular-wave delay characteristic equation.

This checks local algebra and selected characteristic roots; it does not replace
an infinite-dimensional root-count proof.
"""
import cmath
import math


def char(lam, beta, k):
    h = 1 - cmath.exp(-lam)
    return lam * lam + beta * beta * h * h + beta * k * h


def char_prime(lam, beta, k):
    e = cmath.exp(-lam)
    h = 1 - e
    return 2 * lam + 2 * beta * beta * h * e + beta * k * e


def newton(initial, beta, k):
    lam = complex(initial)
    for _ in range(80):
        delta = char(lam, beta, k) / char_prime(lam, beta, k)
        lam -= delta
        if abs(delta) < 1e-12:
            break
    assert abs(char(lam, beta, k)) < 1e-9
    return lam


checks = [0, 0, 0]
for beta in [math.pi / 6, math.pi / 4, math.pi / 3, 1.4]:
    assert 0 < beta < math.pi / 2
    for j in range(3):
        omega = (2 * j + 1) * math.pi
        alpha_crit = omega * omega / (4 * beta)
        k_crit = 2 * (alpha_crit - beta)
        lam_crit = 1j * omega
        assert abs(char(lam_crit, beta, k_crit)) < 1e-10
        assert abs(char(-lam_crit, beta, k_crit)) < 1e-10
        assert abs(char(0, beta, k_crit)) < 1e-14
        assert abs(char_prime(0, beta, k_crit) - beta * k_crit) < 1e-12
        checks[0] += 1
        A = (omega * omega + 4 * beta * beta) / 2
        derivative = -4 * beta / char_prime(lam_crit, beta, k_crit)
        assert derivative.real > 0
        assert abs(derivative.real - 4 * beta * A / (A * A + 4 * omega * omega)) < 1e-12
        checks[1] += 1
        for sign in [-1, 1]:
            alpha = alpha_crit + sign * 0.03
            k = 2 * (alpha - beta)
            lam = newton(lam_crit, beta, k)
            assert lam.real * sign > 0, (beta, j, alpha, lam)
            checks[2] += 1

print('VERIFY_OK axis_substitutions=%d crossing_derivatives=%d root_continuations=%d' % tuple(checks))

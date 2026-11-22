"""Finite numerical checks for the real-plane cosine–memristor inverse formula.

The mathematical proof, not these finite samples, establishes the asymptotics.
Run: python3 checks/verify_inverse.py
"""
import math
import random


def original(x, y, alpha, beta):
    return (alpha * math.cos(x) + beta * (y * y - 1) * x, y + x)


def scalar(x, u, v, alpha, beta):
    return alpha * math.cos(x) + beta * (x * (x - v) ** 2 - x) - u


def jac(x, y, alpha, beta):
    return -alpha * math.sin(x) + beta * (y * y - 1 - 2 * x * y)


def scalar_deriv(x, v, alpha, beta):
    return -alpha * math.sin(x) + beta * (3 * x * x - 4 * v * x + v * v - 1)


def cbrt(x):
    return math.copysign(abs(x) ** (1 / 3), x)


def bracketed_roots(alpha, beta, u, v, step=0.025):
    """Sampled sign changes, used only as finite numerical spot checks."""
    R = (alpha / beta) ** (1 / 3)
    q = u / alpha
    left = cbrt(q - 1) * R - 20
    right = cbrt(q + 1) * R + 20
    n = math.ceil((right - left) / step)
    dx = (right - left) / n
    roots = []
    prev_x = left
    prev_f = scalar(prev_x, u, v, alpha, beta)
    for i in range(1, n + 1):
        curr_x = left + i * dx
        curr_f = scalar(curr_x, u, v, alpha, beta)
        if prev_f * curr_f < 0:
            lo, hi = prev_x, curr_x
            flo = prev_f
            for _ in range(55):
                mid = (lo + hi) / 2
                fm = scalar(mid, u, v, alpha, beta)
                if fm == 0:
                    lo = hi = mid
                    break
                if flo * fm > 0:
                    lo, flo = mid, fm
                else:
                    hi = mid
            roots.append((lo + hi) / 2)
        prev_x, prev_f = curr_x, curr_f
    return roots


def main():
    rng = random.Random(20231109)
    for _ in range(500):
        alpha = rng.uniform(0.03, 4)
        beta = rng.uniform(0.1, 3)
        x = rng.uniform(-5, 5)
        y = rng.uniform(-5, 5)
        u, v = original(x, y, alpha, beta)
        assert abs(scalar(x, u, v, alpha, beta)) < 1e-10
        assert abs(jac(x, y, alpha, beta) - scalar_deriv(x, v, alpha, beta)) < 1e-10
    for q in (-3.0, -1.5, -0.8, 0.0, 0.8, 1.5, 3.0):
        for R in (20.0, 50.0, 100.0):
            alpha = 1.0
            beta = alpha / R ** 3
            u, v = alpha * q, 1.25
            roots = bracketed_roots(alpha, beta, u, v)
            predicted = R * (cbrt(q + 1) - cbrt(q - 1)) / math.pi
            assert abs(len(roots) - predicted) < 5.0
            assert sum(1 if scalar_deriv(x, v, alpha, beta) > 0 else -1 for x in roots) == 1
            for x in roots:
                assert abs(scalar(x, u, v, alpha, beta)) < 1e-7
                assert abs(scalar_deriv(x, v, alpha, beta)) > 1e-7
    print('PASS: 500 inverse/Jacobian identity cases; 21 finite count spot checks')


if __name__ == '__main__':
    main()

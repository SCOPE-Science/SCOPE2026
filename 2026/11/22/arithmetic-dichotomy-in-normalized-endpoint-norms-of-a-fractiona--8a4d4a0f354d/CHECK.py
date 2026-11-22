#!/usr/bin/env python3
"""Supplementary, finite numerical checks for a fractional-shift norm asymptotic.

Requires numpy.  This is not a proof of an infinite-time assertion.
Run: python CHECK.py
"""
import math
import cmath
from fractions import Fraction
import numpy as np

TESTED = 0

def check(condition, msg):
    global TESTED
    TESTED += 1
    if not condition:
        raise AssertionError(msg)

def geometry(a):
    phi = math.pi / (a + 1)
    theta = math.pi * (a - 1) / (a + 1)
    d = 2 * math.cos(phi)
    c = d ** a * math.cos(phi)
    b = d ** a * math.sin(phi)
    v = a * d ** (a - 1)
    K = v / 2 * complex(a + 1, -(a - 1) * math.tan(phi))
    return phi, theta, c, b, v, K

def theoretical(a, t, q=None, num=24001):
    _, theta, c, b, v, K = geometry(a)
    u, w = (1 / K).real, (1 / K).imag
    if q is None:
        return 4 / math.pi * math.sqrt(abs(K) / K.real)
    y = np.linspace(-12, 12, num)
    g = np.exp(-u * y * y / 2)
    ans = 0.0
    for j in range(q):
        phase = t * b - j * theta - cmath.phase(K) / 2 - w * y * y / 2
        ans += float(np.trapezoid(g * np.abs(np.cos(phase)), y))
    return 2 * ans / (q * math.sqrt(2 * math.pi * abs(K)))

def normalized_wiener_norm(a, t, N=65536):
    _, _, c, _, _, _ = geometry(a)
    z = np.exp(2j * np.pi * np.arange(N) / N)
    f = np.exp(-t * (1 - z) ** a - t * c)
    coefficients = np.fft.fft(f) / N
    check(float(np.max(np.abs(coefficients.imag))) < 5e-13, 'real coefficients')
    # This finite FFT is diagnostic only; no rigorous truncation or alias bound is claimed.
    return float(np.abs(coefficients[:N // 2].real).sum())

def run():
    global TESTED
    examples = [(1.5, 5), (1.8, 7), (1.5 + math.sqrt(2) / 30, None)]
    for a, q in examples:
        phi, theta, c, b, v, K = geometry(a)
        check(1 < a < 2 and c > 0 and b > 0 and v > 0 and K.real > 0, 'valid geometry')
        check(abs(theta - (math.pi - 2 * phi)) < 1e-12, 'peak angle')
        z = cmath.exp(1j * theta)
        ps = -(1 - z) ** a
        ps1 = 1j * a * z * (1 - z) ** (a - 1)
        ps2 = -a * z * (1 - z) ** (a - 1) + a * (a - 1) * z * z * (1 - z) ** (a - 2)
        check(abs(ps - (c + 1j * b)) < 1e-11, 'peak value')
        check(abs(ps1 - 1j * v) < 1e-11, 'peak speed')
        check(abs(ps2 + K) < 1e-11, 'peak curvature')
        angles = np.linspace(-math.pi, math.pi, 12001)
        vals = np.real(-((1 - np.exp(1j * angles)) ** a))
        check(float(np.max(vals)) < c + 1e-9, 'boundary maximum')
        if q is not None:
            frac = Fraction((a - 1) / (a + 1)).limit_denominator(100)
            check(frac.denominator == q and abs(float(frac) - theta / math.pi) < 1e-12, 'denominator')
            period = math.pi / (q * b)
            for t in (55.0, 90.0, 160.0):
                check(abs(theoretical(a, t, q) - theoretical(a, t + period, q)) < 3e-5,
                      'rational periodicity')
            check(abs(theoretical(a, 55.0, q) - theoretical(a, 55 + period / 2, q)) > 1e-8,
                  'nonconstant periodic profile')
        for t, tolerance in [(200.0, 0.010), (400.0, 0.007), (800.0, 0.005)]:
            got = normalized_wiener_norm(a, t)
            expected = theoretical(a, t, q)
            check(abs(got - expected) < tolerance,
                  f'alpha={a}, t={t}, numeric={got}, predicted={expected}')
        print('order', a, 'q', q, 'c', c,
              'large-time test', normalized_wiener_norm(a, 800),
              'prediction', theoretical(a, 800, q))
    print('FRACTIONAL_WIENER_ARITHMETIC_DIAGNOSTIC_OK', TESTED)

if __name__ == '__main__':
    run()

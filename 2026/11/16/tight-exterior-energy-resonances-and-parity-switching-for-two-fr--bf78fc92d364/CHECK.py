#!/usr/bin/env python3
"""Independent finite checks of two-tone symmetric exterior energy transfer.

Requires only the Python 3 standard library. Tests are not an infinite proof.
"""
import cmath
import math
import random


def modes(d, h):
    s = math.sin(d) / d
    q = (math.sin((1.0 + h) * d) - math.sin(d)) / d
    return (h + q) / (1.0 + s), (h - q) / (1.0 - s)


def simpson(f, a, b, steps=2000):
    step = (b - a) / steps
    acc = f(a) + f(b)
    for j in range(1, steps):
        acc += (4 if j % 2 else 2) * f(a + j * step)
    return acc * step / 3.0


def quotient(d, h, A, B):
    def density(t):
        z = A * math.cos(d * t / 2) + B * math.sin(d * t / 2)
        return z.real * z.real + z.imag * z.imag
    interior = simpson(density, -1.0, 1.0)
    exterior = simpson(density, -1.0 - h, -1.0) + simpson(density, 1.0, 1.0 + h)
    return exterior / interior


def f_resonance(d, h):
    return math.sin((1.0 + h) * d) - (1.0 + h) * math.sin(d)


def bracket_root(h, n):
    a = (n + 0.5) * math.pi
    b = (n + 1.5) * math.pi
    fa = f_resonance(a, h)
    fb = f_resonance(b, h)
    assert fa * fb < 0.0
    for _ in range(90):
        m = (a + b) / 2.0
        fm = f_resonance(m, h)
        if abs(fm) < 5e-14:
            return m
        if fm * fa < 0.0:
            b, fb = m, fm
        else:
            a, fa = m, fm
    return (a + b) / 2.0


def main():
    rng = random.Random(20260618)
    count = 0
    for h in (0.1, 0.5, 1.0, 2.0, 3.7):
        for d in (0.15, 0.6, 1.5, 3.2, 11.1):
            even, odd = modes(d, h)
            assert abs(quotient(d, h, 1.0, 0.0) - even) < 5e-9
            assert abs(quotient(d, h, 0.0, 1.0) - odd) < 5e-9
            count += 2
            for _ in range(4):
                A = complex(rng.uniform(-1, 1), rng.uniform(-1, 1))
                B = complex(rng.uniform(-1, 1), rng.uniform(-1, 1))
                value = quotient(d, h, A, B)
                assert min(even, odd) - 5e-9 <= value <= max(even, odd) + 5e-9
                count += 1
        for n in range(6):
            d = bracket_root(h, n)
            even, odd = modes(d, h)
            assert abs(even - h) < 1e-11
            assert abs(odd - h) < 1e-11
            assert abs(quotient(d, h, complex(1, 0.7), complex(-0.2, 0.5)) - h) < 2e-8
            count += 3
        for d in (0.02, 0.04, 0.06):
            even, odd = modes(d, h)
            leading = h * (h * h + 3 * h + 3)
            correction = h * (h + 1)**3 * (h + 2) / 20
            assert odd > even
            assert abs((leading - odd) / (d * d) - correction) < 0.03 * correction
            count += 2
    print(f"CHECK_OK symmetric_transfer_tests={count} (finite corroboration only)")


if __name__ == '__main__':
    main()

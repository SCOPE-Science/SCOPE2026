#!/usr/bin/env python3
"""Finite numerical sanity checks for the sharp rectangle circular Fourier energy.

This quadrature is not a proof of the all-radius asymptotic or the liminf.
"""
import math


def sinc(x):
    if abs(x) < 1e-12:
        return 1.0
    return math.sin(x) / x


def energy(a, b, radius):
    n = max(32000, int(130 * radius * max(a, b)))
    if n % 2:
        n += 1
    h = (math.pi / 2) / n
    s = 0.0
    for i in range(n + 1):
        th = i * h
        # Exact Fourier transform, continuous also on the coordinate axes.
        f = 4 * a * b * sinc(a * radius * math.cos(th)) * sinc(b * radius * math.sin(th))
        w = 1 if i == 0 or i == n else 4 if i % 2 else 2
        s += w * f * f
    return 4 * s * h / 3


def lower_constant(a, b):
    return 8 * math.sqrt(2 * math.pi) * (math.sqrt(a) + math.sqrt(b))


def two_terms(a, b, radius):
    first = 32 * math.pi / radius**3 * (b * math.sin(a * radius)**2 + a * math.sin(b * radius)**2)
    second = 8 * math.sqrt(2 * math.pi) / radius**3.5 * (
        math.sqrt(a) * (math.cos(2*a*radius)-math.sin(2*a*radius))
        + math.sqrt(b) * (math.cos(2*b*radius)-math.sin(2*b*radius)))
    return first, second


def main():
    nchecks = 0
    for a, b in [(1.0, 1.0), (1.0, 2.0), (2.0, 3.0)]:
        c = lower_constant(a, b)
        for m in [100, 240]:
            r = m * math.pi / a
            scaled = energy(a, b, r) * r**3.5
            assert abs(scaled - c) < 0.025 * c, (a,b,m,scaled,c)
            nchecks += 1
    for r in [320.25, 510.75]:
        a, b = 1.2, 0.7
        first, second = two_terms(a,b,r)
        assert abs((energy(a,b,r)-first-second)*r**3.5) < 2.0, r
        nchecks += 1
    print(f'CHECK_OK resonant=6 generic=2 checks={nchecks}')


if __name__ == '__main__':
    main()

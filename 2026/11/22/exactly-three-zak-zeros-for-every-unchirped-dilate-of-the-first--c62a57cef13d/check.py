#!/usr/bin/env python3
"""Diagnostic Gaussian Zak checks; finite samples do not prove the universal theorem."""
import cmath
import math


def zak(beta, x, omega):
    radius = max(8, int(math.ceil(9 / math.sqrt(beta))) + 3)
    return sum((x+k) * math.exp(-beta * (x+k)**2)
               * cmath.exp(-2j * math.pi * k * omega)
               for k in range(-radius, radius+1))


def main():
    checks = 0
    for beta in [0.10, 0.3, 0.7, 1.6, 2.0, 2.7, 5.0, 13.0, 50.0]:
        for x, w in [(0.123, 0.21), (0.37, 0.49), (0.41, 0.74)]:
            b2 = math.pi**2 / beta
            left = zak(beta, x, w)
            right = -1j * (math.pi / beta)**1.5 * cmath.exp(2j * math.pi*x*w) * zak(b2, w, -x)
            assert abs(left-right) < 2e-9 * max(1, abs(left), abs(right)), (beta, x, w)
            checks += 1
        for x, w in [(0, 0), (0, 0.5), (0.5, 0)]:
            assert abs(zak(beta, x, w)) < 1e-10, (beta, x, w)
            checks += 1
        if beta >= 2:
            for x in [0.03, 0.13, 0.32, 0.47, 0.5]:
                for w in [0.06, 0.16, 0.31, 0.73]:
                    assert zak(beta, x, w).real > 0, (beta, x, w)
                    checks += 1
            for w in [0.06, 0.16, 0.31, 0.47]:
                assert zak(beta, 0, w).imag < 0, (beta, w)
                checks += 1
    ratio = sum((n+1)**2 / 400**n for n in range(1, 25))
    assert ratio < 0.011
    checks += 1
    print('PASS:', checks, 'diagnostic checks. Universal claim rests on analytic proof.')


if __name__ == '__main__':
    main()

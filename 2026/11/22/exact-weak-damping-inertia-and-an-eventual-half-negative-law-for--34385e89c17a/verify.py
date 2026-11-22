#!/usr/bin/env python3
"""Finite checks of powered intrinsic-circle Gram signatures (standard library only).

The assertions check selected finite cases; the general theorem is analytic.
"""
import math


def eigenvalues(n, exponent, damping):
    values = [math.exp(-damping * (2 * math.pi * min(j, n-j) / n) ** exponent)
              for j in range(n)]
    return [sum(values[j] * math.cos(2*math.pi*j*k/n) for j in range(n))
            for k in range(n)]


def counts(vals, tolerance=1e-9):
    assert all(abs(v) > tolerance for v in vals), "ambiguous finite precision sign"
    return sum(v > 0 for v in vals), sum(v < 0 for v in vals)


def fourier_coefficient(m, exponent, damping, steps=16000):
    # Independent composite Simpson quadrature; the finite comparisons are only tests.
    h = math.pi / steps
    s = 0.0
    for j in range(steps + 1):
        x = j*h
        weight = 1 if j in (0, steps) else (4 if j & 1 else 2)
        s += weight * math.exp(-damping * x**exponent) * math.cos(m*x)
    return s*h/(3*math.pi)


def main():
    cases = 0
    for exponent in (1.2, 1.5, 2.0, 3.0, 4.0):
        bound = (exponent-1)/(exponent*math.pi**exponent)
        for fraction in (0.2, 0.7, 1.0):
            damping = fraction * bound
            for n in range(2, 66, 2):
                p, m = counts(eigenvalues(n, exponent, damping))
                assert (p, m) == (n//2 + 1, n//2 - 1), (exponent, damping, n, p, m)
                cases += 1
    # Outside the sufficient concavity region, check the finite correction on test cases.
    for damping, corrections in ((0.3, -1), (0.5, -1), (1.0, -3)):
        b = {m: fourier_coefficient(m, 2.0, damping) for m in range(1, 13)}
        j = sum(1 for m, v in b.items() if m & 1 and v < -1e-10) - sum(
            1 for m, v in b.items() if not m & 1 and v > 1e-10)
        assert j == corrections, (damping, j)
        for n in (40, 60, 80, 100):
            p, m = counts(eigenvalues(n, 2.0, damping))
            assert m == n//2 - 1 + 2*j, (damping, n, m, j)
            assert p+m == n
            cases += 1
    print(f"PASS: {cases} finite Fourier-sign and inertia cases")


if __name__ == '__main__':
    main()

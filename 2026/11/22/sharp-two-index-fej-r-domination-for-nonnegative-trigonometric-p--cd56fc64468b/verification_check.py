#!/usr/bin/env python3
"""Exact finite checks for the two-index Fejer convolution domination formula.

The theorem for arbitrary indices is proved analytically in RESULT.md;
these checks guard the matrix construction and sharp equality identity.
Only the Python standard library is required.
"""
from fractions import Fraction
from random import Random


def coordinates(m, n):
    assert m >= 1 and n >= 0
    q, r = divmod(n, m)
    den = (q + 2) * m - r
    x = [Fraction(0) for _ in range(n + 1)]
    for j in range(q + 1):
        x[j * m] += Fraction(m * (q + 1 - j), den)
        x[j * m + r] += Fraction(m * (j + 1), den)
    c = Fraction((q + 1) * (q + 2) * m, den)
    return x, c


def coeff(m, h):
    return Fraction(max(m - abs(h), 0), m)


def quadratic(m, x):
    return sum((x[i] * x[j] * coeff(m, i - j)
                for i in range(len(x)) for j in range(len(x))), Fraction(0))


def run():
    count = 0
    for m in range(1, 23):
        for n in range(0, 4 * m + 5):
            x, c = coordinates(m, n)
            assert all(t >= 0 for t in x)
            assert sum(x) == c
            assert x == x[::-1]
            for i in range(n + 1):
                assert sum((coeff(m, i - j) * x[j] for j in range(n + 1)), Fraction(0)) == 1
                count += 1
            assert quadratic(m, x) == c
            count += 1
    rng = Random(20261117)
    for m in range(1, 18):
        for n in range(0, 2 * m + 5):
            _, c = coordinates(m, n)
            for _ in range(15):
                x = [Fraction(rng.randrange(-9, 10)) for _ in range(n + 1)]
                assert sum(x) ** 2 <= c * quadratic(m, x)
                count += 1
    # Complex vector version reduces to separate rational real and imaginary parts.
    for m in range(1, 12):
        for n in range(0, m + 9):
            _, c = coordinates(m, n)
            for _ in range(10):
                a = [Fraction(rng.randrange(-5, 6)) for _ in range(n + 1)]
                b = [Fraction(rng.randrange(-5, 6)) for _ in range(n + 1)]
                assert sum(a) ** 2 + sum(b) ** 2 <= c * (quadratic(m, a) + quadratic(m, b))
                count += 1
    print(f"PASS {count} exact rational identities and inequalities")


if __name__ == '__main__':
    run()

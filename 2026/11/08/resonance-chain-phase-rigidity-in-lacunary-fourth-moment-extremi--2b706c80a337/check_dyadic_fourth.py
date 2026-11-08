#!/usr/bin/env python3
"""Exact Gaussian-integer checks of lacunary fourth-moment resonances."""
from collections import defaultdict
from fractions import Fraction
from random import Random


def add(x, y):
    return (x[0] + y[0], x[1] + y[1])


def mul(x, y):
    return (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def conj(x):
    return (x[0], -x[1])


def norm2(x):
    return x[0] * x[0] + x[1] * x[1]


def spectral_power(coeffs, base):
    frequencies = [0] + [base**j for j in range(len(coeffs) - 1)]
    convolution = defaultdict(lambda: (0, 0))
    for i, x in enumerate(frequencies):
        for j, y in enumerate(frequencies):
            convolution[x + y] = add(convolution[x + y], mul(coeffs[i], coeffs[j]))
    return sum(norm2(v) for v in convolution.values())


def baseline(coeffs):
    s = sum(norm2(v) for v in coeffs)
    return 2 * s * s - sum(norm2(v)**2 for v in coeffs)


def dyadic_formula(coeffs):
    correction = 4 * sum(mul(mul(coeffs[0], coeffs[j + 1]),
                             mul(conj(coeffs[j]), conj(coeffs[j])))[0]
                         for j in range(1, len(coeffs) - 1))
    return baseline(coeffs) + correction


def collisions(base, m):
    frequencies = [0] + [base**j for j in range(m)]
    pairs = defaultdict(list)
    for i in range(len(frequencies)):
        for j in range(i, len(frequencies)):
            pairs[frequencies[i] + frequencies[j]].append((i, j))
    return {s: tuple(p) for s, p in pairs.items() if len(p) > 1}


def main():
    rng = Random(10817)
    tests = 0
    for m in range(1, 11):
        dyadic_collisions = collisions(2, m)
        assert len(dyadic_collisions) == m - 1
        for j in range(2, m + 1):
            assert set(dyadic_collisions[2**(j - 1)]) == {(0, j), (j - 1, j - 1)}
            tests += 1
        for base in range(3, 8):
            assert not collisions(base, m)
            tests += 1
        for _ in range(30):
            coeffs = [(rng.randrange(-4, 5), rng.randrange(-4, 5))
                      for _ in range(m + 1)]
            assert spectral_power(coeffs, 2) == dyadic_formula(coeffs)
            tests += 1
            for base in (3, 4, 7):
                assert spectral_power(coeffs, base) == baseline(coeffs)
                tests += 1
    s = Fraction(4, 7)
    maximum = 1 + 4*s - Fraction(7, 2)*s*s
    assert maximum == Fraction(15, 7)
    assert 1 + 4*Fraction(3, 7) - Fraction(7, 2)*Fraction(3, 7)**2 < maximum
    tests += 2
    print('EXACT_MOMENT_CHECKS_PASS', tests)


if __name__ == '__main__':
    main()

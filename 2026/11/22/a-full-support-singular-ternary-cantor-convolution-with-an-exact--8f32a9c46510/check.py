#!/usr/bin/env python3
"""Exact finite checks for the ternary Cantor sum convolution theorem.

This is a reproducibility aid, not a replacement for the all-depth proofs.
Requires Python 3 standard library only.
"""
from collections import Counter
from math import comb, sqrt, log

M = (
    ((1, 1), (0, 1)),
    ((1, 0), (1, 1)),
    ((1, 0), (1, 0)),
)


def matrix_fiber(target, depth):
    a, b = 1, 0
    for _ in range(depth):
        digit = target % 3
        target //= 3
        m = M[digit]
        a, b = a * m[0][0] + b * m[1][0], a * m[0][1] + b * m[1][1]
    return a + b


def count_twos(target, depth):
    count = 0
    for _ in range(depth):
        count += target % 3 == 2
        target //= 3
    return count


def check():
    values = [0]
    old_e, e = 1, 6
    assertions = 0
    for k in range(1, 9):
        values = [v + digit * 3 ** (k - 1) for v in values for digit in (0, 1)]
        modulus = 3 ** k
        direct = Counter((x + 2 * y) % modulus for x in values for y in values)
        assert len(direct) == modulus
        for t in range(modulus):
            assert direct[t] == matrix_fiber(t, k) > 0
            assertions += 1
        energy = sum(n * n for n in direct.values())
        if k == 1:
            assert energy == 6
        else:
            old_e, e = e, 6 * e - 2 * old_e
            assert energy == e
        assertions += 1
        spectrum = Counter()
        for t, multiplicity in direct.items():
            spectrum[count_twos(t, k)] += multiplicity
        for j in range(k + 1):
            assert spectrum[j] == comb(k, j) * 3 ** (k - j)
            assertions += 1
        assert sum(direct.values()) == 4 ** k
        assertions += 1

    # Independent recurrence implementation through accumulated quadratic moments.
    E, H = 1, 0
    for k in range(0, 35):
        if k <= 8:
            closed = ((3 + sqrt(7)) ** (k + 1) -
                      (3 - sqrt(7)) ** (k + 1)) / (2 * sqrt(7))
            assert abs(E - closed) < 0.01  # floating-point approximation only
        E, H = 6 * E - 2 * H, E
        assertions += 1
    assert abs(log(16 / (3 + sqrt(7)), 3) - 0.9481829495698588) < 1e-13
    print(f'CHECK_OK {assertions} finite exact assertions plus floating-point sanity check')


if __name__ == '__main__':
    check()

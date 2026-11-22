#!/usr/bin/env python3
"""Independent integer checks for minimal-domination Fourier multipliers.

Requires Python 3, standard library only. Run: python3 verification_mindom.py
"""
from math import comb


def minimal_sets(a, b):
    n = a + b
    whole = (1 << n) - 1
    left = (1 << a) - 1
    right = whole ^ left
    neighborhoods = ([right] * a) + ([left] * b)

    def dominating(mask):
        covered = mask
        for vertex, neighbors in enumerate(neighborhoods):
            if mask & (1 << vertex):
                covered |= neighbors
        return covered == whole

    return {mask for mask in range(1 << n)
            if dominating(mask) and all(
                not dominating(mask ^ (1 << vertex))
                for vertex in range(n) if mask & (1 << vertex))}


def walsh_in_place(values):
    n = len(values)
    stride = 1
    while stride < n:
        for base in range(0, n, 2 * stride):
            for j in range(stride):
                u = values[base + j]
                v = values[base + j + stride]
                values[base + j] = u + v
                values[base + j + stride] = u - v
        stride *= 2


def predicted_nullity(a, b):
    if a % 2 and b % 2:
        return 0
    if a % 2 == 0 and b % 2 == 0:
        ca, cb = comb(a, a // 2), comb(b, b // 2)
        return (ca * 2 ** (b - 1) + cb * 2 ** (a - 1)
                - (ca * cb if (a // 2 - b // 2) % 2 else 0))
    if a % 2:
        a, b = b, a
    return (comb(a, a // 2) * 2 ** (b - 1)
            + comb(a, a // 2 - 1) * comb(b, (b - 1) // 2))


def check():
    assertions = 0
    shapes = 0
    for a in range(2, 8):
        for b in range(2, 8):
            if a + b > 12:
                continue
            shapes += 1
            n = a + b
            actual = minimal_sets(a, b)
            expected_support = {((1 << a) - 1), ((1 << n) - (1 << a))}
            expected_support |= {(1 << i) | (1 << j)
                                 for i in range(a) for j in range(a, n)}
            assert actual == expected_support
            assertions += 1
            values = [int(mask in actual) for mask in range(1 << n)]
            walsh_in_place(values)
            for alpha, value in enumerate(values):
                ia = (alpha & ((1 << a) - 1)).bit_count()
                ib = (alpha >> a).bit_count()
                expected = ((a - 2 * ia) * (b - 2 * ib)
                            + (-1) ** ia + (-1) ** ib)
                assert value == expected, (a, b, alpha, value, expected)
                assertions += 1
            zeros = sum(v == 0 for v in values)
            assert zeros == predicted_nullity(a, b), (a, b, zeros)
            assertions += 1
            expected_gap = 1 if (a % 2 and b % 2) else 2
            assert min(abs(v) for v in values if v) == expected_gap
            assert max(abs(v) for v in values) == a * b + 2
            assertions += 2
            assert (zeros == 0) == (a % 2 == 1 and b % 2 == 1)
            assertions += 1
    print(f'PASS: {shapes} graph shapes, {assertions} exact assertions')


if __name__ == '__main__':
    check()

"""Exact rational evaluation of the Hamming two-boson collision formula.

Usage: python formula_replay.py
Python standard library only. No external data files are required.
"""
from fractions import Fraction
from math import comb


def multiply(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, u in enumerate(a):
        for j, v in enumerate(b):
            out[i + j] += u * v
    return out


def poly_power(a, exponent):
    out = [1]
    for _ in range(exponent):
        out = multiply(out, a)
    return out


def capture(d, q, separation):
    assert d >= 1 and q >= 3 and 1 <= separation <= d
    total = Fraction(0)
    for b in range(d - separation + 1):
        for r in range(separation + 1):
            w = b + r
            denominator = multiply(poly_power([1, 0, q - 1], d - w),
                                   poly_power([0, 2, q - 2], w))
            numerator = multiply(
                multiply(poly_power([1, 0, q - 1], d - separation - b),
                         poly_power([0, 2, q - 2], b)),
                multiply(poly_power([1, 0, -1], separation - r),
                         poly_power([0, 1, -1], r)))
            inner = Fraction(0)
            for t, coefficient in enumerate(numerator):
                if coefficient:
                    assert denominator[t] > 0
                    inner += Fraction(coefficient ** 2, denominator[t])
            total += (comb(d - separation, b) * comb(separation, r)
                      * (q - 1) ** b * (2 * (q - 2)) ** r * inner)
    return 2 * total / q ** (2 * d)


def dark_dimension(d, q):
    n = q ** d
    bright = q ** (d - 1) * ((d + 1) * q + d) - d
    return n * (n + 1) // 2 - bright


EXPECTED = {
    (1, 3): (0, [Fraction(1)]),
    (1, 4): (2, [Fraction(2, 3)]),
    (2, 3): (14, [Fraction(13, 18), Fraction(1, 2)]),
    (2, 4): (82, [Fraction(11, 24), Fraction(2, 9)]),
    (2, 5): (242, [Fraction(33, 100), Fraction(1, 8)]),
    (3, 3): (246, [Fraction(119, 243), Fraction(127, 486), Fraction(23, 108)]),
}


def main():
    for (d, q), (dimension, expected_probabilities) in EXPECTED.items():
        assert dark_dimension(d, q) == dimension, (d, q)
        probabilities = [capture(d, q, s) for s in range(1, d + 1)]
        assert probabilities == expected_probabilities, (d, q, probabilities)
        print(f'H({d},{q}): dark={dimension}; capture={probabilities}')
    for q in range(3, 16):
        assert capture(2, q, 1) == Fraction(q * q + 2 * q - 2, q * q * (q - 1))
        assert capture(2, q, 2) == Fraction(2, (q - 1) ** 2)
    print('Exact rational finite checks passed.')


if __name__ == '__main__':
    main()

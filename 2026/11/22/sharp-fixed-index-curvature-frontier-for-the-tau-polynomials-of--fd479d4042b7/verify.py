#!/usr/bin/env python3
"""Exact finite checks of a fixed-index tau-coefficient curvature formula."""
from fractions import Fraction


def squared_growth(d, x):
    assert d >= 3 and x >= 2
    a = (d - 1) ** 2
    if x <= d - 1:
        return Fraction((d - 1) ** 2) * Fraction(a, a - x) ** (d - 2)
    return Fraction(x * x) * Fraction(x, x - 1) ** (d - 2)


def square_lambda(d, j):
    return squared_growth(d, j + 1) ** 2 / (squared_growth(d, j) * squared_growth(d, j + 2))


def main():
    count = 0
    for d in range(3, 101):
        for j in range(2, d + 25):
            square = square_lambda(d, j)
            if j <= d - 2:
                assert square < 1, (d, j, square)
            else:
                assert square > 1, (d, j, square)
            count += 1
    assert square_lambda(3, 2) == Fraction(2187, 2048)
    assert square_lambda(4, 2) == Fraction(3969, 4096)
    print('EXACT_FIXED_INDEX_CURVATURE_PASS cases=', count)
    print('BOUNDARY_SAMPLES_PASS')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()

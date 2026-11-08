#!/usr/bin/env python3
"""Exact checks for correlations of binary Pascal-row nondivisibility counts.

Only Python's standard library is required. This is a finite consistency check;
the unrestricted conclusions are established by the proof in RESULT.md.
"""
from fractions import Fraction

T0 = ((5, 0), (2, 2))
T1 = ((2, 2), (0, 5))
V = (Fraction(1), Fraction(2, 3))


def row_times(row, matrix):
    return (row[0] * matrix[0][0] + row[1] * matrix[1][0],
            row[0] * matrix[0][1] + row[1] * matrix[1][1])


def matrix_count(h, levels):
    assert 0 <= h < (1 << levels)
    row = (1, 0)
    for j in range(levels):
        row = row_times(row, (T0, T1)[(h >> j) & 1])
    return row[0] + row[1]


def limiting_correlation(h):
    if h == 0:
        return Fraction(1)
    row = (1, 0)
    levels = h.bit_length()
    for j in range(levels):
        row = row_times(row, (T0, T1)[(h >> j) & 1])
    return (row[0] * V[0] + row[1] * V[1]) / (5 ** levels)


def digits_weight(n):
    return 1 << n.bit_count()


def main():
    checked_pairs = 0
    for levels in range(1, 12):
        size = 1 << levels
        values = [digits_weight(n) for n in range(size)]
        assert sum(v*v for v in values) == 5**levels
        assert sum(values) == 3**levels
        for h in range(size):
            direct = sum(values[n] * values[(n+h) % size] for n in range(size))
            assert direct == matrix_count(h, levels), (levels, h, direct)
            checked_pairs += size
    for h in range(1, 4096):
        rho = limiting_correlation(h)
        assert Fraction(0) < rho <= Fraction(2,3)
        assert (rho == Fraction(2,3)) == (h & (h-1) == 0), h
        assert limiting_correlation(2*h) == rho
    prev2, prev1 = Fraction(1), Fraction(2,3)
    for m in range(1, 15):
        h = (4**m-1)//3
        actual = limiting_correlation(h)
        if m == 1:
            assert actual == prev1
        else:
            next_val = (Fraction(24,25)*prev1 - Fraction(4,25)*prev2)
            assert actual == next_val
            assert 0 < actual < prev1
            prev2, prev1 = prev1, next_val
    print('VERIFY_OK checked_cyclic_lag_pairs=%d max_levels=11 bound_shifts=4095 alternating_m=14' % checked_pairs)
    print('EXAMPLES', {h: str(limiting_correlation(h)) for h in (0,1,2,3,5,7,11,21,43)})


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""Exact finite identity checks for a 7-carry digit-parity correlation.

The proof of validity at arbitrary bit length is in RESULT.md; this program
checks the elementary certificate and separately compares small finite sums.
Requires only Python 3 standard library.
"""

from __future__ import annotations

SIZE = 7


def matrix() -> list[list[int]]:
    result = [[0 for _ in range(SIZE)] for _ in range(SIZE)]
    for carry in range(SIZE):
        for bit in (0, 1):
            intermediate = 7 * bit + carry
            output_bit = intermediate & 1
            next_carry = intermediate >> 1
            result[carry][next_carry] += (-1) ** (bit + output_bit)
    return result


def row_times(row: list[int], mat: list[list[int]]) -> list[int]:
    return [sum(row[i] * mat[i][j] for i in range(SIZE)) for j in range(SIZE)]


def mat_times_column(mat: list[list[int]], col: list[int]) -> list[int]:
    return [sum(mat[i][j] * col[j] for j in range(SIZE)) for i in range(SIZE)]


def sign(value: int) -> int:
    return -1 if value.bit_count() & 1 else 1


def direct(level: int) -> int:
    return sum(sign(n) * sign(7 * n) for n in range(1 << level))


def check() -> None:
    mat = matrix()
    expected = [
        [1, 0, 0, 1, 0, 0, 0],
        [-1, 0, 0, 0, -1, 0, 0],
        [0, 1, 0, 0, 1, 0, 0],
        [0, -1, 0, 0, 0, -1, 0],
        [0, 0, 1, 0, 0, 1, 0],
        [0, 0, -1, 0, 0, 0, -1],
        [0, 0, 0, 1, 0, 0, 1],
    ]
    assert mat == expected, 'carry matrix differs'
    tail = [sign(carry) for carry in range(SIZE)]
    assert tail == [1, -1, -1, 1, -1, 1, 1]
    # This exact 7-vector identity is sufficient for the recurrence,
    # because every accessible row has coordinates 2 and 4 equal.
    it = tail
    for _ in range(4):
        it = mat_times_column(mat, it)
    mv = mat_times_column(mat, tail)
    obstruction = [it[i] - mv[i] - 2 * tail[i] for i in range(SIZE)]
    assert obstruction == [0, 0, 4, 0, -4, 0, 0]

    row = [1, 0, 0, 0, 0, 0, 0]
    values = []
    for level in range(41):
        assert row[1] == row[5] and row[2] == row[4]
        values.append(sum(row[i] * tail[i] for i in range(SIZE)))
        row = row_times(row, mat)
    assert values[:4] == [1, 2, 2, 2]
    for level in range(37):
        assert values[level + 4] == values[level + 1] + 2 * values[level]
    for level in range(16):
        assert values[level] == direct(level)
    assert all(value > 0 for value in values)
    print('PASS: carry transitions, tail, exact matrix-vector identity')
    print('PASS: coordinate invariants, first 41 transfer values, recurrence')
    print('PASS: direct 7n binary-digit parity sums for levels 0..15')
    print('first 20 values:', values[:20])


if __name__ == '__main__':
    check()

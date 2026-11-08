#!/usr/bin/env python3
"""Exact checks for the Fourier matrix on binary permutation matrices.

Only Python's standard library is required. The representation-theoretic
proof is independent of these finite calculations.
"""
from functools import lru_cache
from itertools import permutations
from math import comb, factorial


def partitions(n, ceiling=None):
    """All integer partitions, without external tables."""
    if ceiling is None:
        ceiling = n
    if n == 0:
        yield ()
        return
    for top in range(min(ceiling, n), 0, -1):
        for tail in partitions(n - top, top):
            yield (top,) + tail


def removals(shape):
    for i in range(len(shape)):
        if i == len(shape) - 1 or shape[i] > shape[i + 1]:
            if shape[i] == 1:
                yield shape[:i] + shape[i + 1:]
            else:
                yield shape[:i] + (shape[i] - 1,) + shape[i + 1:]


@lru_cache(None)
def dimension(shape):
    if not shape:
        return 1
    return sum(dimension(t) for t in removals(shape))


@lru_cache(None)
def branch_multiplicity(shape, m):
    """Multiplicity of shape in the permutation action on ordered n-m tuples."""
    if len(shape) and sum(shape) < m:
        return 0
    if sum(shape) == m:
        return int(shape == ((m,) if m else ()))
    return sum(branch_multiplicity(t, m) for t in removals(shape))


def multiplier_coefficients(shape):
    """Exact integer coefficients of sum_g z^fix(g) chi_shape(g)/dim."""
    n = sum(shape)
    d = dimension(shape)
    coefficients = [0] * (n + 1)
    for k in range(n + 1):
        c = (factorial(n) // factorial(k)) * branch_multiplicity(shape, n - k)
        for j in range(k + 1):
            coefficients[j] += c * comb(k, j) * (-1) ** (k - j)
    assert all(c % d == 0 for c in coefficients)
    return tuple(c // d for c in coefficients)


def multiply(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def claimed_coefficients(n):
    x = [1]
    for _ in range(n - 3):
        x = multiply(x, [-1, 1])
    x = multiply(x, [1, 1])
    return tuple(multiply(x, [n - 1, n - 4, 1]))


def at_minus_one(coefficients):
    return sum(c * (-1) ** j for j, c in enumerate(coefficients))


def exact_modular_rank(matrix, modulus=1000003):
    A = [[x % modulus for x in row] for row in matrix]
    h, w = len(A), len(A[0]); rank = 0
    for col in range(w):
        pivot = next((i for i in range(rank, h) if A[i][col]), None)
        if pivot is None:
            continue
        A[rank], A[pivot] = A[pivot], A[rank]
        div = pow(A[rank][col], -1, modulus)
        for j in range(col, w):
            A[rank][j] = A[rank][j] * div % modulus
        for i in range(rank + 1, h):
            if c := A[i][col]:
                for j in range(col, w):
                    A[i][j] = (A[i][j] - c * A[rank][j]) % modulus
        rank += 1
        if rank == h:
            break
    return rank


def direct_permutation_fourier_rank(n):
    perm = list(permutations(range(n)))
    H = [[(-1) ** sum(a[i] == b[i] for i in range(n))
          for b in perm] for a in perm]
    return exact_modular_rank(H)


def main():
    # Verify every coefficient of the alleged exact multiplier for 14 sizes.
    for n in range(7, 21):
        shape = (3, 2, 2) + (1,) * (n - 7)
        assert dimension(shape) == n * (n - 1) * (n - 3) * (n - 6) // 8
        assert multiplier_coefficients(shape) == claimed_coefficients(n), n
        assert at_minus_one(claimed_coefficients(n)) == 0

    # Exhaustive representation sector check, not just a finite sample of rows.
    for n in (4, 5, 7):
        sectors = [(shape, dimension(shape), at_minus_one(multiplier_coefficients(shape)))
                   for shape in partitions(n)]
        assert sum(d * d for _, d, _ in sectors) == factorial(n)
        nullity = sum(d * d for _, d, value in sectors if value == 0)
        assert nullity == {4: 18, 5: 25, 7: 441}[n], (n, nullity)
        if n == 7:
            assert [(shape, d) for shape, d, value in sectors if value == 0] == [((3, 2, 2), 21)]

    # Independent construction of the actual Fourier matrix, using the
    # coordinate inner product of the binary permutation matrices.
    for n, expected_rank in [(2, 1), (3, 6), (4, 6), (5, 95)]:
        actual = direct_permutation_fourier_rank(n)
        assert actual == expected_rank, (n, actual, expected_rank)

    print('PERMUTATION_BINARY_FOURIER_RESONANCE_PASS')
    print('POLYNOMIAL_IDS=14; COMPLETE_SECTOR_CENSUS_N=4,5,7; DIRECT_MATRIX_RANK_N=2,3,4,5')
    print('N=7: SIZE=5040 NULLITY=441 RANK=4599')


if __name__ == '__main__':
    main()

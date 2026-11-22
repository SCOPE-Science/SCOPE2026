#!/usr/bin/env python3
"""Exact finite verification of the 64-by-64 theta-translate incidence lattice."""
from collections import Counter
from math import gcd

DIM = 3
N = 1 << (2 * DIM)
MASK = (1 << DIM) - 1
EXPECTED = {0: 8, 1: 14, 2: 20, 3: 14, 4: 8}


def parity_quadratic(z):
    return ((z & MASK) & ((z >> DIM) & MASK)).bit_count() & 1


def matrix():
    return [[parity_quadratic(x ^ y) for y in range(N)] for x in range(N)]


def two_adic_valuations(A, precision=7):
    """Exact elementary divisor valuations modulo 2^precision.

    At each unit pivot, perform invertible row and column operations over
    Z/(2^r). If the remaining block is even, divide by 2, lowering r.
    This preserves the Smith valuations below the original precision.
    """
    B = [row[:] for row in A]
    modulus = 1 << precision
    level = 0
    result = []
    while B:
        m = len(B)
        pivot = next(((i, j) for i in range(m) for j in range(m)
                      if B[i][j] & 1), None)
        if pivot is None:
            assert modulus > 2, 'precision exhausted: unresolved valuations'
            B = [[x // 2 for x in row] for row in B]
            modulus //= 2
            level += 1
            continue
        i, j = pivot
        B[0], B[i] = B[i], B[0]
        for row in B:
            row[0], row[j] = row[j], row[0]
        assert gcd(B[0][0], modulus) == 1
        inv = pow(B[0][0], -1, modulus)
        B[0] = [(x * inv) % modulus for x in B[0]]
        for t in range(1, m):
            coeff = B[t][0]
            if coeff:
                B[t] = [(x - coeff * y) % modulus
                        for x, y in zip(B[t], B[0])]
        assert B[0][0] == 1 and all(B[t][0] == 0 for t in range(1, m))
        # Each first-row off-diagonal entry can be cleared by subtracting
        # its multiple of column zero. Because the lower column is already
        # zero this leaves the lower-right matrix unchanged.
        B = [row[1:] for row in B[1:]]
        result.append(level)
    return dict(sorted(Counter(result).items()))


def verify():
    M = matrix()
    assert len(M) == 64 and len(M[0]) == 64
    assert all(x in (0, 1) for row in M for x in row)
    assert all(sum(row) == 28 for row in M)
    assert all(M[i][i] == 0 for i in range(N))
    assert all(M[i][j] == M[j][i] for i in range(N) for j in range(N))
    # Verify the exact design identity M*M^T = 16 I + 12 J.
    for i in range(N):
        for j in range(N):
            assert sum(M[i][k] * M[j][k] for k in range(N)) == (28 if i == j else 12)
    valuations = two_adic_valuations(M)
    assert valuations == EXPECTED, (valuations, EXPECTED)
    assert sum(v * multiplicity for v, multiplicity in valuations.items()) == 128
    # M^2=16I+12J; row sum 28 implies |det(M)|=28*4^63=7*2^128.
    # Therefore the unique odd-primary factor is 7, adjoining a largest
    # 2-primary invariant factor (16), giving 112.
    invariant_factors = ([1] * 8 + [2] * 14 + [4] * 20
                         + [8] * 14 + [16] * 7 + [112])
    assert len(invariant_factors) == N
    assert all(invariant_factors[i + 1] % invariant_factors[i] == 0
               for i in range(N - 1))
    from math import prod
    assert prod(invariant_factors) == 28 * 4**63
    # Exact inverse: M^{-1}=(7M-3J)/112. Check each coordinate needs 112.
    for i in range(N):
        assert any(M[j][i] == 0 for j in range(N))
        assert gcd(112, 3) == 1
        for k in range(N):
            s = sum(M[i][j] * (7*M[j][k] - 3) for j in range(N))
            assert s == (112 if i == k else 0)
    print('VERIFIED_THETA_TRANSLATES_64_SMITH_1x8_2x14_4x20_8x14_16x7_112x1_EXPONENT_112')


if __name__ == '__main__':
    verify()

#!/usr/bin/env python3
"""Exact finite certificates for the 7-adic Padovan zero-frequency theorem.

This program verifies the finite data entering the proof and compares its
consequences with direct recurrence counts. Infinite lifting is proved in
RESULT.md, not inferred from the finite tests.
"""

from collections import Counter

REGULAR = {
    8: (1, 3), 12: (3, 2), 13: (4, 5),
    24: (4, 6), 28: (5, 4), 29: (2, 3),
    40: (5, 5), 44: (1, 1), 45: (6, 6),
}
EXCEPTIONAL = {
    15: ((1, 2, 2), (2, 4)),
    31: ((6, 3, 4), (4, 6)),
    47: ((3, 4, 1), (1, 6)),
}
ZEROS_MOD7 = sorted(REGULAR) + sorted(EXCEPTIONAL)


def padovan(N, modulus=None):
    a = [1, 1, 1]
    for n in range(3, N):
        v = a[n - 2] + a[n - 3]
        a.append(v if modulus is None else v % modulus)
    return a[:N]


def matmul(A, B, m):
    return [[sum(A[i][k] * B[k][j] for k in range(3)) % m
             for j in range(3)] for i in range(3)]


def matpow(A, n, m):
    R = [[int(i == j) for j in range(3)] for i in range(3)]
    while n:
        if n & 1:
            R = matmul(R, A, m)
        A = matmul(A, A, m)
        n //= 2
    return R


def main():
    p = padovan(144)
    assert sorted(i for i in range(48) if p[i] % 7 == 0) == sorted(ZEROS_MOD7)
    for i, (a, b) in REGULAR.items():
        assert (p[i] // 7) % 7 == a
        assert ((p[i + 48] - p[i]) // 7) % 7 == b
        assert b in range(1, 7)
        assert sum((a + b * t) % 7 == 0 for t in range(7)) == 1
    for i, (coeff, expected_roots) in EXCEPTIONAL.items():
        assert p[i] % 49 == (p[i + 48] - p[i]) % 49 == 0
        c0 = p[i] // 49 % 7
        c1 = (p[i + 48] - p[i]) // 49 % 7
        c2 = (p[i + 96] - 2 * p[i + 48] + p[i]) // 49 % 7
        assert (c0, c1, c2) == coeff
        roots = [t for t in range(7)
                 if (c0 + c1 * t + c2 * (t * (t - 1) // 2)) % 7 == 0]
        assert tuple(roots) == expected_roots
        for t in roots:
            assert (c1 + c2 * ((2 * t - 1) * pow(2, -1, 7))) % 7 != 0

    T = [[0, 1, 0], [0, 0, 1], [1, 1, 0]]
    I = [[int(i == j) for j in range(3)] for i in range(3)]
    assert matpow(T, 48, 7) == I
    for d in range(1, 48):
        if 48 % d == 0:
            T_d = matpow(T, d, 7)
            assert [sum(T_d[i][j] for j in range(3)) % 7 for i in range(3)] != [1, 1, 1]
    T_48 = matpow(T, 48, 49)
    assert [[((T_48[i][j] - I[i][j]) % 49) // 7 for j in range(3)] for i in range(3)] == [
        [4, 6, 1], [1, 5, 6], [6, 0, 5]]
    assert [sum(T_48[i][j] for j in range(3)) % 49 for i in range(3)] == [29, 36, 29]

    direct_zeros = []
    for k in range(1, 7):
        N, m = 48 * 7 ** (k - 1), 7**k
        a, b, c = 1, 1, 1
        count = 0
        special = Counter()
        for n in range(N):
            if a == 0:
                count += 1
                special[n % 48] += 1
            a, b, c = b, c, (a + b) % m
        expect = 12 if k == 1 else 30 if k == 2 else 51
        assert count == expect, (k, count, expect)
        for i in REGULAR:
            assert special[i] == 1
        if k == 2:
            for i in EXCEPTIONAL:
                assert special[i] == 7
        if k >= 3:
            for i in EXCEPTIONAL:
                assert special[i] == 14
        assert (a, b, c) == (1, 1, 1), (k, a, b, c)
        print('k=%d period=%d zeros=%d' % (k, N, count))

    for k, n in [(2, 100), (3, 1001), (5, 12345), (6, 806735)]:
        m = 7 ** k
        f = padovan(n + 3, m)
        Tn = matpow(T, n, m)
        assert [sum(Tn[i][j] for j in range(3)) % m for i in range(3)] == f[n:n + 3]
    print('CHECK_OK; finite certificates support, but do not replace, the all-level proof')


if __name__ == '__main__':
    main()

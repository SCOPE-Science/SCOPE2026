#!/usr/bin/env python3
"""Exact integer checks for Fourier inversion on path maximal-independent-set indicators."""

def all_maximal_independent_masks(n):
    for mask in range(1 << n):
        if mask & (mask << 1):
            continue
        if any(not ((mask >> j) & 1) and
               not (j > 0 and ((mask >> (j - 1)) & 1)) and
               not (j < n - 1 and ((mask >> (j + 1)) & 1))
               for j in range(n)):
            continue
        yield mask


def walsh_transform(f):
    f = list(f)
    h = 1
    while h < len(f):
        for start in range(0, len(f), 2 * h):
            for j in range(start, start + h):
                a, b = f[j], f[j + h]
                f[j], f[j + h] = a + b, a - b
        h *= 2
    return f


def count(n):
    m = [1, 1, 2, 2]
    if n < 4:
        return m[n]
    for i in range(4, n + 1):
        m.append(m[i - 2] + m[i - 3])
    return m[n]


def witness(n):
    if n == 2:
        return {1}
    if n < 2 or n % 7 not in (2, 3, 5):
        raise ValueError('n must be a singular path length')
    base = {2: 9, 3: 3, 5: 5}[n % 7]
    bad = {4} if base == 9 else {1}
    for start in range(base + 1, n + 1, 7):
        bad.add(start + 5)
    return bad


def weighted_sum(n, negative_positions):
    sign = lambda i: -1 if i in negative_positions else 1
    if n == 1:
        return sign(1)
    F = {1: sign(1), 2: sign(2)}
    if n >= 3:
        F[3] = sign(1) * sign(3)
    for j in range(4, n + 1):
        F[j] = sign(j) * (F[j - 2] + F[j - 3])
    return F[n - 1] + F[n]


def multiply(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(3))
             for j in range(3)] for i in range(3)]


def matrix_for(s):
    return [[0, s, s], [1, 0, 0], [0, 1, 0]]


def verify():
    B = [[int(i == j) for j in range(3)] for i in range(3)]
    for s in [1, 1, 1, 1, 1, -1, 1]:
        B = multiply(matrix_for(s), B)
    assert B == [[3, 4, 2], [-2, -3, -2], [2, 2, 1]]
    assert [B[0][j] + B[1][j] for j in range(3)] == [1, 1, 0]
    # Exhaustive independent enumeration plus independent Walsh transform.
    for n in range(1, 17):
        f = [0] * (1 << n)
        for mask in all_maximal_independent_masks(n):
            f[mask] = 1
        spectrum = walsh_transform(f)
        assert sum(f) == count(n)
        expected_invertible = n % 7 not in (2, 3, 5)
        assert all(c != 0 for c in spectrum) == expected_invertible
        assert spectrum[0] == count(n)
        if not expected_invertible:
            freq = sum(1 << (j-1) for j in witness(n))
            assert spectrum[freq] == 0
        assert (spectrum[0] % 2 == 1) == (n % 7 not in (2, 3, 5))
    # Check every recurrence witness through 500 vertices, beyond enumeration.
    for n in range(2, 501):
        if n % 7 in (2, 3, 5):
            assert weighted_sum(n, witness(n)) == 0
            assert count(n) % 2 == 0
        else:
            assert count(n) % 2 == 1
    print('PASS: 16 exhaustive Walsh spectra, seven-step transfer, 499 lengths')


if __name__ == '__main__':
    verify()

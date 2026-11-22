#!/usr/bin/env python3
"""Exact, standalone verification of signed connected-subtree spectra.

All counts are integers. No third-party packages are needed.
"""
from collections import Counter
from math import comb


def predicted(m):
    h = Counter()
    for k in range(m + 1):
        weight = comb(m, k) * 3 ** (m - k)
        h[4 * k - m + 3 ** k] += weight
        h[4 * k - m - 3 ** k] += weight
    return h


def connected_indicator(m):
    # Vertex 0 is center; arm i has near vertex 2*i+1 and leaf 2*i+2.
    n = 2 * m + 1
    neighbours = [0] * n
    for i in range(m):
        a, b = 2 * i + 1, 2 * i + 2
        for x, y in ((0, a), (a, b)):
            neighbours[x] |= 1 << y
            neighbours[y] |= 1 << x
    f = [0] * (1 << n)
    for mask in range(1, 1 << n):
        frontier = mask & -mask
        visited = 0
        while frontier:
            bit = frontier & -frontier
            frontier ^= bit
            visited |= bit
            v = bit.bit_length() - 1
            frontier |= neighbours[v] & mask & ~visited & ~frontier
        if visited == mask:
            f[mask] = 1
    return f


def transform(f):
    n = len(f)
    p = 1
    while p < n:
        step = p * 2
        for i in range(0, n, step):
            for j in range(i, i + p):
                a, b = f[j], f[j + p]
                f[j], f[j + p] = a + b, a - b
        p = step
    return f


def check(m):
    n = 2 * m + 1
    observed = Counter(transform(connected_indicator(m)))
    theoretical = predicted(m)
    assert observed == theoretical, (m, observed - theoretical, theoretical - observed)
    assert sum(observed.values()) == 1 << n
    assert sum(v * count for v, count in observed.items()) == 0
    assert sum(v * v * count for v, count in observed.items()) == (1 << n) * (3 ** m + 3 * m)
    if m >= 2:
        z = sum(comb(m, k) * 3 ** (m - k) for k in range(1, m + 1) if 4*k+3**k==m)
        assert observed[0] == z
    return {'arms':m,'vertices':n,'connected_subtrees':3**m+3*m,
            'zeros':observed[0], 'min_positive_abs':min(abs(v) for v in observed if v),
            'spectrum_levels':len(observed)}


def test_resonance_arithmetic():
    for m in range(2, 500):
        z = predicted(m)[0]
        expected = sum(comb(m,k)*3**(m-k) for k in range(1,m+1) if m==4*k+3**k)
        assert z == expected
    for k in range(1, 8):
        m = 4*k + 3**k
        h = predicted(m)  # formula uses O(m) terms, no large Walsh transform
        assert h[0] == comb(m,k)*3**(m-k)
        assert min(abs(v) for v in h if v) == 4 + 2*3**(k-1)


if __name__ == '__main__':
    for m in range(1,9):
        print(check(m))
    test_resonance_arithmetic()
    print('PASS: two exact methods agree for all 1<=m<=8; resonance and sharp gaps checked for k<=7.')

#!/usr/bin/env python3
"""Exact calculation for cubic-surface tritangents and Spence catalogue graph 2.

Requires only Python 3 standard library. The companion adjacency data consists of
45 binary strings, each of length 45, transcribed from Spence's catalogue.
"""
from collections import Counter
from itertools import combinations
from pathlib import Path


def cubic_graph():
    # Classes written aH - b_1 E_1 - ... - b_6 E_6.
    curves = []
    for i in range(6):
        v = [0] * 7
        v[i + 1] = -1
        curves.append(tuple(v))
    for i, j in combinations(range(6), 2):
        v = [1] + [0] * 6
        v[i + 1] = v[j + 1] = 1
        curves.append(tuple(v))
    for i in range(6):
        v = [2] + [1] * 6
        v[i + 1] = 0
        curves.append(tuple(v))
    assert len(curves) == 27

    def intersect(v, w):
        return v[0] * w[0] - sum(x * y for x, y in zip(v[1:], w[1:]))

    anticanonical = (3, 1, 1, 1, 1, 1, 1)
    triples = [c for c in combinations(range(27), 3)
               if all(intersect(curves[i], curves[j]) == 1
                      for i, j in combinations(c, 2))
               and tuple(sum(curves[i][j] for i in c) for j in range(7)) == anticanonical]
    assert len(triples) == 45
    adjacency = [[0] * 45 for _ in range(45)]
    for i, j in combinations(range(45), 2):
        if len(set(triples[i]).intersection(triples[j])) == 1:
            adjacency[i][j] = adjacency[j][i] = 1
    return adjacency


def catalog_graph():
    rows = Path(__file__).with_name('spence_second.txt').read_text(encoding='ascii').splitlines()
    assert len(rows) == 45 and all(len(row) == 45 and set(row) <= {'0', '1'} for row in rows)
    return [[int(x) for x in row] for row in rows]


def check_srg(A):
    n = len(A)
    assert n == 45 and all(len(row) == n for row in A)
    assert all(A[i][i] == 0 and sum(A[i]) == 12 for i in range(n))
    assert all(A[i][j] == A[j][i] for i in range(n) for j in range(n))
    adjacent, nonadjacent = 0, 0
    for i, j in combinations(range(n), 2):
        common = sum(A[i][k] * A[j][k] for k in range(n))
        assert common == 3
        if A[i][j]:
            adjacent += 1
        else:
            nonadjacent += 1
    assert (adjacent, nonadjacent) == (270, 720)


def reduced_laplacian(A, sink):
    n = len(A)
    return [[12 * (i == j) - A[i][j] for j in range(n) if j != sink]
            for i in range(n) if i != sink]


def padic_exponents(M, p, precision):
    """Smith valuations of an integral full-rank matrix modulo p**precision.

    Each pivot is of least p-adic valuation in the trailing block. Row and
    column swaps and row elimination are invertible over Z/(p**precision).
    """
    mod = p ** precision
    A = [[int(x) % mod for x in row] for row in M]
    n = len(A)
    output = []
    for i in range(n):
        best = precision
        at = None
        for r in range(i, n):
            for c in range(i, n):
                v = A[r][c]
                if v == 0:
                    continue
                order = 0
                while v % p == 0:
                    v //= p
                    order += 1
                if order < best:
                    best, at = order, (r, c)
        assert at is not None, 'increase p-adic precision'
        r, c = at
        A[i], A[r] = A[r], A[i]
        for row in A:
            row[i], row[c] = row[c], row[i]
        power = p ** best
        modulus_for_unit = mod // power
        inverse = pow(A[i][i] // power, -1, modulus_for_unit)
        for j in range(i + 1, n):
            entry = A[j][i]
            assert entry % power == 0
            multiplier = (entry // power * inverse) % modulus_for_unit
            if multiplier:
                for col in range(i, n):
                    A[j][col] = (A[j][col] - multiplier * A[i][col]) % mod
            assert A[j][i] == 0
        output.append(best)
    return output


def bareiss_determinant(M):
    A = [list(row) for row in M]
    n = len(A)
    sign, previous = 1, 1
    for k in range(n - 1):
        if A[k][k] == 0:
            r = next((r for r in range(k+1,n) if A[r][k]), None)
            assert r is not None
            A[k], A[r] = A[r], A[k]
            sign = -sign
        pivot = A[k][k]
        for i in range(k + 1,n):
            for j in range(k + 1,n):
                numerator = A[i][j] * pivot - A[i][k] * A[k][j]
                assert numerator % previous == 0
                A[i][j] = numerator // previous
            A[i][k] = 0
        previous = pivot
    return sign * A[-1][-1]


def main():
    expected = ((3 ** 62) * (5 ** 23))
    expected_spectra = [
        {3: {0: 15, 1: 10, 2: 5, 3: 14}, 5: {0: 21, 1: 23}},
        {3: {0: 17, 1: 8, 2: 3, 3: 16}, 5: {0: 21, 1: 23}},
    ]
    for tag, A, targets in zip(('cubic', 'spence_second'),
                               (cubic_graph(), catalog_graph()), expected_spectra):
        check_srg(A)
        for sink in (0, 9, 20):
            M = reduced_laplacian(A, sink)
            determinant = bareiss_determinant(M)
            assert determinant == expected, (tag, sink, determinant)
            for p, precision in ((3, 9), (5, 6)):
                values = padic_exponents(M, p, precision)
                assert dict(Counter(values)) == targets[p], (tag, sink, p, Counter(values))
                assert sum(values) == (62 if p == 3 else 23)
        print(f'{tag}: strongly regular (45,12,3,3), three sink checks, determinant and Smith valuations PASS')
    print('CUBIC_TRITANGENT_CRITICAL_GROUP_COMPARISON_OK')


if __name__ == '__main__':
    main()

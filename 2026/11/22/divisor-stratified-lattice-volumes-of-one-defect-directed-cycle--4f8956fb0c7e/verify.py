#!/usr/bin/env python3
"""Exact-integer, stdlib-only checks of the one-defect cycle-simplex volume law.
Scientific claim and proof are in RESULT.md; these finite checks are not the proof.
"""
from math import gcd
from functools import reduce


def det_bareiss(mat):
    n = len(mat)
    if n == 0:
        return 1
    a = [list(map(int, row)) for row in mat]
    sign = 1
    prev = 1
    for k in range(n - 1):
        if a[k][k] == 0:
            r = next((i for i in range(k + 1, n) if a[i][k]), None)
            if r is None:
                return 0
            a[k], a[r] = a[r], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                t = a[i][j] * pivot - a[i][k] * a[k][j]
                assert t % prev == 0
                a[i][j] = t // prev
        for i in range(k + 1, n):
            a[i][k] = 0
        prev = pivot
    return sign * a[n - 1][n - 1]


def columns(n, w, u):
    cols = []
    for i in range(n):
        col = [0] * n
        col[i] = 1
        col[(i + 1) % n] = w if i < n - 1 else u
        cols.append(col)
    return cols


def intrinsic_volume_via_minors(cols):
    n = len(cols)
    # The signed maximal minors of the n x (n-1) difference matrix
    # generate exactly the relative lattice volume index.
    edges = [[cols[j][i] - cols[-1][i] for j in range(n - 1)] for i in range(n)]
    minors = [det_bareiss(edges[:i] + edges[i+1:]) for i in range(n)]
    return reduce(gcd, (abs(v) for v in minors)), minors


def run():
    cases = 0
    determinant_checks = 0
    index_checks = 0
    unimodular_cases = 0
    for n in range(3, 9):
        for w in range(2, 6):
            s = sum((-w)**k for k in range(n))
            for u in range(1, 12):
                cols = columns(n, w, u)
                matrix = [[col[i] for col in cols] for i in range(n)]
                d = det_bareiss(matrix)
                wantdet = 1 + u * (-w)**(n-1)
                assert d == wantdet != 0, (n, w, u, d, wantdet)
                determinant_checks += 1
                v, minors = intrinsic_volume_via_minors(cols)
                expected = gcd(abs(s), abs(u - w))
                assert v == expected, (n, w, u, v, expected, minors)
                index_checks += 1
                if v == 1:
                    unimodular_cases += 1
                cases += 1
    print('PASS: exact integer Bareiss determinants:', determinant_checks)
    print('PASS: independent maximal-minor lattice-index checks:', index_checks)
    print('PASS: unimodular cases in this sample:', unimodular_cases)
    print('PASS: tested parameters 3<=n<=8, 2<=w<=5, 1<=u<=11; total', cases)

if __name__ == '__main__':
    run()

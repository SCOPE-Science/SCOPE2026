#!/usr/bin/env python3
"""Finite exact checks for the single-Jordan-block local-derivation theorem.

The all-k theorem is proved in RESULT.md. These checks only corroborate the
centralizer/flag dimensions and the pointwise polynomial representation on
small rational examples; they are not a substitute for the proof.
"""
from fractions import Fraction


def zeros(n, m):
    return [[0 for _ in range(m)] for _ in range(n)]


def eye(n):
    a = zeros(n, n)
    for i in range(n):
        a[i][i] = 1
    return a


def matmul(a, b):
    n, p, m = len(a), len(b), len(b[0])
    return [[sum(a[i][r] * b[r][j] for r in range(p)) for j in range(m)] for i in range(n)]


def matsub(a, b):
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def rank(matrix):
    if not matrix:
        return 0
    a = [[Fraction(x) for x in row] for row in matrix]
    rows, cols = len(a), len(a[0])
    r = 0
    for c in range(cols):
        pivot = next((i for i in range(r, rows) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        scale = a[r][c]
        a[r] = [x / scale for x in a[r]]
        for i in range(rows):
            if i != r and a[i][c]:
                scale = a[i][c]
                a[i] = [a[i][j] - scale * a[r][j] for j in range(cols)]
        r += 1
        if r == rows:
            break
    return r


def column_rank(columns, nrows):
    if not columns:
        return 0
    return rank([[columns[j][i] for j in range(len(columns))] for i in range(nrows)])


def shift(k):
    s = zeros(k, k)
    for i in range(k - 1):
        s[i + 1][i] = 1
    return s


def commutator_map_rank(s):
    k = len(s)
    columns = []
    for a in range(k):
        for b in range(k):
            e = zeros(k, k)
            e[a][b] = 1
            c = matsub(matmul(e, s), matmul(s, e))
            columns.append([c[i][j] for i in range(k) for j in range(k)])
    return rank([[columns[j][i] for j in range(k * k)] for i in range(k * k)])


def apply(a, v):
    return [sum(a[i][j] * v[j] for j in range(len(v))) for i in range(len(a))]


def flag_matrix(k, seed):
    # B e_j lies in span(e_j,...,e_k): lower triangular in this basis.
    b = zeros(k, k)
    for i in range(k):
        for j in range(i + 1):
            b[i][j] = ((seed + 3 * i + 5 * j) % 7) - 3
    return b


def polynomial_witness(s, b, v):
    k = len(v)
    w = apply(b, v)
    j = next((i for i, z in enumerate(v) if z != 0), None)
    if j is None:
        assert all(z == 0 for z in w)
        return
    assert all(w[i] == 0 for i in range(j))
    coeff = []
    for r in range(k - j):
        i = j + r
        previous = sum(coeff[t] * v[i - t] for t in range(r))
        coeff.append((w[i] - previous) / v[j])
    # Verify p(S)v = w exactly over Q.
    power = eye(k)
    out = [Fraction(0) for _ in range(k)]
    for c in coeff:
        pv = apply(power, v)
        out = [out[i] + c * pv[i] for i in range(k)]
        power = matmul(power, s)
    assert out == [Fraction(z) for z in w]


def main():
    for k in range(1, 9):
        s = shift(k)
        assert commutator_map_rank(s) == k * k - k
        centralizer_dim = k * k - commutator_map_rank(s)
        assert centralizer_dim == k
        flag_columns = []
        for i in range(k):
            for j in range(i + 1):
                e = zeros(k, k)
                e[i][j] = 1
                flag_columns.append([e[r][c] for r in range(k) for c in range(k)])
        flag_dim = column_rank(flag_columns, k * k)
        assert flag_dim == k * (k + 1) // 2
        polynomial_columns = []
        power = eye(k)
        for _ in range(k):
            polynomial_columns.append([power[r][c] for r in range(k) for c in range(k)])
            power = matmul(power, s)
        polynomial_dim = column_rank(polynomial_columns, k * k)
        assert polynomial_dim == k and centralizer_dim == polynomial_dim
        assert k + flag_dim == k + k * (k + 1) // 2
        # A diagonal map with a final diagonal entry 2 is flag-preserving.
        # For k >= 2 it fails to commute with S, hence is not a derivation.
        if k >= 2:
            b0 = zeros(k, k)
            for i in range(k):
                b0[i][i] = 2 if i == k - 1 else 1
            assert all(b0[i][j] == 0 for i in range(k) for j in range(i + 1, k))
            assert matmul(b0, s) != matmul(s, b0)
        for seed in range(1, 25):
            b = flag_matrix(k, seed)
            v = [Fraction(((seed * (i + 2) + i * i) % 9) - 4) for i in range(k)]
            polynomial_witness(s, b, v)
    print("PASS: exact centralizer dimensions, flag dimensions, and rational pointwise witnesses checked for k=1..8.")
    print("The finite checks corroborate but do not replace the all-k symbolic proof in RESULT.md.")


if __name__ == '__main__':
    main()

"""Exact checks for the two-token complete-bipartite Laplacian theorem.

Python 3.10+ and SymPy 1.12+ are required. All characteristic polynomials,
cofactors, and eigenvalue multiplicities are compared as exact integers.
"""
from itertools import combinations
from collections import Counter
from math import comb
from sympy import Matrix, symbols, Poly


def laplacian(m, n):
    """Build the token graph directly from the one-particle edge definition."""
    vertices = tuple(combinations(range(m+n), 2))
    positions = {v: i for i, v in enumerate(vertices)}
    L = [[0] * len(vertices) for _ in vertices]
    for u in range(m):
        for v in range(m, m+n):
            for t in vertices:
                if (u in t) == (v in t):
                    continue
                tnew = tuple(sorted((set(t) - {u, v}) | ({v} if u in t else {u})))
                i, j = positions[t], positions[tnew]
                if i < j:
                    L[i][i] += 1
                    L[j][j] += 1
                    L[i][j] = -1
                    L[j][i] = -1
    return Matrix(L)


def expected(m, n):
    """Compute the claimed spectrum without diagonalizing any matrices."""
    C = Counter()
    def insert(eigenvalue, multiplicity):
        if multiplicity:
            assert multiplicity > 0
            C[eigenvalue] += multiplicity
    insert(0, 1)
    insert(m + n, 1)
    insert(2 * (m + n - 1), 1)
    insert(m + n - 2, (m - 1) * (n - 1))
    insert(n, m - 1)
    if m >= 3:
        insert(m + 2*n - 2, m - 1)
    insert(m, n - 1)
    if n >= 3:
        insert(2*m + n - 2, n - 1)
    if m >= 4:
        insert(2*n, m * (m - 3) // 2)
    if n >= 4:
        insert(2*m, n * (n - 3) // 2)
    return C


def check():
    x = symbols('x')
    checked = 0
    for m in range(2, 8):
        for n in range(2, 8):
            L = laplacian(m, n)
            C = expected(m, n)
            assert L.rows == comb(m+n, 2) == sum(C.values())
            assert all(sum(L.row(i)) == 0 for i in range(L.rows))
            observed = Poly(L.charpoly(x).as_expr(), x)
            predicted = Poly(1, x)
            for eigenvalue, multiplicity in C.items():
                predicted *= Poly(x-eigenvalue, x)**multiplicity
            assert observed == predicted, (m, n, observed, predicted)
            checked += 1
    print(f'EXACT_CHARPOLY_PASS pairs={checked} range=2..7')
    for m, n in [(2, 2), (2, 3), (3, 3), (3, 4), (4, 4)]:
        L = laplacian(m, n)
        tree_cofactor = L.minor_submatrix(0, 0).det(method='bareiss')
        numerator = 1
        for eigenvalue, multiplicity in expected(m, n).items():
            if eigenvalue:
                numerator *= eigenvalue ** multiplicity
        assert numerator % L.rows == 0
        spectral_tree_count = numerator // L.rows
        assert tree_cofactor == spectral_tree_count
        print(f'EXACT_MATRIX_TREE_PASS m={m} n={n} trees={int(tree_cofactor)}')
    print('ALL_TESTS_PASS')


if __name__ == '__main__':
    check()

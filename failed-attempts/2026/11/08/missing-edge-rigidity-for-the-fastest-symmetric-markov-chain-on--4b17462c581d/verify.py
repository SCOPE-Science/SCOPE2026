#!/usr/bin/env python3
"""Exact finite sanity checks for the missing-edge mixing theorem.

The general result is proved in RESULT.md; finite checks here are not a proof.
Only Python's standard library is required.
"""
from fractions import Fraction as F


def mm(A, B):
    n = len(A)
    return [[sum((A[i][k] * B[k][j] for k in range(n)), F(0))
             for j in range(n)] for i in range(n)]


def check(n, pairs):
    Q = [[F(int(i == j)) for j in range(n)] for i in range(n)]
    for a, b in pairs:
        assert a != b
        Q[a][a] = Q[b][b] = F(0)
        Q[a][b] = Q[b][a] = F(1)
    assert mm(Q, Q) == [[F(int(i == j)) for j in range(n)] for i in range(n)]
    P = [[(F(1) - Q[i][j]) / (n - 1) for j in range(n)] for i in range(n)]
    assert all(sum(row) == 1 for row in P)
    assert all(P[i][j] == P[j][i] and P[i][j] >= 0
               for i in range(n) for j in range(n))
    assert all(P[a][b] == 0 for a, b in pairs)
    M = [[P[i][j] - F(1, n) for j in range(n)] for i in range(n)]
    M2 = mm(M, M)
    target = [[(F(int(i == j)) - F(1, n)) / ((n - 1) ** 2)
               for j in range(n)] for i in range(n)]
    assert M2 == target
    return 1


def main():
    count = 0
    for n in range(3, 16):
        for k in range(1, n // 2 + 1):
            count += check(n, [(2 * j, 2 * j + 1) for j in range(k)])
    inequalities = 0
    for n in range(3, 80):
        for r in range(1, n):
            # The column/Cauchy lower bound is r/((n-1)(n-r)).
            t2 = F(r, (n - 1) * (n - r))
            assert t2 >= F(1, (n - 1) ** 2)
            if r >= 2:
                assert t2 > F(1, (n - 1) ** 2)
            # Exact minimum of ||p-1/n||_2^2 with r forbidden entries.
            assert F(1, n - r) - F(1, n) == F(r, n * (n - r))
            inequalities += 1
    print(f'VERIFY_OK matching_cases={count} bound_cases={inequalities}')


if __name__ == '__main__':
    main()

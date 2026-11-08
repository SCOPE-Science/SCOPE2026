"""Exact rational least-squares checks for matching-deleted square tables.

Python 3 standard library only. Run: python crown_projection_checker.py
Finite tests supplement, but do not establish, the all-dimensional theorem.
"""
from fractions import Fraction as Q


def inverse(A):
    n = len(A)
    B = [[Q(A[i][j]) for j in range(n)] + [Q(i == j) for j in range(n)] for i in range(n)]
    for k in range(n):
        pivot = next(i for i in range(k, n) if B[i][k])
        B[k], B[pivot] = B[pivot], B[k]
        v = B[k][k]
        B[k] = [x / v for x in B[k]]
        for i in range(n):
            if i != k:
                v = B[i][k]
                B[i] = [a - v*b for a, b in zip(B[i], B[k])]
    return [row[n:] for row in B]


def test(n, r):
    E = [(i, j) for i in range(n) for j in range(n) if not(i == j and i < r)]
    X = [[int(i == k) for k in range(n)] + [int(j == k) for k in range(n-1)] for i,j in E]
    d = 2*n-1
    gram = [[sum(row[i]*row[j] for row in X) for j in range(d)] for i in range(d)]
    G = inverse(gram)
    XG = [[sum(Q(X[a][i])*G[i][j] for i in range(d)) for j in range(d)] for a in range(len(E))]
    H = [[sum(XG[a][j]*X[b][j] for j in range(d)) for b in range(len(E))] for a in range(len(E))]
    T = n*(n-2)+r
    norm = Q(3*n-4,n) if r == n else Q(3*n-4,n) + Q(2*(n-2),n*T)
    assert all(sum(row) == 1 for row in H)
    for i, (a,b) in enumerate(E):
        h = sum(abs(x) for x in H[i])
        if r < n and a >= r and b >= r:
            assert h == norm
        if 0 < r < n and (a < r) != (b < r):
            z = r*r - n*r + n*n - 3*n + 3
            assert h == norm - Q(2*z,n*(n-2)*T)
        if r >= 2 and a < r and b < r:
            assert h == Q(3*n-4,n)
    assert max(sum(abs(x) for x in row) for row in H) == norm
    return len(E)

if __name__ == '__main__':
    cells = sum(test(n,r) for n in range(3,7) for r in range(n+1))
    print('INDEPENDENT_RATIONAL_GRAM_TESTS_PASSED',cells,'cells across 22 designs')

#!/usr/bin/env python3
"""Dependency-free exact checks for two-sensor finite-cycle dynamical sampling."""
from math import gcd


def matmul(left, right):
    return [[sum(x*y for x,y in zip(row, col)) for col in zip(*right)] for row in left]


def determinant(a):
    """Fraction-free Bareiss determinant over integers (exact)."""
    a = [list(row) for row in a]
    n = len(a)
    sign = 1
    prev = 1
    for k in range(n - 1):
        if a[k][k] == 0:
            pos = next((i for i in range(k + 1, n) if a[i][k]), None)
            if pos is None:
                return 0
            a[k], a[pos] = a[pos], a[k]
            sign *= -1
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numer = a[i][j] * pivot - a[i][k] * a[k][j]
                assert numer % prev == 0
                a[i][j] = numer // prev
            a[i][k] = 0
        prev = pivot
    return sign * a[-1][-1]


def observation(m, d, alpha=1, beta=0):
    n = 2*m
    b = [[0]*n for _ in range(n)]
    for j in range(n):
        b[j][j] += beta
        b[j][(j-1)%n] += alpha
        b[j][(j+1)%n] += alpha
    t0 = [int(j==0) for j in range(n)]
    td = [int(j==d) for j in range(n)]
    rows = []
    for _ in range(m):
        rows += [t0, td]
        t0 = [sum(t0[j]*b[j][k] for j in range(n)) for k in range(n)]
        td = [sum(td[j]*b[j][k] for j in range(n)) for k in range(n)]
    return rows


def check():
    checks = 0
    for m in range(2, 10):
        n = 2*m
        for d in range(1, n):
            det = determinant(observation(m, d))
            assert abs(det) == (1 if gcd(d, n)==1 else 0), (m,d,det)
            checks += 1
    for m in range(2, 7):
        n = 2*m
        for alpha, beta in [(1, 5), (2, 3), (-1, 1)]:
            for d in range(1, n):
                det = determinant(observation(m,d,alpha,beta))
                pred = abs(alpha)**(m*(m-1)) if gcd(d,n)==1 else 0
                assert abs(det) == pred, (m,d,alpha,beta,det,pred)
                checks += 1
    # Boundary: M=1 would make C_2 a multigraph; deliberately excluded.
    print(f'CHECK_OK exact_determinants={checks} even_cycles=4..18')

if __name__ == '__main__':
    check()

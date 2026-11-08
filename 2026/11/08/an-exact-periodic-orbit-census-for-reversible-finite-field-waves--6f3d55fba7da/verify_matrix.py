"""Exact modular-linear-algebra test of the stated cyclic wave census (stdlib)."""
from math import gcd


def valuation(n, p):
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


def prediction(n, k, p):
    g = gcd(n, k)
    if p != 2:
        defect = (valuation(n, p) == valuation(k, p)) * (1 + (g % 2 == 0))
    else:
        defect = (n % 2 == 1 and k % 2 == 1)
    return 2*g-int(defect)


def matmul(A, B, p):
    d = len(A)
    C = [[0]*d for _ in range(d)]
    for i, row in enumerate(A):
        for j, a in enumerate(row):
            if a:
                for k in range(d):
                    C[i][k] += a*B[j][k]
        C[i] = [v % p for v in C[i]]
    return C


def rank(A, p):
    a = [list(row) for row in A]
    d = len(a)
    r = 0
    for c in range(d):
        pivot = next((i for i in range(r, d) if a[i][c] % p), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        inv = pow(a[r][c] % p, -1, p)
        a[r] = [v*inv % p for v in a[r]]
        for i in range(r+1, d):
            f = a[i][c] % p
            if f:
                a[i] = [(x-f*y) % p for x, y in zip(a[i], a[r])]
        r += 1
    return r


number = 0
for n in range(3, 13):
    for p in (2, 3, 5, 7):
        d = 2*n
        M = [[0]*d for _ in range(d)]
        for i in range(n):
            M[i][(i-1) % n] += 1
            M[i][(i+1) % n] += 1
            M[i][n+i] -= 1
            M[n+i][i] = 1
        M = [[a % p for a in row] for row in M]
        I = [[int(i == j) for j in range(d)] for i in range(d)]
        P = I
        period = n * (p if p != 2 or n % 2 else 1)
        for k in range(1, period+1):
            P = matmul(P, M, p)
            D = [[(P[i][j]-I[i][j]) % p for j in range(d)] for i in range(d)]
            observed = d-rank(D, p)
            assert observed == prediction(n, k, p), (n, p, k, observed)
            number += 1
        assert P == I, (n, p, 'identity')
print('PASS exact modular ranks: %d (n,p,k) tests, n=3..12 and p=2,3,5,7' % number)

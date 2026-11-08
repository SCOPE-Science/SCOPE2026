#!/usr/bin/env python3
"""Finite reproducibility checks for balanced endpoint sampling on paths.

All infinite-size assertions are proved analytically in RESULT.md; this program
checks algebraic reconstruction identities and determinant normalizations.
Uses only the Python standard library.
"""
import math


def cheb_coefficients(n):
    arr = [[1], [0, 1]]
    if n == 0:
        return [arr[0]]
    for k in range(1, n):
        nxt = [0] * (k + 2)
        for i, v in enumerate(arr[-1]):
            nxt[i + 1] += 2 * v
        for i, v in enumerate(arr[-2]):
            nxt[i] -= v
        arr.append(nxt)
    return arr[:n+1]


def normalized_path(n):
    d = [1] + [2] * (n - 2) + [1]
    P = [[0.0] * n for _ in range(n)]
    for j in range(n-1):
        v = 1 / math.sqrt(d[j] * d[j+1])
        P[j][j+1] = P[j+1][j] = v
    return P


def observe(P, site, num_times):
    n = len(P)
    v = [float(j == site) for j in range(n)]
    out = []
    for _ in range(num_times):
        out.append(v[:])
        v = [sum(v[k] * P[k][j] for k in range(n)) for j in range(n)]
    return out


def inverse_single(n):
    coeffs = cheb_coefficients(n-1)
    B = [[0.0] * n for _ in range(n)]
    for j in range(n):
        scale = 1.0 if j in (0, n-1) else math.sqrt(2)
        for t, c in enumerate(coeffs[j]):
            B[j][t] = scale * c
    return B


def inverse_double(n):
    m = n // 2
    coeffs = cheb_coefficients(m-1)
    B = [[0.0] * n for _ in range(n)]
    for j in range(m):
        scale = 1.0 if j == 0 else math.sqrt(2)
        for t, c in enumerate(coeffs[j]):
            B[j][t] = scale * c
            B[n-1-j][m+t] = scale * c
    return B


def multiply(A, B):
    return [[sum(a * B[k][j] for k,a in enumerate(row)) for j in range(len(B[0]))] for row in A]


def check_identity(X, eps=1e-7):
    errors = 0
    for i,row in enumerate(X):
        for j,x in enumerate(row):
            assert abs(x - float(i == j)) < eps, (i,j,x)
            errors += 1
    return errors


def test_all():
    checks = 0
    rho = 1 + math.sqrt(2)
    for m in range(2,9):
        n = 2 * m
        P = normalized_path(n)
        O = observe(P,0,n)
        D = observe(P,0,m) + observe(P,n-1,m)
        B1 = inverse_single(n)
        B2 = inverse_double(n)
        checks += check_identity(multiply(B1,O))
        checks += check_identity(multiply(B2,D))
        for j in range(m):
            for t in range(m):
                assert abs(D[t][n-1-j]) < 1e-13
                assert abs(D[m+t][j]) < 1e-13
                checks += 2
        # Triangular determinant exact powers (without unstable elimination).
        diag_single = [O[i][i] for i in range(n)]
        logdet_one = sum(math.log(abs(x)) for x in diag_single)
        assert abs(logdet_one + n*(n-2)*math.log(2)/2) < 1e-9
        block = [D[i][i] for i in range(m)]
        logdet_double = 2*sum(math.log(abs(x)) for x in block)
        assert abs(logdet_double + (m-1)**2*math.log(2)) < 1e-9
        checks += 2
        for j,c in enumerate(cheb_coefficients(m-1)):
            norm = math.sqrt(sum(t*t for t in c))
            assert norm <= rho**j * (1+1e-12)
            if j>=1:
                assert norm * math.sqrt(j+1) +1e-10 >= (rho**j-rho**(-j))/2
            checks += 1 + int(j>=1)
    print('PATH_DOUBLE_ENDPOINT_CHEB_CHECKS_PASSED',checks)

if __name__ == '__main__':
    test_all()

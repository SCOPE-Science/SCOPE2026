"""Exact rational tests for the small-polar-cap Slepian constants.

Run: python3 verify.py. No third-party packages are required.
The finite tests corroborate, but do not prove, the all-bandwidth theorem.
"""
from fractions import Fraction as F
from math import factorial, comb


def determinant(a):
    n = len(a)
    if n == 0:
        return F(1)
    a = [list(map(F, r)) for r in a]
    out = F(1)
    for i in range(n):
        pivot = next((k for k in range(i, n) if a[k][i]), None)
        assert pivot is not None
        if pivot != i:
            a[pivot], a[i] = a[i], a[pivot]
            out = -out
        p = a[i][i]
        out *= p
        for k in range(i + 1, n):
            if a[k][i]:
                f = a[k][i] / p
                for j in range(i + 1, n):
                    a[k][j] -= f * a[i][j]
                a[k][i] = F(0)
    return out


def beta_integer(a, b):
    assert a >= 1 and b >= 1
    return F(factorial(a - 1) * factorial(b - 1), factorial(a + b - 1))


def hmatrix(m, k):
    return [[F(1, m + i + j + 1) for j in range(k)] for i in range(k)]


def qtail(L, m, j):
    d = L - m
    return [[beta_integer(m + i + h + 1, m + 1)
             for h in range(j, d + 1)] for i in range(j, d + 1)]


def endpoint_kernel(alpha, beta, n):
    # Christoffel--Darboux kernel at t=0 for t^alpha(1-t)^beta.
    return F(factorial(n + alpha + beta + 1) * factorial(n + alpha + 1),
             (alpha + 1) * factorial(alpha)**2 * factorial(n + beta) * factorial(n))


def coefficient(L, m, j):
    return endpoint_kernel(m + 2*j, m, L-m-j) / F((m + 2*j + 1)*comb(m + 2*j, j)**2)


def check():
    tests = 0
    for L in range(9):
        mult = [0]*(2*L+1)
        for m in range(L+1):
            d = L-m
            hdet = [determinant(hmatrix(m, k)) for k in range(d+2)]
            qdet = [determinant(qtail(L,m,j)) for j in range(d+2)]
            product = F(1)
            for j in range(d+1):
                # Exterior-power determinant coefficient versus Jacobi endpoint formula.
                a = (hdet[j+1]/hdet[j]) * (qdet[j+1]/qdet[j])
                b = coefficient(L,m,j)
                assert a == b > 0, (L,m,j,a,b)
                tests += 1
                product *= a
                mult[m+2*j] += (1 if m == 0 else 2)
            assert product == hdet[d+1]/qdet[0]
            tests += 1
            assert sum(m+2*j+1 for j in range(d+1)) == (d+1)*(m+d+1)
            tests += 1
        assert mult == [min(k+1, 2*L-k+1) for k in range(2*L+1)]
        assert sum(mult) == (L+1)**2
        assert coefficient(L,0,0) == (L+1)**2
        assert coefficient(L,0,L) == F(1, comb(2*L,L)**2)
        tests += 4
    return tests

if __name__ == '__main__':
    print('PASS:', check(), 'exact rational assertions')

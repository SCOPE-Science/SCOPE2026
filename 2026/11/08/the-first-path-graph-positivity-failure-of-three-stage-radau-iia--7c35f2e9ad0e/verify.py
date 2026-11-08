"""Exact standard-library certificates for fifth-order Radau IIA on unweighted paths.

Run: python3 verify.py
The proof document explains why the finite polynomial certificates prove
positivity for every positive real time step, not merely at sampled times.
"""
from fractions import Fraction as F
from math import comb


def path_laplacian(n):
    assert n >= 2
    a = [[0] * n for _ in range(n)]
    for i in range(n - 1):
        a[i][i] += 1
        a[i + 1][i + 1] += 1
        a[i][i + 1] = a[i + 1][i] = -1
    return a


def eye(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def laplacian_times(L, X):
    n = len(L)
    return [[sum(L[i][k] * X[k][j] for k in range(n))
             for j in range(n)] for i in range(n)]


def zero(n):
    return [[0] * n for _ in range(n)]


def polydata(n):
    """Return the exact determinant D and entrywise polynomial coefficients N.

    Q(hL) = 60I + 36hL + 9h^2L^2 + h^3L^3,
    P(hL) = 60I - 24hL + 3h^2L^2,
    and P(hL)Q(hL)^(-1) = N(h)/D(h).
    """
    L = path_laplacian(n)
    L2 = laplacian_times(L, L)
    L3 = laplacian_times(L, L2)
    d = 3 * (n - 1)

    # Formal logarithm log(Q(z)/60) and exact Newton identities.
    q = [F(1), F(3, 5), F(3, 20), F(1, 60)]
    logq = [F(0)] * (d + 1)
    for k in range(1, d + 1):
        s = sum(q[a] * (k - a) * logq[k - a]
                for a in range(1, min(3, k - 1) + 1))
        logq[k] = (k * (q[k] if k < len(q) else 0) - s) / k

    traces = [0] * (d + 1)
    power = eye(n)
    for k in range(1, d + 1):
        power = laplacian_times(L, power)
        traces[k] = sum(power[i][i] for i in range(n))
    e = [F(0)] + [logq[k] * traces[k] for k in range(1, d + 1)]
    D = [F(60 ** n)] + [F(0)] * d
    for k in range(1, d + 1):
        D[k] = sum(j * e[j] * D[k - j] for j in range(1, k + 1)) / k
    assert all(v.denominator == 1 and v >= 0 for v in D)
    D = [int(v) for v in D]
    assert D[-1] > 0

    # Polynomial identity Q(hL)N(h)=D(h)P(hL).
    N = [[[0] * (d + 1) for _ in range(n)] for _ in range(n)]
    prev = [zero(n) for _ in range(3)]
    for k in range(d + 1):
        t1 = laplacian_times(L, prev[-1]) if k >= 1 else zero(n)
        t2 = laplacian_times(L2, prev[-2]) if k >= 2 else zero(n)
        t3 = laplacian_times(L3, prev[-3]) if k >= 3 else zero(n)
        Nk = zero(n)
        for i in range(n):
            for j in range(n):
                v = 60 * D[k] * int(i == j)
                if k >= 1: v -= 24 * D[k - 1] * L[i][j]
                if k >= 2: v += 3 * D[k - 2] * L2[i][j]
                v -= 36 * t1[i][j] + 9 * t2[i][j] + t3[i][j]
                assert v % 60 == 0, ('nonintegral coefficient', n, i, j, k)
                Nk[i][j] = v // 60
                N[i][j][k] = Nk[i][j]
        prev = (prev + [Nk])[-3:]
    # Check the three trailing equations, proving the computed polynomial
    # is EXACTLY the numerator, not just a truncated Taylor expansion.
    for k in range(d + 1, d + 4):
        t1 = laplacian_times(L, prev[-1])
        t2 = laplacian_times(L2, prev[-2])
        t3 = laplacian_times(L3, prev[-3])
        assert all(36 * t1[i][j] + 9 * t2[i][j] + t3[i][j] ==
                   (-24 * D[k-1] * L[i][j] if k-1 <= d else 0) +
                   (3 * D[k-2] * L2[i][j] if k-2 <= d else 0)
                   for i in range(n) for j in range(n)), ('trailing', n, k)
        prev = (prev + [zero(n)])[-3:]
    return D, N


def multiply_one_plus_h(poly, m):
    """Exact monomial coefficients of (1+h)^m poly(h)."""
    choose = [comb(m, j) for j in range(m + 1)]
    result = [0] * (len(poly) + m)
    for a, coefficient in enumerate(poly):
        if coefficient:
            for b, c in enumerate(choose):
                result[a + b] += coefficient * c
    return result


def evaluate(poly, x):
    y = F(0)
    for a in reversed(poly):
        y = y * x + a
    return y


def direct_endpoint_value(n, h):
    """Independent exact rational solve of Q(hL)x=e_n, then (Px)_1."""
    L = path_laplacian(n)
    L2 = laplacian_times(L, L)
    L3 = laplacian_times(L, L2)
    Q = [[F(60 * int(i == j)) + 36*h*L[i][j] +
          9*h*h*L2[i][j] + h*h*h*L3[i][j]
          for j in range(n)] for i in range(n)]
    P = [[F(60 * int(i == j)) - 24*h*L[i][j] +
          3*h*h*L2[i][j] for j in range(n)] for i in range(n)]
    A = [Q[i] + [F(int(i == n-1))] for i in range(n)]
    for j in range(n):
        pivot = next(k for k in range(j, n) if A[k][j])
        A[j], A[pivot] = A[pivot], A[j]
        factor = A[j][j]
        for k in range(j, n + 1):
            A[j][k] /= factor
        for i in range(j+1, n):
            factor = A[i][j]
            for k in range(j, n + 1):
                A[i][k] -= factor*A[j][k]
    y = [F(0)]*n
    for i in range(n-1, -1, -1):
        y[i] = A[i][n] - sum(A[i][j]*y[j] for j in range(i+1, n))
    return sum(P[0][i]*y[i] for i in range(n))


def verify():
    # These are sufficient degree elevations, not claims of minimality.
    elevations = {**{n: 0 for n in range(2, 10)}, 10: 1, 11: 17,
                  12: 66, 13: 451}
    checked = 0
    for n in range(2, 14):
        D, N = polydata(n)
        assert D[0] == 60 ** n
        m = elevations[n]
        for i in range(n):
            for j in range(n):
                q = multiply_one_plus_h(N[i][j], m)
                assert all(x >= 0 for x in q), ('negative coefficient', n, i, j)
                assert any(x > 0 for x in q), ('zero polynomial', n, i, j)
                checked += len(q) + 1
        print('P_%d: all %d entry numerators positive for h>0 via degree elevation %d'
              % (n, n * n, m))
    D, N = polydata(14)
    h = F(5, 2)
    witness = evaluate(N[0][13], h) / evaluate(D, h)
    expected = F(-513016184045167720763721348125,
                 7821977770020587781141217755303635636)
    assert witness == expected and witness < 0
    assert direct_endpoint_value(14, h) == expected
    checked += 3
    print('P_14 endpoint witness at h=5/2:', str(witness))
    print('VERIFY_OK', checked, 'exact coefficient/sign checks')


if __name__ == '__main__':
    verify()

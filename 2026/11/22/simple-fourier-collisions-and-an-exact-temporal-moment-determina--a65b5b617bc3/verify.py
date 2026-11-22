"""Exact small-order checks for a two-step cyclic Fourier observability identity.
Run: python3 verify.py. Uses the Python 3 standard library only.
Finite checks corroborate, but do not replace, the theorem's proof.
"""
from fractions import Fraction
from cmath import exp
from math import cos, pi


def determinant(matrix):
    m = [list(row) for row in matrix]
    n = len(m)
    out = Fraction(1)
    for j in range(n):
        pivot = next((i for i in range(j, n) if m[i][j] != 0), None)
        if pivot is None:
            return Fraction(0)
        if pivot != j:
            m[j], m[pivot] = m[pivot], m[j]
            out = -out
        v = m[j][j]
        out *= v
        for i in range(j + 1, n):
            if m[i][j]:
                r = m[i][j] / v
                for k in range(j + 1, n):
                    m[i][k] -= r * m[j][k]
                m[i][j] = Fraction(0)
    return out


def observability(n, a, b):
    row = [Fraction(int(j == 0)) for j in range(n)]
    out = []
    for _ in range(n):
        out.append(row)
        row = [a * row[(j - 1) % n] + b * row[(j - 2) % n]
               for j in range(n)]
    return out


def factored_product(n, a, b):
    p = a ** (n // 2 if n % 2 == 0 else 0)
    for d in range(1, (n - 1) // 2 + 1):
        p *= a**n - (-1)**(n + d) * b**n * (2*cos(pi*d/n))**n
    return p


def direct_product(n, a, b):
    zeta = exp(2j*pi/n)
    z = [zeta**j for j in range(n)]
    p = 1+0j
    for j in range(n):
        for k in range(j+1, n):
            p *= a+b*(z[j]+z[k])
    return p


def close(x, y, tol=2e-7):
    return abs(x-y) <= tol * max(abs(x), abs(y)) + 1e-12


def test():
    checks = 0
    for n in range(2, 13):
        for a in [Fraction(2, 5), Fraction(3, 5), Fraction(1, 2), Fraction(7, 10)]:
            b = 1-a
            det = determinant(observability(n, a, b))
            if a == b and n % 3 == 0:
                assert det == 0, (n, a, det)
            else:
                assert det != 0, (n, a, det)
            f = factored_product(n, float(a), float(b))
            direct = direct_product(n, float(a), float(b))
            assert close(float(det), f), ('factor', n, a, det, f)
            assert close(complex(float(det)), direct), ('direct', n, a, det, direct)
            checks += 3
    for n in range(3, 19):
        zeta = exp(2j*pi/n)
        for k in range(1, n//2+1):
            if not (n/4 < k < n/2):
                continue
            ratio = -2*cos(2*pi*k/n)
            a, b = ratio/(1+ratio), 1/(1+ratio)
            lam = [a*zeta**j+b*zeta**(2*j) for j in range(n)]
            equal_pairs = [(i,j) for i in range(n) for j in range(i+1,n)
                           if abs(lam[i]-lam[j]) < 2e-8]
            assert equal_pairs == [(k, n-k)], (n,k,equal_pairs)
            checks += 1
    for n in (3, 6, 9, 12, 15):
        zeta = exp(2j*pi/n)
        a, b = 0.49, 0.51
        i, j = n//3, 2*n//3
        li = a*zeta**i+b*zeta**(2*i)
        lj = a*zeta**j+b*zeta**(2*j)
        assert close(abs(li-lj), 3**0.5*abs(a-b))
        checks += 1
    print('VERIFIED: rational exact determinants and two product formulas through n=12;')
    print('one-double-eigenvalue resonance checks through n=18; local slope through n=15.')
    print('Individual assertions passed:', checks)


if __name__ == '__main__':
    test()

#!/usr/bin/env python3
"""Exact elementary checks for the independent enharmonic polynomial model.

Requires only Python 3 standard library. This checks examples and identities;
the proof for arbitrary m,n is mathematical, not an exhaustive test.
"""
from fractions import Fraction
from math import gcd, isqrt
from functools import reduce


def prod(xs):
    return reduce(lambda a, b: a*b, xs, 1)


def poly_mul(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return c


def row_poly(boundary, energy):
    assert len(boundary) == len(energy)
    n = len(boundary)
    c = [0] * n
    for j in range(n):
        q = [1]
        for k in range(n):
            if j != k:
                q = poly_mul(q, [-boundary[k], 1])
        for h in range(n):
            c[h] += energy[j]*q[h]
    return c  # ascending coefficient order


def evaluate(c, x):
    return sum(v*x**i for i, v in enumerate(c))


def cubic_discriminant(c):
    z, y, x, a = c
    return x*x*y*y - 4*a*y*y*y - 4*x*x*x*z - 27*a*a*z*z + 18*a*x*y*z


def divisors(n):
    n = abs(n)
    assert n >= 1
    out = set()
    for i in range(1, isqrt(n)+1):
        if n % i == 0:
            out.add(i)
            out.add(n//i)
    return sorted(out)


def has_rational_root(c):
    assert len(c) == 4 and c[0] != 0 and c[-1] != 0
    for a in divisors(c[0]):
        for b in divisors(c[-1]):
            for sign in (-1, 1):
                if evaluate(c, Fraction(sign*a, b)) == 0:
                    return True
    return False


def squarefree_part(n):
    assert n != 0
    sign = -1 if n < 0 else 1
    n = abs(n)
    r = 1
    p = 2
    while p*p <= n:
        j = 0
        while n % p == 0:
            n //= p
            j += 1
        if j % 2:
            r *= p
        p += 1
    return sign*r*n



def det(matrix):
    a = [[Fraction(v) for v in row] for row in matrix]
    n = len(a)
    result = Fraction(1)
    for k in range(n):
        pivot = next((i for i in range(k, n) if a[i][k]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != k:
            a[k], a[pivot] = a[pivot], a[k]
            result = -result
        v = a[k][k]
        result *= v
        for i in range(k+1, n):
            z = a[i][k]/v
            for j in range(k+1, n):
                a[i][j] -= z*a[k][j]
            a[i][k] = 0
    return result


def power_sums(monic):
    d = len(monic)-1
    assert monic[-1] == 1
    s = [Fraction(d)]
    for k in range(1, 2*d-1):
        v = sum(monic[d-j]*s[k-j] for j in range(1, min(k-1,d)+1))
        if k <= d:
            v += k*monic[d-k]
        s.append(-v)
    return s


def trace_matrix(c):
    c = [Fraction(x, c[-1]) for x in c]
    d = len(c)-1
    sums = power_sums(c)
    return [[sums[i+j] for j in range(d)] for i in range(d)]


def kronecker(a, b):
    return [[a[i][j]*b[u][v]
             for j in range(len(a)) for v in range(len(b))]
            for i in range(len(a)) for u in range(len(b))]

def run():
    for n in range(3, 9):
        b = list(range(n))
        for row in range(1, 5):
            e = [2*j + row + 1 for j in range(n)]
            f = row_poly(b, e)
            assert f[-1] == sum(e)
            for j in range(n):
                assert evaluate(f, b[j]) == e[j]*prod(b[j]-b[k] for k in range(n) if k != j)
    b = [0, 1, 2, 3]
    f = row_poly(b, [2, 3, 5, 7])
    g = row_poly(b, [1, 2, 3, 4])
    assert f == [-12, 69, -68, 17]
    assert g == [-6, 40, -40, 10]
    assert not has_rational_root(f)
    assert not has_rational_root(g)
    d1, d2 = cubic_discriminant(f), cubic_discriminant(g)
    assert (d1, d2) == (688908, 94800)
    assert squarefree_part(d1) == 3*11*17*307
    assert squarefree_part(d2) == 3*79
    assert squarefree_part(d1) != squarefree_part(d2)
    assert d1 > 0 and d2 > 0
    u, v = trace_matrix(f), trace_matrix(g)
    normdisc1 = Fraction(d1, f[-1]**4)
    normdisc2 = Fraction(d2, g[-1]**4)
    assert det(u) == normdisc1
    assert det(v) == normdisc2
    assert det(kronecker(u, v)) == normdisc1**3 * normdisc2**3
    print('PASS: independent interpolation tests n=3..8; exact S3 x S3 specialization')
    print('numerators:', f, g, 'discriminants:', d1, d2)


if __name__ == '__main__':
    run()

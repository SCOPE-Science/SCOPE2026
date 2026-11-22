#!/usr/bin/env python3
"""Exact arithmetic checks for a unit-restricted GCD-difference matrix theorem.
Requires Python 3 and SymPy (tested with 1.14). No network or input files.
"""
from collections import Counter
from itertools import combinations
from math import gcd
from sympy import Matrix, ZZ, primerange
from sympy.matrices.normalforms import smith_normal_form


def predicted(p):
    if p == 2:
        return [2, 6]
    s = p - 1
    return ([1] + [s] * (s - 1) + [p * s] * (s * (s - 1))
            + [p * p * s] + [2 * p * p * s] * (s - 2)
            + [6 * p * p * s * s])


def gcd_difference(p):
    units = [a for a in range(p * p) if a % p]
    q = p * p
    return Matrix([[gcd(a - b, q) for b in units] for a in units])


def minor_gcd(M, order):
    z = 0
    n = M.rows
    for rows in combinations(range(n), order):
        for cols in combinations(range(n), order):
            z = gcd(z, abs(int(M.extract(rows, cols).det())))
    return z


def check():
    checks = 0
    # Entire original integer Smith forms at three primes.
    for p in (2, 3, 5):
        M = gcd_difference(p)
        D = smith_normal_form(M, domain=ZZ)
        got = [abs(int(D[i, i])) for i in range(D.rows)]
        assert got == predicted(p), (p, got, predicted(p))
        checks += len(got)
    # Entrywise block identity for larger primes, entirely independent of the Smith formula.
    for p in (3, 5, 7, 11, 13):
        M = gcd_difference(p)
        units = [a for a in range(p * p) if a % p]
        s, c = p - 1, p * (p - 1)
        for i, a in enumerate(units):
            for j, b in enumerate(units):
                rhs = c * (i == j) + s * (a % p == b % p) + 1
                assert int(M[i, j]) == rhs
                checks += 1
    # Determinantal divisors of the reduced 2x2 and 4x4 blocks.
    for p in primerange(3, 102):
        s = p - 1
        T = Matrix([[2 * p * s, 0], [s, p * s]])
        K = Matrix([[2 * p * s, 0, 0, 0],
                    [p, 3 * p * s, 0, 0],
                    [s, 0, p * s, 0],
                    [1, 2 * s, 0, p * s]])
        assert [minor_gcd(T, j) for j in (1, 2)] == [s, 2*p*p*s*s]
        assert [minor_gcd(K, j) for j in (1, 2, 3, 4)] == [1, s, p*p*s*s, 6*p**4*s**4]
        checks += 6
    # Verify all factors are positive, ordered by divisibility, and have the right count.
    for p in primerange(2, 102):
        ds = predicted(p)
        assert len(ds) == p * (p - 1)
        assert all(a > 0 and b % a == 0 for a, b in zip(ds, ds[1:]))
        checks += 2
    print('VERIFY_OK', checks, 'exact assertions')

if __name__ == '__main__':
    check()

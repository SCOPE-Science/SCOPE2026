#!/usr/bin/env python3
"""Finite independent checks of cross-work decomposition and exact moments."""
from fractions import Fraction
from itertools import permutations, product
from math import factorial


def cross_work(a):
    n = len(a)
    return sum(abs(i - a[i]) + abs(i + 1 - a[i - 1]) for i in range(1, n))


def footrule(a):
    return sum(abs(i + 1 - a[i]) for i in range(len(a)))


def fixed_count(a):
    return sum(x == i + 1 for i, x in enumerate(a))


def decomposition(a):
    n = len(a)
    return 2 * footrule(a) + 2 * fixed_count(a) + a[-1] - a[0] - (n + 1)


def expected_cross(n):
    return Fraction((n - 1) * (2 * n - 1), 3)


def variance_sym(n):
    return Fraction(16*n**3 - 29*n*n - 229*n + 536, 90)


def covariance_sym_footrule(n):
    return Fraction((n + 1) * (8*n*n - 15*n - 32), 90)


def variance_full(n):
    return Fraction((n-1)*(6*n**3-9*n*n-79*n+176), 30*n)


def moments(maps):
    a = [cross_work(p) for p in maps]
    b = [footrule(p) for p in maps]
    count = len(a)
    mean_a = Fraction(sum(a), count)
    mean_b = Fraction(sum(b), count)
    var_a = Fraction(sum(v*v for v in a), count) - mean_a**2
    cov = Fraction(sum(x*y for x, y in zip(a, b)), count) - mean_a*mean_b
    return count, mean_a, var_a, cov


def main():
    # Every permutation for all n <= 8; all full transformations for all n <= 6.
    for n in range(2, 9):
        perms = list(permutations(range(1, n+1)))
        assert all(cross_work(p) == decomposition(p) for p in perms)
        count, mean, var, cov = moments(perms)
        assert count == factorial(n)
        assert mean == expected_cross(n), (n, mean, expected_cross(n))
        assert var == variance_sym(n), (n, var, variance_sym(n))
        assert cov == covariance_sym_footrule(n), (n, cov, covariance_sym_footrule(n))
        print('S', n, 'count', count, 'mean', str(mean), 'variance', str(var), 'covariance', str(cov))
    for n in range(2, 7):
        maps = list(product(range(1, n+1), repeat=n))
        assert all(cross_work(p) == decomposition(p) for p in maps)
        count, mean, var, _ = moments(maps)
        assert count == n**n
        assert mean == expected_cross(n)
        assert var == variance_full(n), (n, var, variance_full(n))
        print('T', n, 'count', count, 'mean', str(mean), 'variance', str(var))
    # Independent array-moment checks at larger n without factorial enumeration.
    for n in (9, 10, 20, 50, 100):
        A = [[(abs(i-1-j) if i > 1 else 0) + (abs(i+1-j) if i < n else 0)
              for j in range(1,n+1)] for i in range(1,n+1)]
        D = [[abs(i-j) for j in range(1,n+1)] for i in range(1,n+1)]
        def covariance(B, C):
            rb = [sum(row) for row in B]
            rc = [sum(row) for row in C]
            cb = [sum(B[i][j] for i in range(n)) for j in range(n)]
            cc = [sum(C[i][j] for i in range(n)) for j in range(n)]
            v = n*n*sum(B[i][j]*C[i][j] for i in range(n) for j in range(n))
            v -= n * (sum(x*y for x,y in zip(rb,rc)) + sum(x*y for x,y in zip(cb,cc)))
            v += sum(rb)*sum(rc)
            return Fraction(v,n*n*(n-1))
        assert covariance(A,A) == variance_sym(n)
        assert covariance(A,D) == covariance_sym_footrule(n)
        va = sum(a*a for row in A for a in row)
        vb = sum(sum(row)**2 for row in A)
        assert Fraction(va, n) - Fraction(vb,n*n) == variance_full(n)
    print('VERIFY_OK')

if __name__ == '__main__':
    main()

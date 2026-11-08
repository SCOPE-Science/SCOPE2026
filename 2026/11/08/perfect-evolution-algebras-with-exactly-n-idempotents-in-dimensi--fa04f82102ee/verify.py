#!/usr/bin/env python3
"""Exact checks of an explicit family of evolution-algebra structure matrices.
Uses only Python's standard library; finite-field searches complement the proof.
"""
from fractions import Fraction as Q
from itertools import product


def structure_matrix(n):
    assert n >= 2
    a = [[Q(0) for j in range(n)] for i in range(n)]
    a[0][0], a[0][1] = Q(3, 4), Q(1, 4)
    a[1][0], a[1][1] = Q(1, 4), Q(3, 4)
    for j in range(2, n):
        a[j][j] = Q(1)
        a[0][j] = Q(1, 4) * Q(3, 4) ** (j - 2)
        for i in range(2, j):
            a[i][j] = Q(1, 4) * Q(3, 4) ** (j - i - 1)
    return a


def claimed_idempotents(n):
    out = [(Q(0),) * n]
    out.append((Q(1), Q(1)) + (Q(1, 2),) * (n - 2))
    for k in range(2, n):
        out.append((Q(0),) * k + (Q(1),) + (Q(1, 2),) * (n - k - 1))
    return out


def has_idempotent_equations(a, x):
    n = len(a)
    return all(sum(a[i][j] * x[i] * x[i] for i in range(n)) == x[j]
               for j in range(n))


def rational_rank(a):
    a = [list(map(Q, row)) for row in a]
    if not a:
        return 0
    nrows, ncols = len(a), len(a[0])
    r = 0
    for col in range(ncols):
        pivot = next((i for i in range(r, nrows) if a[i][col]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        coeff = a[r][col]
        a[r] = [v / coeff for v in a[r]]
        for i in range(nrows):
            if i != r:
                factor = a[i][col]
                if factor:
                    a[i] = [u - factor * v for u, v in zip(a[i], a[r])]
        r += 1
        if r == nrows:
            break
    return r


def modp(q, p):
    return (q.numerator * pow(q.denominator, -1, p)) % p


def verify():
    tested = 0
    for n in range(2, 13):
        a = structure_matrix(n)
        pts = claimed_idempotents(n)
        assert len(pts) == len(set(pts)) == n
        assert a[0][0] * a[1][1] - a[0][1] * a[1][0] == Q(1, 2)
        assert all(a[i][j] == 0 for i in range(2, n) for j in range(i))
        assert all(a[i][i] == 1 for i in range(2, n))
        assert all(has_idempotent_equations(a, x) for x in pts)
        assert rational_rank([[z*z for z in x] for x in pts[1:]]) == n-1
        for x in pts:
            h = x[0]*x[0] / 4
            for j in range(2, n):
                assert x[j]*x[j] - x[j] + h == 0
                h = (3*h + x[j]*x[j]) / 4
        tested += 1
    finite_cases = 0
    finite_vectors = 0
    for prime in (3, 5, 7):
        for n in range(2, 6):
            a = structure_matrix(n)
            aa = [[modp(z, prime) for z in row] for row in a]
            expected = {tuple(modp(z, prime) for z in x)
                        for x in claimed_idempotents(n)}
            actual = set()
            for x in product(range(prime), repeat=n):
                finite_vectors += 1
                if all(sum(aa[i][j]*x[i]*x[i] for i in range(n)) % prime == x[j]
                       for j in range(n)):
                    actual.add(x)
            assert actual == expected, (prime, n, actual, expected)
            finite_cases += 1
    print('VERIFY_OK symbolic_dimensions=%d finite_fields_cases=%d brute_force_vectors=%d' %
          (tested, finite_cases, finite_vectors))

if __name__ == '__main__':
    verify()

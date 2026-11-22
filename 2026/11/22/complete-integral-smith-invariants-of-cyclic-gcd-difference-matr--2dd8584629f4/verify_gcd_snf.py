#!/usr/bin/env python3
"""Direct finite checks for cyclic gcd-difference matrix Smith invariants.

Standard-library checks suffice; optional SymPy adds larger Smith comparisons.
No finite run substitutes for the general proof in RESULT.md.
"""
from collections import Counter
from itertools import combinations, product
from math import gcd, prod


def prime_factors(n):
    out = []
    d = 2
    while d*d <= n:
        if n % d == 0:
            out.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        out.append(n)
    return out


def factor(n):
    out = Counter()
    d = 2
    while d*d <= n:
        while n % d == 0:
            out[d] += 1
            n //= d
        d += 1
    if n > 1:
        out[n] += 1
    return out


def matrix(n):
    return [[gcd(i-j, n) for j in range(n)] for i in range(n)]


def bareiss(M):
    """Exact determinant by integer-preserving fraction-free elimination."""
    n = len(M)
    if n == 0:
        return 1
    A = [list(row) for row in M]
    prev = 1
    sign = 1
    for k in range(n-1):
        if A[k][k] == 0:
            row = next((i for i in range(k+1, n) if A[i][k] != 0), None)
            if row is None:
                return 0
            A[k], A[row] = A[row], A[k]
            sign = -sign
        pivot = A[k][k]
        for i in range(k+1, n):
            for j in range(k+1, n):
                numerator = A[i][j]*pivot - A[i][k]*A[k][j]
                assert numerator % prev == 0
                A[i][j] = numerator // prev
            A[i][k] = 0
        prev = pivot
    return sign*A[-1][-1]


def rank_mod(A, prime):
    a = [[v % prime for v in row] for row in A]
    rows = len(a)
    cols = len(a[0])
    r = 0
    for c in range(cols):
        pivot = next((i for i in range(r, rows) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        inverse = pow(a[r][c], -1, prime)
        for j in range(c, cols):
            a[r][j] = a[r][j]*inverse % prime
        for i in range(r+1, rows):
            if a[i][c]:
                mul = a[i][c]
                for j in range(c, cols):
                    a[i][j] = (a[i][j] - mul*a[r][j]) % prime
        r += 1
        if r == rows:
            break
    return r


def predicted(n):
    pools = []
    for p in prime_factors(n):
        pools.append([1] + [p-1]*(p-2) + [(p-1)*(2*p-1)])
    raw = [prod(x) for x in product(*pools)]
    assert len(raw) == n
    primes = sorted({q for b in raw for q in factor(b)})
    valuations = {q: sorted(factor(b)[q] for b in raw) for q in primes}
    return [prod(q**valuations[q][i] for q in primes) for i in range(n)]


def exact_minors_smith(A):
    n = len(A)
    previous = 1
    factors = []
    for r in range(1, n+1):
        g = 0
        for rows in combinations(range(n), r):
            for cols in combinations(range(n), r):
                m = [[A[i][j] for j in cols] for i in rows]
                g = gcd(g, bareiss(m))
        assert g % previous == 0, (r, g, previous)
        factors.append(g//previous)
        previous = g
    return factors


def direct_predicted_rank(n, ell):
    local = []
    for p in prime_factors(n):
        if (p-1) % ell == 0:
            local.append(1)
        elif (2*p-1) % ell == 0:
            local.append(p-1)
        else:
            local.append(p)
    return prod(local)


def expected_min_generators(n):
    if n % 2:
        return n-1
    if n == 2:
        return 1
    return n-1 if all(p % 3 == 1 for p in prime_factors(n//2)) else n-2


def main():
    sizes = [2, 3, 5, 6, 7, 10, 14, 15, 21, 22, 30]
    assertions = 0
    for n in sizes:
        A = matrix(n)
        d = predicted(n)
        assert all(d[i+1] % d[i] == 0 for i in range(n-1))
        assertions += n-1
        expect_det = prod(((p-1)**(p-1)*(2*p-1))**(n//p)
                          for p in prime_factors(n))
        assert bareiss(A) == expect_det == prod(d)
        assertions += 2
        assert sum(x > 1 for x in d) == expected_min_generators(n)
        assertions += 1
        for ell in [2, 3, 5, 7, 11, 13, 17, 19, 23, 31, 37, 41, 43]:
            predicted_rank = direct_predicted_rank(n, ell)
            assert rank_mod(A, ell) == predicted_rank
            assert sum(x % ell != 0 for x in d) == predicted_rank
            assertions += 2
        if n <= 6:
            assert exact_minors_smith(A) == d
            assertions += n

    assert predicted(6) == [1, 1, 2, 6, 30, 30]
    assertions += 1
    optional = []
    try:
        from sympy import ZZ, Matrix
        from sympy.matrices.normalforms import smith_normal_form
        for n in [10, 14, 15, 21, 22]:
            S = smith_normal_form(Matrix(matrix(n)), domain=ZZ)
            vals = [abs(int(S[i, i])) for i in range(n)]
            assert vals == predicted(n), (n, vals, predicted(n))
            optional.append(n)
            assertions += n
    except ImportError:
        pass

    print('PASS', assertions, 'exact assertions; stdlib direct minors for 2,3,5,6;')
    print('direct determinants and modular ranks:', sizes)
    print('optional independent Smith forms:', optional)
    print('example G_6:', predicted(6))


if __name__ == '__main__':
    main()

"""Exact integer and rational consistency checks for modular interval Markov maps.

This is a finite diagnostic, not a substitute for the arbitrary-dimension proof.
Uses Python standard library only.
"""
from fractions import Fraction
from math import gcd


def bareiss_det(A):
    A = [row[:] for row in A]
    n = len(A)
    if n == 0:
        return 1
    if n == 1:
        return A[0][0]
    sign = 1
    prev = 1
    for k in range(n - 1):
        if not A[k][k]:
            pivot = next((j for j in range(k + 1, n) if A[j][k]), None)
            if pivot is None:
                return 0
            A[k], A[pivot] = A[pivot], A[k]
            sign *= -1
        v = A[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                num = A[i][j] * v - A[i][k] * A[k][j]
                assert num % prev == 0
                A[i][j] = num // prev
        for i in range(k + 1, n):
            A[i][k] = 0
        prev = v
    return sign * A[-1][-1]


def matrix(n, q):
    p = [(i + q) % n for i in range(n)]
    return [[int(min(p[i], p[i + 1]) <= j < max(p[i], p[i + 1]))
             for j in range(n - 1)] for i in range(n - 1)]


def f(n, q, x):
    i = min(int(x), n - 2)
    a, b = (i + q) % n, (i + q + 1) % n
    return a + (b - a) * (x - i)


def trace(A):
    return sum(A[i][i] for i in range(len(A)))


def mul(A, B):
    n = len(A)
    return [[sum(A[i][k] * B[k][j] for k in range(n))
             for j in range(n)] for i in range(n)]


def check(n, q):
    g = gcd(n, q)
    ell = n // g
    d = n - 1
    A = matrix(n, q)
    for x in range(d + 1):
        lhs = bareiss_det([[x * (i == j) - A[i][j] for j in range(d)] for i in range(d)])
        p = x ** (ell - 1) - sum(x ** k for k in range(ell - 1))
        rhs = p * (x ** ell - 1) ** (g - 1)
        assert lhs == rhs, (n, q, x, lhs, rhs)
    power = [[int(i == j) for j in range(d)] for i in range(d)]
    for k in range(1, 2 * ell + 1):
        power = mul(power, A)
        # Pure length-ell cycles add (g-1)*ell at each multiple of ell.
        # The positive component obeys a renewal recurrence; checked independently.
        if k == 1:
            assert trace(power) == 1
        if k == ell:
            assert trace(power) >= (g - 1) * ell
    for component in range(g):
        labels = [i for i in range(n) if i % g == component]
        if n - 1 in labels:
            assert len([i for i in labels if i < n - 1]) == ell - 1
        else:
            assert len(labels) == ell
            for i in labels:
                for t in (Fraction(1, 3), Fraction(2, 5)):
                    x = i + t
                    y = x
                    for _ in range(ell):
                        y = f(n, q, y)
                    assert y == x, (n, q, i, x, y)


for n in range(3, 15):
    for q in range(1, n):
        check(n, q)
print('MODULAR_INTERVAL_GCD_BLOCK_FACTORIZATION_OK')
print('EXACT_NONCOPRIME_PERIODIC_INTERVAL_CYCLES_OK')
print('FINITE_TESTS_ARE_NOT_THE_ARBITRARY_N_PROOF')

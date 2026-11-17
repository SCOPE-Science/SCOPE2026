#!/usr/bin/env python3
"""Exact finite-case diagnostics for harmonic Bergman polynomial commutators.

This finite checker is supplementary; the universal rank result is proved
mathematically and does not rely on experimental exhaustion.
"""
from fractions import Fraction
from itertools import product
from random import Random


def compress(a):
    a = list(a)
    while a and a[-1] == 0:
        a.pop()
    return a


def conv(a, b):
    r = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            r[i + j] += x * y
    return r


def derivative(a):
    return [j * a[j] for j in range(1, len(a))]


def w_degree(a, b):
    a, b = compress(a), compress(b)
    if not a or not b:
        return -1
    a[0] = b[0] = Fraction(0)
    a, b = compress(a), compress(b)
    if not a or not b:
        return -1
    w1, w2 = conv(derivative(a), b), conv(a, derivative(b))
    m = max(len(w1), len(w2))
    w = [(w1[j] if j < len(w1) else 0) -
         (w2[j] if j < len(w2) else 0) for j in range(m)]
    return len(compress(w)) - 1


def project_monomial(p, signed_n):
    # T_(z^p) acts on z^k for k>=0 and on conjugate z^n for k<0.
    if signed_n >= 0:
        return {p + signed_n: Fraction(1)}
    n = -signed_n
    if p >= n:
        return {p - n: Fraction(p - n + 1, p + 1)}
    return {p - n: Fraction(n - p + 1, n + 1)}


def apply_twice(p, q, signed_n):
    result = {}
    for index, factor in project_monomial(q, signed_n).items():
        for out_index, additional in project_monomial(p, index).items():
            result[out_index] = result.get(out_index, Fraction(0)) + factor * additional
    return result


def commutator_matrix(a, b):
    # Explicit composition T_a T_b - T_b T_a on anti-analytic inputs.
    a, b = compress(a), compress(b)
    D = (len(a) - 1) + (len(b) - 1)
    if D <= 1:
        return []
    out = [[Fraction(0) for _ in range(D - 1)] for _ in range(D - 1)]
    for n in range(1, D):
        column = {}
        for p, ap in enumerate(a):
            for q, bq in enumerate(b):
                if not ap or not bq:
                    continue
                first = apply_twice(p, q, -n)
                second = apply_twice(q, p, -n)
                for k in first.keys() | second.keys():
                    column[k] = column.get(k, Fraction(0)) + ap * bq * (
                        first.get(k, Fraction(0)) - second.get(k, Fraction(0)))
        assert all(k > 0 or value == 0 for k, value in column.items())
        for k in range(1, D):
            out[k - 1][n - 1] = column.get(k, Fraction(0))
    return out


def rank(A):
    if not A:
        return 0
    A = [row[:] for row in A]
    m, n = len(A), len(A[0]); r = 0
    for c in range(n):
        i = next((i for i in range(r, m) if A[i][c] != 0), None)
        if i is None:
            continue
        A[r], A[i] = A[i], A[r]
        pivot = A[r][c]
        for j in range(c, n):
            A[r][j] /= pivot
        for i in range(r + 1, m):
            factor = A[i][c]
            if factor:
                for j in range(c, n):
                    A[i][j] -= factor * A[r][j]
        r += 1
        if r == m:
            break
    return r


def check(a, b):
    a, b = [list(map(Fraction, arr)) for arr in (a, b)]
    w = w_degree(a, b)
    M = commutator_matrix(a, b)
    r = rank(M)
    expected = 2 * (w // 2) if w >= 0 else 0
    assert r == expected, (a, b, w, r, expected)
    for i in range(len(M)):
        for j in range(len(M)):
            assert M[i][j] / (i + 2) == -M[j][i] / (j + 2), (a, b, i, j)
    return True


def main():
    checks = 0
    base = (-1, 0, 1)
    polynomials = list(product(base, repeat=3))
    for a in polynomials:
        for b in polynomials:
            check(a, b)
            checks += 1
    rng = Random(4783)
    for deg_a in range(1, 9):
        for deg_b in range(1, 9):
            for _ in range(9):
                a = [rng.randint(-3, 3) for _ in range(deg_a)] + [rng.choice((-2, -1, 1, 2))]
                b = [rng.randint(-3, 3) for _ in range(deg_b)] + [rng.choice((-2, -1, 1, 2))]
                check(a, b)
                checks += 1
    print(f"PASS: {checks} exact polynomial-pair rank and skewness diagnostics")


if __name__ == "__main__":
    main()

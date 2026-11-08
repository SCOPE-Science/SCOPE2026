#!/usr/bin/env python3
"""Independent finite checks for terminal-chain avoidance in recursive trees.

Run with Python 3 (standard library). The infinite analytic proof is in RESULT.md.
"""
from fractions import Fraction
from itertools import product
from math import factorial, exp


def allowed(parent, r):
    n = len(parent) - 1
    children = [[] for _ in range(n + 1)]
    for v in range(2, n + 1):
        children[parent[v]].append(v)
    sizes = [0] * (n + 1)
    is_chain = [False] * (n + 1)
    for v in range(n, 0, -1):
        ch = children[v]
        if not ch:
            sizes[v] = 1
            is_chain[v] = True
        else:
            sizes[v] = 1 + sum(sizes[w] for w in ch)
            is_chain[v] = len(ch) == 1 and is_chain[ch[0]]
        if sizes[v] == r and is_chain[v]:
            return False
    return True


def enumeration(n, r):
    total = 0
    for choices in product(*(range(1, j) for j in range(2, n + 1))):
        total += allowed([0, 0, *choices], r)
    return total


def coefficient_counts(r, max_n):
    u = [Fraction(0)] * (max_n + 1)
    u[0] = Fraction(1)
    u[1] = Fraction(-1)
    for n in range(1, max_n):
        if n >= r - 1:
            u[n + 1] = u[n - r + 1] / ((n + 1) * factorial(r - 1))
    inv = [Fraction(0)] * max_n
    inv[0] = Fraction(1)
    for n in range(1, max_n):
        inv[n] = -sum(u[j] * inv[n-j] for j in range(1, n+1))
    out = {}
    for n in range(1, max_n + 1):
        count = factorial(n - 1) * inv[n - 1] - int(n == r)
        assert count.denominator == 1
        out[n] = int(count)
    return out


def test():
    checks = 0
    for r in range(2, 7):
        coeffs = coefficient_counts(r, 10)
        assert coeffs[1] == 1
        checks += 1
        for n in range(1, 10):
            count = enumeration(n, r)
            assert count == coeffs[n], (n, r, count, coeffs[n])
            assert 0 <= count <= factorial(n - 1)
            checks += 2
        if r <= 9:
            assert coeffs[r] == factorial(r-1) - 1
            checks += 1
    print('VERIFY_OK', checks, 'comparisons including exhaustive recursive trees through 9 vertices')

if __name__ == '__main__':
    test()

#!/usr/bin/env python3
"""Exact small-size checks of orientation-weighted Markov cancellation."""
from itertools import product
from math import comb
from sympy import Matrix, diag, eye, ones, symbols, expand

t = symbols('t')
for n in range(2, 10):
    qualifying = 0
    for signs in product((-1, 1), repeat=n):
        u = [0] + [int(signs[j - 1] == -1 and signs[j] == 1) for j in range(1, n)]
        v = [0] + [int(signs[j - 1] == 1 and signs[j] == -1) for j in range(1, n)]
        M = ones(n, n) - Matrix(u)*Matrix([[int(j == 0) for j in range(n)]]) - Matrix(v)*Matrix([[int(j == n - 1) for j in range(n)]])
        S = diag(*signs)*M
        A, B = sum(u), sum(v)
        a, b = u[-1], v[-1]
        e, f, ss = signs[0], signs[-1], sum(signs)
        d = 1 + (b*f-ss)*t + (e*A-f*B-ss*b*f)*t**2 + e*f*(A*b+B*a)*t**3
        coeff = [1, b*f-ss, e*A-f*B-ss*b*f, e*f*(A*b+B*a)]
        assert S.charpoly().all_coeffs() == [*coeff[:n+1], *([0]*(n-3) if n > 3 else [])]
        nil = d == 1
        pred = (ss == 0 and signs[0] == signs[-2] == signs[-1])
        assert nil == pred, (n, signs, d)
        if pred:
            qualifying += 1
            assert S**4 == Matrix.zeros(n, n)
    expected = 2*comb(n-3, n//2-3) if n >= 6 and n % 2 == 0 else 0
    assert qualifying == expected, (n, qualifying, expected)
    print(f'length {n}: all {2**n} words checked; exactly {qualifying} nilpotent cases')
print('all checks passed')

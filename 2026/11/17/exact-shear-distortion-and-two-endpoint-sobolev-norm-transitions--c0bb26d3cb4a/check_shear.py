#!/usr/bin/env python3
"""Exact finite algebra checks supplementing the analytic norm theorem."""
from fractions import Fraction
from math import comb


def column_sum(k, s, q):
    return sum(Fraction(comb(i, s)) * q ** (i - s)
               for i in range(s, k + 1))


def derivative_matrix(k, t):
    return [[Fraction(comb(i, s)) * t ** (i - s)
             if i >= s else Fraction(0)
             for s in range(k + 1)]
            for i in range(k + 1)]


checks = 0
for k in range(1, 9):
    for t in ([Fraction(j, 13) for j in range(-39, 40)]
              + [Fraction(7, 2), -Fraction(7, 2)]):
        matrix = derivative_matrix(k, t)
        q = abs(t)
        for s in range(k + 1):
            assert sum(abs(row[s]) for row in matrix) == column_sum(k, s, q)
            checks += 1
        dominant = max(column_sum(k, s, q) for s in range(k + 1))
        for j in range(k):
            lower = max(column_sum(j, s, q) for s in range(j + 1))
            assert lower < dominant if q else lower == dominant == 1
            checks += 1

for i in range(0, 601):
    q = Fraction(i, 100)
    order2 = [column_sum(2, s, q) for s in range(3)]
    assert max(order2) == (1 + 2*q if q <= 1 else 1 + q + q*q)
    checks += 1
    order3 = [column_sum(3, s, q) for s in range(4)]
    if 3*q <= 1:
        expected = 1 + 3*q
    elif q*q <= 2*q + 1:
        expected = 1 + 2*q + 3*q*q
    else:
        expected = 1 + q + q*q + q*q*q
    assert max(order3) == expected
    assert order3[1] - order3[0] == q * (1 + 2*q - q*q)
    assert order3[1] - order3[2] == q * (3*q - 1)
    checks += 3

assert column_sum(3, 1, Fraction(1, 3)) == column_sum(3, 2, Fraction(1, 3))
checks += 1
print('SHEAR_COEFFICIENT_CHECKS_OK', checks)

#!/usr/bin/env python3
"""Exact-rational finite consistency tests for a spectral-cone theorem.
These checks are finite illustrations and do not replace the analytic proof.
"""
from fractions import Fraction as F
from itertools import product


def solve(matrix, rhs):
    n = len(rhs)
    a = [[F(x) for x in row] + [F(rhs[i])] for i, row in enumerate(matrix)]
    for j in range(n):
        pivot = next(i for i in range(j, n) if a[i][j] != 0)
        a[j], a[pivot] = a[pivot], a[j]
        z = a[j][j]
        a[j] = [v / z for v in a[j]]
        for i in range(n):
            if i != j:
                z = a[i][j]
                a[i] = [x - z * y for x, y in zip(a[i], a[j])]
    return [a[i][-1] for i in range(n)]


def gram(rates, weights, d, k=1):
    def a(n):
        return sum((w * r ** abs(n) for w, r in zip(weights, rates)), F(0))

    def row(n):
        return [a(n)] + [a(n - j * k) + a(n + j * k) for j in range(1, d + 1)]

    return [row(i * k) for i in range(d + 1)], row


def check():
    assertions = 0
    supports = [
        ((F(1, 4), F(3, 4)), (F(1, 2), F(1, 2))),
        ((F(1, 3), F(4, 5)), (F(2, 5), F(3, 5))),
        ((F(1, 9), F(1, 2), F(7, 8)), (F(1, 6), F(1, 3), F(1, 2))),
        ((F(1, 5), F(2, 5), F(3, 5), F(4, 5)), (F(1, 10), F(1, 5), F(3, 10), F(2, 5))),
    ]
    for rates, weights in supports:
        for d in range(2, 7):
            for k in range(1, 5):
                M, row = gram(rates, weights, d, k)
                for j in range(d + 1):
                    knots = [F(i == j) for i in range(d + 1)]
                    c = solve(M, knots)
                    for n in range(d + 1):
                        assert sum((x*y for x, y in zip(row(n*k), c)), F(0)) == knots[n]
                        assertions += 1
                    for n in range(0, (d + 9) * k):
                        if n in [i * k for i in range(d + 1)]:
                            continue
                        value = sum((x*y for x, y in zip(row(n), c)), F(0))
                        assert value > 0, (rates, weights, d, k, j, n, value)
                        assertions += 1
                for knot_pattern in product((F(0), F(1)), repeat=min(d + 1, 4)):
                    knots = list(knot_pattern) + [F(0)] * max(0, d + 1 - len(knot_pattern))
                    if not any(knots):
                        continue
                    c = solve(M, knots)
                    for n in range(d*k + 1, (d + 3) * k + 1):
                        assert sum((x*y for x, y in zip(row(n), c)), F(0)) > 0
                        assertions += 1
    M, row = gram((F(1, 4), F(3, 4)), (F(1, 2), F(1, 2)), 2)
    c = solve(M, (F(1), F(0), F(0)))
    assert c == [F(317, 195), F(-112, 195), F(-16, 195)]
    assertions += 1
    assert sum((x*y for x, y in zip(row(3), c)), F(0)) == F(1, 30)
    assertions += 1
    assert sum((x*y for x, y in zip(row(4), c)), F(0)) == F(1, 30)
    assertions += 1
    for d in range(2, 8):
        M, row = gram((F(1, 4),), (F(1),), d)
        for j in range(d):
            c = solve(M, [F(i == j) for i in range(d + 1)])
            for n in range(d + 1, d + 15):
                assert sum((x*y for x, y in zip(row(n), c)), F(0)) == 0
                assertions += 1
    print(f"PASS: {assertions} exact-rational consistency assertions")

if __name__ == '__main__':
    check()

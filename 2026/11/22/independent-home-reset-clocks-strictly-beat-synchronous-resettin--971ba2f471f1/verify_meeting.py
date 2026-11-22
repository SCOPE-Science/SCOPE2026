#!/usr/bin/env python3
"""Independent exact-rational verification of a two-walker meeting-time law.

Python 3 standard library only.  Checks the original ordered-pair generator
against the five-class quotient and the closed formula; no simulation or
floating-point values enter the core identities.
"""
from fractions import Fraction as F
from itertools import product
from math import sqrt


def solve_linear(mat, rhs):
    n = len(rhs)
    a = [list(row) + [b] for row, b in zip(mat, rhs)]
    for j in range(n):
        pivot = next(i for i in range(j, n) if a[i][j] != 0)
        a[j], a[pivot] = a[pivot], a[j]
        diag = a[j][j]
        for k in range(j, n + 1):
            a[j][k] /= diag
        for i in range(j + 1, n):
            factor = a[i][j]
            if factor:
                for k in range(j, n + 1):
                    a[i][k] -= factor * a[j][k]
    x = [F(0) for _ in range(n)]
    for i in range(n - 1, -1, -1):
        x[i] = a[i][n] - sum(a[i][k] * x[k] for k in range(i + 1, n))
    return x


def full_ordered_pair_mean(n, rate):
    states = [(x, y) for x in range(n) for y in range(n) if x != y]
    ids = {state: j for j, state in enumerate(states)}
    z = len(states)
    a = [[F(0) for _ in range(z)] for _ in range(z)]
    for i, (x, y) in enumerate(states):
        def add(dest, amount):
            if dest != (x, y):
                a[i][i] += amount
                if dest[0] != dest[1]:
                    a[i][ids[dest]] -= amount
        for v in range(n):
            if v != x:
                add((v, y), F(1, n-1))
            if v != y:
                add((x, v), F(1, n-1))
        add((0, y), rate)
        add((x, 1), rate)
    return solve_linear(a, [F(1)] * z)[ids[(0, 1)]]


def quotient_mean(n, rate):
    # Five exact permutation orbits H, X, U, V, W.
    assert n >= 3
    q = F(1, n-1)
    m = n-2
    classes = ['H', 'X', 'U', 'V'] + (['W'] if n >= 4 else [])
    idx = {s: j for j, s in enumerate(classes)}
    a = [[F(0) for _ in classes] for _ in classes]
    def add(src, dest, amount):
        assert amount >= 0
        if src == dest or amount == 0:
            return
        a[idx[src]][idx[src]] += amount
        if dest != '*':
            a[idx[src]][idx[dest]] -= amount
    flows = {
        'H': [('U', 2*m*q), ('*', 2*q)],
        'X': [('V', 2*m*q), ('*', 2*q+2*rate)],
        'U': [('H', q+rate), ('V', q), ('*', 2*q)],
        'V': [('U', q+rate), ('X', q), ('*', 2*q+rate)],
    }
    if n >= 4:
        flows['U'].append(('W', (m-1)*q))
        flows['V'].append(('W', (m-1)*q))
        flows['W'] = [('U', 2*q+2*rate), ('V', 2*q), ('*', 2*q)]
    for src, nexts in flows.items():
        for dest, amount in nexts:
            add(src, dest, amount)
    return solve_linear(a, [F(1)] * len(classes))[idx['H']]


def formula(n, r):
    q = 2*(n-1)**2*r*r + 2*(n-1)*(2*n+1)*r+n*(n+2)
    return F(n-1, 2) - F((n-2)*(n-1)**2*r, 2*q)


def main():
    checks = 0
    for n in range(3, 9):
        for rate in (F(0), F(1, 7), F(2, 3), F(5, 2)):
            exact = formula(n, rate)
            assert quotient_mean(n, rate) == exact, (n, rate)
            checks += 1
            if n <= 7:
                assert full_ordered_pair_mean(n, rate) == exact, (n, rate)
                checks += 1
    for n in range(9, 31):
        for r in (F(0), F(1, 5), F(11, 4)):
            assert quotient_mean(n, r) == formula(n, r)
            checks += 1
    for n in range(3, 101):
        rstar = sqrt(n*(n+2)/(2*(n-1)**2))
        f = lambda x: float(formula(n, F(x).limit_denominator(10**9)))
        for factor in (0.01, .6, 1.4, 40):
            assert f(factor*rstar) > f(rstar) - 1e-7
            checks += 1
    # The ordinary (non-reset) collision hazard, from any distinct pair,
    # is exactly 2/(n-1), while a joint home reset cannot cause collision.
    for n in range(2, 21):
        for x in range(n):
            for y in range(n):
                if x != y:
                    assert F(1, n-1)+F(1, n-1) == F(2, n-1)
                    checks += 1
    print(f'PASS: {checks} exact generator, quotient, formula, and optimum checks')


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""Finite exact consistency checks for rank-two three-block Grassmann charts.
Run: python check_charts.py
The uniform theorem follows from the written symbolic chart proof, not from this finite check.
"""
from itertools import combinations
from math import comb
from sympy import Matrix, symbols, simplify, binomial


def chart_check(a, b, c):
    X = symbols('x0:' + str(a - 1)) if a > 1 else ()
    Y = symbols('y0:' + str(b - 1)) if b > 1 else ()
    U = symbols('u0:' + str(c))
    V = symbols('v0:' + str(c))
    A = [(1, 0)] + [(x, 0) for x in X]
    B = [(0, 1)] + [(0, y) for y in Y]
    C = list(zip(U, V))
    columns = A + B + C
    # The Grassmann chart has exactly the same-block Pluecker minors.
    for block in (A, B):
        for i, j in combinations(block, 2):
            assert simplify(i[0] * j[1] - i[1] * j[0]) == 0
    minors = []
    for i, j in combinations(range(c), 2):
        minor = U[i] * V[j] - U[j] * V[i]
        minors.append(minor)
        assert simplify(C[i][0] * C[j][1] - C[i][1] * C[j][0] - minor) == 0
    # A cross-block pair has at least one Pluecker coordinate equal to 1.
    assert columns[0][0] * columns[a][1] - columns[0][1] * columns[a][0] == 1
    if c >= 2:
        vars_ = list(U) + list(V)
        J = Matrix([[expr.diff(t) for t in vars_] for expr in minors])
        origin = {x: 0 for x in vars_}
        rank_one = origin.copy()
        rank_one[U[0]] = 1
        assert J.subs(origin).rank() == 0
        assert J.subs(rank_one).rank() == c - 1
        # In a nonzero rank-one chart, the cone has dimension c+1.
        assert len(vars_) - J.subs(rank_one).rank() == c + 1
    for d in range(10):
        # The Segre ring R has dimension R_d=(d+1)*binomial(d+c-1,c-1).
        # Series (1+(c-1)t)/(1-t)^(c+1).
        lhs = (d + 1) * comb(d + c - 1, c - 1)
        rhs = comb(d + c, c)
        if d >= 1:
            rhs += (c - 1) * comb(d + c - 1, c)
        assert lhs == rhs, (a, b, c, d, lhs, rhs)
    return (a, b, c)

if __name__ == '__main__':
    cases = [chart_check(a, b, c) for a in (1, 2, 3) for b in (1, 2) for c in (1, 2, 3, 4, 5)]
    print('EXACT_CHART_AND_JACOBIAN_CHECK_OK', len(cases))
    print('SEGRE_HILBERT_SERIES_AND_MULTIPLICITY_CHECK_OK')
    print('CHECK_OK')

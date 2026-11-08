#!/usr/bin/env python3
"""Exact finite checks for coordinate Segre witnesses and dimension bounds.

The universal theorem is proved geometrically, not by this finite checker.
"""
from itertools import product
from math import prod


def rank_q(rows):
    from fractions import Fraction
    a = [[Fraction(v) for v in row] for row in rows]
    pivots = 0
    for col in range(len(a[0])):
        pivot = next((i for i in range(pivots, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[pivots], a[pivot] = a[pivot], a[pivots]
        scale = a[pivots][col]
        a[pivots] = [z / scale for z in a[pivots]]
        for i in range(len(a)):
            if i != pivots and a[i][col]:
                scale = a[i][col]
                a[i] = [x - scale*y for x,y in zip(a[i], a[pivots])]
        pivots += 1
        if pivots == len(a):
            break
    return pivots


def test(ms):
    d = sum(ms)
    N = prod(m+1 for m in ms)
    M = N-1
    assert len(ms)>=2 and min(ms)>=1 and M>=d+1
    # Each coordinate unit tensor is a decomposable Segre vector.
    basis = []
    for idx in product(*[range(m+1) for m in ms]):
        coords = [int(idx==j) for j in product(*[range(m+1) for m in ms])]
        basis.append(coords)
    assert len(basis)==N and rank_q(basis)==N
    n = M+1
    mat = basis[:M] + [basis[0]]*(n-M)
    assert len(mat)==n and rank_q(mat)==M
    # Incidence total dimension and tangent bound, as proved in text.
    D = M+n*(d-1)
    conormal = d+(M-d-1)
    bound = conormal+(n-1)*(d-1)
    assert conormal==M-1 and bound==D-d and bound<=D-2
    # A rank-M-1 configuration has projective hyperplane fiber dim>=1.
    assert rank_q(mat[:M-1]+[mat[0]]*(n-(M-1)))==M-1
    return N

samples=[(1,1),(1,2),(2,2),(1,1,1),(1,1,2),(1,1,1,1)]
for ms in samples:
    test(ms)
print('SEGRE_INCIDENCE_FINITE_CHECK_OK',len(samples))

#!/usr/bin/env python3
"""Exact rational checks for the three-cube single-edge controllability theorem.

Requires only the Python standard library. Finite tests are supplementary to
an analytic theorem; they do not certify its universal parameter quantifier.
"""
from fractions import Fraction as F
from itertools import combinations
from collections import Counter

VERTICES = tuple(range(8))
EDGES = [(u, u ^ (1 << bit)) for u in VERTICES for bit in range(3)
         if u < (u ^ (1 << bit))]
assert len(EDGES) == 12 and (0, 1) in EDGES

def laplacian(t):
    a = [[F(0) for _ in VERTICES] for _ in VERTICES]
    for u, v in EDGES:
        w = t if (u, v) == (0, 1) else F(1)
        a[u][u] += w
        a[v][v] += w
        a[u][v] -= w
        a[v][u] -= w
    return a

def product(a, x):
    return [sum(a[i][j] * x[j] for j in VERTICES) for i in VERTICES]

def rational_rank(a):
    a = [row[:] for row in a]
    m, n = len(a), len(a[0])
    rank = 0
    for col in range(n):
        pivot = next((i for i in range(rank, m) if a[i][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        lead = a[rank][col]
        for j in range(col, n):
            a[rank][j] /= lead
        for i in range(rank+1, m):
            factor = a[i][col]
            if factor:
                for j in range(col, n):
                    a[i][j] -= factor*a[rank][j]
        rank += 1
        if rank == m:
            break
    return rank

def kalman_rank(l, sites):
    cols = []
    active = [[F(int(v == site)) for v in VERTICES] for site in sites]
    for _ in VERTICES:
        cols += active
        active = [product(l, c) for c in active]
    return rational_rank([list(row) for row in zip(*cols)])

def color(v):
    return ((v >> 1) & 1) ^ ((v >> 2) & 1)

def test():
    pair_count = 0
    for t in [F(1, 7), F(1, 4), F(1, 2), F(2, 3), F(3, 2),
              F(2), F(3), F(7), F(11)]:
        l = laplacian(t)
        ranks = Counter()
        for u, v in combinations(VERTICES, 2):
            rank = kalman_rank(l, (u, v))
            ranks[rank] += 1
            assert (rank == 8) == (color(u) != color(v)), (t, u, v, rank)
            pair_count += 1
        assert ranks == {8: 16, 7: 4, 6: 8}, (t, ranks)
    uniform = laplacian(F(1))
    assert all(kalman_rank(uniform, pair) < 8 for pair in combinations(VERTICES, 2))
    assert kalman_rank(uniform, (0, 1, 2)) == 8
    print('PASS: %d exact-rational defect-pair ranks at 9 conductances' % pair_count)
    print('PASS: t=1 has no full-rank pair and has a full-rank triple')
    print('Note: all-parameter claim is proved analytically in RESULT.md.')

if __name__ == '__main__':
    test()

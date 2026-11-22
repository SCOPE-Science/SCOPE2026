#!/usr/bin/env python3
"""Independent exact linear-system solution and screening converse checks."""
from fractions import Fraction as F
from itertools import combinations
from math import comb


def solve(A, y):
    n = len(A)
    mat = [list(map(F, row)) + [F(y[i])] for i, row in enumerate(A)]
    for j in range(n):
        p = next(k for k in range(j, n) if mat[k][j])
        mat[j], mat[p] = mat[p], mat[j]
        t = mat[j][j]
        mat[j] = [v/t for v in mat[j]]
        for i in range(n):
            if i != j and mat[i][j]:
                q = mat[i][j]
                mat[i] = [x-q*z for x, z in zip(mat[i], mat[j])]
    return [row[-1] for row in mat]


def trial(n, k, weights, a, b, twin):
    states = [sum(1 << v for v in x) for x in combinations(range(n), k)]
    index = {s:i for i, s in enumerate(states)}
    t = len(states)
    A = [[F(0) for _ in states] for _ in states]
    for x in states:
        i = index[x]
        for u, v, w in weights + [(0, 1, None)]:
            if (x >> u & 1) == (x >> v & 1):
                continue
            rate = (F(a) if (x >> u & 1) else F(b)) if w is None else F(w)
            j = index[x ^ (1 << u) ^ (1 << v)]
            A[j][i] += rate
            A[i][i] -= rate
    A[-1] = [F(1) for _ in states]
    pi = solve(A, [0]*(t-1)+[1])
    assert min(pi) > 0 and sum(pi) == 1
    density = [sum(pi[i] * (s >> v & 1) for i, s in enumerate(states))
               for v in range(n)]
    flat = all(density[v] == F(k, n) for v in range(2, n))
    assert flat == twin, (density, twin)
    if twin:
        s = sum((F(w) for u,v,w in weights if u == 0), F(0))
        d = (F(b)-F(a))/(s+F(a)+F(b))
        formula = [(1+d*((state&1)-((state>>1)&1)))/comb(n,k)
                   for state in states]
        assert pi == formula
    return density

if __name__ == '__main__':
    twin_edges = [(0,2,F(2,3)), (1,2,F(2,3)),
                  (0,3,F(5,4)), (1,3,F(5,4)),
                  (2,4,F(3,2)), (4,5,2), (5,3,3)]
    non_twin_edges = [(0,2,F(2,3)), (1,2,F(2,3)),
                      (0,3,F(5,4)), (1,3,F(6,4)),
                      (2,4,F(3,2)), (4,5,2), (5,3,3)]
    total = 0
    for k in [1,2,3,4,5]:
        for ed, twin in [(twin_edges, True),(non_twin_edges,False)]:
            trial(6,k,ed,F(5,3),F(1,4),twin)
            total += 1
    print('PASS: independent rational stationary solve for 10 instances,')
    print('twin iff external means are equilibrium, with exact law when twin')

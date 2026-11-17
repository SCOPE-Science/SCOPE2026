#!/usr/bin/env python3
"""Exact, standalone finite checks for the three-angle ridge-spectrum theorem.
Requires Python 3 standard library only. No external data files.
Checks all labelled bipartite graphs with fixed shores p <= q and p+q <= 5,
with no isolated vertices, and a deterministic subset at 6 vertices.
Finite checks are illustrative, not a substitute for the all-graph proof.
"""
from itertools import combinations
from fractions import Fraction
from math import comb


def affine_rank(vertices, n):
    if not vertices:
        return -1
    matrix = [[Fraction(v[k] - vertices[0][k]) for k in range(n)]
              for v in vertices[1:]]
    pivot = 0
    for col in range(n):
        j = next((t for t in range(pivot, len(matrix))
                  if matrix[t][col]), None)
        if j is None:
            continue
        matrix[pivot], matrix[j] = matrix[j], matrix[pivot]
        a = matrix[pivot][col]
        matrix[pivot] = [z / a for z in matrix[pivot]]
        for i in range(pivot + 1, len(matrix)):
            a = matrix[i][col]
            if a:
                matrix[i] = [x - a*y for x, y in zip(matrix[i], matrix[pivot])]
        pivot += 1
        if pivot == len(matrix):
            break
    return pivot


def analyze(p, q, edge_mask):
    n = p + q
    possibles = [(i, p+j) for i in range(p) for j in range(q)]
    edges = [e for k, e in enumerate(possibles) if edge_mask >> k & 1]
    m = len(edges)
    degrees = [sum(i in e for e in edges) for i in range(n)]
    if min(degrees) == 0:
        return False
    vlist = [tuple(s >> i & 1 for i in range(n)) for s in range(1 << n)
             if all(not (s >> u & 1 and s >> v & 1) for u, v in edges)]
    facets = [[v for v in vlist if v[i] == 0] for i in range(n)]
    facets += [[v for v in vlist if v[u] + v[w] == 1] for u, w in edges]
    assert all(affine_rank(f, n) == n-1 for f in facets), (p, q, edges)
    angles = {'right': 0, 'acute45': 0, 'obtuse120': 0}
    for i, j in combinations(range(n + m), 2):
        s = set(facets[i]) & set(facets[j])
        if affine_rank(list(s), n) != n - 2:
            continue
        if i < n and j < n:
            typ = 'right'
        elif i < n:
            typ = 'acute45' if i in edges[j-n] else 'right'
        else:
            typ = 'obtuse120' if set(edges[i-n]) & set(edges[j-n]) else 'right'
        angles[typ] += 1
    leaves = sum(deg == 1 for deg in degrees)
    wedges = sum(comb(deg, 2) for deg in degrees)
    edge_set = {tuple(e) for e in edges}
    fourcycles = sum(all((a, b) in edge_set for a in (i, j) for b in (u, v))
                     for i, j in combinations(range(p), 2)
                     for u, v in combinations(range(p, n), 2))
    expected_right = comb(n+m, 2)-2*m-2*fourcycles-wedges
    assert angles == {'right': expected_right, 'acute45': leaves,
                      'obtuse120': wedges}, (p, q, edges, angles)
    return True


def main():
    tested = 0
    for n in range(2, 7):
        for p in range(1, n//2 + 1):
            q = n-p
            for mask in range(1, 1 << (p*q)):
                # All possible cases through 5 vertices; deterministic subset at 6,
                # including stars, complete bicliques and selected mixed graphs.
                if n == 6 and mask not in (1, (1 << (p*q))-1) and mask % 7:
                    continue
                tested += bool(analyze(p, q, mask))
    print('BIPARTITE_RIDGE_SPECTRUM_EXACT_PASS graphs=' + str(tested))


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""Finite checks for 3,2-geodesic domination of rank-two Kneser graphs.
Run: python3 verify.py (Python 3.9+ standard library).
This is a finite corroboration, not an infinite-family proof.
"""
from itertools import combinations
from math import comb, factorial

def check(n):
    vertices = list(combinations(range(n), 2))
    size = len(vertices)
    adj = [[not (set(u) & set(v)) for v in vertices] for u in vertices]
    triple_pairs = {}
    geodesics = 0
    for a, b, c in combinations(range(size), 3):
        if ((adj[a][b] and adj[b][c] and not adj[a][c])
            or (adj[a][c] and adj[c][b] and not adj[a][b])
            or (adj[b][a] and adj[a][c] and not adj[b][c])):
            geodesics += 1
            for i, j, k in ((a, b, c), (a, c, b), (b, c, a)):
                triple_pairs[i, j] = triple_pairs.get((i, j), 0) | (1 << k)
    mask_all = (1 << size) - 1
    def dominates(indices):
        seen = sum(1 << i for i in indices)
        for i, j in combinations(indices, 2):
            seen |= triple_pairs.get((i, j), 0)
        return seen == mask_all
    counts = {}
    for k in (2, 3):
        candidates = [s for s in combinations(range(size), k) if dominates(s)]
        counts[k] = len(candidates)
        if k == 3:
            expected = 0 if n not in (6, 7) else factorial(n) // (factorial(n-6) * (2**3) * factorial(3))
            assert len(candidates) == expected, (n, len(candidates), expected)
            assert all(all(adj[x][y] for x, y in combinations(s, 2)) for s in candidates)
    witness = ((0, 1), (0, 2), (1, 2), (3, 4))
    inds = tuple(vertices.index(e) for e in witness)
    assert dominates(inds)
    if n in (5, 8, 9, 10):
        count4 = sum(dominates(s) for s in combinations(range(size), 4))
        counts[4] = count4
        assert count4 > 0
    target = 3 if n in (6, 7) else 4
    assert counts[2] == 0 and ((counts[3] > 0) == (target == 3))
    print('CHECK_OK', 'n', n, 'geodesics', geodesics, 'min', target, 'size2', counts[2], 'size3', counts[3], 'size4', counts.get(4, 'witness'))

for n in range(5, 11):
    check(n)
print('VERIFY_OK')

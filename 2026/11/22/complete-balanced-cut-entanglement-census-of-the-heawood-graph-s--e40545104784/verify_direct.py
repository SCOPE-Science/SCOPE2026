#!/usr/bin/env python3
"""Exact cut-rank census for a 14-qubit Heawood graph state.
No external dependencies. Execute with python3 verify_direct.py.
"""
from itertools import combinations
from collections import Counter
from fractions import Fraction

VERTICES = tuple(range(14))
P = range(1, 8)
# The Heawood graph is the Fano plane's point-line incidence graph.
ADJ = [[0] * 14 for _ in VERTICES]
for p in P:
    for l in P:
        if ((p & l).bit_count() % 2) == 0:
            ADJ[p-1][l+6] = ADJ[l+6][p-1] = 1

assert all(sum(row) == 3 for row in ADJ)
assert sum(sum(row) for row in ADJ) == 42
assert all(ADJ[u][v] == ADJ[v][u] for u in VERTICES for v in VERTICES)

def binary_rank(row_masks):
    pivots = {}
    for mask in row_masks:
        t = mask
        while t:
            pivot = (t & -t).bit_length() - 1
            if pivot in pivots:
                t ^= pivots[pivot]
            else:
                pivots[pivot] = t
                break
    return len(pivots)

def entropy_for_cut(cut):
    B = tuple(v for v in VERTICES if v not in cut)
    rows = [sum((1 << j) for j, b in enumerate(B) if ADJ[a][b]) for a in cut]
    return binary_rank(rows)

counts = Counter()
composition = Counter()
edge_profiles = Counter()
representatives = {}
for cut in combinations(VERTICES, 7):
    k = entropy_for_cut(cut)
    counts[k] += 1
    composition[(sum(v < 7 for v in cut), k)] += 1
    other = set(VERTICES) - set(cut)
    crossing_edges = sum(ADJ[u][v] for u in cut for v in other)
    edge_profiles[(k, crossing_edges)] += 1
    representatives.setdefault(k, cut)

assert counts == {4:100, 5:980, 6:1680, 7:672}, counts
assert sum(counts.values()) == 3432
assert entropy_for_cut(tuple(range(7))) == 4
assert Fraction(sum(k*n for k,n in counts.items()), 3432) == Fraction(5021,858)
assert Fraction(counts[7],3432) == Fraction(28,143)
assert Fraction(counts[4],3432) == Fraction(25,858)
assert {e: n for (k,e),n in edge_profiles.items() if k == 7} == {11:336, 13:336}
assert edge_profiles[(4, 21)] == 2  # The two oriented point-versus-line cuts.
assert sorted(set(composition)) == sorted([(a,k) for a in range(8) for k in range(4,8) if composition[a,k]])
print('DIRECT_OK histogram='+str(sorted(counts.items())))
print('DIRECT_RANK7_EDGES='+str(sorted((e,n) for (r,e),n in edge_profiles.items() if r==7)))
print('DIRECT_BY_POINTS='+str(sorted(composition.items())))
print('DIRECT_EXAMPLES='+str(representatives))

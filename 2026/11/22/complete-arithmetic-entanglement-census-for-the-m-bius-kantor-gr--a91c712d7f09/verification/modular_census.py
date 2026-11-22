#!/usr/bin/env python3
"""Independent exact finite-field census from the (8_3) point-triple incidence model.
Run: python verification/modular_census.py ; Python 3.9+, standard library only.
"""
from collections import Counter
from itertools import combinations

# Eight points P_i and eight triples L_j={P_j,P_(j+1),P_(j+3)}, mod 8.
# Labels 0..7 are points, 8..15 are triples.
incidence_edges = {
    tuple(sorted((8 + j, (j + d) % 8)))
    for j in range(8) for d in (0, 1, 3)
}
assert len(incidence_edges) == 24

# Explicit graph isomorphism from GP(8,3) vertex labels to incidence labels.
# This is independent of the Smith-normal-form enumeration.
phi = (0, 15, 2, 9, 4, 11, 6, 13, 8, 7, 10, 1, 12, 3, 14, 5)
gp = set()
for i in range(8):
    for a, b in ((i, (i + 1) % 8), (i, 8+i), (8+i, 8+(i+3)%8)):
        gp.add(tuple(sorted((phi[a], phi[b]))))
assert gp == incidence_edges

def modular_rank(matrix, prime):
    rows = [[x % prime for x in row] for row in matrix]
    pivot = 0
    for col in range(len(rows[0])):
        found = next((i for i in range(pivot, len(rows))
                      if rows[i][col]), None)
        if found is None:
            continue
        rows[pivot], rows[found] = rows[found], rows[pivot]
        inverse = pow(rows[pivot][col], -1, prime)
        rows[pivot] = [(inverse*x) % prime for x in rows[pivot]]
        for i in range(len(rows)):
            if i != pivot and rows[i][col]:
                scalar = rows[i][col]
                rows[i] = [(x - scalar*y) % prime
                           for x, y in zip(rows[i], rows[pivot])]
        pivot += 1
        if pivot == len(rows):
            break
    return pivot

EXPECTED = {
    2: {5:124, 6:1923, 7:3056, 8:1332},
    3: {5:189, 6:1851, 7:2892, 8:1503},
    5: {5:124, 6:1539, 7:2888, 8:1884},
    7: {5:124, 6:1539, 7:2888, 8:1884},
}
counts = {p: Counter() for p in EXPECTED}
triple_drops = []
for chosen in combinations(range(1, 16), 7):
    left = (0,) + chosen
    remaining = tuple(i for i in range(16) if i not in left)
    block = [[int(tuple(sorted((i, j))) in incidence_edges)
              for j in remaining] for i in left]
    ranks = {p:modular_rank(block, p) for p in EXPECTED}
    for p, r in ranks.items():
        counts[p][r] += 1
    if ranks[5] - ranks[3] >= 3:
        triple_drops.append((left, ranks))
assert all(counts[p] == Counter(EXPECTED[p]) for p in EXPECTED)
assert len(triple_drops) == 1
assert triple_drops[0][0] == tuple(range(8))
assert triple_drops[0][1] == {2:8, 3:5, 5:8, 7:8}
for p in sorted(counts):
    print('prime', p, 'rank counts', sorted(counts[p].items()))
print('PASS: independent 6435-cut modular census; unique point/line qutrit triple drop')

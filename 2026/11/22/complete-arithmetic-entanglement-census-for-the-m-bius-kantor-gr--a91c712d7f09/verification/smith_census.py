#!/usr/bin/env python3
"""Exhaustive integral Schmidt-cut certificate for the 16-vertex Mobius-Kantor graph.
Run: python verification/smith_census.py ; requires sympy >=1.10.
"""
from collections import Counter
from itertools import combinations
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form

N = 8
edges = set()
for i in range(N):
    for a, b in ((i, (i + 1) % N), (i, i + N),
                 (N + i, N + (i + 3) % N)):
        edges.add(tuple(sorted((a, b))))
assert len(edges) == 24

# key=(number of nonzero integral invariants, tuple of nonunit invariants)
EXPECTED = {
    (7, ()): 2232,
    (6, ()): 1491,
    (8, ()): 999,
    (8, (2,)): 432,
    (7, (3,)): 328,
    (7, (2,)): 312,
    (8, (3,)): 300,
    (5, ()): 124,
    (6, (3,)): 48,
    (8, (2, 2)): 48,
    (8, (6,)): 48,
    (8, (3, 3)): 32,
    (8, (2, 4)): 24,
    (7, (3, 3)): 16,
    (8, (3, 3, 3)): 1,
}

observed = Counter()
unique_triplet = []
for chosen in combinations(range(1, 16), 7):
    left = (0,) + chosen  # one representative from each complement pair
    right = tuple(i for i in range(16) if i not in left)
    A = Matrix([[int(tuple(sorted((i, j))) in edges) for j in right]
                for i in left])
    S = smith_normal_form(A, domain=ZZ)
    invariants = [abs(int(S[i, i])) for i in range(8) if S[i, i] != 0]
    assert all(invariants[j+1] % invariants[j] == 0
               for j in range(len(invariants)-1))
    key = (len(invariants), tuple(x for x in invariants if x != 1))
    observed[key] += 1
    if key == (8, (3, 3, 3)):
        unique_triplet.append(left)
assert observed == Counter(EXPECTED), (observed-EXPECTED, EXPECTED-observed)
assert sum(observed.values()) == 6435
assert len(unique_triplet) == 1
assert unique_triplet[0] == (0, 2, 4, 6, 9, 11, 13, 15)
for (rank, factors), count in sorted(observed.items(),
                                    key=lambda entry: (-entry[1], entry[0])):
    print('rank', rank, 'nonunit', factors, 'multiplicity', count)
print('PASS: 6435 balanced cuts, 15 integral classes; unique three-factor cut')

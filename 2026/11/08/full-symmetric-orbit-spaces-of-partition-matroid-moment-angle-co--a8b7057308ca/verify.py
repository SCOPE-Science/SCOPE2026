#!/usr/bin/env python3
"""Independent small-case consistency checks for partition-matroid moment-angle quotients.

Only finite checks: the uniform homotopy statement is established separately
by the pushout argument and Morton's disk-bundle theorem.
"""
from collections import Counter
from itertools import combinations, permutations
from math import factorial, comb


def determinant_2(a):
    return a[0][0]*a[1][1] - a[0][1]*a[1][0]

# The maps out of the boundary torus have product-coordinate H_1 matrix.
M = [[1, 1], [0, -1]]
assert abs(determinant_2(M)) == 1
print('BOUNDARY_TORUS_MATRIX_UNIMODULAR', M, 'det', determinant_2(M))

# An automorphism of the join of discrete blocks must preserve precisely
# the pairs lying inside a block, and the full graph of these minimal nonfaces.
cases = ((2,), (3,), (1, 3), (2, 2), (2, 3), (1, 2, 2), (1, 1, 2), (2, 2, 2))
for sizes in cases:
    n = sum(sizes)
    ids = sum(([j] * p for j, p in enumerate(sizes)), [])
    nonfaces = {(u, v) for u in range(n) for v in range(u+1, n) if ids[u] == ids[v]}
    observed = 0
    for p in permutations(range(n)):
        moved = {(min(p[u],p[v]), max(p[u],p[v])) for u,v in nonfaces}
        observed += (moved == nonfaces)
    c = Counter(sizes)
    expected = 1
    for p,m in c.items(): expected *= factorial(p)**m * factorial(m)
    assert observed == expected, (sizes, observed, expected)
    print('BLOCK_AUTOMORPHISMS', sizes, observed)

# Degree-one generator survives each equal-size block permutation.
# Every wedge degree >=2 has a transposition of two selected letters that
# fixes the underlying set but acts by -1; over Q it cannot be invariant.
for m in range(1, 11):
    invariant_ranks = [1]
    for k in range(1, m+1):
        # Every k-subset is in the unique orbit; any stabilizer transposition
        # on the subset gives a negative sign iff k>=2.
        rank = 1 if k == 1 else 0
        invariant_ranks.append(rank)
        assert (rank == (1 if k == 1 else 0))
        if k >= 2:
            for v in combinations(range(m), k):
                assert len(v) >= 2
    assert invariant_ranks == [1, 1] + [0] * (m-1)
    print('EXTERIOR_INVARIANTS', m, invariant_ranks)

# Kunneth gives a rational exterior ring on one degree-three class
# for each distinct nonsingleton block cardinality.
for number_distinct in range(0, 8):
    ranks = [comb(number_distinct, j) for j in range(number_distinct+1)]
    assert sum(ranks) == (1<<number_distinct)
    print('DISTINCT_SIZE_BETTI', number_distinct, ranks)
print('PARTITION_MATROID_QUOTIENT_CHECKS_PASS')

#!/usr/bin/env python3
"""Exact finite enumeration of odd-independent sets and strong-odd color partitions of GP(10,2).
Standard-library only. Each vertex is a fixed bit position, so no graph generator is needed.
"""
from collections import Counter
from functools import lru_cache
from itertools import combinations

N = 20
FULL = (1 << N) - 1
nbr = [0] * N
for i in range(10):
    for u, v in ((i, (i + 1) % 10), (i, i + 10), (10+i, 10+(i+2) % 10)):
        nbr[u] |= 1 << v
        nbr[v] |= 1 << u
assert all(x.bit_count() == 3 for x in nbr)

def odd_independent(s):
    return all(
        (not (s & (1 << v)) or not (s & nbr[v]))
        and ((s & (1 << v)) or ((s & nbr[v]).bit_count() != 2))
        for v in range(N))

valid = [s for s in range(1, FULL + 1) if odd_independent(s)]
size_count = Counter(s.bit_count() for s in valid)
assert dict(sorted(size_count.items())) == {1: 20, 2: 100, 3: 120, 4: 90, 6: 10}
sets4 = set(s for s in valid if s.bit_count() == 4)
sets6 = [s for s in valid if s.bit_count() == 6]
disjoint6 = [(a, b) for a, b in combinations(sets6, 2) if not a & b]
assert len(disjoint6) == 15
assert all(a & b or b & c or a & c for a, b, c in combinations(sets6, 3))
assert all(not any((s & ~ (FULL ^ (a | b))) == 0 for s in sets4) for a, b in disjoint6)
# The preceding condition is: no valid four-set lies inside the eight-vertex complement.

by_vertex = [[s for s in valid if s & (1 << v)] for v in range(N)]
@lru_cache(None)
def partition_profiles(uncovered, blocks):
    if uncovered == 0:
        return {(): 1} if blocks == 0 else {}
    if blocks == 0 or uncovered.bit_count() < blocks: return {}
    pivot = (uncovered & -uncovered).bit_length() - 1
    answer = Counter()
    for s in by_vertex[pivot]:
        if s & uncovered != s: continue
        for profile, count in partition_profiles(uncovered ^ s, blocks - 1).items():
            answer[tuple(sorted((s.bit_count(),) + profile))] += count
    return dict(answer)

assert partition_profiles(FULL, 4) == {}
profile5 = partition_profiles(FULL, 5)
expected = {(2, 3, 3, 6, 6): 60,
            (3, 3, 4, 4, 6): 100,
            (4, 4, 4, 4, 4): 52}
assert profile5 == expected, (profile5, expected)
assert sum(profile5.values()) == 212
# Square-color classes are independent in the distance-at-most-two graph.
# Union each neighbor's adjacency mask with the direct-neighbor mask.
square_nbr = [nbr[v] | __import__('functools').reduce(lambda a, b: a | b, (nbr[u] for u in range(N) if nbr[v] & (1 << u)), 0) for v in range(N)]
square_nbr = [mask & ~(1 << v) for v, mask in enumerate(square_nbr)]
square_classes = set(s for s in valid if all(not((s >> v) & 1 and (s & square_nbr[v])) for v in range(N)))
square_by_vertex = [[s for s in square_classes if s & (1 << v)] for v in range(N)]
@lru_cache(None)
def square_partitions(uncovered, blocks):
    if not uncovered: return int(blocks == 0)
    if not blocks: return 0
    v = (uncovered & -uncovered).bit_length() - 1
    return sum(square_partitions(uncovered ^ s, blocks-1) for s in square_by_vertex[v] if s & uncovered == s)
assert square_partitions(FULL, 5) == 2
# Every block contains the lowest-index uncovered vertex in exactly one position,
# so every unlabelled partition is counted precisely once.
print('ODD_INDEPENDENT_POLYNOMIAL=1+20t+100t^2+120t^3+90t^4+10t^6')
print('SIX_SETS=10; DISJOINT_SIX_PAIRS=15; DISJOINT_SIX_TRIPLES=0')
print('FOUR_COVERS=0; FIVE_COVERS=212; FIVE_SQUARE_COVERS=2')
print('FIVE_COVER_SIZE_PROFILES=' + repr(sorted(profile5.items())))
print('VERIFY_EXACT_COVER_OK')

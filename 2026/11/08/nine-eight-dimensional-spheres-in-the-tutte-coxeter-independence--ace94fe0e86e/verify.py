#!/usr/bin/env python3
"""Exact finite verification of a Tutte--Coxeter incidence-graph independence complex.
Uses the duad/syntheme incidence construction; Python standard library only.
"""
import itertools
import collections
from collections import deque
from math import comb

DUADS = list(itertools.combinations(range(6), 2))
SYNTHEMES = [triple for triple in itertools.combinations(range(15), 3)
             if len({x for i in triple for x in DUADS[i]}) == 6]
assert len(DUADS) == len(SYNTHEMES) == 15
NEIGHBORS = [0] * 30
for t, triple in enumerate(SYNTHEMES):
    for edge in triple:
        NEIGHBORS[edge] |= (1 << (15 + t))
        NEIGHBORS[15 + t] |= (1 << edge)
assert all(n.bit_count() == 3 for n in NEIGHBORS)
assert sum(x.bit_count() for x in NEIGHBORS) == 90

# Verify girth is exactly 8 by a BFS from every vertex.
def girth():
    best = 100
    for root in range(30):
        dist = [-1] * 30
        parent = [-1] * 30
        dist[root] = 0
        q = deque([root])
        while q:
            a = q.popleft()
            m = NEIGHBORS[a]
            while m:
                b = m & -m
                m ^= b
                v = b.bit_length() - 1
                if dist[v] < 0:
                    dist[v], parent[v] = dist[a] + 1, a
                    q.append(v)
                elif parent[a] != v:
                    best = min(best, dist[a] + dist[v] + 1)
    return best
assert girth() == 8

# Independent face generation, using branching on vertex and its closed neighborhood.
FACES = set()
def enumerate_independent(available, chosen):
    if not available:
        FACES.add(chosen)
        return
    bit = available & -available
    vertex = bit.bit_length() - 1
    enumerate_independent(available ^ bit, chosen)
    enumerate_independent(available & ~(bit | NEIGHBORS[vertex]), chosen | bit)

enumerate_independent((1 << 30) - 1, 0)
assert len(FACES) == 476187

# Independent combinatorial census: choose arbitrary duads, then free synthemes.
NUM_BY_SIZE = [0] * 31
for duad_subset in range(1 << 15):
    blocked = 0
    for i in range(15):
        if duad_subset & (1 << i):
            blocked |= (NEIGHBORS[i] >> 15)
    free = 15 - blocked.bit_count()
    k = duad_subset.bit_count()
    for t in range(free + 1):
        NUM_BY_SIZE[k + t] += comb(free, t)
assert len(FACES) == sum(NUM_BY_SIZE)
assert [sum(1 for face in FACES if face.bit_count() == k)
        for k in range(16)] == NUM_BY_SIZE[:16]
assert NUM_BY_SIZE[:16] == [1,30,390,2890,13515,41736,86610,120690,
                               111225,66090,24948,6420,1370,240,30,2]
assert not any(NUM_BY_SIZE[16:])
assert sum((-1) ** (k - 1) * n for k, n in enumerate(NUM_BY_SIZE)) == 9

# Sequential vertex-toggle matching, over augmented faces including empty.
UNMATCHED = FACES.copy()
PARTNERS = {}
PAIR_COUNTS = []
for vertex in range(30):
    bit = 1 << vertex
    lows = [a for a in UNMATCHED if not a & bit and (a | bit) in UNMATCHED]
    for low in lows:
        high = low | bit
        PARTNERS[low] = high
        PARTNERS[high] = low
    UNMATCHED.difference_update(lows)
    UNMATCHED.difference_update({a | bit for a in lows})
    PAIR_COUNTS.append(len(lows))
assert len(PARTNERS) == 476178
assert len(UNMATCHED) == 9
assert {v.bit_count() - 1 for v in UNMATCHED} == {8}
assert 0 in PARTNERS and PARTNERS[0] == 1
assert sum(PAIR_COUNTS) == 238089

# Orient every Hasse relation downward unless it belongs to a matched pair.
# This checks all the relevant directed edges, not merely the critical count.
# The augmented empty/vertex pair is retained during this check.
indegree = {face: 0 for face in FACES}
cover_count = 0
for high in FACES:
    bits = high
    while bits:
        bit = bits & -bits
        bits ^= bit
        low = high ^ bit
        assert low in FACES
        if PARTNERS.get(low) == high:
            indegree[high] += 1
        else:
            indegree[low] += 1
        cover_count += 1
assert cover_count == sum(k * cnt for k, cnt in enumerate(NUM_BY_SIZE))
q = deque(face for face, n in indegree.items() if n == 0)
visited = 0
while q:
    face = q.popleft()
    visited += 1
    bits = face
    while bits:
        bit = bits & -bits
        bits ^= bit
        low = face ^ bit
        if PARTNERS.get(low) != face:
            indegree[low] -= 1
            if indegree[low] == 0:
                q.append(low)
    partner = PARTNERS.get(face)
    if partner is not None and partner.bit_count() == face.bit_count() + 1:
        indegree[partner] -= 1
        if indegree[partner] == 0:
            q.append(partner)
assert visited == len(FACES), (visited, len(FACES))

# Remove the empty/vertex pair from the matching; only vertex 0 becomes
# an additional critical 0-simplex in the non-augmented face poset.
assert set(UNMATCHED) & {0, 1} == set()
print('vertices=30 edges=45 girth=8')
print('face_count_including_empty=', len(FACES))
print('face_count_by_cardinality=', NUM_BY_SIZE[:16])
print('matching_pairs=', len(PARTNERS) // 2)
print('matching_pairs_by_stage=', PAIR_COUNTS)
print('unmatched_augmented_cell_dimensions=',dict(sorted(collections.Counter(x.bit_count()-1 for x in UNMATCHED).items())))
print('Hasse_cover_count=', cover_count)
print('directed_acyclicity_toposort_vertices=', visited)
print('ordinary_critical_cells=',{0: 1, 8: 9})
print('reduced_euler_characteristic=',9)
print('ALL_CHECKS_PASS')

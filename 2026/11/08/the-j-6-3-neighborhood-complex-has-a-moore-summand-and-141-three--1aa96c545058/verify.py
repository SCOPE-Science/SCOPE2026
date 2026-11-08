#!/usr/bin/env python3
"""Exact finite verification for the open-neighborhood complex of J(6,3).

Requires Python 3.9+ standard library only; no downloaded data.
The 20 vertices are lexicographically ordered triples of {0,...,5}.
Each face is encoded as a 20-bit positive integer.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache, reduce
from itertools import combinations
from math import gcd

VERTICES = tuple(combinations(range(6), 3))
N = len(VERTICES)
assert N == 20
NEIGHBORS = tuple(sum(1 << j for j, b in enumerate(VERTICES)
                      if len(set(a).intersection(b)) == 2)
                  for a in VERTICES)
assert all(a.bit_count() == 9 for a in NEIGHBORS)
assert all((NEIGHBORS[i] >> j & 1) == (NEIGHBORS[j] >> i & 1)
           for i in range(N) for j in range(N))


def union_of_neighborhood_simplices():
    faces = {0}
    for mask in NEIGHBORS:
        ids = [i for i in range(N) if mask >> i & 1]
        for subset in range(1, 1 << len(ids)):
            face = 0
            for k in range(len(ids)):
                if subset >> k & 1:
                    face |= 1 << ids[k]
            faces.add(face)
    return faces


def common_neighbor_faces():
    # A separate 2^20-subset test: intersection of all selected
    # vertices' neighborhoods must be nonempty.
    support = [0] * (1 << N)
    support[0] = (1 << N) - 1
    faces = {0}
    for mask in range(1, 1 << N):
        low = mask & -mask
        support[mask] = support[mask ^ low] & NEIGHBORS[low.bit_length() - 1]
        if support[mask]:
            faces.add(mask)
    return faces


faces = union_of_neighborhood_simplices()
assert faces == common_neighbor_faces()
assert len(faces) == 8621
fv = tuple(sum(x.bit_count() == k for x in faces) for k in range(10))
assert fv == (1,20,180,960,2340,2520,1680,720,180,20), fv


def oriented_boundary(mask):
    ids = [i for i in range(N) if mask >> i & 1]
    return [(mask ^ (1 << i), (-1) ** j) for j,i in enumerate(ids)]


ORDER = (10,18,16,14,0,17,11,2,3,9,5,7,4,19,6,15,8,1,13,12)
unmatched = set(faces) - {0}
partner = {}
pairs = []
for vertex in ORDER:
    bit = 1 << vertex
    for lower in list(unmatched):
        higher = lower | bit
        if (lower & bit) == 0 and higher in unmatched:
            unmatched.remove(lower)
            unmatched.remove(higher)
            partner[lower] = higher
            partner[higher] = lower
            pairs.append((lower,higher))
assert len(pairs) == 4238
crit = defaultdict(list)
for face in unmatched:
    crit[face.bit_count() - 1].append(face)
assert {dimension:len(items) for dimension,items in crit.items()} == {0:1,2:1,3:142}
assert (min(crit[0]), min(crit[2])) == (1 << 10, 458752)

# Check that the globally oriented Hasse graph is acyclic; the matched
# incidences point upward, all others point downward.
in_degree = {f:0 for f in faces if f}
upward = defaultdict(list)
downward = defaultdict(list)
incidences = 0
for higher in in_degree:
    if higher.bit_count() <= 1:
        continue
    for lower,sgn in oriented_boundary(higher):
        incidences += 1
        if partner.get(lower) == higher:
            upward[lower].append(higher)
            in_degree[higher] += 1
        else:
            downward[higher].append(lower)
            in_degree[lower] += 1
assert incidences == 41940
queue = deque(f for f,v in in_degree.items() if not v)
visited = 0
while queue:
    face = queue.popleft()
    visited += 1
    for nxt in upward[face] + downward[face]:
        in_degree[nxt] -= 1
        if in_degree[nxt] == 0:
            queue.append(nxt)
assert visited == 8620, (visited,len(in_degree))

# Integer Morse differential in degrees 3 -> 2. A degree-2 matched-up
# cell is eliminated using its paired degree-3 oriented boundary; a
# degree-2 cell matched downward to an edge has coefficient zero.
critical_two = crit[2][0]
@lru_cache(None)
def weight(face):
    assert face.bit_count() == 3
    if face == critical_two:
        return 1
    assert face in partner
    other = partner[face]
    if other.bit_count() == 2:
        return 0
    assert other.bit_count() == 4
    signed_faces = oriented_boundary(other)
    sign = dict(signed_faces)[face]
    total = sum(s * weight(f) for f,s in signed_faces if f != face)
    return -total * sign

coefficients = [sum(s * weight(f) for f,s in oriented_boundary(face))
                for face in sorted(crit[3])]
counts = Counter(coefficients)
assert counts == Counter({0:95,2:30,-2:17}), counts
assert reduce(gcd, coefficients, 0) == 2
for lower,higher in pairs:
    if lower.bit_count() == 3 and higher.bit_count() == 4:
        assert sum(s * weight(f) for f,s in oriented_boundary(higher)) == 0

# Independent mod-two boundary ranks in every positive dimension,
# calculated directly on the original 8620 simplices (not Morse cells).
by_size = {k:sorted(f for f in faces if f.bit_count() == k)
           for k in range(1,10)}

def gf2_rank(columns):
    pivots = {}
    rank = 0
    for column in columns:
        while column:
            lead = column.bit_length() - 1
            if lead in pivots:
                column ^= pivots[lead]
            else:
                pivots[lead] = column
                rank += 1
                break
    return rank

ranks = []
for k in range(2,10):
    rows = {f:i for i,f in enumerate(by_size[k-1])}
    columns = []
    for higher in by_size[k]:
        bitset = 0
        for lower,sgn in oriented_boundary(higher):
            bitset ^= 1 << rows[lower]
        columns.append(bitset)
    ranks.append(gf2_rank(columns))
assert tuple(ranks) == (19,161,798,1400,1120,560,160,20)

# Morse CW cellular chains C3=Z^142 -> C2=Z -> C0=Z.
# The 142 degree values generate 2Z; hence the homotopy type is
# M(Z/2,2) wedge 141 three-spheres, by integral basis changes in C3
# and pi_2(S2)=Z. All 1-cells, and all cells above dimension 3,
# have been cancelled by the acyclic matching.
print('GRAPH: J(6,3), 20 vertices, regular degree 9')
print('FACE_COUNTS_BY_CARDINALITY:', fv)
print('FACE_ENUMERATIONS_AGREE: True; examined 1048576 subsets')
print('MORSE_PAIRS:', len(pairs))
print('MORSE_CRITICAL_DIMS:', dict(sorted((d,len(v)) for d,v in crit.items())))
print('HASSE_INCIDENCES:', incidences, 'ACYCLIC_VERTICES:', visited)
print('MORSE_D3_COEFFICIENT_DISTRIBUTION:', dict(sorted(counts.items())))
print('MORSE_D3_GCD:', reduce(gcd,coefficients,0))
print('DIRECT_GF2_BOUNDARY_RANKS_D1_TO_D8:', tuple(ranks))
print('INTEGRAL_REDUCED_H2: Z/2, H3: Z^141; all other reduced groups zero')
print('HOMOTOPY: M(Z/2,2) wedge 141 S^3')
print('JOHNSON_NEIGHBORHOOD_INTEGER_TORSION_VERIFIED')

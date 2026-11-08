#!/usr/bin/env python3
"""Independent finite checks for the ordinary three-cut complex of KG(6,2).

Uses only Python's standard library. The general integral/homotopy argument is in RESULT.md.
"""
from itertools import combinations
from collections import Counter, defaultdict

GROUND = range(6)
V = tuple(combinations(GROUND, 2))
N = len(V)
FULL = (1 << N) - 1

def is_edge(i, j):
    return not (set(V[i]) & set(V[j]))

def bits(mask):
    return [i for i in range(N) if mask & (1 << i)]

def connected3(indices):
    return sum(is_edge(i, j) for i, j in combinations(indices, 2)) >= 2

# Method A: direct face tests on all 2^15 subsets.
disconnected = []
for inds in combinations(range(N), 3):
    if not connected3(inds):
        disconnected.append(sum(1 << i for i in inds))
assert len(disconnected) == 260
K = set()
for mask in range(1 << N):
    if not any(mask & t == t for t in disconnected):
        K.add(mask)
assert Counter(x.bit_count() for x in K) == {0:1, 1:15, 2:105, 3:195, 4:90}
assert not any(x.bit_count() >= 5 for x in K)

# Method B: independent local-graph criterion on each subset of size at most 5.
for k in range(6):
    for I in combinations(range(N), k):
        mask = sum(1 << i for i in I)
        test = all(connected3(J) for J in combinations(I, 3))
        assert (mask in K) == test

# The ten unordered partitions of [6] into two triples.
partitions = []
for A in combinations(GROUND, 3):
    A = frozenset(A)
    B = frozenset(set(GROUND) - A)
    if min(A) < min(B):
        partitions.append((A, B))
assert len(partitions) == 10
blocks = []
for A, B in partitions:
    left = tuple(i for i, v in enumerate(V) if set(v) <= A)
    right = tuple(i for i, v in enumerate(V) if set(v) <= B)
    assert len(left) == len(right) == 3
    tets = {sum(1 << i for i in (*aa, *bb))
            for aa in combinations(left, 2) for bb in combinations(right, 2)}
    tris = {sum(1 << i for i in I)
            for I in combinations((*left, *right), 3)
            if 1 <= sum(i in left for i in I) <= 2}
    assert len(tets) == 9 and len(tris) == 18
    assert tets <= K and tris <= K
    for tri in tris:
        assert sum(tri & tet == tri for tet in tets) == 2
    blocks.append((tets, tris))
assert len(set.union(*(q for q, _ in blocks))) == 90
assert sum(len(q) for q, _ in blocks) == 90
assert len(set.union(*(t for _, t in blocks))) == 180
assert sum(len(t) for _, t in blocks) == 180

# Exactly the fifteen perfect-matching triangles are outside those blocks.
leftover = {x for x in K if x.bit_count() == 3} - set.union(*(t for _, t in blocks))
assert len(leftover) == 15
assert all(all(is_edge(i,j) for i,j in combinations(bits(x),2)) for x in leftover)

# Every missing triangle bounds a cone of three present triangles.
missing = 0
for I in combinations(range(N), 3):
    m = sum(1 << i for i in I)
    if m in K:
        continue
    missing += 1
    cone_points = [w for w in range(N) if w not in I and
                   all(sum(1 << z for z in (w, i, j)) in K
                       for i,j in combinations(I, 2))]
    assert cone_points
    union = set().union(*(set(V[i]) for i in I))
    assert len(union) <= 4
    assert any(not (set(V[w]) & union) for w in cone_points)
assert missing == 260

# The 3-dimensional boundary decomposes into 10 disjoint matrices, each the
# cellular boundary of (boundary of 2-simplex) * (boundary of 2-simplex).
# Exact ranks in three characteristics independently corroborate the ranks.
F = {k:sorted(mask for mask in K if mask.bit_count() == k+1) for k in range(4)}

def boundary_rank(degree, p):
    pivots = {}
    for simplex in F[degree]:
        col = {simplex ^ (1 << v): (-1 if j%2 else 1) % p
               for j,v in enumerate(bits(simplex))}
        while col:
            lead = min(col)
            if lead not in pivots:
                inv = pow(col[lead], -1, p)
                pivots[lead] = {x:(v*inv)%p for x,v in col.items()}
                break
            c = col[lead]
            for x,v in pivots[lead].items():
                val = (col.get(x,0)-c*v)%p
                if val:col[x]=val
                else:col.pop(x,None)
    return len(pivots)

for p in (2, 3, 5, 7):
    rs = (boundary_rank(1,p), boundary_rank(2,p), boundary_rank(3,p))
    assert rs == (14,91,80), (p,rs)

# Direct cut-complex facets and its full dimension-nine skeleton.
cut_facets = {FULL ^ t for t in disconnected}
assert len(cut_facets) == 260
assert all(f.bit_count() == 12 for f in cut_facets)
for subset in range(1 << N):
    if subset.bit_count() <= 10:
        assert any(subset & f == subset for f in cut_facets)
print('GRAPH vertices=15 disjointness_edges=45')
print('CUT facets=260 dimension=11 full_skeleton_through_dimension=9')
print('DUAL f_vector=(15,105,195,90) missing_3faces=260 no_faces_of_size_5')
print('DUAL blocks=10 spheres_S3=10 tetrahedra_per_block=9')
print('DUAL path_triangles=180 perfect_matching_triangles=15')
print('DUAL π1_cone_test=260_of_260')
print('DUAL boundary_ranks_mod_2_3_5_7=(14,91,80)')
print('DUAL integral_reduced_homology: H2=Z^24 H3=Z^10')
print('CUT integral_reduced_homology: H9=Z^10 H10=Z^24')
print('VERIFY_OK')

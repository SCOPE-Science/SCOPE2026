#!/usr/bin/env python3
"""Self-contained exact finite proof of the Frucht perfect-matching-complex homotopy type."""
from collections import Counter, deque
from itertools import combinations

LCF = (-5, -2, -4, 2, 5, -2, 2, 5, -2, -5, 4, 2)
V = frozenset(range(12))
E = {tuple(sorted((i, (i + 1) % 12))) for i in V}
E.update(tuple(sorted((i, (i + LCF[i]) % 12))) for i in V)
E = tuple(sorted(E))
assert len(E) == 18 and all(sum(v in edge for edge in E) == 3 for v in V)
A = {v: [] for v in V}
for label, (a, b) in enumerate(E):
    A[a].append((b, label)); A[b].append((a, label))

# Exhaustive recursion: choose the smallest still-unmatched vertex at every branch.
perfect = []
def recurse(unmatched, bits):
    if not unmatched:
        perfect.append(bits)
        return
    u = min(unmatched)
    for v, e in A[u]:
        if v in unmatched:
            recurse(unmatched - {u, v}, bits | (1 << e))
recurse(set(V), 0)
P = tuple(perfect)
assert len(P) == len(set(P)) == 8

# Independent 2^18 subset enumeration, without using recursive matching outputs.
P2 = []
for bits in range(1 << 18):
    if bits.bit_count() != 6: continue
    seen = 0
    for j, (u, v) in enumerate(E):
        if (bits >> j) & 1:
            seen |= (1 << u) | (1 << v)
    if seen == (1 << 12) - 1:
        # No overlapping edges can occur among six edges covering 12 vertices.
        P2.append(bits)
assert set(P2) == set(P)
print('FRUCHT_EDGES', len(E), E)
print('PERFECT_MATCHINGS', len(P), P)

# Perfect matching complex: all edge-subsets of the eight perfect matchings.
K = {0}
for p in P:
    labels = [i for i in range(18) if (p >> i) & 1]
    for k in range(1 << len(labels)):
        s = sum(1 << labels[i] for i in range(len(labels)) if k & (1 << i))
        K.add(s)
counts = tuple(sum(s.bit_count() == k for s in K) for k in range(7))
assert counts == (1, 18, 88, 147, 118, 48, 8)
assert len(K) == 428
ordinary_compatible_pairs = sum(set(E[i]).isdisjoint(E[j]) for i in range(18) for j in range(i + 1, 18))
assert ordinary_compatible_pairs == 117
assert ordinary_compatible_pairs - counts[2] == 29
print('PERFECT_COMPLEX_FACE_COUNTS_INCLUDING_EMPTY', counts)
print('NONEXTENDIBLE_DISJOINT_EDGE_PAIRS', 29)

# Compute nerve by two independent exact definitions.
# Definition A: an index subset is a face iff its perfect matchings share an edge.
N1 = {0}
for face in range(1, 1 << len(P)):
    intersection = (1 << 18) - 1
    for j, matching in enumerate(P):
        if face & (1 << j): intersection &= matching
    if intersection: N1.add(face)
# Definition B: union of all subsets of the index-sets that contain a graph edge.
N2 = {0}
for e in range(18):
    owners = [j for j, matching in enumerate(P) if matching & (1 << e)]
    for sub in range(1 << len(owners)):
        N2.add(sum(1 << owners[j] for j in range(len(owners)) if sub & (1 << j)))
assert N1 == N2
N = N1
fv = tuple(sum(s.bit_count() == k for s in N) for k in range(6))
assert fv == (1, 8, 25, 22, 7, 1)
print('NERVE_FACE_COUNTS_INCLUDING_EMPTY', fv)

# Explicit certificate of elementary simplicial collapses; no search heuristic is trusted.
# Each pair (free face, unique coface) is checked in the current complex.
CERTIFICATE = (
    (60,124), (7,15), (28,92), (38,166), (44,108), (52,116), (56,120),
    (17,19), (3,11), (9,13), (5,37), (20,84), (24,88), (34,162),
    (40,104), (48,112), (66,74), (10,14), (6,134), (72,76),
    (12,140), (68,100), (36,164), (1,33), (4,132), (8,136),
)
C = N - {0}
pairs = []
for small, big in CERTIFICATE:
    assert small in C and big in C
    assert small.bit_count() + 1 == big.bit_count()
    assert small & big == small
    assert [s for s in C if s != small and (small & s) == small] == [big]
    C.remove(small); C.remove(big)
    pairs.append((small, big))
assert len(pairs) == 26
assert len(C) == 11
assert sum(s.bit_count() == 1 for s in C) == 5
assert sum(s.bit_count() == 2 for s in C) == 6
assert all(s.bit_count() in (1, 2) for s in C)
print('EXACT_ELEMENTARY_COLLAPSE_PAIRS', pairs)
print('REMAINING_GRAPH_SIMPLEX_MASKS', sorted(C))

# Connected residual graph, Euler cycle rank = E - V + 1 = 2.
verts = {s for s in C if s.bit_count() == 1}
edges = {s for s in C if s.bit_count() == 2}
seen = {min(verts)}
while True:
    new_seen = seen | {x for e in edges if e & sum(seen) for x in verts if x & e}
    if new_seen == seen: break
    seen = new_seen
assert seen == verts
assert len(edges) - len(verts) + 1 == 2
print('CONNECTED_SPINE', len(verts), 'vertices', len(edges), 'edges', 'cycle_rank', 2)
print('FRUCHT_PERFECT_MATCHING_NERVE_WEDGE_TWO_CIRCLES_PASS')

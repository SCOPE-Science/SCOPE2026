#!/usr/bin/env python3
"""Reproduce the simplicial Morse and rational character calculations for C16(1,2,6).
Only Python's standard library is required.
"""
from collections import Counter, defaultdict, deque
from itertools import combinations

N = 16
STEPS = (1, 2, 6)
TOGGLE_ORDER = (10, 1, 8, 7, 3, 5, 14, 0, 12, 15, 11, 13, 9, 2, 6, 4)
assert sorted(TOGGLE_ORDER) == list(range(N))

# All graph edges use the usual cyclic-distance convention.
graph_edges = set()
for i, j in combinations(range(N), 2):
    if min((j-i) % N, (i-j) % N) in STEPS:
        graph_edges.add((i, j))
assert len(graph_edges) == 48
neighbors = [set() for _ in range(N)]
for i, j in graph_edges:
    neighbors[i].add(j)
    neighbors[j].add(i)
assert {len(n) for n in neighbors} == {6}

# Enumerate every nonempty independent set, not just the facets.
faces = set()
by_dim = defaultdict(list)
for mask in range(1, 1 << N):
    chosen = [v for v in range(N) if mask & (1 << v)]
    if all(not ((1 << w) & mask) for v in chosen for w in neighbors[v]):
        faces.add(mask)
        by_dim[len(chosen) - 1].append(mask)
assert {d: len(a) for d, a in by_dim.items()} == {0: 16, 1: 72, 2: 112, 3: 60}
assert len(faces) == 260
assert all((mask ^ (1 << i)) in faces for mask in faces
           for i in range(N) if mask & (1 << i) and mask.bit_count() > 1)

# An exact discrete-Morse matching.  At each stage pair all still-available
# masks F,F+v with the first mask not containing the toggled vertex.
unmatched = set(faces)
matching = set()
for v in TOGGLE_ORDER:
    bit = 1 << v
    for mask in sorted(unmatched):
        upper = mask | bit
        if not (mask & bit) and mask in unmatched and upper in unmatched:
            unmatched.remove(mask)
            unmatched.remove(upper)
            matching.add((mask, upper))
assert len(matching) == 127
assert Counter(mask.bit_count() - 1 for mask in unmatched) == {3: 4, 0: 1, 1: 1}
critical = sorted(unmatched)

# Check acyclicity exhaustively on the oriented face-incidence graph.
# Unmatched edges point downward; matched Hasse edges point upward.
down = defaultdict(list)
indegree = {m: 0 for m in faces}
incidence_count = 0
for upper in faces:
    if upper.bit_count() == 1:
        continue
    for i in range(N):
        if upper & (1 << i):
            lower = upper ^ (1 << i)
            incidence_count += 1
            source, target = ((lower, upper) if (lower, upper) in matching
                              else (upper, lower))
            down[source].append(target)
            indegree[target] += 1
assert incidence_count == 720
queue = deque(sorted(m for m in faces if not indegree[m]))
visited = 0
while queue:
    m = queue.popleft()
    visited += 1
    for nxt in down[m]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            queue.append(nxt)
assert visited == len(faces), "The matching must be acyclic"

# Forman's theorem: K is homotopy equivalent to a CW complex with exactly
# one 0-cell, one 1-cell, no 2-cells and four 3-cells.  Since pi_2(S^1)=0,
# all four attaching maps are null; hence K ~ S^1 vee 4 S^3.

# Compute automorphisms as *all* graph permutations, by adjacency/nonadjacency
# preserving backtracking.  Then compare with 32 dihedral permutations.
def graph_automorphisms():
    output = set()
    assigned = {}
    used = set()
    def rec():
        if len(assigned) == N:
            output.add(tuple(assigned[i] for i in range(N)))
            return
        best_v = None
        best_candidates = None
        for v in range(N):
            if v in assigned:
                continue
            candidates = [w for w in range(N) if w not in used
                          and all(((u in neighbors[v]) == (assigned[u] in neighbors[w]))
                                  for u in assigned)]
            if not candidates:
                return
            if best_candidates is None or len(candidates) < len(best_candidates):
                best_v, best_candidates = v, candidates
        for w in best_candidates:
            assigned[best_v] = w
            used.add(w)
            rec()
            used.remove(w)
            del assigned[best_v]
    rec()
    return output

dihedral = {(tuple((a + (-1 if b else 1) * i) % N for i in range(N)))
            for b in (0, 1) for a in range(N)}
assert len(dihedral) == 32
assert graph_automorphisms() == dihedral

# Integral 1-cocycle. Entries are 0 except at the fifteen oriented edges
# below (all oriented from smaller to larger endpoint).
cochain = {
    (1, 6): 1, (2, 6): 1, (2, 7): 1, (6, 9): -1,
    (1, 10): 1, (2, 10): 1, (5, 10): 1, (2, 11): 1,
    (6, 13): -1, (10, 13): -1, (1, 14): 1,
    (2, 14): 1, (5, 14): 1, (9, 14): 1, (2, 15): 1,
}
def omega(i, j):
    return cochain.get((i, j), 0) if i < j else -cochain.get((j, i), 0)

all_simplex_edges = {
    tuple(i for i in range(N) if mask & (1 << i)) for mask in by_dim[1]
}
assert set(cochain) <= all_simplex_edges
for mask in by_dim[2]:
    i, j, k = [v for v in range(N) if mask & (1 << v)]
    assert omega(j, k) - omega(i, k) + omega(i, j) == 0
# This closed cochain evaluates to +1 on a genuine graph 1-cycle.
cycle = [(1, 6), (6, 3), (3, 0), (0, 4), (4, 1)]
assert all(tuple(sorted(edge)) in all_simplex_edges for edge in cycle)
assert sum(omega(i, j) for i, j in cycle) == 1
# Thus omega is a primitive H^1 generator because the Morse complex has
# H_1=Z.  Its pullback along each graph automorphism determines the H1 trace.

def perm(a, b):
    return tuple((a + (-1 if b else 1) * i) % N for i in range(N))

def reduced_lefschetz(p):
    total = -1  # the augmented empty-face contribution
    for d, masks in by_dim.items():
        for mask in masks:
            image = [p[i] for i in range(N) if mask & (1 << i)]
            image_mask = sum(1 << i for i in image)
            if image_mask != mask:
                continue
            inversions = sum(image[i] > image[j] for i in range(len(image))
                             for j in range(i + 1, len(image)))
            total += (-1) ** (d + inversions)
    return total

character_H1, character_H3 = {}, {}
for b in (0, 1):
    for a in range(N):
        p = perm(a, b)
        tr1 = sum(omega(p[i], p[j]) for i, j in cycle)
        assert tr1 == (-1 if b else 1)
        # Reduced Lefschetz = -tr(H1)-tr(H3); no other reduced homology.
        tr3 = -reduced_lefschetz(p) - tr1
        assert tr3 == (4 if a % 8 == 0 else -4 if a % 8 == 4 else 0) if b == 0 else tr3 == 0
        character_H1[a, b] = tr1
        character_H3[a, b] = tr3

assert sum(character_H1.values()) == 0
assert sum(character_H3.values()) == 0
# H3 is the rational four-dimensional cyclotomic D16 representation
# Q(zeta_8), with r multiplication by zeta_8 and s complex conjugation.
# The rotation r has order eight on this representation, although it has
# order sixteen on the graph. H1 is the reflection-sign character.
# Both full-group invariant spaces vanish.
print('C16_126_FULL_TOPOLOGY_AND_DIHEDRAL_CHARACTER_PASS')
print('graph=16_vertices_48_edges; simplices_by_dimension=(16,72,112,60)')
print('matching=127_pairs; critical_by_dimension=(1,1,0,4); incidences=720; oriented_dag_nodes=260')
print('critical_masks=' + repr(critical))
print('Aut_graph=D16_order_32')
print('integral_cochain_support=15; evaluation_on_5_edge_cycle=1')
print('H1_rotations=' + repr(tuple(character_H1[a,0] for a in range(N))))
print('H1_reflections=' + repr(tuple(character_H1[a,1] for a in range(N))))
print('H3_rotations=' + repr(tuple(character_H3[a,0] for a in range(N))))
print('H3_reflections=' + repr(tuple(character_H3[a,1] for a in range(N))))
print('homotopy=S1_vee_4S3; rational_quotient_positive_Betti=0')

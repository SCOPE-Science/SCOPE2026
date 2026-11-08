#!/usr/bin/env python3
"""Verify total-cut homotopy data for the 18-vertex Pappus graph.
Only Python standard library is required.  All face and incidence tests are exhaustive.
"""
from collections import Counter, deque
from itertools import combinations
from math import comb

N = 18
LIMIT = 1 << N
FULL = LIMIT - 1
LCF = (5, 7, -7, 7, -7, -5) * 3
EXPECTED = (0, 1, 10, 55, 202, 481, 688, 460, 64, 1)

adj = [0] * N
for i, offset in enumerate(LCF):
    for j in ((i-1) % N, (i+1) % N, (i+offset) % N):
        adj[i] |= 1 << j
        adj[j] |= 1 << i
assert all(m.bit_count() == 3 for m in adj)
assert sum(a.bit_count() for a in adj) == 54
# Breadth-first color and shortest cycles verify the graph's incidence properties.
colors = [-1] * N
colors[0] = 0
q = deque([0])
while q:
    v = q.popleft()
    for u in range(N):
        if adj[v] & (1 << u):
            if colors[u] == -1:
                colors[u] = 1 - colors[v]
                q.append(u)
            else:
                assert colors[u] != colors[v]
assert Counter(colors) == {0: 9, 1: 9}
assert all((adj[v] >> v & 1) == 0 for v in range(N))
assert sum(1 for a,b,c,d in combinations(range(N), 4)
           if sum(((adj[x] >> y) & 1)
                  for x,y in combinations((a,b,c,d),2)) == 4 and
           all(sum((adj[x] >> y) & 1 for y in (a,b,c,d) if y!=x)==2
               for x in (a,b,c,d))) == 0  # No four-cycles.

# Algorithm I: independent-set thresholds by vertex-deletion recurrence.
non = [FULL ^ (a | (1 << v)) for v,a in enumerate(adj)]
ind = [bytearray(LIMIT) for _ in range(10)]
ind[0][:] = b'\1' * LIMIT
for mask in range(1, LIMIT):
    bit = mask & -mask
    v = bit.bit_length() - 1
    rest = mask ^ bit
    avail = rest & non[v]
    for k in range(1, min(9, mask.bit_count()) + 1):
        ind[k][mask] = ind[k][rest] or ind[k-1][avail]

# Algorithm II: maximum independent-subset cardinality by a distinct recurrence.
alpha = bytearray(LIMIT)
for mask in range(1, LIMIT):
    bit = mask & -mask
    v = bit.bit_length() - 1
    rest = mask ^ bit
    alpha[mask] = max(alpha[rest], 1+alpha[rest & non[v]])
assert max(alpha) == 9
for k in range(1,10):
    assert all(ind[k][mask] == (alpha[mask] >= k)
               for mask in range(LIMIT)), (k, 'face methods disagree')
# Explicit independent subset lists provide a third, distinct spot enumeration.
for k in (2, 4, 6, 8, 9):
    triples = 0
    for t in combinations(range(N), k):
        m = sum(1 << v for v in t)
        if all((adj[v] & m) == 0 for v in t):
            triples += 1
            assert alpha[m] == k
    assert triples == sum(alpha[m] == k and all((adj[v] & m) == 0 for v in range(N) if m >> v & 1)
                          for m in range(LIMIT) if m.bit_count() == k)

print('Pappus: 18 vertices, 27 edges, bipartite 9+9, independence number 9')
print('k faces morse_pairs critical_cells all_Hasse_incidence reduced_spheres dimension')

for k in range(1, 10):
    faces = bytearray(alpha[FULL ^ mask] >= k for mask in range(LIMIT))
    assert faces[0]
    num_faces = sum(faces)
    paired = bytearray(LIMIT)
    matched_lower = {} # upper -> lower for the selected Hasse incidences
    matched_upper = {} # lower -> upper
    for v in range(N):
        bit = 1 << v
        for lower in range(LIMIT):
            upper = lower | bit
            if (lower & bit) == 0 and faces[lower] and faces[upper] and not paired[lower] and not paired[upper]:
                paired[lower] = paired[upper] = 1
                matched_lower[upper] = lower
                matched_upper[lower] = upper
    assert len(matched_lower) == len(matched_upper)
    assert num_faces == 2*len(matched_lower) + sum(faces[m] and not paired[m] for m in range(LIMIT))
    critical = Counter(m.bit_count()-1 for m in range(LIMIT) if faces[m] and not paired[m])
    assert critical == Counter({18-2*k: EXPECTED[k]}), (k,critical)
    assert matched_upper[0].bit_count() == 1  # Empty face paired to a vertex.
    # Independently determine reduced Euler characteristic from all faces.
    chi = -sum((-1)**m.bit_count() for m in range(LIMIT) if faces[m])
    assert chi == (-1)**(18-2*k) * EXPECTED[k]
    # Directed Hasse graph: unmatched upper -> lower, matched lower -> upper.
    # A linear-time topological sort checks absence of a closed gradient path.
    indeg = [0] * LIMIT
    incidences = 0
    for upper in range(1, LIMIT):
        if not faces[upper]:
            continue
        mm = upper
        while mm:
            bit = mm & -mm
            mm ^= bit
            lower = upper ^ bit
            assert faces[lower]
            incidences += 1
            if matched_lower.get(upper) == lower:
                indeg[upper] += 1
            else:
                indeg[lower] += 1
    todo = deque(m for m in range(LIMIT) if faces[m] and indeg[m] == 0)
    visited = 0
    while todo:
        m = todo.popleft()
        visited += 1
        mm = m
        while mm:
            bit = mm & -mm
            mm ^= bit
            lower = m ^ bit
            if matched_lower.get(m) != lower:
                indeg[lower] -= 1
                if indeg[lower] == 0:
                    todo.append(lower)
        upper = matched_upper.get(m)
        if upper is not None:
            indeg[upper] -= 1
            if indeg[upper] == 0:
                todo.append(upper)
    assert visited == num_faces, (k,visited,num_faces)
    # Passing to ordinary nonempty faces and discarding the empty/vertex pair
    # leaves one critical vertex and EXPECTED[k] critical (18-2k)-cells.
    assert len(matched_lower) * 2 + EXPECTED[k] == num_faces
    print(k, num_faces, len(matched_lower), EXPECTED[k], incidences, EXPECTED[k], 18-2*k)

assert all(alpha[mask] < 10 for mask in range(LIMIT))
print('PASS: all nine levels, all 18-bit masks, two independent alpha algorithms,')
print('all directed incidences, all critical cells and all reduced Euler characteristics.')

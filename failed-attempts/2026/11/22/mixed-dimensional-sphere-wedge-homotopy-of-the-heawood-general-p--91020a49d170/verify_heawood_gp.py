#!/usr/bin/env python3
"""Exact finite combinatorial certificate for the Heawood graph GP complex.

Only Python standard-library arithmetic; all 14-vertex subsets and all Hasse
incidences are visited. Successful exit verifies the stated discrete Morse
matching, its acyclicity, and independent finite-field boundary ranks.
"""
from collections import Counter, deque
from itertools import combinations

N = 14
vertices = range(N)
adj = [set() for _ in vertices]
# Vertices 0,...,6 are points; 7+i is the Fano line {i,i+1,i+3}.
for i in range(7):
    for p in (i, (i + 1) % 7, (i + 3) % 7):
        adj[7 + i].add(p)
        adj[p].add(7 + i)
assert len({tuple(sorted(x)) for x in adj}) == 14
assert sum(map(len, adj)) == 42

def distances(start):
    d = [N + 1] * N
    d[start] = 0
    queue = deque([start])
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if d[v] > d[u] + 1:
                d[v] = d[u] + 1
                queue.append(v)
    assert max(d) <= 3
    return d

dist = [distances(v) for v in vertices]
assert all(dist[u][v] == dist[v][u] for u in vertices for v in vertices)

forbidden = []
for triple in combinations(vertices, 3):
    a, b, c = triple
    if (dist[a][b] + dist[b][c] == dist[a][c]
        or dist[a][c] + dist[c][b] == dist[a][b]
        or dist[b][a] + dist[a][c] == dist[b][c]):
        forbidden.append(sum(1 << v for v in triple))
assert len(forbidden) == 210
assert Counter(sum(bool(mask & (1 << p)) for p in range(7))
               for mask in forbidden) == {1: 105, 2: 105}

faces = sorted((mask for mask in range(1, 1 << N)
                if not any((mask & triple) == triple for triple in forbidden)),
               key=lambda mask: (mask.bit_count(), mask))
face_set = set(faces)
assert len(faces) == len(face_set) == 478
assert [sum(mask.bit_count() == k for mask in faces)
        for k in range(1, 8)] == [14, 91, 154, 147, 56, 14, 2]
assert all((mask ^ (1 << v)) in face_set
           for mask in faces for v in vertices
           if mask & (1 << v) and mask.bit_count() > 1)

# Complete deterministic vertex-toggle matching, increasing vertex pivots.
partner = {}
for v in vertices:
    bit = 1 << v
    for low in faces:
        high = low | bit
        if (not(low & bit) and low not in partner
            and high in face_set and high not in partner):
            partner[low] = high
            partner[high] = low
assert all(partner.get(partner[x]) == x for x in partner)
assert all(abs(x.bit_count() - partner[x].bit_count()) == 1 for x in partner)
critical = [mask for mask in faces if mask not in partner]
assert len(partner) == 450
assert Counter(mask.bit_count() - 1 for mask in critical) == {0: 1, 1: 21, 3: 6}
assert [x for x in critical if x.bit_count() == 1] == [1]

# Reverse each matched cover arrow in the full nonempty-face Hasse diagram.
# An exhaustive topological sort rules out ALL closed gradient paths.
out = {face: [] for face in faces}
in_degree = dict.fromkeys(faces, 0)
incidences = 0
for upper in faces:
    for v in vertices:
        if upper & (1 << v):
            lower = upper ^ (1 << v)
            if lower not in face_set:
                continue
            source, target = ((lower, upper) if partner.get(lower) == upper
                              else (upper, lower))
            out[source].append(target)
            in_degree[target] += 1
            incidences += 1
assert incidences == 1610
queue = deque(f for f in faces if in_degree[f] == 0)
visited = 0
while queue:
    face = queue.popleft()
    visited += 1
    for successor in out[face]:
        in_degree[successor] -= 1
        if in_degree[successor] == 0:
            queue.append(successor)
assert visited == len(faces) == 478, "A gradient cycle was found"

# Independent verification: signed simplicial boundaries over four fields.
# This corroborates ranks but is NOT used to infer integral torsion-freeness.
levels = [[mask for mask in faces if mask.bit_count() == k + 1]
          for k in range(7)]

def rank_mod_p(columns, prime):
    pivots = {}
    for column in columns:
        remaining = {i: (value % prime)
                     for i, value in column.items() if value % prime}
        while remaining:
            pivot_row = max(remaining)
            if pivot_row not in pivots:
                inv = pow(remaining[pivot_row], -1, prime)
                pivots[pivot_row] = {
                    i: (value * inv) % prime for i, value in remaining.items()
                }
                break
            coeff = remaining[pivot_row]
            for i, value in pivots[pivot_row].items():
                delta = (remaining.get(i, 0) - coeff * value) % prime
                if delta:
                    remaining[i] = delta
                else:
                    remaining.pop(i, None)
    return len(pivots)

for prime in (2, 3, 5, 101):
    ranks = []
    for degree in range(1, 7):
        index = {face: i for i, face in enumerate(levels[degree - 1])}
        columns = []
        for face in levels[degree]:
            column = {}
            for position, vertex in enumerate(v for v in vertices
                                              if face & (1 << v)):
                column[index[face ^ (1 << vertex)]] = (-1) ** position
            columns.append(column)
        ranks.append(rank_mod_p(columns, prime))
    assert ranks == [13, 57, 97, 44, 12, 2], (prime, ranks)
    betti = [len(levels[d]) - (ranks[d - 1] if d > 0 else 1)
             - (ranks[d] if d < 6 else 0) for d in range(7)]
    assert betti == [0, 21, 0, 6, 0, 0, 0], (prime, betti)

print("PASS: 210 forbidden triples; 478 faces; 225 acyclic pairs;")
print("      critical cells (dimension:count) = {0:1, 1:21, 3:6};")
print("      478/478 Hasse vertices topologically sorted; 1610 arcs;")
print("      signed chain ranks agree over F_2,F_3,F_5,F_101.")

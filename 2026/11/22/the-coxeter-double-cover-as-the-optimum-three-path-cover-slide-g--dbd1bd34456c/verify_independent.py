#!/usr/bin/env python3
"""Independent complete search via the binary-vector model of the Fano plane."""
from collections import Counter, deque
from itertools import combinations

# Points are the seven nonzero vectors in GF(2)^3; lines use nonzero normals.
# A point p is incident to a line a exactly when their binary dot product is 0.
n = 14
neighbours = [set() for _ in range(n)]
for p in range(1, 8):
    for a in range(1, 8):
        if ((p & a).bit_count() & 1) == 0:
            neighbours[p - 1].add(a + 6)
            neighbours[a + 6].add(p - 1)
assert all(len(N) == 3 for N in neighbours)
assert sum(len(N) for N in neighbours) == 42

# List all three-vertex paths (not just cyclically consecutive triples).
paths = set()
for middle in range(n):
    for u, v in combinations(sorted(neighbours[middle]), 2):
        paths.add((1 << u) | (1 << middle) | (1 << v))
assert len(paths) == 14 * 3

def is_cover(mask):
    return all(mask & path for path in paths)

# Enumerate all cardinalities, establishing optimality independently.
least = None
covers = []
for k in range(n + 1):
    current = [sum(1 << x for x in part)
               for part in combinations(range(n), k)
               if is_cover(sum(1 << x for x in part))]
    if current:
        least = k
        covers = current
        break
assert least == 7 and len(covers) == 58
cover_set = set(covers)

# Direct adjacency by changing one occupied vertex to an empty vertex.
def adjacency(sliding):
    graph = {v: set() for v in covers}
    for v in covers:
        for x in range(n):
            if not (v >> x) & 1:
                continue
            for y in (neighbours[x] if sliding else range(n)):
                if (v >> y) & 1:
                    continue
                target = v ^ (1 << x) ^ (1 << y)
                if target in cover_set:
                    graph[v].add(target)
    return graph

slide_graph = adjacency(True)
jump_graph = adjacency(False)
assert slide_graph == jump_graph
assert sum(len(X) for X in slide_graph.values()) // 2 == 84
assert Counter(len(X) for X in slide_graph.values()) == {3: 56, 0: 2}

visited = set()
component_data = []
for root in covers:
    if root in visited:
        continue
    distances = {root: 0}
    queue = deque([root])
    while queue:
        s = queue.popleft()
        for t in slide_graph[s]:
            if t not in distances:
                distances[t] = distances[s] + 1
                queue.append(t)
    visited.update(distances)
    component_data.append((len(distances), max(distances.values())))
assert sorted(component_data) == [(1, 0), (1, 0), (56, 7)]

mobile = [v for v in covers if slide_graph[v]]
expected_shells = [1, 3, 6, 12, 18, 12, 3, 1]
for root in mobile:
    distance = {root: 0}
    queue = deque([root])
    while queue:
        v = queue.popleft()
        for u in slide_graph[v]:
            if u not in distance:
                distance[u] = distance[v] + 1
                queue.append(u)
    assert len(distance) == 56
    assert [Counter(distance.values())[i] for i in range(8)] == expected_shells
print('INDEPENDENT PASS: direct 3-path-cover enumeration on Fano vector incidence')
print('Optimal size', least, '; optima', len(covers), '; edges', 84)
print('Components', sorted(component_data), '; distance shells', tuple(expected_shells))
print('Token jumping equals token sliding')

"""Independent exact validation using Cartesian-coordinate neighborhoods and combinations.
Run with Python 3 standard library: python verify_independent.py
"""
from itertools import combinations, permutations, product
from collections import Counter, deque
from math import comb

V = tuple(product(range(3), repeat=3))
lookup = {x: i for i, x in enumerate(V)}
adj = []
for i, x in enumerate(V):
    adj.append({j for j, y in enumerate(V) if sum(a != b for a, b in zip(x, y)) == 1})
closed = [sum(1 << v for v in adj[i] | {i}) for i in range(27)]
complete = (1 << 27) - 1

def qualifies(indices):
    dominated = 0
    for v in indices:
        dominated |= closed[v]
    if dominated != complete:
        return False
    target = set(indices)
    visited = {indices[0]}
    todo = [indices[0]]
    for p in todo:
        for v in adj[p] & target:
            if v not in visited:
                visited.add(v)
                todo.append(v)
    return visited == target

solutions = []
for k in range(4, 9):
    found = []
    for chosen in combinations(range(27), k):
        if qualifies(chosen):
            found.append(sum(1 << v for v in chosen))
    if k < 8:
        assert not found
    else:
        solutions = found
assert len(solutions) == 11340
assert len(set(solutions)) == len(solutions)

index = {s: i for i, s in enumerate(solutions)}
n = len(solutions)
jump = [set() for _ in range(n)]
slide = [set() for _ in range(n)]
for i, s in enumerate(solutions):
    occupied = [u for u in range(27) if s >> u & 1]
    vacant = [v for v in range(27) if not (s >> v & 1)]
    for u in occupied:
        for v in vacant:
            j = index.get(s ^ (1 << u) ^ (1 << v))
            if j is not None and i < j:
                jump[i].add(j)
                jump[j].add(i)
                if v in adj[u]:
                    slide[i].add(j)
                    slide[j].add(i)
assert sum(map(len, jump)) == 146772
assert sum(map(len, slide)) == 28188

def components(graph):
    membership = [-1] * n
    families = []
    for start in range(n):
        if membership[start] >= 0:
            continue
        cid = len(families)
        todo = [start]
        membership[start] = cid
        for p in todo:
            for q in graph[p]:
                if membership[q] < 0:
                    membership[q] = cid
                    todo.append(q)
        families.append(todo)
    return families, membership

sfam, smem = components(slide)
jfam, _ = components(jump)
assert len(jfam) == 1
assert Counter(map(len, sfam)) == {2: 162, 9: 72, 18: 108, 52: 162}

# The eight generators produce the full wreath-product automorphism group of
# K3 square K3 square K3. Vertex maps are derived from coordinate operations.
generators = []
for a, b in ((0, 1), (1, 2)):
    generators.append([lookup[tuple((x[b] if j == a else x[a] if j == b else x[j])
                                    for j in range(3))] for x in V])
for c in range(3):
    for a, b in ((0, 1), (1, 2)):
        generators.append([lookup[tuple((b if j == c and x[j] == a else
                                          a if j == c and x[j] == b else x[j])
                                         for j in range(3))] for x in V])
assert len(generators) == 8
bit_maps = [tuple(1 << g[i] for i in range(27)) for g in generators]

def transform(mask, bm):
    output = 0
    while mask:
        bit = mask & -mask
        output |= bm[bit.bit_length() - 1]
        mask -= bit
    return output

def breadth_first(graph, start):
    d = [-1] * n
    d[start] = 0
    todo = [start]
    for p in todo:
        for q in graph[p]:
            if d[q] == -1:
                d[q] = d[p] + 1
                todo.append(q)
    return d

# All 11340 configurations partition into orbits under the full graph
# automorphism group; eccentricity is constant in each orbit.
seen = set()
orbit_sizes = Counter()
for root in range(n):
    if root in seen:
        continue
    orbit = {root}
    todo = [root]
    for p in todo:
        for bm in bit_maps:
            q = index[transform(solutions[p], bm)]
            if q not in orbit:
                orbit.add(q)
                todo.append(q)
    assert max(breadth_first(jump, root)) == 9
    seen.update(orbit)
    orbit_sizes[len(orbit)] += 1
assert len(seen) == n

# Every slide component type is a single orbit under these automorphisms.
seen_components = set()
for cid, family in enumerate(sfam):
    if cid in seen_components:
        continue
    orbit = {cid}
    todo = [cid]
    for component_id in todo:
        p = sfam[component_id][0]
        for bm in bit_maps:
            q = smem[index[transform(solutions[p], bm)]]
            if q not in orbit:
                orbit.add(q)
                todo.append(q)
    assert len(orbit) == {2: 162, 9: 72, 18: 108, 52: 162}[len(family)]
    diameter = max(max(d for d in breadth_first(slide, p) if d >= 0)
                   for p in family)
    assert diameter == {2: 1, 9: 4, 18: 9, 52: 11}[len(family)]
    seen_components.update(orbit)
assert len(seen_components) == len(sfam)
print("VERIFIED k=8 configurations=11340 jump_edges=73386 slide_edges=14094 "
      "jump_radius=9 jump_diameter=9 slide_components=504")
print("slide_sizes", dict(sorted(Counter(map(len, sfam)).items())))
print("vertex_orbits", dict(sorted(orbit_sizes.items())))
print("slide_component_orbits", 4)

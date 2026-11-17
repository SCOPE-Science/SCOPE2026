#!/usr/bin/env python3
"""Exact finite checks for a graph-metric simplicial-complex result.

No external Python packages or external files are required.
"""
from collections import Counter, defaultdict, deque
from itertools import combinations
import json

N = 24
LCF = (12, 7, -7) * 8
edges = set()
for i in range(N):
    edges.add(tuple(sorted((i, (i + 1) % N))))
    edges.add(tuple(sorted((i, (i + LCF[i]) % N))))
assert len(edges) == 36
adj = [set() for _ in range(N)]
for a, b in edges:
    adj[a].add(b)
    adj[b].add(a)
assert all(len(a) == 3 for a in adj)

def bfs(start, banned=None):
    distance = [None] * N
    distance[start] = 0
    todo = deque([start])
    while todo:
        u = todo.popleft()
        for v in sorted(adj[u]):
            if banned == tuple(sorted((u, v))):
                continue
            if distance[v] is None:
                distance[v] = distance[u] + 1
                todo.append(v)
    return distance

D = [bfs(i) for i in range(N)]
assert all(D[i][j] is not None and D[i][j] == D[j][i]
           for i in range(N) for j in range(N))
assert max(max(row) for row in D) == 4
assert min(bfs(a, (a, b))[b] + 1 for a, b in edges) == 7
hist = Counter(D[i][j] for i in range(N) for j in range(i + 1, N))
assert hist == {1: 36, 2: 72, 3: 144, 4: 24}

def clique_faces_at_two():
    # Exhaustive clique induction: each (k+1)-face extends a k-face.
    faces = {(i,) for i in range(N)}
    layer = sorted(faces)
    while layer:
        next_layer = set()
        for face in layer:
            for j in range(face[-1] + 1, N):
                if all(D[j][v] <= 2 for v in face):
                    next_layer.add(face + (j,))
        faces.update(next_layer)
        layer = sorted(next_layer)
    return faces

r2 = clique_faces_at_two()
face_vec2 = Counter(len(s) - 1 for s in r2)
assert face_vec2 == {0: 24, 1: 108, 2: 96, 3: 24}

def relative_collapse(reverse):
    faces = set(r2)
    pairs = []
    while True:
        co = defaultdict(list)
        for high in faces:
            if len(high) >= 3:
                for low in combinations(high, len(high) - 1):
                    co[low].append(high)
        choices = [(len(low), low, highs[0]) for low, highs in co.items()
                   if low in faces and len(highs) == 1 and len(low) >= 2
                   and low not in edges]
        if not choices:
            break
        if reverse:
            _, low, high = max(choices)
        else:
            _, low, high = min(choices, key=lambda t: (-t[0], t[1], t[2]))
        assert low in faces and high in faces
        assert len(low) + 1 == len(high) and set(low) < set(high)
        assert sum(low == tuple(v for v in q if v != rem)
                   for q in faces if len(q) == len(high)
                   for rem in q) == 1
        faces.remove(low)
        faces.remove(high)
        pairs.append((low, high))
    assert len(pairs) == 96
    assert faces == {(i,) for i in range(N)} | edges
    return len(pairs)

collapse_forward = relative_collapse(False)
collapse_reverse = relative_collapse(True)

# The graph of pairs at distance four is the complement of the radius-three
# graph power. Each connected component is checked to be exactly a four-cycle.
far = {tuple(sorted((i, j))) for i in range(N) for j in range(i + 1, N)
       if D[i][j] == 4}
faradj = [set() for _ in range(N)]
for a, b in far:
    faradj[a].add(b)
    faradj[b].add(a)
assert all(len(x) == 2 for x in faradj)
seen = set()
components = []
for v in range(N):
    if v in seen:
        continue
    block = set([v])
    todo = [v]
    while todo:
        u = todo.pop()
        for w in faradj[u]:
            if w not in block:
                block.add(w)
                todo.append(w)
    seen |= block
    components.append(tuple(sorted(block)))
components.sort()
assert len(components) == 6
assert all(len(c) == 4 and sum(w in faradj[u] for u, w in combinations(c, 2)) == 4
           for c in components)

sides = []
for block in components:
    x = block[0]
    # Bipartition classes are the non-adjacent pairs in a C4.
    antipodal = next(y for y in block if y != x and y not in faradj[x])
    a = tuple(sorted((x, antipodal)))
    b = tuple(sorted(set(block) - set(a)))
    pair = tuple(sorted((a, b)))
    assert all(u in faradj[v] for u in pair[0] for v in pair[1])
    sides.append(pair)

# Direct combinatorial description: at radius three, an allowed face is
# an independent set in the far graph, which is a join of six complexes
# whose two connected components are edges (each collapses to a vertex).
# Polynomial (1+4t+2t^2)^6 gives the counts by face cardinality.
poly = [1]
for _ in components:
    nxt = [0] * (len(poly) + 2)
    for k, coeff in enumerate(poly):
        for j, ways in enumerate((1, 4, 2)):
            nxt[k + j] += coeff * ways
    poly = nxt
assert sum(poly) == 7 ** 6 == 117649
assert poly[0] == 1 and poly[12] == 64
# Verify the 64 claimed facets are exactly the maximal cliques of radius three.
facets = []
for bits in range(1 << 6):
    face = tuple(sorted(v for i in range(6) for v in sides[i][(bits >> i) & 1]))
    assert len(face) == 12
    assert all(D[a][b] <= 3 for a, b in combinations(face, 2))
    facets.append(face)
assert len(set(facets)) == 64
assert all(any({u, v}.issubset(set(facet)) for facet in facets)
           for u, v in combinations(range(N), 2) if D[u][v] <= 3)

# Determine the full symmetry group directly by adjacency-preserving backtracking.
# Each complete permutation is checked against the original edge set.
permutations = []
def visit(mapping, used):
    if len(mapping) == N:
        m = tuple(mapping[i] for i in range(N))
        assert all(tuple(sorted((m[a], m[b]))) in edges for a, b in edges)
        permutations.append(m)
        return
    choices = []
    for u in range(N):
        if u in mapping:
            continue
        known = sum(v in mapping for v in adj[u])
        if mapping and known == 0:
            continue
        candidates = [v for v in range(N) if v not in used and
                      all((w in adj[u]) == (mapping[w] in adj[v]) for w in mapping)]
        if not candidates:
            return
        choices.append((-known, len(candidates), u, candidates))
    if choices:
        _, _, u, candidates = min(choices)
    else:
        u = next(v for v in range(N) if v not in mapping)
        candidates = [v for v in range(N) if v not in used]
    for v in candidates:
        mapping[u] = v
        used.add(v)
        visit(mapping, used)
        used.remove(v)
        del mapping[u]

visit({}, set())
assert len(permutations) == len(set(permutations)) == 32

def orientation(m):
    component_perm = []
    swaps = []
    for i, block in enumerate(components):
        target = components.index(tuple(sorted(m[v] for v in block)))
        component_perm.append(target)
        image_side = {m[v] for v in sides[i][0]}
        assert image_side in (set(sides[target][0]), set(sides[target][1]))
        swaps.append(int(image_side == set(sides[target][1])))
    inversion_count = sum(component_perm[i] > component_perm[j]
                          for i in range(6) for j in range(i + 1, 6))
    return (-1) ** (inversion_count + sum(swaps))

sign_counts = Counter(orientation(m) for m in permutations)
assert sign_counts == {1: 16, -1: 16}
rotation_by_three = tuple((i + 3) % N for i in range(N))
assert rotation_by_three in permutations and orientation(rotation_by_three) == -1

print(json.dumps({
    'marker': 'MCGEE_RIPS_DISTANCE_FOUR_JOIN_AND_ORIENTATION_VERIFIED',
    'graph': {'vertices': N, 'edges': len(edges), 'girth': 7, 'diameter': 4,
              'distance_histogram': dict(sorted(hist.items()))},
    'rips_scale_two': {'face_vector': dict(sorted(face_vec2.items())),
                       'relative_collapse_pairs_forward': collapse_forward,
                       'relative_collapse_pairs_reverse': collapse_reverse,
                       'terminal_complex': 'original_24_vertex_36_edge_graph'},
    'rips_scale_three': {'distance_four_components': components,
                         'component_bipartitions': sides,
                         'all_faces_including_empty': sum(poly),
                         'facets': len(facets),
                         'maximal_dimension': 11,
                         'reduced_homotopy_type': 'S^5'},
    'symmetry': {'automorphisms': len(permutations),
                 'orientation_character_counts': {str(k): v for k, v in sorted(sign_counts.items())},
                 'rotation_by_three_orientation': orientation(rotation_by_three)},
}, sort_keys=True, indent=2))

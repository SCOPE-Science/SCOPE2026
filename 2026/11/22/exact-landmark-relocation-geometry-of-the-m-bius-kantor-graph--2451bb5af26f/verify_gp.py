#!/usr/bin/env python3
"""Complete finite verifier for landmark relocation on GP(8,3).

Uses resolving-pair bitmasks and breadth-first search; standard library only.
"""
from collections import Counter, deque
from itertools import combinations
import json

N = 16
edges = set()
def add(x, y):
    edges.add(tuple(sorted((x, y))))
for t in range(8):
    add(t, (t + 1) % 8)
    add(t, t + 8)
    add(t + 8, 8 + ((t + 3) % 8))
assert len(edges) == 24
adj = [set() for _ in range(N)]
for x, y in edges:
    adj[x].add(y)
    adj[y].add(x)
assert sorted(map(len, adj)) == [3] * N

def bfs(root, graph):
    ds = [-1] * len(graph)
    ds[root] = 0
    todo = deque([root])
    while todo:
        v = todo.popleft()
        for w in graph[v]:
            if ds[w] < 0:
                ds[w] = ds[v] + 1
                todo.append(w)
    return ds

D = [bfs(v, adj) for v in range(N)]
assert all(d >= 0 for row in D for d in row)
# Pairwise witness: a landmark z distinguishes x and y iff d(z,x) != d(z,y).
witness = []
for x in range(N):
    for y in range(x + 1, N):
        witness.append(sum((1 << z) for z in range(N) if D[z][x] != D[z][y]))
assert len(witness) == 120

def is_resolving(mask):
    return all((mask & w) != 0 for w in witness)

for k in range(4):
    assert not any(is_resolving(sum(1 << x for x in cc)) for cc in combinations(range(N), k))
bases = [sum(1 << x for x in cc) for cc in combinations(range(N), 4)
         if is_resolving(sum(1 << x for x in cc))]
assert len(bases) == 320 and len(set(bases)) == 320
index = {b: i for i, b in enumerate(bases)}

def transitions(local):
    neigh = [set() for _ in bases]
    for i, b in enumerate(bases):
        for out in range(N):
            if not (b >> out) & 1:
                continue
            for into in range(N):
                if (b >> into) & 1 or (local and into not in adj[out]):
                    continue
                b2 = (b ^ (1 << out)) | (1 << into)
                j = index.get(b2)
                if j is not None:
                    neigh[i].add(j)
    assert all(i not in v for i, v in enumerate(neigh))
    assert all(i in neigh[j] for i, row in enumerate(neigh) for j in row)
    return neigh

J = transitions(False)
S = transitions(True)
assert sum(map(len, J)) == 3968 and sum(map(len, S)) == 1152
out = {'graph_vertices': N, 'graph_edges': len(edges), 'minimum_landmarks': 4,
       'metric_bases': len(bases)}
all_distances = []
for name, graph, E, diameter, rad, degrees, eccentricities, histogram in [
    ('jump', J, 1984, 5, 4, {12: 288, 16: 32}, {4: 128, 5: 192},
     {1:1984,2:9888,3:23008,4:16064,5:96}),
    ('slide', S, 576, 12, 12, {3:192,4:96,6:32}, {12:320},
     {1:576,2:1440,3:3072,4:5744,5:7392,6:9192,7:8448,
      8:7584,9:4512,10:2344,11:576,12:160})]:
    ds = [bfs(v, graph) for v in range(len(bases))]
    assert all(x >= 0 for row in ds for x in row)
    h = Counter(ds[i][j] for i in range(len(bases)) for j in range(i+1, len(bases)))
    ecc = Counter(max(row) for row in ds)
    assert h == histogram and ecc == eccentricities
    assert Counter(map(len, graph)) == degrees
    assert sum(map(len, graph)) // 2 == E
    assert min(ecc) == rad and max(ecc) == diameter
    assert sum(h.values()) == 320 * 319 // 2
    out[name] = {'edges': E, 'degrees': dict(sorted(degrees.items())),
                 'eccentricities': dict(sorted(ecc.items())),
                 'distances_unordered': dict(sorted(h.items())),
                 'radius': rad, 'diameter': diameter}
    all_distances.append(ds)
penalty = Counter()
max_examples = []
for i in range(len(bases)):
    for j in range(i+1, len(bases)):
        p = all_distances[1][i][j] - all_distances[0][i][j]
        assert p >= 0
        penalty[p] += 1
        if p == 8 and len(max_examples) < 2:
            max_examples.append(([k for k in range(N) if (bases[i] >> k) & 1],
                                 [k for k in range(N) if (bases[j] >> k) & 1],
                                 all_distances[0][i][j], all_distances[1][i][j]))
assert penalty == {0:4480,1:5856,2:7200,3:10048,4:10152,5:7968,6:3984,7:1216,8:136}
out['slide_minus_jump_distance'] = dict(sorted(penalty.items()))
out['maximum_penalty_examples'] = max_examples
# Complete orbit check under graph automorphisms.  Compare the entire
# adjacency/nonadjacency relation during each partial permutation extension.
automorphisms = []
partial = {}
used = set()
def extend():
    if len(partial) == N:
        automorphisms.append(tuple(partial[v] for v in range(N)))
        return
    unassigned = [v for v in range(N) if v not in partial]
    v = max(unassigned, key=lambda x: (len(adj[x] & partial.keys()), -x))
    for w in range(N):
        if w in used:
            continue
        if any((u in adj[v]) != (partial[u] in adj[w]) for u in partial):
            continue
        partial[v] = w
        used.add(w)
        extend()
        used.remove(w)
        del partial[v]
extend()
assert len(automorphisms) == 96
seenset = set()
orbits = []
for mask in bases:
    if mask in seenset:
        continue
    members = set()
    for p in automorphisms:
        members.add(sum(1 << p[v] for v in range(N) if (mask >> v) & 1))
    assert members <= set(bases)
    seenset.update(members)
    rep = min(members)
    i = index[rep]
    orbits.append({'size': len(members), 'representative': [v for v in range(N) if (rep >> v) & 1],
                   'jump_degree': len(J[i]), 'slide_degree': len(S[i]),
                   'jump_eccentricity': max(all_distances[0][i]),
                   'slide_eccentricity': max(all_distances[1][i])})
assert len(seenset) == 320
assert sorted(x['size'] for x in orbits) == [24,24,32,48,96,96]
out['automorphism_order'] = 96
out['orbit_data'] = sorted(orbits, key=lambda r: (r['size'], r['representative']))
print(json.dumps(out, ensure_ascii=False, sort_keys=True, separators=(',', ':')))
print('VERIFIED_GP_OK')

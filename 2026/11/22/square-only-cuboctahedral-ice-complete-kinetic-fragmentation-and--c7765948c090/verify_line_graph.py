#!/usr/bin/env python3
"""Exact line-graph and orbit enumeration for directed four-regular ice."""
from collections import Counter, defaultdict
from itertools import combinations, product

# Cube vertices and edges. Every cube edge becomes a cuboctahedron vertex.
cube = list(product((0, 1), repeat=3))
vid = {v: k for k, v in enumerate(cube)}
cedges = sorted((vid[v], vid[tuple(1-v[j] if j==a else v[j] for j in range(3))])
                for v in cube for a in range(3) if v[a] == 0)
assert len(cedges) == 12 and all(u < v for u,v in cedges)
# Two cube edges are adjacent in the cuboctahedron iff they share a cube endpoint.
edges = [(a, b) for a,b in combinations(range(12), 2)
         if len(set(cedges[a]) & set(cedges[b])) == 1]
assert len(edges) == 24
# The six old square faces of the cube become six disjoint square cycles.
faces = []
for axis in range(3):
    for layer in (0,1):
        old_face = {a for a,(u,v) in enumerate(cedges)
                    if cube[u][axis] == cube[v][axis] == layer}
        four = tuple(i for i,(u,v) in enumerate(edges) if u in old_face and v in old_face)
        assert len(four) == 4
        faces.append(four)
assert sorted(i for face in faces for i in face) == list(range(24))

# DFS branches on every one of the 24 directed edges. The pruning below is
# logically necessary (and sufficient at the leaves) for two outgoing edges
# at every vertex. Therefore this explores EVERY ice orientation.
outs = [0]*12
remaining = [4]*12
ice = []
def visit(pos, code):
    if pos == len(edges):
        assert all(v == 2 for v in outs)
        ice.append(code)
        return
    u,v = edges[pos]
    remaining[u] -= 1; remaining[v] -= 1
    for bit,src in ((0,u),(1,v)):
        outs[src] += 1
        if all(outs[w] <= 2 <= outs[w]+remaining[w] for w in (u,v)):
            visit(pos+1, code | (bit << pos))
        outs[src] -= 1
    remaining[u] += 1; remaining[v] += 1
visit(0, 0)
assert len(ice) == len(set(ice)) == 600
ice_set = set(ice)

def flippable(code, face):
    involved = {v for i in face for v in edges[i]}
    assert len(involved) == 4
    return all(sum(((code >> i)&1) == int(edges[i][1] == v)
                   for i in face if v in edges[i]) == 1 for v in involved)

masks = [sum(1 << i for i in f) for f in faces]
activity = Counter()
pattern_counts = Counter()
adjacency = {}
face_hits = [0]*6
for code in ice:
    active = [j for j,f in enumerate(faces) if flippable(code,f)]
    activity[len(active)] += 1
    pattern_counts[sum(1 << j for j in active)] += 1
    for j in active: face_hits[j] += 1
    neighbors = {code ^ masks[j] for j in active}
    assert len(neighbors) == len(active) and neighbors <= ice_set
    adjacency[code] = neighbors
assert activity == {0:144, 1:144, 2:120, 3:128, 6:64}, activity
assert face_hits == [192]*6, face_hits
# Joint face-activity census: 0, singleton, all pair, transversal triple, all six.
expected_patterns = {0:144, 63:64}
expected_patterns.update({1<<j:24 for j in range(6)})
expected_patterns.update({(1<<j)|(1<<k):8 for j,k in combinations(range(6),2)})
expected_patterns.update({(1<<j)|(1<<k)|(1<<h):16
                          for j in (0,1) for k in (2,3) for h in (4,5)})
assert pattern_counts == expected_patterns, pattern_counts

# Independently validate that the actual kinetic adjacency components are Q_d.
seen = set()
component_hist = Counter()
for code in ice:
    if code in seen: continue
    orbit = {code}
    pending = [code]
    while pending:
        for nxt in adjacency[pending.pop()]:
            if nxt not in orbit:
                orbit.add(nxt); pending.append(nxt)
    assert not (orbit & seen)
    seen.update(orbit)
    degree_set = {len(adjacency[c]) for c in orbit}
    assert len(degree_set) == 1
    degree = degree_set.pop()
    assert len(orbit) == 1 << degree
    component_hist[degree] += 1
assert len(seen) == 600
assert component_hist == {0:144,1:72,2:30,3:16,6:1}, component_hist
assert sum(len(z) for z in adjacency.values()) // 2 == 576
# A direct, exact-matrix annihilator check uses the enumerated 600 by 600
# transition matrix, rather than relying on the abstract hypercube spectrum.
for start in ice:
    vec = {start:1}
    for root in (0, 1, -1, 2, -2, 3, -3, 4, -4, 6, -6):
        target = defaultdict(int)
        for state,coeff in vec.items():
            target[state] -= root*coeff
            for nxt in adjacency[state]: target[nxt] += coeff
        vec = {k:v for k,v in target.items() if v}
    assert not vec, start

print('PASS line graph: 600 states; face hits 192 each; activity', sorted(activity.items()))
print('PASS joint face-activity polynomial: empty=144, singleton=24, pair=8, opposite-pair transversal triple=16, full=64')
print('PASS components (dimension: multiplicity)', sorted(component_hist.items()))
print('PASS exact adjacency annihilator on all 600 coordinate basis vectors')
print('PASS 576 undirected resonance edges; 263 components')

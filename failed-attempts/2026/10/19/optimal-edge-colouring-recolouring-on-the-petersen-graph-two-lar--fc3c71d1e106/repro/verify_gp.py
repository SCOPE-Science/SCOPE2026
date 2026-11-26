#!/usr/bin/env python3
"""Enumerate all proper four-edge-colourings of the Petersen graph and its single-edge recolouring graph.
Only the Python standard library is required. The graph is built as GP(5,2).
"""
from collections import Counter

E = [tuple(sorted((i, (i + 1) % 5))) for i in range(5)]
E += [(i, i + 5) for i in range(5)]
E += [tuple(sorted((5 + i, 5 + (i + 2) % 5))) for i in range(5)]
assert len(set(E)) == 15
N = len(E)
CONFLICT = [tuple(j for j, (a, b) in enumerate(E) if j != i and (a in e or b in e)) for i, e in enumerate(E)]
assert all(len(x) == 4 for x in CONFLICT)

color = [-1] * N
states = []

def generate(i):
    if i == N:
        states.append(tuple(color))
        return
    forbidden = {color[j] for j in CONFLICT[i] if color[j] >= 0}
    for c in range(4):
        if c not in forbidden:
            color[i] = c
            generate(i + 1)
    color[i] = -1

generate(0)
index = {s:i for i,s in enumerate(states)}
assert len(index) == len(states)
parent = list(range(len(states)))
rank = [0] * len(states)

def find(i):
    while parent[i] != i:
        parent[i] = parent[parent[i]]
        i = parent[i]
    return i

def unite(a,b):
    a,b = find(a),find(b)
    if a == b:
        return
    if rank[a] < rank[b]:
        a,b = b,a
    parent[b] = a
    if rank[a] == rank[b]:
        rank[a] += 1

degrees=Counter()
edges_twice=0
for z, s in enumerate(states):
    d=0
    for e in range(N):
        bad = {s[j] for j in CONFLICT[e]}
        for new in range(4):
            if new == s[e] or new in bad:
                continue
            t = s[:e] + (new,) + s[e+1:]
            assert t in index
            unite(z,index[t])
            d+=1
    degrees[d]+=1
    edges_twice+=d
components=Counter(find(i) for i in range(len(states)))
hist=Counter(components.values())
profiles=Counter(tuple(sorted(s.count(i) for i in range(4))) for s in states if components[find(index[s])] == 1)
assert len(states) == 49920
assert edges_twice % 2 == 0 and edges_twice//2 == 109440
assert hist == Counter({1:960,24480:2})
assert degrees[0] == 960
assert profiles == Counter({(3,4,4,4):960})
assert sum(degrees.values())==49920
assert sum(k*v for k,v in degrees.items())==2*109440
print('representation=GP(5,2)')
print('edges=' + repr(E))
print('states=49920')
print('reconfiguration_edges=109440')
print('components=962')
print('component_size_histogram=' + repr(sorted(hist.items())))
print('isolated_four_edge_colourings=960')
print('isolated_color_class_sizes=' + repr(sorted(profiles.items())))
print('degree_histogram=' + repr(sorted(degrees.items())))
print('VERIFY_OK')

#!/usr/bin/env python3
"""Exhaustive 4-coloring reconfiguration certificate for the Petersen graph.

Independent graph realization: two pentagons (outer and inner pentagram) with spokes.
Only Python standard library is needed.
"""
import itertools
import collections
import hashlib
import json

Q = 4
V = tuple(range(10))
E = set()
for i in range(5):
    E.add(tuple(sorted((i, (i + 1) % 5))))
    E.add(tuple(sorted((i, i + 5))))
    E.add(tuple(sorted((i + 5, ((i + 2) % 5) + 5))))
assert len(E) == 15
N = [set() for _ in V]
for i, j in E:
    N[i].add(j)
    N[j].add(i)
assert all(len(a) == 3 for a in N)

# Independent enumeration rather than a constraint-solver DFS.
colorings = [t for t in itertools.product(range(Q), repeat=10)
             if all(t[u] != t[v] for u, v in E)]
lookup = {c: i for i, c in enumerate(colorings)}
assert len(lookup) == len(colorings) == 12960
neighbors = [[] for _ in colorings]
for idx, c in enumerate(colorings):
    for u in V:
        for new_color in range(Q):
            if new_color != c[u] and all(c[w] != new_color for w in N[u]):
                changed = c[:u] + (new_color,) + c[u+1:]
                neighbors[idx].append(lookup[changed])
assert all(i in neighbors[j] for i, ns in enumerate(neighbors) for j in ns)

# One explicit isomorphism of this ten-vertex graph with KG(5,2).
P = ((0,1),(2,3),(0,4),(1,2),(3,4),
     (2,4),(1,4),(1,3),(0,3),(0,2))
assert all((len(set(P[i]) & set(P[j])) == 0) == ((i,j) in E)
           for i in range(10) for j in range(i+1,10))
index = {pair: i for i, pair in enumerate(P)}

def normalized(c):
    names = {}
    result = []
    for x in c:
        if x not in names:
            names[x] = len(names)
        result.append(names[x])
    return tuple(result)

# S5 automorphisms act on the two-element Kneser coordinates.
permutation_maps = []
for p in itertools.permutations(range(5)):
    permutation_maps.append(tuple(index[tuple(sorted((p[a],p[b])))] for a,b in P))
assert len(set(permutation_maps)) == 120

patterns = {}
for i,c in enumerate(colorings):
    patterns.setdefault(normalized(c),i)
assert all(len(set(key)) in (3,4) for key in patterns)
assert len(patterns)*24 == len(colorings)
seen = set()
reps = []
sizes = []
for pat, idx in patterns.items():
    if pat in seen:
        continue
    orb = set()
    for pos in permutation_maps:
        transported = [None]*10
        for i,j in enumerate(pos):
            transported[j] = pat[i]
        orb.add(normalized(transported))
    seen.update(orb)
    reps.append(idx)
    sizes.append(24*len(orb))
assert seen == set(patterns)
assert len(reps) == 11
assert sum(sizes) == 12960

# All coloring-space eccentricities follow from one BFS per orbit.
ecc_counts=collections.Counter()
orbit_results=[]
for root, size in zip(reps, sizes):
    dist=[-1]*len(colorings)
    dist[root]=0
    queue=collections.deque([root])
    visited=0
    while queue:
        i=queue.popleft();visited+=1
        for j in neighbors[i]:
            if dist[j]<0:
                dist[j]=dist[i]+1
                queue.append(j)
    assert visited == len(colorings)
    ecc=max(dist)
    ecc_counts[ecc]+=size
    orbit_results.append((size,ecc))
assert dict(ecc_counts)=={13:3360,14:9600}
assert sum(map(len,neighbors))//2==53280
assert dict(collections.Counter(map(len,neighbors))) == {6:720,7:2880,8:4560,9:2880,10:1440,11:480}
print(json.dumps({'vertices':len(colorings),'edges':sum(map(len,neighbors))//2,
    'components':1,'radius':min(ecc_counts),'diameter':max(ecc_counts),
    'eccentricity_counts':dict(sorted(ecc_counts.items())),
    'degree_counts':dict(sorted(collections.Counter(map(len,neighbors)).items())),
    'orbit_sizes_eccentricities':sorted(orbit_results)},sort_keys=True))

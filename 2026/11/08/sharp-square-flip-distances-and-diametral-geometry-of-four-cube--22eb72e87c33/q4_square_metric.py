#!/usr/bin/env python3
"""Exact square-flip metric for perfect matchings of Q4. Python 3, stdlib only."""
from collections import Counter, deque
from itertools import combinations, permutations

N = 16
ADJ = {v: tuple(v ^ (1 << a) for a in range(4)) for v in range(N)}

def edge(u, v):
    return (u, v) if u < v else (v, u)

def matchings(unused):
    if not unused:
        yield frozenset()
        return
    u = min(unused)
    for v in ADJ[u]:
        if v in unused:
            for rest in matchings(unused - {u, v}):
                yield rest | {edge(u, v)}

M = sorted(set(matchings(frozenset(range(N)))), key=lambda x: tuple(sorted(x)))
assert len(M) == 272
idx = {m: i for i, m in enumerate(M)}
assert len(idx) == len(M)
SQUARES = set()
for x in range(N):
    for a, b in combinations(range(4), 2):
        y = x ^ (1 << a)
        z = y ^ (1 << b)
        w = x ^ (1 << b)
        SQUARES.add(frozenset((edge(x, y), edge(y, z), edge(z, w), edge(w, x))))
assert len(SQUARES) == 24

G = [set() for _ in M]
for i, m in enumerate(M):
    for face in SQUARES:
        if len(m & face) == 2:
            t = idx[m ^ face]
            assert t != i
            G[i].add(t)
assert all(i in G[j] for i, neigh in enumerate(G) for j in neigh)
assert sum(map(len, G)) // 2 == 768
assert Counter(map(len, G)) == {0:8, 3:32, 4:12, 5:96, 6:48, 8:72, 12:4}

components = []
remaining = set(range(len(M)))
while remaining:
    start = min(remaining)
    seen = {start}
    stack = [start]
    while stack:
        x = stack.pop()
        for y in G[x]:
            if y not in seen:
                seen.add(y)
                stack.append(y)
    components.append(seen)
    remaining -= seen
assert Counter(map(len, components)) == {1:8, 264:1}
large = max(components, key=len)
assert len(large) == 264

all_dist = {}
ecc = {}
unordered = Counter()
for source in sorted(large):
    distances = {source: 0}
    queue = deque([source])
    while queue:
        x = queue.popleft()
        for y in G[x]:
            if y not in distances:
                distances[y] = distances[x] + 1
                queue.append(y)
    assert len(distances) == 264
    all_dist[source] = distances
    ecc[source] = max(distances.values())
    for y, d in distances.items():
        if y > source:
            unordered[d] += 1
assert Counter(ecc.values()) == {7:252, 8:12}
assert dict(sorted(unordered.items())) == {1:768, 2:2640, 3:6032, 4:9360,
                                            5:9504, 6:5296, 7:1104, 8:12}
assert sum(unordered.values()) == 264*263//2
peripheral = {x for x in large if ecc[x] == 8}
assert peripheral == {x for x in range(len(M)) if len(G[x]) == 4}
diametral = {x: {y for y in peripheral if all_dist[x][y] == 8} for x in peripheral}
assert all(len(neighbors) == 2 for neighbors in diametral.values())
seen = set()
sizes = []
for x in sorted(peripheral):
    if x in seen:
        continue
    todo = [x]; seen.add(x); group = set()
    while todo:
        y = todo.pop(); group.add(y)
        for z in diametral[y]:
            if z not in seen:
                seen.add(z);todo.append(z)
    sizes.append(len(group))
assert sorted(sizes) == [4,4,4]
assert sum(len(s) for s in diametral.values()) // 2 == 12

# An explicit sharpness witness, encoded as odd partners of even cube vertices.
evens = [v for v in range(N) if v.bit_count() % 2 == 0]
witness_A = (1, 2, 7, 4, 11, 8, 13, 14)
witness_B = (4, 7, 13, 14, 1, 2, 8, 11)
ua = idx[frozenset(edge(u, v) for u, v in zip(evens, witness_A))]
ub = idx[frozenset(edge(u, v) for u, v in zip(evens, witness_B))]
assert all_dist[ua][ub] == 8

# All automorphisms of Q4 are coordinate permutations followed by bit translations.
def image_of_matching(m, perm, translation):
    def transform(x):
        return translation ^ sum(((x >> a) & 1) << perm[a] for a in range(4))
    return frozenset(edge(transform(u), transform(v)) for u, v in m)

unseen = set(range(len(M)))
orbit_sizes = []
peripheral_orbits = []
for i in range(len(M)):
    if i not in unseen:
        continue
    orbit = {idx[image_of_matching(M[i], p, t)] for p in permutations(range(4))
             for t in range(16)}
    unseen -= orbit
    orbit_sizes.append(len(orbit))
    if i in peripheral:
        peripheral_orbits.append(orbit)
assert sorted(orbit_sizes) == [4, 8, 12, 24, 32, 48, 48, 96]
assert len(peripheral_orbits) == 1 and peripheral_orbits[0] == peripheral

# The twelve diametral pairs form one orbit under coordinate symmetries.
pairset = {tuple(sorted((a,b))) for a in peripheral for b in diametral[a] if a < b}
assert len(pairset) == 12
seed = min(pairset)
transform_orbit = set()
for p in permutations(range(4)):
    for t in range(16):
        a, b = (idx[image_of_matching(M[q], p, t)] for q in seed)
        transform_orbit.add(tuple(sorted((a, b))))
assert transform_orbit == pairset

print('PYTHON_Q4_SQUARE_METRIC_PASS')
print('matchings=272 squares=24 flip_edges=768 components=264+8*1')
print('mobile_radius=7 mobile_diameter=8 mobile_ecc=7:252,8:12')
print('mobile_unordered_distances=' + repr(dict(sorted(unordered.items()))))
print('degree_histogram=' + repr(dict(sorted(Counter(map(len,G)).items()))))
print('hyperoctahedral_orbits=' + repr(sorted(orbit_sizes)))
print('diametral_pair_graph=3*C4 peripheral_iff_degree4=true, 12 pairs form one symmetry orbit')

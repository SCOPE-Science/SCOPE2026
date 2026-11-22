#!/usr/bin/env python3
"""Self-contained exhaustive checker for the Coxeter graph sensor-relocation theorem.
Run with: python3 verify_cyclic.py. No external dependencies.
"""
import itertools
import collections
import json

full = (1 << 28) - 1
lines = {frozenset((i, (i + 1) % 7, (i + 3) % 7)) for i in range(7)}
assert len(lines) == 7
assert all(sum({i, j} <= L for L in lines) == 1 for i, j in itertools.combinations(range(7), 2))
vertices = [frozenset(p) for p in itertools.combinations(range(7), 3) if frozenset(p) not in lines]
assert len(vertices) == 28
nb = [sum(1 << j for j, t in enumerate(vertices) if t.isdisjoint(vertices[i])) for i in range(28)]
assert all(x.bit_count() == 3 for x in nb)
assert sum(x.bit_count() for x in nb) // 2 == 42

def closure(seed):
    obs = seed
    for i in range(28):
        if seed >> i & 1:
            obs |= nb[i]
    while True:
        add = 0
        for i in range(28):
            if obs >> i & 1:
                U = nb[i] & ~obs
                if U and not (U & (U - 1)):
                    add |= U
        if not add & ~obs:
            return obs
        obs |= add

def masks(k):
    return [sum(1 << j for j in s) for s in itertools.combinations(range(28), k)]

assert closure(0) != full
assert not any(closure(m) == full for k in (1, 2) for m in masks(k))
states = [m for m in masks(3) if closure(m) == full]
assert len(states) == 336
state_set = set(states)
jump = {s: set() for s in states}
slide = {s: set() for s in states}
for s in states:
    for i in range(28):
        if not (s >> i) & 1:
            continue
        remain = s ^ (1 << i)
        for j in range(28):
            if s >> j & 1:
                continue
            new = remain | (1 << j)
            if new not in state_set:
                continue
            jump[s].add(new)
            if nb[i] >> j & 1:
                slide[s].add(new)

assert all(s in jump[t] for s in states for t in jump[s])
assert all(s in slide[t] for s in states for t in slide[s])

def distance_layers(A):
    output = collections.Counter()
    eccentricity = collections.Counter()
    for s in A:
        distances = {s: 0}
        queue = collections.deque([s])
        while queue:
            u = queue.popleft()
            for v in A[u]:
                if v not in distances:
                    distances[v] = distances[u] + 1
                    queue.append(v)
        eccentricity[max(distances.values())] += 1
        for t, d in distances.items():
            if t > s:
                output[d] += 1
    return output, eccentricity

jump_layers, jump_ecc = distance_layers(jump)
assert sum(jump_layers.values()) == 336 * 335 // 2
assert jump_layers == {1:1764,2:7392,3:19740,4:22428,5:4844,6:112}
assert jump_ecc == {5:112,6:224}
assert collections.Counter(map(len, jump.values())) == {9:168, 12:168}
assert sum(map(len,jump.values()))//2 == 1764
assert collections.Counter(map(len,slide.values())) == {0:168,2:168}
assert sum(map(len,slide.values()))//2 == 168

unseen = set(states)
components = []
while unseen:
    start = next(iter(unseen))
    component = {start}; queue = [start]; unseen.remove(start)
    while queue:
        for nxt in slide[queue.pop()]:
            if nxt in unseen:
                unseen.remove(nxt); component.add(nxt); queue.append(nxt)
    components.append(component)
assert collections.Counter(map(len,components)) == {1:168,6:28}
assert all(len(slide[s]) == 2 for c in components if len(c)==6 for s in c)
matching_supports = set()
for c in components:
    if len(c) != 6:
        continue
    U = {i for s in c for i in range(28) if (s >> i) & 1}
    assert len(U) == 6
    pairs = [(i, j) for i, j in itertools.combinations(sorted(U), 2) if (nb[i] >> j) & 1]
    assert len(pairs) == 3 and {v for pair in pairs for v in pair} == U
    assert all(all((s >> u & 1) + (s >> v & 1) == 1 for u, v in pairs) for s in c)
    corners = {sum(1 << pair[bit] for pair, bit in zip(pairs, bits)) for bits in itertools.product((0, 1), repeat=3)}
    assert len(corners) == 8 and set(c) <= corners
    missing = corners - c
    assert len(missing) == 2
    a,b = sorted(missing)
    assert a & b == 0 and a | b == sum(1 << v for v in U)
    matching_supports.add(tuple(sorted(pairs)))
assert len(matching_supports) == 28

# Geometry within the parent graph: shortest-path signatures of the three sensors.
def graph_dist(i, j):
    q = collections.deque([(i,0)]); seen={i}
    while q:
        u,d=q.popleft()
        if u==j:return d
        for v in range(28):
            if nb[u]>>v&1 and v not in seen:
                seen.add(v);q.append((v,d+1))
    raise AssertionError('disconnected')
D = [[graph_dist(i,j) for j in range(28)] for i in range(28)]
signatures = collections.Counter()
for s in states:
    v = [i for i in range(28) if s>>i&1]
    sig = tuple(sorted(D[u][w] for u,w in itertools.combinations(v,2)))
    signatures[(sig,len(slide[s]))] += 1
assert signatures == {((3,3,3),0):168,((3,3,4),2):168}

result = dict(vertices=28,edges=42,minimum_size=3,optimal_sets=336,
    jump_edges=1764,jump_degrees={str(k):v for k,v in sorted(collections.Counter(map(len,jump.values())).items())},
    jump_distance_pairs={str(k):v for k,v in sorted(jump_layers.items())},
    jump_eccentricities={str(k):v for k,v in sorted(jump_ecc.items())},
    slide_edges=168,slide_degrees={str(k):v for k,v in sorted(collections.Counter(map(len,slide.values())).items())},
    slide_components={str(k):v for k,v in sorted(collections.Counter(map(len,components)).items())},
    slide_signature_counts={','.join(map(str,k[0]))+':'+str(k[1]):v for k,v in sorted(signatures.items())})
print('VERIFY_OK',json.dumps(result,sort_keys=True))

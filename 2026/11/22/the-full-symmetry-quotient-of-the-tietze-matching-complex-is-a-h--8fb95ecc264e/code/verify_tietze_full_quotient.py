#!/usr/bin/env python3
"""Exact standard-library certificate for the ordinary Tietze matching orbit space.

Run: python3 verify_tietze_full_quotient.py
All incidence, chain and group computations are over the integers.
"""
import itertools
from collections import Counter, defaultdict, deque
from functools import lru_cache

# Petersen = KG(5,2). Expand its vertex {0,1} to a triangle.
P = list(itertools.combinations(range(5), 2))
removed = P.index((0, 1))
neighbors = [i for i, s in enumerate(P) if i != removed and set(s).isdisjoint((0, 1))]
vertices = [i for i in range(10) if i != removed] + [10, 11, 12]
relabel = {v: i for i, v in enumerate(vertices)}
edges = set()
for i, j in itertools.combinations(range(10), 2):
    if removed not in (i, j) and set(P[i]).isdisjoint(P[j]):
        edges.add(tuple(sorted((relabel[i], relabel[j]))))
for a, b in itertools.combinations((10, 11, 12), 2):
    edges.add(tuple(sorted((relabel[a], relabel[b]))))
for a, n in enumerate(neighbors):
    edges.add(tuple(sorted((relabel[10 + a], relabel[n]))))
edges = sorted(edges)
assert len(vertices) == 12 and len(edges) == 18
assert all(sum(v in e for e in edges) == 3 for v in range(12))
triangles = [c for c in itertools.combinations(range(12), 3)
             if all(tuple(sorted(e)) in edges for e in itertools.combinations(c, 2))]
assert triangles == [tuple(sorted(relabel[v] for v in (10, 11, 12)))]

# The 12 full automorphisms arise by permutations of labels preserving {0,1}.
group = []
for p in itertools.permutations(range(5)):
    if set(p[:2]) != {0, 1}:
        continue
    on_petersen = {i: P.index(tuple(sorted(p[x] for x in s)))
                   for i, s in enumerate(P) if i != removed}
    perm = [None] * 12
    for i in range(10):
        if i != removed:
            perm[relabel[i]] = relabel[on_petersen[i]]
    for a, n in enumerate(neighbors):
        perm[relabel[10 + a]] = relabel[10 + neighbors.index(on_petersen[n])]
    group.append(tuple(perm))
assert len(set(group)) == 12
assert all({tuple(sorted((p[a], p[b]))) for a, b in edges} == set(edges)
           for p in group)
# Exhaustive graph automorphism enumeration, independently of Petersen's known group.
target_triangle = set(triangles[0])
aut = set()
for tri_perm in itertools.permutations(triangles[0]):
    partial = dict(zip(triangles[0], tri_perm))
    candidate = {x: [y for y in range(12)
                     if (y in target_triangle) == (x in target_triangle)]
                 for x in range(12)}
    def extend(mapping):
        if len(mapping) == 12:
            aut.add(tuple(mapping[x] for x in range(12)))
            return
        remaining = [x for x in range(12) if x not in mapping]
        options = {}
        for x in remaining:
            opts = [y for y in candidate[x] if y not in mapping.values()
                    and all(((min(x, z), max(x, z)) in edges)
                            == ((min(y, w), max(y, w)) in edges)
                            for z, w in mapping.items())]
            options[x] = opts
        x = min(remaining, key=lambda z: (len(options[z]), z))
        for y in options[x]:
            extend({**mapping, x: y})
    extend(partial)
assert aut == set(group)
edge_id = {e: i for i, e in enumerate(edges)}
actions = [tuple(1 << edge_id[tuple(sorted((p[u], p[v])))] for u, v in edges)
           for p in group]

def transform(mask, action):
    out = 0
    while mask:
        bit = mask & -mask
        out |= action[bit.bit_length() - 1]
        mask -= bit
    return out

@lru_cache(None)
def images(mask):
    return tuple(transform(mask, a) for a in actions)

def orbit(chain):
    a = [images(m) for m in chain]
    return min(tuple(x[i] for x in a) for i in range(12))

# Independently check every subset of the 18 graph edges is a matching.
conflicts = [sum(1 << j for j, (x, y) in enumerate(edges)
                 if i != j and ({u, v} & {x, y}))
             for i, (u, v) in enumerate(edges)]
faces = [0]
for i in range(18):
    faces += [m | (1 << i) for m in faces if m & conflicts[i] == 0]
faces = sorted(set(faces) - {0})
assert len(faces) == 1051
assert Counter(m.bit_count() - 1 for m in faces) == Counter({0: 18, 1: 117,
    2: 335, 3: 408, 4: 165, 5: 8})
assert all(not (m & conflicts[i]) for m in faces
           for i in range(18) if m & (1 << i))

# All strict face chains form the first barycentric subdivision.
@lru_cache(None)
def flags_ending(mask):
    out = {(mask,)}
    sub = (mask - 1) & mask
    while sub:
        for c in flags_ending(sub):
            out.add(c + (mask,))
        sub = (sub - 1) & mask
    return out

flags = set().union(*(flags_ending(f) for f in faces))
assert len(flags) == 162053
representative = {f: orbit(f) for f in flags}
cells = set(representative.values())
assert len(cells) == 13904
assert Counter(len(c) - 1 for c in cells) == Counter({0:121, 1:1250,
    2:3981, 3:5222, 4:2850, 5:480})
# Independent Burnside count: a chain fixed as an ordered tuple is fixed pointwise.
assert sum(sum(all(images(f)[g] == f for f in c) for c in flags)
               for g in range(12)) == 12 * len(cells)

# Integral cellular boundaries. Action cannot reverse a chain's order.
boundaries = {}
cofaces = defaultdict(set)
for c in sorted(cells, key=lambda c: (len(c), c)):
    coeffs = defaultdict(int)
    if len(c) > 1:
        for i in range(len(c)):
            sub = c[:i] + c[i+1:]
            coeffs[representative[sub]] += (-1)**i
    boundaries[c] = {s: v for s, v in coeffs.items() if v}
    for s in boundaries[c]:
        cofaces[s].add(c)
assert sum(map(len, boundaries.values())) == 52461
for c in cells:
    if len(c) >= 3:
        squared = defaultdict(int)
        for s, v in boundaries[c].items():
            for t, w in boundaries[s].items():
                squared[t] += v*w
        assert all(v == 0 for v in squared.values())

# Elementary topological collapses in the regular orbit-cell complex.
active = set(cells)
counts = {c: len(cofaces[c]) for c in cells}
queue = deque(sorted(c for c in cells if counts[c] == 1))
collapse_count = 0
while queue:
    low = queue.popleft()
    if low not in active or counts[low] != 1:
        continue
    high = next(c for c in cofaces[low] if c in active)
    assert len(high) == len(low)+1
    assert abs(boundaries[high].get(low, 0)) == 1
    for c in (low, high):
        active.remove(c)
        for s in boundaries[c]:
            if s in active:
                counts[s] -= 1
                if counts[s] == 1:
                    queue.append(s)
    collapse_count += 1
assert collapse_count == 6524
assert Counter(len(c)-1 for c in active) == Counter({0:43, 1:235,
    2:385, 3:193})

# Exact algebraic (unimodular) chain-pair cancellations. These certify
# integral homology, but are not incorrectly asserted to be space collapses.
B = {c: {s:v for s,v in boundaries[c].items() if s in active}
     for c in active}
rows = defaultdict(set)
for c, d in B.items():
    for s in d:
        rows[s].add(c)
unit_queue = deque(sorted((s,c) for c,d in B.items()
                          for s,v in d.items() if abs(v) == 1))
unit_count = 0
while unit_queue:
    s, c = unit_queue.popleft()
    if s not in B or c not in B or abs(B[c].get(s, 0)) != 1:
        continue
    pivot = B[c][s]
    pivot_column = B[c]
    for other in sorted(rows[s]):
        if other == c:
            continue
        a = B[other][s] // pivot
        for r, v in pivot_column.items():
            old = B[other].get(r, 0)
            new = old - a*v
            if old == 0 and new != 0:
                rows[r].add(other)
            if old != 0 and new == 0:
                rows[r].discard(other)
            if new:
                B[other][r] = new
            else:
                B[other].pop(r, None)
        for r,v in B[other].items():
            if abs(v) == 1:
                unit_queue.append((r,other))
    for r in pivot_column:
        rows[r].discard(c)
    for r in B[s]:
        rows[r].discard(s)
    del B[c]
    del B[s]
    rows.pop(s, None)
    unit_count += 1
assert unit_count == 427
assert Counter(len(c)-1 for c in B) == Counter({0:1, 3:1})
assert all(not d for d in B.values())

# Direct pi1 calculation on the topologically collapsed 2-skeleton.
verts = sorted(c for c in active if len(c) == 1)
one = sorted(c for c in active if len(c) == 2)
two = sorted(c for c in active if len(c) == 3)
parent = {v:v for v in verts}
def root(v):
    while parent[v] != v:
        v = parent[v]
    return v
spanning = set()
for e in one:
    a,b = (orbit((f,)) for f in e)
    ra,rb = root(a),root(b)
    if ra != rb:
        parent[ra] = rb
        spanning.add(e)
assert len(spanning) == 42 and len({root(v) for v in verts}) == 1
generators = {e:i+1 for i,e in enumerate(x for x in one if x not in spanning)}
assert len(generators) == 193

def letter(pair, sign=1):
    e = orbit(pair)
    return () if e in spanning else (sign*generators[e],)

def free_reduce(word):
    stack = []
    for x in word:
        if stack and stack[-1] == -x:
            stack.pop()
        else:
            stack.append(x)
    out = tuple(stack)
    while len(out) > 1 and out[0] == -out[-1]:
        out = out[1:-1]
    return out

relations = [free_reduce(letter((a,b)) + letter((b,c)) + letter((a,c),-1))
             for a,b,c in two]
live = set(generators.values())
nonabelian_count = 0
while live:
    choice = None
    for i, w in enumerate(relations):
        counts = Counter(abs(x) for x in w)
        opts = [(len(w),abs(x),j) for j,x in enumerate(w)
                if counts[abs(x)] == 1 and abs(x) in live]
        if opts:
            o = min(opts)
            if choice is None or o < choice[0]:
                choice = (o,i)
    assert choice is not None, 'unresolved nonabelian presentation'
    (_,g,j),i = choice
    w = relations[i]
    w = w[j:]+w[:j]
    tail = w[1:]
    substitute = tuple(-x for x in reversed(tail)) if w[0] > 0 else tail
    inverse = tuple(-x for x in reversed(substitute))
    newrelations = []
    for k, v in enumerate(relations):
        if k == i:
            continue
        nxt = []
        for x in v:
            nxt.extend(substitute if x == g else inverse if x == -g else (x,))
        newrelations.append(free_reduce(nxt))
    relations = newrelations
    live.remove(g)
    nonabelian_count += 1
assert nonabelian_count == 193 and not live and all(not w for w in relations)
print('TIETZE_FULL_MATCHING_ORBIT_S3_VERIFIED')
print('graph automorphisms=12; matching faces=1051; flags=162053')
print('quotient cells=(121,1250,3981,5222,2850,480)')
print('topological collapses=6524; integral unit chain cancellations=427')
print('residual integral complex: one 0-cell and one 3-cell; differential zero')
print('fundamental group: 193 generators eliminated by exact triangular relations')

"""Independent exact-coordinate audit of rhombicuboctahedral square-face dynamics.

Uses algebraic Euclidean distances, exhaustive cycle detection, an independent
matching recursion, bit-mask flip transitions and disjoint-set connectivity.
Python 3 standard library only.
"""
from collections import Counter, defaultdict
from itertools import combinations, permutations, product

# Coordinates: permutations of (0, ±1, ±(1 + sqrt(2))) are NOT this solid.
# The correct rhombicuboctahedron has permutations of (±1, ±1,
# ±(1+sqrt(2))). Represent each coordinate by (a,b) for a+b*sqrt(2).
V = []
for axis in range(3):
    for signs in product((-1, 1), repeat=3):
        V.append(tuple((s, s if i == axis else 0) for i, s in enumerate(signs)))
assert len(V) == 24 and len(set(V)) == 24

def norm2_difference(u, v):
    rational = irrational = 0
    for (a, b), (c, d) in zip(u, v):
        x, y = a-c, b-d
        rational += x*x + 2*y*y
        irrational += 2*x*y
    return (rational, irrational)

edges = sorted((i, j) for i in range(24) for j in range(i+1, 24)
               if norm2_difference(V[i], V[j]) == (4, 0))
assert len(edges) == 48
edge_index = {e: j for j, e in enumerate(edges)}
adj = [0] * 24
for u, v in edges:
    adj[u] |= 1 << v; adj[v] |= 1 << u
assert set(x.bit_count() for x in adj) == {4}

# This construction does not assume a list of faces: discover all chordless
# induced 4-cycles, and separately verify that exactly 18 exist.
face_sets = []
for vs in combinations(range(24), 4):
    em = [edge_index[e] for e in combinations(vs, 2) if e in edge_index]
    if len(em) != 4:
        continue
    if all(sum(1 for e in em if v in edges[e]) == 2 for v in vs):
        face_sets.append(frozenset(em))
assert len(face_sets) == len(set(face_sets)) == 18
square_masks = [sum(1 << e for e in f) for f in face_sets]

match_masks = []
def enumerate_matchings(free, picked):
    if not free:
        match_masks.append(picked)
        return
    first = (free & -free).bit_length() - 1
    rest = free ^ (1 << first)
    partners = rest & adj[first]
    while partners:
        bit = partners & -partners
        partner = bit.bit_length() - 1
        e = edge_index[tuple(sorted((first, partner)))]
        enumerate_matchings(rest ^ bit, picked | (1 << e))
        partners ^= bit
enumerate_matchings((1 << 24) - 1, 0)
assert len(match_masks) == len(set(match_masks)) == 1088
lookup = {mask: i for i, mask in enumerate(match_masks)}

# Instead of inspecting occupied edges around each face, use symmetric
# difference against its edge-incidence bit vector and match-mask membership.
parent = list(range(len(match_masks)))
sizes = [1] * len(parent)
def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(x, y):
    x = find(x); y = find(y)
    if x != y:
        if sizes[x] < sizes[y]: x, y = y, x
        parent[y] = x; sizes[x] += sizes[y]

resonances = set()
for i, mask in enumerate(match_masks):
    for f in square_masks:
        j = lookup.get(mask ^ f)
        if j is not None and i < j:
            resonances.add((i, j)); union(i, j)
assert len(resonances) == 2616
classes = defaultdict(list)
for i in range(len(match_masks)):
    classes[find(i)].append(i)
assert dict(Counter(map(len, classes.values()))) == {1:14, 2:24, 14:24, 16:6, 594:1}
assert len(classes) == 69

# Face-boundary quotient: linear charges must be unchanged by each flip.
basis = {}
for f in square_masks:
    w = f
    for k in sorted(basis, reverse=True):
        if (w >> k) & 1: w ^= basis[k]
    assert w != 0
    basis[w.bit_length()-1] = w
assert len(basis) == 18

def charge(x):
    for k in sorted(basis, reverse=True):
        if (x >> k) & 1: x ^= basis[k]
    return x

charges = defaultdict(list)
for i, mask in enumerate(match_masks):
    charges[charge(mask)].append(i)
assert dict(Counter(map(len, charges.values()))) == {594:1, 32:3, 28:12, 4:12, 2:7}
assert len(charges) == 35
for ids in charges.values():
    by = Counter(find(i) for i in ids)
    if len(ids) == 594:
        assert list(by.values()) == [594]
    else:
        assert len(by) == 2 and set(by.values()) == {len(ids)//2}

# The root-space of the uniform RK dimer Hamiltonian is the kernel of the
# connected-component graph Laplacian, hence exactly 69-dimensional. If v>t>0,
# every flippable bond contributes a strictly positive 2x2 operator, leaving
# only the 14 isolated matching configurations as zero-energy ground states.
isolated = [i for i in range(len(match_masks)) if not any(i in e for e in resonances)]
assert len(isolated) == 14
assert sum(len(v) for v in classes.values()) == 1088
print('independent coordinate construction: V=24 E=48 induced square faces=18')
print('independent exhaustive matching count: 1088')
print('independent resonance edges:',len(resonances))
print('exact quantum connectivity size histogram:',dict(sorted(Counter(map(len, classes.values())).items())))
print('independent boundary-rank=18 and quotient-charge histogram:',dict(sorted(Counter(map(len, charges.values())).items())))
print('RK zero-energy degeneracy=69; v>t>0 zero-energy degeneracy=14')
print('PASS: independent Euclidean model and exhaustive symmetric-difference transitions')

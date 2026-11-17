#!/usr/bin/env python3
"""Finite certificate for the octahedral character of permutahedron independence homology.

Python 3, standard library only. A complete acyclic matching supplies the
homology concentration; two different signed-trace computations agree for
all full octahedral symmetries. No stored tables or third-party dependencies.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import permutations, product
from math import prod

# The three-dimensional permutahedron (truncated-octahedron) has vertices
# the signed coordinate permutations of (0,1,2) and edges of square length 2.
V = sorted({tuple(s[i]*p[i] for i in range(3))
            for p in set(permutations((0, 1, 2)))
            for s in product((-1, 1), repeat=3)})
assert len(V) == 24
lookup = {v:i for i, v in enumerate(V)}
adj = [0]*24
edges = []
for i in range(24):
    for j in range(i):
        if sum((V[i][k]-V[j][k])**2 for k in range(3)) == 2:
            adj[i] |= 1<<j
            adj[j] |= 1<<i
            edges.append((j, i))
assert len(edges) == 36 and all(a.bit_count()==3 for a in adj)

# Independent simplices as bit masks, including the empty simplex.
faces = set()
def build(mask, available):
    assert mask not in faces
    faces.add(mask)
    while available:
        bit = available & -available
        available ^= bit
        i = bit.bit_length()-1
        build(mask | bit, available & ~adj[i])
build(0, (1<<24)-1)
profile = dict(sorted(Counter(f.bit_count() for f in faces).items()))
assert profile == {0:1, 1:24, 2:240, 3:1304, 4:4218,
                   5:8400, 6:10356, 7:7824, 8:3555,
                   9:960, 10:168, 11:24, 12:2}
assert len(faces) == 37076
assert sum((-1)**m * count for m,count in profile.items()) == 4

# An explicit augmented acyclic matching. All stages use a fixed vertex
# order, pair unmatched faces differing by that vertex, and do not reuse faces.
remaining = set(faces)
matched = []
for i in range(24):
    bit = 1<<i
    pairs_here = [(x, x|bit) for x in remaining
                  if not x & bit and (x|bit) in remaining]
    for a,b in pairs_here:
        assert a in remaining and b in remaining
        remaining.remove(a)
        remaining.remove(b)
    matched.extend(pairs_here)
assert len(matched) == 18536
assert len(remaining) == 4 and {f.bit_count() for f in remaining} == {6}
assert 0 not in remaining
matched_pairs = set(matched)

# Exhaustive acyclicity test: matched Hasse arrows point up; other covers
# point down. A topological ordering of every face is a finite certificate.
out = defaultdict(list)
indeg = dict.fromkeys(faces, 0)
incidences = 0
for upper in faces:
    mask = upper
    while mask:
        b = mask & -mask
        mask ^= b
        lower = upper ^ b
        a,z = (lower,upper) if (lower,upper) in matched_pairs else (upper,lower)
        out[a].append(z)
        indeg[z] += 1
        incidences += 1
assert incidences == 219240
queue = deque(x for x,degree in indeg.items() if degree == 0)
visited = 0
while queue:
    x = queue.popleft()
    visited += 1
    for y in out[x]:
        indeg[y] -= 1
        if indeg[y] == 0:queue.append(y)
assert visited == len(faces) == 37076
# The only unreduced critical cells are four 5-cells, while unpairing the
# empty simplex adds a 0-cell. Hence Ind(G) is a wedge of four 5-spheres.

# Independent backtracking enumeration of the FULL graph automorphism group.
# Graph isomorphisms preserve adjacency AND nonadjacency with prior images.
search_order=[]
visited_vertex={0}
search_queue=deque([0])
while search_queue:
    v=search_queue.popleft()
    search_order.append(v)
    for w in range(24):
        if adj[v] & (1<<w) and w not in visited_vertex:
            visited_vertex.add(w)
            search_queue.append(w)
assert len(search_order)==24
chosen=[-1]*24
used_images=set()
aut_set=set()
def enumerate_automorphisms(depth):
    if depth == 24:
        aut_set.add(tuple(chosen))
        return
    v=search_order[depth]
    for candidate in range(24):
        if candidate in used_images:continue
        if any(bool(adj[v] & (1<<search_order[k])) !=
               bool(adj[candidate] & (1<<chosen[search_order[k]]))
               for k in range(depth)):
            continue
        chosen[v]=candidate
        used_images.add(candidate)
        enumerate_automorphisms(depth+1)
        used_images.remove(candidate)
        chosen[v]=-1
enumerate_automorphisms(0)
assert len(aut_set)==48

# All 48 signed coordinate permutations; the action preserves graph edges.
G = list(product(permutations(range(3)), product((-1,1), repeat=3)))
assert len(G) == 48

def apply(v,g):
    p,s = g
    return tuple(s[i]*v[p[i]] for i in range(3))

def homology_trace_from_faces(perm):
    """Trace H_5 from signed reduced Lefschetz alternating face trace."""
    ret = 0
    for f in faces:
        src = []
        a = f
        while a:
            bit = a & -a
            a ^= bit
            src.append(perm[bit.bit_length()-1])
        image = sum(1<<i for i in src)
        if image != f:continue
        inversions = sum(src[i]>src[j]
                         for i in range(len(src))
                         for j in range(i+1,len(src)))
        ret += (-1)**(len(src)+inversions)
    return ret

def homology_trace_from_orbits(perm):
    """Independent computation via independent-orbit conflict graph at -1."""
    visited = set()
    admissible = []
    for i in range(24):
        if i in visited:continue
        orbit = []
        j = i
        while j not in visited:
            visited.add(j)
            orbit.append(j)
            j=perm[j]
        if all(not (adj[a] & (1<<b))
               for pos,a in enumerate(orbit) for b in orbit[:pos]):
            admissible.append(orbit)
    conflicts = [0]*len(admissible)
    for i,a in enumerate(admissible):
        for j,b in enumerate(admissible[:i]):
            if any(adj[x] & (1<<y) for x in a for y in b):
                conflicts[i] |= 1<<j
                conflicts[j] |= 1<<i
    @lru_cache(None)
    def eval_minus_one(mask):
        if mask == 0:return 1
        bit = mask & -mask
        i = bit.bit_length()-1
        return eval_minus_one(mask^bit) - eval_minus_one((mask^bit)&~conflicts[i])
    return eval_minus_one((1<<len(admissible))-1)

def signed_type(g):
    p,s=g
    seen=set();pos=[];neg=[]
    for i in range(3):
        if i in seen:continue
        cycle=[];j=i
        while j not in seen:
            seen.add(j)
            cycle.append(j)
            j=p[j]
        (pos if prod(s[j] for j in cycle) == 1 else neg).append(len(cycle))
    return tuple(sorted(pos,reverse=True)),tuple(sorted(neg,reverse=True))

classes=defaultdict(list)
all_traces=[]
for g in G:
    perm = [lookup[apply(v,g)] for v in V]
    assert sorted(perm) == list(range(24))
    assert tuple(perm) in aut_set
    assert all(tuple(sorted((perm[i],perm[j]))) in edges for i,j in edges)
    signed = homology_trace_from_faces(perm)
    assert signed == homology_trace_from_orbits(perm)
    p,s=g
    sign_p = (-1)**sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))
    # Direct sum of 1-dimensional flip-parity and signed natural
    # 3-dimensional coordinate module twisted by permutation sign.
    representation_trace = prod(s) + sign_p * sum(s[i] for i in range(3) if p[i] == i)
    assert signed == representation_trace,(g,signed,representation_trace)
    all_traces.append(signed)
    classes[signed_type(g)].append(signed)
assert len(classes)==10
assert sum(all_traces)==0
assert sum(t*t for t in all_traces) == 96 # two irreducible constituents
expected={
    ((),(1,1,1)):(1,-4), ((),(2,1)):(6,2), ((),(3,)):(8,-1),
    ((1,),(1,1)):(3,0), ((1,),(2,)):(6,-2),
    ((1,1),(1,)):(3,0), ((1,1,1),()):(1,4),
    ((2,),(1,)):(6,0), ((2,1),()):(6,0), ((3,),()):(8,1),
}
assert {k:(len(v),v[0]) for k,v in classes.items()} == expected
assert all(len(set(v))==1 for v in classes.values())
print('TRUNCATED_OCTAHEDRON_FULL_SYMMETRY_PASS')
print('vertices=24 edges=36 augmented_faces=37076 hasse_covers=219240')
print('face_vector_by_cardinality='+repr(profile))
print('matched_pairs=18536 critical_5_cells=4 acyclic_toposort=37076')
print('symmetries=48 complete_graph_automorphisms=48 classes=10 trace_methods=2 character_formula=pass')
print('character_by_signed_cycle_type:')
for k in sorted(classes):print(repr(k),len(classes[k]),classes[k][0])
print('invariants=0 inner_product=2 central_inversion_trace=-4')

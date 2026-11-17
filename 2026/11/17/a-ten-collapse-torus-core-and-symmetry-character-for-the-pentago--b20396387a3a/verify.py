#!/usr/bin/env python3
"""Standalone exact finite verification of a pentagonal-bipyramid matching complex.

The enumerator constructs every simplex from the original graph, independently
checks the specified free-face collapses, the residual closed surface,
orientability, and its natural finite symmetry action.
"""
from collections import Counter, defaultdict, deque
from itertools import combinations
from math import gcd

N = 5
R = lambda i: i % N
# Graph vertices 0,...,4 (rim), 5 (top apex), 6 (bottom apex).
# Matching-complex vertices 0,...,4 (rim edges), 5,...,9 and 10,...,14 (spokes).
edge = [tuple(sorted((i, R(i+1)))) for i in range(N)]
edge += [(5, i) for i in range(N)] + [(6, i) for i in range(N)]
assert len(set(edge)) == 15

def compatible(simplex):
    flat = [v for eidx in simplex for v in edge[eidx]]
    return len(flat) == len(set(flat))

faces = {k: set(c for c in combinations(range(15), k+1) if compatible(c))
         for k in range(3)}
assert [len(faces[k]) for k in range(3)] == [15, 55, 40]
assert all(not compatible(c) for c in combinations(range(15), 4))
# The original complex is not a 2-manifold even with boundary: link of r0
# has four link vertices of degree three, not a circle or interval.
original_link_0 = {tuple(x for x in tri if x != 0) for tri in faces[2] if 0 in tri}
original_degrees_0 = Counter(v for e in original_link_0 for v in e)
assert sorted(original_degrees_0.values()) == [2,2,2,2,3,3,3,3]

pairs = []
for i in range(N):
    pairs.extend([
       ((5+i, 10+R(i+2)), (R(i+3), 5+i, 10+R(i+2))),
       ((5+i, 10+R(i+3)), (R(i+1), 5+i, 10+R(i+3))),
    ])
assert len(pairs) == 10
removed_edges, removed_triangles = set(), set()
for f, t in pairs:
    f, t = tuple(sorted(f)), tuple(sorted(t))
    assert f in faces[1] and t in faces[2] and set(f).issubset(t)
    assert sum(set(f).issubset(s) for s in faces[2]) == 1
    assert f not in removed_edges and t not in removed_triangles
    removed_edges.add(f); removed_triangles.add(t)
surface = {0: faces[0], 1: faces[1] - removed_edges,
           2: faces[2] - removed_triangles}
assert [len(surface[k]) for k in range(3)] == [15,45,30]

edge_frequency = Counter(tuple(sorted(e)) for tri in surface[2]
                         for e in combinations(tri,2))
assert set(edge_frequency) == surface[1]
assert set(edge_frequency.values()) == {2}

def num_components(edgeset):
    adj = defaultdict(set)
    for v,w in edgeset:
        adj[v].add(w); adj[w].add(v)
    seen = set(); component_count = 0
    for root in adj:
        if root in seen: continue
        component_count += 1
        q = [root]; seen.add(root)
        for v in q:
            for w in adj[v]:
                if w not in seen: seen.add(w); q.append(w)
    return component_count

assert num_components(surface[1]) == 1
linksizes = {}
for v in range(15):
    links = {tuple(w for w in t if w != v) for t in surface[2] if v in t}
    degrees = Counter(w for e in links for w in e)
    assert len(links) == len(degrees)
    assert set(degrees.values()) == {2}
    assert num_components(links) == 1
    linksizes[v] = len(links)
assert [linksizes[i] for i in range(15)] == [8]*5 + [5]*10

# Rationally independent orientation check: this signed chain gives each
# residual triangle coefficient +/-1 and has exactly zero integral boundary.
representatives = [((0,2,9),1),((0,2,14),-1),
                   ((2,5,11),1),((3,5,11),-1),
                   ((1,5,14),1),((2,5,14),-1)]
def sign(sequence):
    return -1 if sum(sequence[i] > sequence[j] for i in range(len(sequence))
                     for j in range(i+1,len(sequence))) % 2 else 1

def rotation_edge(e):
    if e < 5: return R(e+1)
    if e < 10: return 5+R(e-5+1)
    return 10+R(e-10+1)

z=Counter()
for tri,c in representatives:
    t=list(tri)
    for power in range(5):
        z[tuple(sorted(t))] += c*sign(t)
        t = [rotation_edge(a) for a in t]
assert set(z)==surface[2] and set(z.values()) == {-1,1}
boundary=Counter()
for tri,c in z.items():
    for j in range(3):
        boundary[tri[:j]+tri[j+1:]] += c * (-1)**j
assert all(v==0 for v in boundary.values())
assert 15-45+30==0

# Exact generator/symmetry Lefschetz traces on original K; group order 20.
map_index = {tuple(sorted(x)):i for i,x in enumerate(edge)}
def transformation(a, reflection, swap):
    # vertex action i -> a +/- i; apex swap optional
    vertex = [(a+(-i if reflection else i))%5 for i in range(5)]
    vertex += [6,5] if swap else [5,6]
    emap = []
    for u,v in edge:
        emap.append(map_index[tuple(sorted((vertex[u],vertex[v])))])
    return emap

def chain_traces(emap):
    result=[]
    for k in range(3):
        total=0
        for f in faces[k]:
            image=[emap[v] for v in f]
            if tuple(sorted(image))==f:total += sign(image)
        result.append(total)
    return tuple(result)

def top_sign(emap):
    transformed=Counter()
    for tri,c in z.items():
        image=[emap[v] for v in tri]
        transformed[tuple(sorted(image))]+=c*sign(image)
    ratio=set(transformed[tri]*z[tri] for tri in z)
    assert len(ratio)==1 and next(iter(ratio)) in (-1,1)
    return next(iter(ratio))

for a in range(5):
    for reflection in (False,True):
        for swap in (False,True):
            emap=transformation(a,reflection,swap)
            assert sorted(emap)==list(range(15))
            for k in range(3):
                assert {tuple(sorted(emap[i] for i in f)) for f in faces[k]} == faces[k]
                assert {tuple(sorted(emap[i] for i in f)) for f in surface[k]} == surface[k]
            tr=chain_traces(emap)
            h2=top_sign(emap)
            # Reduced Lefschetz = ordinary alternating chain trace - 1
            h1=h2 - (tr[0]-tr[1]+tr[2]-1)
            assert h2 == (-1 if reflection^swap else 1)
            assert h1 == (-2 if reflection and swap else (0 if reflection or swap else 2))

# Independent mod-2 rank and Betti checks for K; theorem proof does not use them.
matrices=[]
for k in (1,2):
    rows={f:i for i,f in enumerate(sorted(faces[k-1]))}
    cols=[]
    for face in sorted(faces[k]):
        v=0
        for i in range(k+1):v ^= 1<<rows[face[:i]+face[i+1:]]
        cols.append(v)
    piv={};rank=0
    for v in cols:
        while v:
            bit=v.bit_length()-1
            if bit in piv:v^=piv[bit]
            else:piv[bit]=v;rank+=1;break
    matrices.append(rank)
assert matrices == [14,39]
assert (15-matrices[0]-1,55-matrices[0]-matrices[1],40-matrices[1]) == (0,2,1)

print('GRAPH vertices=7 edges=15; MATCHING_COMPLEX faces=(15,55,40); original rim-edge link has degree-three vertices')
print('COLLAPSES count=10; residual faces=(15,45,30); all links C5/C8; closed connected orientable Euler=0')
print('INTEGRAL_ORIENTATION nonzero_triangles=30 boundary_zero=True')
print('AUTOMORPHISMS order=20; H1 and H2 characters verified for all elements')
print('MOD2_BOUNDARIES ranks=(14,39) Betti=(0,2,1)')
print('VERIFY_OK')

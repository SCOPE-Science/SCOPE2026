#!/usr/bin/env python3
"""Exact integral Morse-chain verification for a 4x7 bounded rook complex.
Requires Python 3 and SymPy (integer Smith normal form).
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from sympy import zeros
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

COLS = 7
CAPS = (1, 2, 2, 3)
POWERS = tuple(5**j for j in range(COLS))
N = 5**COLS
valid = bytearray(N)
size = bytearray(N)
faces = []
for code in range(N):
    t = code
    counts = [0, 0, 0, 0]
    degree = 0
    for j in range(COLS):
        v = t % 5
        t //= 5
        if v:
            counts[v-1] += 1
            degree += 1
    if all(counts[i] <= CAPS[i] for i in range(4)):
        valid[code] = 1
        size[code] = degree
        faces.append(code)

# Iterated first-available vertex match on the complete augmented face poset.
# The final matched pair (empty, a vertex) is removed when constructing the
# ordinary unreduced CW Morse model, leaving one critical vertex.
mate = [-1]*N
for col in range(COLS):
    for row in range(1, 5):
        step = row*POWERS[col]
        for f in faces:
            if mate[f] != -1 or (f // POWERS[col]) % 5:
                continue
            g = f + step
            if valid[g] and mate[g] == -1:
                mate[f] = g
                mate[g] = f
assert mate[0] > 0 and size[mate[0]] == 1
for f in faces:
    if mate[f] != -1:
        assert valid[mate[f]]
        assert mate[mate[f]] == f
        assert abs(size[mate[f]]-size[f]) == 1

# Independently verify global gradient acyclicity: unmatched cover arrows
# point from coface to face, matched cover arrows point from face to coface.
indeg = [0]*N
covers = 0
for f in faces:
    for col in range(COLS):
        if (f // POWERS[col]) % 5:
            continue
        for row in range(1, 5):
            g = f + row*POWERS[col]
            if not valid[g]:
                continue
            covers += 1
            if mate[f] == g:
                indeg[g] += 1
            else:
                indeg[f] += 1
q = deque(f for f in faces if indeg[f] == 0)
visited = 0
while q:
    f = q.popleft()
    visited += 1
    g = mate[f]
    if g >= 0 and size[g] == size[f]+1:
        indeg[g] -= 1
        if indeg[g] == 0: q.append(g)
    for col in range(COLS):
        row = (f // POWERS[col]) % 5
        if row:
            h = f - row*POWERS[col]
            if mate[h] != f:
                indeg[h] -= 1
                if indeg[h] == 0: q.append(h)
assert visited == len(faces), 'gradient digraph is not acyclic'

critical = defaultdict(list)
for f in faces:
    if mate[f] == -1:
        critical[size[f]-1].append(f)
assert set(critical) == {3, 4, 5}
assert [len(critical[k]) for k in (3,4,5)] == [2,124,270]

@lru_cache(None)
def boundary(f):
    t = f
    i = 0
    output = []
    for col in range(COLS):
        row = t % 5
        t //= 5
        if row:
            output.append((f-row*POWERS[col], -1 if i % 2 else 1))
            i += 1
    return output

@lru_cache(None)
def reduce_to_critical(f):
    # Projection in the algebraic Morse cancellation induced by the matching.
    g = mate[f]
    if g == -1: return {f:1}
    if size[g] < size[f]: return {}
    signed_faces = boundary(g)
    incidence = next(s for h,s in signed_faces if h==f)
    out = defaultdict(int)
    for h,s in signed_faces:
        if h == f: continue
        for c,v in reduce_to_critical(h).items():
            out[c] -= incidence*s*v
    return {c:v for c,v in out.items() if v}

matrices = {}
for degree in (4,5):
    source = critical[degree]
    target = critical[degree-1]
    rows = {code:i for i,code in enumerate(target)}
    mat = zeros(len(target),len(source))
    for j,f in enumerate(source):
        out = defaultdict(int)
        for h,s in boundary(f):
            for c,v in reduce_to_critical(h).items():
                out[c] += s*v
        for c,v in out.items():
            if v:
                assert c in rows
                mat[rows[c],j] = v
    matrices[degree] = mat
A,B = matrices[4],matrices[5]
assert A*B == zeros(2,270)

def smith_invariants(mat):
    normal = smith_normal_form(mat, domain=ZZ)
    return [int(abs(normal[j,j])) for j in range(min(normal.shape)) if normal[j,j] != 0]
a, b = smith_invariants(A),smith_invariants(B)
assert a == [1,1], ('D4 smith', a)
assert b == [1]*122, ('D5 smith', Counter(b))
assert 270-len(b) == 148 and 124-len(a)-len(b) == 0
f_vector = [sum(size[x]==k for x in faces) for k in range(8)]
assert f_vector == [1,28,315,1820,5670,9240,6930,1680]
red_euler = sum((-1 if k % 2 == 0 else 1)*f_vector[k] for k in range(8))
assert red_euler == -148
print('facets+faces',len(faces),'cover_edges',covers,'matching_pairs',sum(mate[f]!=-1 for f in faces)//2)
print('f-vector including empty',f_vector,'reduced_euler',red_euler)
print('gradient_acyclic',visited==len(faces),'critical dimensions',[(k,len(critical[k])) for k in (3,4,5)])
print('morse_d4',list(A.shape),'smith',Counter(a),'morse_d5',list(B.shape),'smith',Counter(b))
print('boundary_composition_zero',True)
print('reduced_integral_homology: H5=Z^148, all other Hk=0')
print('unreduced Morse CW: one 0-cell, two 3-cells, 124 4-cells, 270 5-cells')
print('homotopy: wedge of 148 five-spheres by 2-connectivity and homological Whitehead')

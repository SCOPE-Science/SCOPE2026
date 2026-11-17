#!/usr/bin/env python3
"""Exact integral and rational homology calculations for M(L(K5)).
Uses only Python's standard library; no precomputed matrix or external data.
"""
from collections import Counter, deque
from functools import lru_cache
from itertools import permutations
from math import factorial

points = tuple(range(5))
V = tuple((a, b) for a in range(5) for b in range(a + 1, 5))
E = tuple((i, j) for i in range(10) for j in range(i + 1, 10)
          if set(V[i]).intersection(V[j]))
assert len(V) == 10 and len(E) == 30

# Enumerate all matchings, including the empty face.
faces_by_size = [[0]]
for k in range(1, 6):
    new = []
    for mask in faces_by_size[-1]:
        used = 0
        for j in range(30):
            if mask & (1 << j):
                used |= (1 << E[j][0]) | (1 << E[j][1])
        for j in range(30):
            if j < (mask.bit_length()):
                continue
            a, b = E[j]
            if not (used & ((1 << a) | (1 << b))):
                new.append(mask | (1 << j))
    faces_by_size.append(new)
counts = tuple(map(len, faces_by_size))
assert counts == (1, 30, 285, 980, 1020, 144), counts
all_faces = set(f for row in faces_by_size for f in row)
assert len(all_faces) == 2460

def ordered_vertices(face):
    return [i for i in range(30) if face & (1 << i)]

# Descending-pivot acyclic matching. Every original face is used once.
remaining = set(all_faces)
pairs = []
for j in range(29, -1, -1):
    for low in sorted(f for f in remaining if not (f & (1 << j))):
        high = low | (1 << j)
        if low in remaining and high in remaining:
            remaining.remove(low)
            remaining.remove(high)
            pairs.append((low, high))
critical2 = sorted(f for f in remaining if f.bit_count() == 3)
critical3 = sorted(f for f in remaining if f.bit_count() == 4)
assert len(pairs) == 1146
assert sum(low == 0 for low, high in pairs) == 1
assert len(remaining) == 168 and len(critical2) == 8 and len(critical3) == 160

# Independently check acyclicity of the oriented Hasse graph by Kahn's algorithm.
matched = set(pairs)
indegree = {f: 0 for f in all_faces}
adjacency = {f: [] for f in all_faces}
for high in all_faces:
    for j in ordered_vertices(high):
        low = high ^ (1 << j)
        source, target = (low, high) if (low, high) in matched else (high, low)
        adjacency[source].append(target)
        indegree[target] += 1
queue = deque(f for f, deg in indegree.items() if deg == 0)
visited = 0
while queue:
    source = queue.popleft()
    visited += 1
    for target in adjacency[source]:
        indegree[target] -= 1
        if indegree[target] == 0:
            queue.append(target)
assert visited == len(all_faces), (visited, len(all_faces))

# Exact integral elementary chain cancellations (pivot coefficients always +/-1).
boundary = {}
for face in all_faces:
    boundary[face] = {face ^ (1 << j): (-1 if s % 2 else 1)
                      for s, j in enumerate(ordered_vertices(face))}
for low, high in pairs:
    eps = boundary[high].get(low, 0)
    assert abs(eps) == 1, (low, high, eps)
    dimension = high.bit_count()
    other = [(f, d[low]) for f, d in boundary.items()
             if f != high and f.bit_count() == dimension and low in d]
    for f, a in other:
        d = boundary[f]
        for q, b in boundary[high].items():
            value = d.get(q, 0) - a * eps * b
            if value:
                d[q] = value
            else:
                d.pop(q, None)
    for f, d in boundary.items():
        if f != high and f.bit_count() == dimension:
            d.pop(low, None)
        if f.bit_count() == dimension + 1:
            d.pop(high, None)
    del boundary[low]
    del boundary[high]
assert set(boundary) == remaining
B = [[boundary[h].get(q, 0) for h in critical3] for q in critical2]
assert len(B) == 8 and len(B[0]) == 160
assert sum(v != 0 for row in B for v in row) == 625
assert max(abs(v) for row in B for v in row) == 4
assert all(not boundary[q] for q in critical2)
assert all(set(boundary[h]).issubset(critical2) for h in critical3)

# Small exact determinant and finite-field rank certificates.
def determinant(A):
    n = len(A)
    mat = [list(row) for row in A]
    assert all(len(row) == n for row in mat)
    sign = 1
    previous = 1
    for k in range(n-1):
        if mat[k][k] == 0:
            r = next((j for j in range(k+1,n) if mat[j][k]),None)
            if r is None:
                return 0
            mat[k],mat[r] = mat[r],mat[k]
            sign = -sign
        pivot = mat[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                value = mat[i][j] * pivot - mat[i][k] * mat[k][j]
                assert value % previous == 0
                mat[i][j] = value // previous
            mat[i][k] = 0
        previous = pivot
    return sign * mat[-1][-1]

def extract(rows, cols):
    return [[B[i][j] for j in cols] for i in rows]
minor7rows = (1, 2, 3, 4, 5, 6, 7)
minor7cols = (11, 20, 46, 60, 62, 97, 115)
minor8cols = (11, 13, 51, 96, 97, 108, 116, 117)
assert determinant(extract(minor7rows, minor7cols)) == -1
assert abs(determinant(extract(tuple(range(8)), minor8cols))) == 3

def modrank(rows, prime):
    A = [[v % prime for v in row] for row in rows]
    m, n = len(A),len(A[0])
    r = 0
    for j in range(n):
        i = next((k for k in range(r,m) if A[k][j]), None)
        if i is None:
            continue
        A[r],A[i] = A[i],A[r]
        a = pow(A[r][j], -1, prime)
        A[r] = [(a*v) % prime for v in A[r]]
        for k in range(r+1,m):
            c = A[k][j]
            if c:
                A[k] = [(v-c*w) % prime for v,w in zip(A[k],A[r])]
        r += 1
        if r == m:
            break
    return r
assert modrank(B,3) == 7
assert modrank(B,2) == 8
assert modrank(B,5) == 8
# Thus coker B has order exactly 3, and ker B is free rank 152.

# Complete signed Lefschetz character of the degree-three rational homology.
def cycle_type(p):
    seen=set(); lengths=[]
    for i in range(len(p)):
        if i not in seen:
            j=i;length=0
            while j not in seen:
                seen.add(j);length+=1;j=p[j]
            lengths.append(length)
    return tuple(sorted(lengths,reverse=True))

def parity_sign(values):
    return (-1)**sum(values[i] > values[j]
                     for i in range(len(values)) for j in range(i+1,len(values)))

vindex={v:i for i,v in enumerate(V)}
eindex={e:i for i,e in enumerate(E)}
character={}
for p in permutations(points):
    typ=cycle_type(p)
    ve=[vindex[tuple(sorted((p[a],p[b])))] for a,b in V]
    em=[eindex[tuple(sorted((ve[i],ve[j])))] for i,j in E]
    lefschetz = 0
    for face in all_faces:
        old=ordered_vertices(face)
        image=[em[j] for j in old]
        if sorted(image) == old:
            lefschetz += (-1 if len(old)%2==0 else 1) * parity_sign(image)
    if typ in character:
        assert character[typ] == -lefschetz
    character[typ] = -lefschetz
expected = {(1,1,1,1,1):152, (2,1,1,1):0, (2,2,1):4,
            (3,1,1):-4, (3,2):0, (4,1):-2, (5,):-3}
assert character == expected, character

@lru_cache(None)
def partitions(n, top=None):
    if n<0: return ()
    if n==0: return ((),)
    if top is None:top=n
    return tuple((k,)+tail for k in range(min(top,n),0,-1)
                 for tail in partitions(n-k,k))

@lru_cache(None)
def sn_character(shape,typ):
    if not typ:
        return 1 if not shape else 0
    r=typ[0]
    before={(i,j) for i,length in enumerate(shape) for j in range(length)}
    value=0
    for smaller in partitions(sum(shape)-r):
        if any(i>=len(shape) or v>shape[i] for i,v in enumerate(smaller)):
            continue
        after={(i,j) for i,length in enumerate(smaller) for j in range(length)}
        strip=before-after
        if len(strip)!=r: continue
        if any((i+1,j) in strip and (i,j+1) in strip and (i+1,j+1) in strip
               for i,j in strip):
            continue
        reachable={next(iter(strip))};stack=list(reachable)
        while stack:
            i,j=stack.pop()
            for neighbor in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
                if neighbor in strip and neighbor not in reachable:
                    reachable.add(neighbor);stack.append(neighbor)
        if len(reachable)!=r: continue
        height=len({i for i,j in strip})
        value+=(-1)**(height-1)*sn_character(smaller,typ[1:])
    return value

multiplicities={}
for shape in partitions(5):
    numerator=0
    # Multiply by 120 for exact integer arithmetic.
    for typ,trace in character.items():
        centralizer=1
        for length,n in Counter(typ).items():
            centralizer*=length**n*factorial(n)
        numerator+=(120//centralizer)*trace*sn_character(shape,typ)
    assert numerator % 120 == 0
    multiplicities[shape]=numerator//120
assert multiplicities == {(5,):0,(4,1):5,(3,2):8,(3,1,1):6,
                          (2,2,1):7,(2,1,1,1):5,(1,1,1,1,1):1}
assert sum(multiplicities[s]*sn_character(s,(1,1,1,1,1))
           for s in multiplicities)==152
print('graph_vertices=10 graph_edges=30; face_counts_by_cardinality=',counts)
print('morse_pairs=1146 critical_2=8 critical_3=160; oriented_hasse_dag=PASS')
print('morse_boundary=8x160 entries_nonzero=625 largest_absolute_entry=4')
print('7_minor=-1 8_minor_abs=3 rank_mod_3=7; homotopy=Moore(Z/3,2) wedge 152 S^3')
print('S5_character_by_cycle_type=',sorted(character.items()))
print('S5_specht_multiplicities=',sorted(multiplicities.items()))
print('TRIANGULAR_T5_MATCHING_TORSION_CHARACTER_PASS')

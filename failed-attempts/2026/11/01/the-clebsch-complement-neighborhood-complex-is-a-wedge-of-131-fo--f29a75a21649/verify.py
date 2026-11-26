#!/usr/bin/env python3
"""Exact finite certificate for the Clebsch-complement neighborhood complex.

Uses Python standard library only. All orientations are increasing-vertex order.
Run: python verify.py
"""
from collections import Counter
from functools import lru_cache
import heapq
from itertools import permutations

N = 16
STEPS = (1, 2, 4, 8, 15)
FULL = (1 << N) - 1

def near(x, y):
    return x != y and (x ^ y) in STEPS

def bits(m):
    while m:
        b = m & -m
        yield b.bit_length() - 1
        m ^= b

def count_common(x, y):
    return sum(near(x, z) and near(y, z) for z in range(N))

assert all(sum(near(x, y) for y in range(N)) == 5 for x in range(N))
assert all(count_common(x,y) == (0 if near(x,y) else 2)
           for x in range(N) for y in range(x+1,N))

# Each maximal neighborhood in the graph complement contains ten vertices.
facets = [sum(1 << y for y in range(N) if y != x and not near(x,y))
          for x in range(N)]
assert len(set(facets)) == 16 and all(f.bit_count() == 10 for f in facets)
faces = set()
for f in facets:
    sub = f
    while sub:
        faces.add(sub)
        sub = (sub - 1) & f
expected_counts = (16,120,560,1740,3312,3240,1920,720,160,16)
fvec = tuple(sum(m.bit_count() == d+1 for m in faces) for d in range(10))
assert fvec == expected_counts
assert len(faces) == 11804

# First perform genuine elementary free-face collapses. Track immediate
# upper coface counts and use a highest-dimension-first priority queue.
F = set(faces)
co = {m:0 for m in F}
for m in F:
    for v in bits(m):
        s = m ^ (1 << v)
        if s: co[s] += 1
heap = [(-m.bit_count(), m) for m in F if co[m] == 1]
heapq.heapify(heap)
collapses = []
while heap:
    _, lo = heapq.heappop(heap)
    if lo not in F or co[lo] != 1:
        continue
    possible = [lo | (1<<v) for v in range(N)
                if not (lo >> v) & 1 and (lo | (1<<v)) in F]
    assert len(possible) == 1
    up = possible[0]
    # The unique immediate coface must be maximal, as an upper extension
    # would force a second immediate coface of lo.
    assert not any((up | (1<<v)) in F for v in range(N)
                   if not (up >> v) & 1)
    F.remove(lo); F.remove(up)
    collapses.append((lo,up))
    for f in (lo,up):
        for v in bits(f):
            s = f ^ (1<<v)
            if s in F:
                co[s] -= 1
                if co[s] == 1:
                    heapq.heappush(heap,(-s.bit_count(),s))
assert len(collapses) == 4780
assert len(F) == 2244
assert Counter(m.bit_count()-1 for m in F) == {0:16,1:120,2:500,3:936,4:672}

# The remaining vertex-toggle pairings are checked acyclic on the full
# original face poset, together with the elementary collapses.
critical = set(F)
toggles=[]
for v in range(N):
    for m in sorted(critical):
        up = m | (1<<v)
        if not m & (1<<v) and up in critical:
            critical.remove(m);critical.remove(up)
            toggles.append((m,up))
assert len(toggles) == 1050
assert Counter(m.bit_count()-1 for m in critical) == {0:1,3:6,4:137}

matches=collapses+toggles
assert len(matches)==5830 and len({a for pair in matches for a in pair})==2*5830
up_of = {lo: up for lo, up in matches}
lo_of = {up: lo for lo, up in matches}

# In the reversed-cover directed Hasse diagram, check acyclicity by
# an exhaustive topological sort (not merely a gradient-path sample).
indeg = {m:0 for m in faces}
adj = {m:[] for m in faces}
count=0
for lo in faces:
    for v in range(N):
        if (lo >> v) & 1:
            continue
        up = lo | (1<<v)
        if up not in faces:
            continue
        a,b = (up,lo) if up_of.get(lo)==up else (lo,up)
        adj[a].append(b); indeg[b] += 1;count += 1
assert count==65680
queue=[m for m,d in indeg.items() if d==0]
k=0
while k<len(queue):
    m=queue[k];k+=1
    for nxt in adj[m]:
        indeg[nxt]-=1
        if indeg[nxt]==0:queue.append(nxt)
assert len(queue)==len(faces)==11804

# Signed algebraic Morse boundary from critical 4-cells to 3-cells.
# For a 3-simplex paired upward into a 4-simplex, eliminate its
# pivot coefficient ±1 by the standard gradient-path recurrence.
c3=sorted(m for m in critical if m.bit_count()==4)
c4=sorted(m for m in critical if m.bit_count()==5)
index3={m:i for i,m in enumerate(c3)}
@lru_cache(None)
def reduce3(m):
    if m in index3:
        return {index3[m]:1}
    up=up_of.get(m)
    if up is None:
        return {}
    assert up.bit_count()==5 and m.bit_count()==4
    vs=list(bits(up))
    piv=next(i for i,v in enumerate(vs) if (up^(1<<v))==m)
    out={}
    for i,v in enumerate(vs):
        sub=up^(1<<v)
        if sub==m: continue
        coef=-((-1)**(i+piv))
        for row,a in reduce3(sub).items():
            out[row]=out.get(row,0)+coef*a
    return {j:a for j,a in out.items() if a}

boundary=[[0]*len(c4) for _ in range(len(c3))]
for j,up in enumerate(c4):
    for i,v in enumerate(bits(up)):
        for row,a in reduce3(up^(1<<v)).items():
            boundary[row][j] += ((-1)**i)*a
assert len(boundary)==6 and len(boundary[0])==137
assert max(abs(v) for row in boundary for v in row)==1

# Explicit 6-by-6 unimodular minor, selected with zero-based critical
# 4-cell column indices in ascending face-mask order.
columns=(2,4,9,10,23,26)
minor=[[row[j] for j in columns] for row in boundary]
expected_minor=[[-1,0,0,0,1,-1],
                [ 1,0,0,0,0, 1],
                [-1,-1,0,0,0,0],
                [0,0,-1,0,-1,0],
                [0,0,0,-1,0,-1],
                [0,-1,0,0,0,0]]
assert minor==expected_minor

def det(a):
    # Exact Leibniz formula for the small 6-by-6 certificate.
    val=0
    for p in permutations(range(len(a))):
        inversions=sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
        prod=1
        for i,j in enumerate(p): prod*=a[i][j]
        val+=(-1 if inversions%2 else 1)*prod
    return val
assert det(minor)==1

# An independent direct computation of every mod-2 simplicial boundary
# rank on the complete unreduced neighborhood complex.
bydim={d:sorted(m for m in faces if m.bit_count()==d+1) for d in range(10)}
def boundary_rank_2(d):
    p={m:i for i,m in enumerate(bydim[d-1])}
    piv={}
    for u in bydim[d]:
        vector=0
        for v in bits(u):vector ^= 1<<p[u^(1<<v)]
        while vector:
            k=vector.bit_length()-1
            if k not in piv:
                piv[k]=vector;break
            vector^=piv[k]
    return len(piv)
ranks=tuple(boundary_rank_2(d) for d in range(1,10))
assert ranks==(15,105,455,1285,1896,1344,576,144,16)
reduced_betti=tuple(fvec[d]-(ranks[d-1] if d else 0)
                    -(ranks[d] if d<9 else 0)-(1 if d==0 else 0)
                    for d in range(10))
assert reduced_betti==(0,0,0,0,131,0,0,0,0,0)

# Directly test the definition of the Clebsch dominance complex, rather
# than using the Alexander-duality formula to construct its faces.
dom_counts=Counter()
for sigma in range(1<<N):
    dominating=FULL^sigma
    covered=dominating
    for x in bits(dominating):
        for s in STEPS:
            covered |= 1<<(x^s)
    if covered==FULL:
        dom_counts[sigma.bit_count()-1]+=1
expected_dominance={-1:1,0:16,1:120,2:560,3:1820,4:4368,5:7992,
                    6:11280,7:12150,8:9520,9:4768,10:1056,11:80}
assert dict(dom_counts)==expected_dominance
chi=sum((-1)**k*v for k,v in dom_counts.items() if k>=0)
assert chi==-130  # 1 - 131, consistent with integral Alexander duality.

print('GRAPH: strongly regular (16,5,0,2); complement valency 10')
print('COMPLEMENT NEIGHBORHOOD: faces',len(faces),'f-vector',fvec)
print('MATCHED: elementary',len(collapses),'toggles',len(toggles))
print('MORSE CRITICAL: one degree-0, six degree-3, 137 degree-4')
print('HASSE ACYCLIC:',len(queue),'vertices,',count,'covers checked')
print('SIGNED MORSE BOUNDARY: 6 x 137; unimodular minor columns',columns,'determinant',det(minor))
print('DIRECT MOD-2 RANKS:',ranks)
print('DIRECT MOD-2 REDUCED BETTI:',reduced_betti)
print('CLEBSCH DOMINANCE: face counts',dict(sorted(dom_counts.items())))
print('CLEBSCH DOMINANCE: Euler characteristic',chi)
print('HOMOTOPY: neighborhood of complement = wedge of 131 four-spheres')
print('INTEGRAL HOMOLOGY: dominance has Z^131 in reduced degree 9 only')
print('VERIFY_CLEBSCH_COMPLEMENT_NEIGHBORHOOD_131_S4_AND_DOMINANCE_131_H9_OK')

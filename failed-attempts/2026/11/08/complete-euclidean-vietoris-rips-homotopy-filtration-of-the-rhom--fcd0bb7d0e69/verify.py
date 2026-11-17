#!/usr/bin/env python3
"""Independent exact checker for a 14-point Euclidean Rips homotopy calculation.

Run next to collapse_certificate.json: python3 verify.py
Only the Python standard library is required. All distances are squared integers.
"""
import collections
import itertools
import json
from pathlib import Path

P = list(itertools.product((-1, 1), repeat=3))
P += [tuple(2*s if j==i else 0 for j in range(3))
      for i in range(3) for s in (-1, 1)]
N=len(P)
assert N==14 and len(set(P))==14
D = [[sum((P[i][k]-P[j][k])**2 for k in range(3))
      for j in range(N)] for i in range(N)]
assert collections.Counter(D[i][j] for i in range(N) for j in range(i)) == {
    3:24, 4:12, 8:24, 11:24, 12:4, 16:3}

def faces(q):
    return {m for m in range(1, 1<<N)
            if all(D[i][j]<=q for i in range(N) if (m>>i)&1
                   for j in range(i) if (m>>j)&1)}

def vector(fs):
    c=collections.Counter(m.bit_count()-1 for m in fs)
    return tuple(c[i] for i in range(max(c)+1))

def free_pair(fs,a,b):
    if a not in fs or b not in fs or a & b != a or b.bit_count()!=a.bit_count()+1:
        return False
    # A free face occurs in exactly one maximal coface, equivalently
    # exactly one containing face of any positive codimension.
    return all((m==b or m & a != a or m==a) for m in fs)

def bettis_F2(fs):
    cells=collections.defaultdict(list)
    for m in fs:cells[m.bit_count()-1].append(m)
    rank={}
    for k in range(1,max(cells)+1):
        idx={mask:i for i,mask in enumerate(cells[k-1])}
        piv={}
        for mask in cells[k]:
            col=0
            for i in range(N):
                if (mask>>i)&1:col ^= 1<<idx[mask^(1<<i)]
            while col:
                h=col.bit_length()-1
                if h in piv:col ^= piv[h]
                else:piv[h]=col;break
        rank[k]=len(piv)
    out=[len(cells[i])-rank.get(i,0)-rank.get(i+1,0)
         for i in range(max(cells)+1)]
    out[0]-=1
    return tuple(out)

F={q:faces(q) for q in (3,4,8,11,12)}
assert {q:vector(f) for q,f in F.items()}=={
  3:(14,24),
  4:(14,36,24),
  8:(14,60,100,60,6),
  11:(14,84,280,560,672,448,128),
  12:(14,88,328,806,1372,1652,1408,833,326,76,8)}
assert {q:bettis_F2(F[q]) for q in (3,4,8,11)}=={
  3:(0,11), 4:(0,0,1), 8:(0,0,0,1,0),
  11:(0,0,0,0,0,0,1)}
# The first nontrivial complex has no 2-faces and is connected.
assert len(F[3])==38
# At squared scale 4, check the closed triangulated sphere: all links are circles,
# and the complex has Euler characteristic 2. This is also the geometric
# triangulation of the convex rhombic dodecahedron's twelve rhombic facets.
triangles=[m for m in F[4] if m.bit_count()==3]
assert len(triangles)==24
for v in range(N):
    link_vertices={i for i in range(N) if i!=v and (1<<v)|(1<<i) in F[4]}
    link_edges=[(i,j) for i,j in itertools.combinations(sorted(link_vertices),2)
                if (1<<v)|(1<<i)|(1<<j) in F[4]]
    assert len(link_edges)==len(link_vertices)
    assert all(sum(i in e for e in link_edges)==2 for i in link_vertices)
    reached={min(link_vertices)}
    for _ in range(len(link_vertices)):
        reached |= {j for e in link_edges if e[0] in reached or e[1] in reached for j in e}
    assert reached==link_vertices
assert 14-36+24==2
# At scale 8, replay a complete sequence of ordinary free-face collapses to
# the boundary of a four-dimensional cross-polytope on the 8 cube vertices.
cert=json.loads((Path(__file__).parent/'collapse_certificate.json').read_text())
assert cert['coordinates']==[list(x) for x in P]
assert cert['threshold_squared']==8
pairs=cert['elementary_collapse_pairs_bitmasks']
assert len(pairs)==80 and len({tuple(p) for p in pairs})==80
active=F[8].copy()
for j,(a,b) in enumerate(pairs):
    assert free_pair(active,a,b), ('not an elementary collapse',j,a,b)
    active.remove(a);active.remove(b)
assert len(active)==80
assert all((m>>8)==0 for m in active)
assert active=={m for m in F[8] if m < (1<<8)}
# Check the latter complex is the join of four disjoint antipodal pairs.
cube_opposites=[(i,j) for i in range(8) for j in range(i) if D[i][j]==12]
assert len(cube_opposites)==4
assert {x for pair in cube_opposites for x in pair}==set(range(8))
assert all((i,j) in cube_opposites or D[i][j]<=8
           for i in range(8) for j in range(i))
# At scale 11 the whole complex is the 7-fold join of two-point sets.
missing11=[(i,j) for i in range(N) for j in range(i) if D[i][j]>11]
assert len(missing11)==7
assert {x for pair in missing11 for x in pair}==set(range(N))
assert len(F[11])==3**7-1
# At scale 12 only the three antipodal axis pairs remain forbidden.
missing12=[(i,j) for i in range(N) for j in range(i) if D[i][j]>12]
assert missing12==[(9,8),(11,10),(13,12)]
# Cube vertices form a full simplex joined to the axis subcomplex: a cone.
assert all(sum(1<<i for i in c) in F[12]
           for r in range(1,9) for c in itertools.combinations(range(8),r))
assert all((1<<0)|m in F[12] for m in F[12])
print('VERIFY_OK; thresholds=3,4,8,11,12,16; collapse_pairs=80')
print('face_vectors=' + repr({q:vector(f) for q,f in F.items()}))
print('reduced_F2_betti=' + repr({q:bettis_F2(F[q]) for q in (3,4,8,11)}))
print('homotopy=14points,wedge11S1,S2,S3,S6,point')

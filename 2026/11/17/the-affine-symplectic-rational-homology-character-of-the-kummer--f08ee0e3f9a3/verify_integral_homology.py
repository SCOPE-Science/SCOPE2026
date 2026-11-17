#!/usr/bin/env python3
"""Exhaustive elementary collapse plus integer Smith form for Kummer biplane topology."""
from collections import Counter, defaultdict
from itertools import combinations
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form

# Six noncentral rook neighbors of each grid point.
blocks=[]
for a in range(4):
    for b in range(4):
        block=frozenset([4*a+c for c in range(4) if c!=b]
                       + [4*c+b for c in range(4) if c!=a])
        blocks.append(block)
faces={frozenset(c) for block in blocks for k in range(1,7)
       for c in combinations(sorted(block),k)}
assert len(faces)==808
pairs=0
while True:
    cofac=defaultdict(list)
    for f in faces:
        if len(f)>1:
            for v in f:
                cofac[f-{v}].append(f)
    free=[(len(s),tuple(sorted(s)),s,cofac[s][0])
          for s in faces if len(cofac.get(s,()))==1]
    if not free:break
    free.sort(key=lambda t:(-t[0],t[1]))
    _,_,s,t=free[0]
    faces.remove(s);faces.remove(t)
    pairs+=1
assert len(faces)==808-2*pairs
assert len(faces)==296 and pairs==256
assert Counter(map(len,faces))=={1:16,2:120,3:160}
triangles=sorted(tuple(sorted(f)) for f in faces if len(f)==3)
edges=sorted(tuple(sorted(f)) for f in faces if len(f)==2 and 0 not in f)
edge_row={e:i for i,e in enumerate(edges)}
M=[[0]*len(triangles) for _ in edges]
for j,(a,b,c) in enumerate(triangles):
    for edge,sign in [((a,b),1),((a,c),-1),((b,c),1)]:
        if edge in edge_row:
            M[edge_row[edge]][j]=sign
S=smith_normal_form(Matrix(M),domain=ZZ)
factors=Counter(abs(int(S[i,i])) for i in range(min(S.shape)))
assert factors=={1:104,2:1},factors
print('KUMMER_INTEGRAL_HOMOLOGY_VERIFIED')
print('elementary_collapse_pairs=256 remaining_faces=296')
print('remaining_vertices=16 edges=120 triangles=160; graph spanning tree algebraically eliminated')
print('boundary_smith_factors=1x104,2x1')
print('H1=Z/2 H2=Z^55 other_reduced_homology=0')

#!/usr/bin/env python3
"""Exact elementary integer checks for the toric fourfold of Bruhat interval [1324,4231]."""
from itertools import combinations, permutations, product
from fractions import Fraction

P1=((0,1,1,0),(0,1,0,0),(1,0,0,0),(0,0,0,0))
P2=((1,0,1,0),(0,0,1,0),(1,0,0,0),(0,0,0,0))
P3=((1,0,0,1),(0,0,0,1),(0,0,1,0),(0,0,0,0))
R=((1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1),
   (0,0,0,-1),(0,1,-1,-1),(0,-1,0,0),(-1,-1,0,1))
b=(0,0,0,0,-1,-2,-1,-2)
PAIR=((0,7),(1,6),(2,5),(3,4))

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def det4(rows):
    z=0
    for pi in permutations(range(4)):
        inv=sum(pi[i]>pi[j] for i in range(4) for j in range(i+1,4))
        z+=(-1 if inv%2 else 1)*rows[0][pi[0]]*rows[1][pi[1]]*rows[2][pi[2]]*rows[3][pi[3]]
    return z

def inter(ids,rhs):
    rows=[R[i] for i in ids]
    d=det4(rows)
    if not d:return None
    return tuple(Fraction(det4([[rhs[ids[k]] if j==col else rows[k][j] for j in range(4)] for k in range(4)]),d)
                 for col in range(4))

def poly_vertices(rhs):
    ret=set()
    for ids in combinations(range(8),4):
        x=inter(ids,rhs)
        if x is not None and all(dot(x,r)>=rhs[i] for i,r in enumerate(R)):
            ret.add(x)
    return ret

sums={tuple(a[i]+bb[i]+c[i] for i in range(4)) for a,bb,c in product(P1,P2,P3)}
assert len(sums)==34
assert all(dot(s,r)>=b[i] for s in sums for i,r in enumerate(R))
poly=poly_vertices(b)
assert len(poly)==16 and all(all(y.denominator==1 for y in x) for x in poly)
assert poly.issubset(sums)
print('SOURCE_MINKOWSKI_POLYTOPE_OK 34 sums, 16 integral vertices, 8 facet normals')

max_cones={tuple(i for i,r in enumerate(R) if dot(x,r)==b[i]) for x in poly}
assert len(max_cones)==16
assert all(len(c)==4 and abs(det4([R[i] for i in c]))==1 for c in max_cones)
assert {tuple(sorted(c)) for c in max_cones}=={
    tuple(sorted(p)) for p in product(*PAIR)}
print('SMOOTH_CUBICAL_NORMAL_FAN_OK 16 unimodular cones')

# Character m=(1,1,1,1) gives 2L=-K in the Picard group.
m=(1,1,1,1)
a=tuple((1-dot(r,m))//2 for r in R)
assert all(1-dot(r,m)==2*a[i] for i,r in enumerate(R))
assert a==(0,0,0,0,1,1,1,1)
assert tuple(R[0][i]+R[7][i] for i in range(4)) == tuple(R[6][i]+R[3][i] for i in range(4))
assert tuple(R[2][i]+R[5][i] for i in range(4)) == tuple(R[1][i]+R[4][i] for i in range(4))
Q=poly_vertices((-1,)*8)
assert len(Q)==12
assert all(all(v.denominator==1 for v in q) for q in Q)
from collections import Counter
fibre=Counter(inter(cone,(-1,)*8) for cone in max_cones)
assert sorted(fibre.values())==[1]*8+[2]*4
assert all(all(dot(q,r)>=-1 for r in R) for q in fibre)
assert all(q in Q for q in fibre)
print('WEAK_FANO_NONFANO_INDEX_TWO_OK 12 anticanonical vertices; multiplicity pattern 8+4 pairs')

# The anticanonical map coarsens the fan along exactly two independent
# square circuits, each of which has two torus-fixed endpoints.
exceptions=[(1,4),(3,6)]
for ex in exceptions:
    cones=[c for c in max_cones if all(i in c for i in ex)]
    assert len(cones)==4
    assert {tuple(R[i][j] for j in (0,2)) for c in cones for i in c if i not in ex} == {
        (-1,0),(1,0),(0,-1),(0,1)}
assert not any(set(exceptions[0]+exceptions[1]).issubset(c) for c in max_cones)
print('TWO_DISJOINT_EXCEPTIONAL_P1xP1_OK 4 maximal cones through each')

# Use Ehrhart polynomial: its fourth forward difference is 4! times volume.
LV={tuple((q[i]+m[i])/2 for i in range(4)) for q in Q}
assert all(all(v.denominator==1 for v in q) for q in LV)
lo=[int(min(v[i] for v in LV)) for i in range(4)]
hi=[int(max(v[i] for v in LV)) for i in range(4)]
counts=[]
for t in range(5):
    counts.append(sum(all(dot(z,R[i])>=-t*a[i] for i in range(8)) for z in
        product(*(range(t*lo[i],t*hi[i]+1) for i in range(4)))))
assert counts==[1,14,69,216,525]
assert counts[4]-4*counts[3]+6*counts[2]-4*counts[1]+counts[0]==20
print('EHRHART_HALF_ANTICANONICAL_OK',counts,'L^4=20, (-K)^4=320')

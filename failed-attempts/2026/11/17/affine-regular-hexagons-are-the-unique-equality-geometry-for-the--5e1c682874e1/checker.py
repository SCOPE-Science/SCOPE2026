#!/usr/bin/env python3
"""Exact rational check of the canonical equality hexagon; no external data."""
from fractions import Fraction as Q
from itertools import combinations
v = [(Q(1), Q(0)), (Q(0), Q(1)), (Q(-1), Q(-1))]
q = [(Q(2,3)*(v[i][j]-v[k][j]), Q(2,3)*(v[i][1]-v[k][1])) for i,k in [(0,1),(1,2),(2,0)] for j in [0]][:]
verts = q + [(-a,-b) for a,b in q]
def cross(a,b): return a[0]*b[1]-a[1]*b[0]
def norm(x):
    # For the six oriented sides, norm is the maximal nonnegative support inequality ratio.
    from functools import cmp_to_key
    def cmp(a,b):
        ha=(a[1]>0 or (a[1]==0 and a[0]>0)); hb=(b[1]>0 or (b[1]==0 and b[0]>0))
        if ha!=hb: return -1 if ha else 1
        z=cross(a,b)
        return -1 if z>0 else (1 if z<0 else 0)
    pts=sorted(verts,key=cmp_to_key(cmp))
    return max(cross((b[0]-a[0],b[1]-a[1]), x)/cross((b[0]-a[0],b[1]-a[1]),a) for a,b in zip(pts,pts[1:]+pts[:1]))
assert len(set(verts))==6
assert all(norm(x)==1 for x in verts)
assert all(norm(x)==1 for x in v)
assert all(norm((v[i][0]-v[j][0],v[i][1]-v[j][1]))==Q(3,2) for i,j in combinations(range(3),2))
assert tuple(sum(x[i] for x in v) for i in range(2))==(0,0)
print('PASS: six vertices, three unit midpoints, three opposite chords, and zero sum (exact rational).')

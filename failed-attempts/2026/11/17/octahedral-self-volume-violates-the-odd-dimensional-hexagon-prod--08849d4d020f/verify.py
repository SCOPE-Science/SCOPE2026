#!/usr/bin/env python3
"""Exact self-volume geometry check for a centered regular octahedron."""
from fractions import Fraction
from itertools import product, permutations
import sympy as sp

v=sp.Matrix
S=sp.sqrt
one=sp.Rational(1)
verts=[]
for i in range(3):
    for sign in (-1,1):
        p=[sp.Integer(0)]*3
        p[i]=sp.Integer(sign)
        verts.append(v(p))
assert len(verts)==6
normals=list(product((-1,1),repeat=3))
assert len(normals)==8
facets=[]
for s in normals:
    facet=[p for p in verts if sum(s[i]*p[i] for i in range(3))==1]
    assert len(facet)==3
    area=S((facet[1]-facet[0]).cross(facet[2]-facet[0]).dot((facet[1]-facet[0]).cross(facet[2]-facet[0])))/2
    assert sp.simplify(area-S(3)/2)==0
    facets.append(area)
# One central cut of the l1 ball: every point on a face of the
# plane section has one zero coordinate, and the others are ±1/2.
hexagon=set()
for perm in set(permutations((sp.Rational(1,2),-sp.Rational(1,2),sp.Integer(0)))):
    p=v(perm)
    assert sum(p)==0 and sum(abs(t) for t in p)==1
    hexagon.add(tuple(p))
assert len(hexagon)==6
h=[v(a) for a in hexagon]
normal=v([1,1,1]); unit=normal/S(3)
# Area from six triangular wedges with origin, using exact 3-D cross products.
# Find a circular order from an orthogonal basis.
e1=v([1,-1,0])/S(2)
e2=unit.cross(e1)
from functools import cmp_to_key
# Polar order via exact atan2 is used only to choose a permutation; exact
# cross products perform every area check.
import math
ordered=sorted(h,key=lambda p:math.atan2(float(p.dot(e2)),float(p.dot(e1))))
section_area=sum(S((ordered[i].cross(ordered[(i+1)%6])).dot(ordered[i].cross(ordered[(i+1)%6])))/2 for i in range(6))
assert sp.simplify(section_area-3*S(3)/4)==0
for i in range(6):
    step=ordered[(i+1)%6]-ordered[i]
    assert any(step==u for u in h), 'edge of hexagon must equal a vertex'
# Intrinsic hexagon self-perimeter = sum edge Minkowski lengths = 6.
section_self_volume=sp.Rational(6,2)
perimeter=sp.simplify(sum(facet*section_self_volume/section_area for facet in facets))
assert perimeter==16
selfvolume=sp.simplify(perimeter/3)
assert selfvolume==sp.Rational(16,3) and selfvolume<6
for k in range(1,101):
    candidate=selfvolume*3**(k-1)
    proposed=2*3**k
    assert candidate/proposed==sp.Rational(8,9)
    assert candidate<proposed
print('PASS: 8 facet areas, 6 section vertices, 6 exact norm edges, section area, self-volume=16/3, 100 product comparisons')

#!/usr/bin/env python3
"""Exact face/circuit checks for the regular GL4 Gelfand--Tsetlin polytope.
Run: python3 verify_gt4.py. Uses only the Python standard library.
"""
from fractions import Fraction
from itertools import product, combinations
from collections import Counter
from math import gcd

TOP = (4, 3, 2, 1)

def rank(rows):
    if not rows: return 0
    a = [[Fraction(z) for z in row] for row in rows]
    p = 0
    for col in range(len(a[0])):
        piv = next((r for r in range(p, len(a)) if a[r][col]), None)
        if piv is None: continue
        a[p], a[piv] = a[piv], a[p]
        q = a[p][col]
        a[p] = [u/q for u in a[p]]
        for r in range(p+1, len(a)):
            q = a[r][col]
            if q: a[r] = [u-q*v for u,v in zip(a[r],a[p])]
        p += 1
        if p == len(a): break
    return p

def det3(m):
    a,b,c=m
    return (a[0]*(b[1]*c[2]-b[2]*c[1])
           -a[1]*(b[0]*c[2]-b[2]*c[0])
           +a[2]*(b[0]*c[1]-b[1]*c[0]))

# At each stage the interlacing coordinate is at one bounding endpoint.
vertices = set()
for bits in product((0,1), repeat=6):
    y = [TOP[i+bits[i]] for i in range(3)]
    z = [y[i+bits[3+i]] for i in range(2)]
    vertices.add(tuple(y+z+[z[bits[5]]]))
V = sorted(vertices)
assert len(V)==40

# Fixed facet identifiers, all inequalities A[i] dot x <= b[i].
A = [(1,0,0,0,0,0),(-1,0,0,0,0,0),
     (0,1,0,0,0,0),(0,-1,0,0,0,0),
     (0,0,1,0,0,0),(0,0,-1,0,0,0),
     (-1,0,0,1,0,0),(0,1,0,-1,0,0),
     (0,-1,0,0,1,0),(0,0,1,0,-1,0),
     (0,0,0,-1,0,1),(0,0,0,0,1,-1)]
b = [4,-3,3,-2,2,-1,0,0,0,0,0,0]
assert all(sum(q*x for q,x in zip(a,v))<=q0 for v in V for a,q0 in zip(A,b))
facet_sets = [frozenset(i for i,v in enumerate(V)
              if sum(q*x for q,x in zip(a,v))==q0)
              for a,q0 in zip(A,b)]
assert all(len(f)>0 for f in facet_sets)

# Independent exhaustive vertex check: a vertex is a feasible unique solution of
# some six linearly independent supporting facet hyperplanes. There are 924.
def solve6(rows, rhs):
    m=[[Fraction(a) for a in row]+[Fraction(b0)] for row,b0 in zip(rows,rhs)]
    for col in range(6):
        piv=next((r for r in range(col,6) if m[r][col]),None)
        if piv is None: return None
        m[col],m[piv]=m[piv],m[col]
        q=m[col][col]
        m[col]=[x/q for x in m[col]]
        for j in range(6):
            if j==col:continue
            q=m[j][col]
            if q:m[j]=[x-q*y for x,y in zip(m[j],m[col])]
    return tuple(m[i][6] for i in range(6))
solved=set()
for ids in combinations(range(12),6):
    w=solve6([A[i] for i in ids],[b[i] for i in ids])
    if w is not None and all(sum(ai*wi for ai,wi in zip(row,w))<=bb for row,bb in zip(A,b)):
        solved.add(w)
assert solved==set(V)

# The complete nonempty face lattice is all nonempty intersections of facets.
faces = {frozenset(range(len(V)))}
for mask in range(1,1<<len(A)):
    f=frozenset(range(len(V)))
    for j in range(len(A)):
        if (mask>>j)&1: f=f.intersection(facet_sets[j])
        if not f: break
    if f: faces.add(f)
assert len(faces)==567

def dimension(f):
    v0=V[next(iter(f))]
    return rank([[V[i][j]-v0[j] for j in range(6)] for i in f])

all_faces_by_dim=Counter(dimension(f) for f in faces)
assert [all_faces_by_dim[k] for k in range(7)]==[40,132,186,139,57,12,1]

singular={}
for f in faces:
    d=dimension(f)
    active=tuple(j for j,g in enumerate(facet_sets) if f<=g)
    assert rank([A[j] for j in active])==6-d
    # For these directed-graph incidence normals, a simplicial cone is unimodular.
    if len(active)>6-d: singular[f]=(d, active)

assert [sum(d==j for d,active in singular.values()) for j in range(4)]==[16,28,16,3]
max_faces=[f for f in singular if not any(f<g for g in singular)]
assert len(max_faces)==3 and all(dimension(f)==3 for f in max_faces)
component_ids={tuple(singular[f][1]):f for f in max_faces}
assert set(component_ids)=={(1,2,6,7),(3,4,8,9),(7,8,10,11)}
assert sorted(len(f) for f in max_faces)==[6,6,8]
assert all(any(f<=g for g in max_faces) for f in singular)

outer1=component_ids[(1,2,6,7)]
outer2=component_ids[(3,4,8,9)]
center=component_ids[(7,8,10,11)]
assert not outer1.intersection(outer2)
assert dimension(outer1.intersection(center))==1
assert dimension(outer2.intersection(center))==1
assert len(outer1.intersection(center))==2
assert len(outer2.intersection(center))==2

# Each component has a rank-three square cone, with primitive relation
# normal_1+normal_2=normal_3+normal_4, and saturated normal lattice.
for ids in component_ids:
    v=[A[i] for i in ids]
    assert rank(v)==3
    assert all(v[0][j]+v[1][j]==v[2][j]+v[3][j] for j in range(6))
    minors=[det3([[row[c] for c in cols] for row in (v[i] for i in rows)])
             for rows in combinations(range(4),3)
             for cols in combinations(range(6),3)]
    assert gcd(*minors)==1
    # In fact, a triple of ray generators is already a lattice basis of its span.
    assert all(gcd(*(det3([[v[i][c] for c in cols] for i in rows])
                      for cols in combinations(range(6),3)))==1
               for rows in combinations(range(4),3))

print('VERIFY_OK: 40 vertices, 567 faces, 63 singular orbits, three conifold strata in a chain')

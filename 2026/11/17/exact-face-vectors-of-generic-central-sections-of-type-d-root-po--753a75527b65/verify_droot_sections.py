#!/usr/bin/env python3
"""Exact face-lattice check for generic central slices of type-D root polytopes.

No external dependencies. Enumerates intersections of all defining facets;
there is no reliance on the formula for the section face counts.
This checks n=4,5,6 and multiple normal chambers, not arbitrary n.
"""
import itertools
import math
from fractions import Fraction


def rank_integer(rows):
    """Exact rational rank for integer row vectors."""
    if not rows:
        return 0
    basis = {}
    for original in rows:
        v = [Fraction(z) for z in original]
        for pivot, b in sorted(basis.items()):
            if v[pivot]:
                t = v[pivot]
                v = [x - t*y for x,y in zip(v,b)]
        nonzero = next((i for i,x in enumerate(v) if x), None)
        if nonzero is not None:
            t = v[nonzero]
            basis[nonzero] = [x/t for x in v]
    return len(basis)


def check(n):
    vertices=[]
    for i,j in itertools.combinations(range(n),2):
        for s,t in itertools.product((-1,1),repeat=2):
            v=[0]*n;v[i]=s;v[j]=t
            vertices.append(tuple(v))
    assert len(vertices)==2*n*(n-1)
    facet_faces=[]
    for i in range(n):
        for s in (-1,1):
            facet_faces.append(frozenset(idx for idx,v in enumerate(vertices) if s*v[i]==1))
    for sign in itertools.product((-1,1),repeat=n):
        facet_faces.append(frozenset(idx for idx,v in enumerate(vertices) if sum(si*vi for si,vi in zip(sign,v))==2))
    assert len(facet_faces)==2*n+2**n
    # All nonempty faces are intersections of facets (including the whole body).
    all_vertices=frozenset(range(len(vertices)))
    seen={all_vertices}; frontier={all_vertices}
    while frontier:
        newer=set()
        for a in frontier:
            for b in facet_faces:
                inter=a & b
                if inter and inter not in seen:
                    seen.add(inter);newer.add(inter)
        frontier=newer
    dims={}
    for ids in seen:
        arr=[vertices[i] for i in ids]
        dims[ids]=rank_integer([[x-y for x,y in zip(p,arr[0])] for p in arr[1:]])
    assert dims[all_vertices]==n
    formula=[(k+1)*2**(k+3)*math.comb(n,k+3)
            +(2**(k+2)-4)*math.comb(n,k+2) for k in range(n-2)]
    formula.append(2**n+2*n-6)
    assert sum((-1)**k*formula[k] for k in range(n-1))==1-(-1)**(n-1)
    normals=[tuple(range(n,0,-1)),tuple(-i for i in range(n,0,-1))]
    # An even and an odd coordinate-sign flip, and a generic permutation.
    base=tuple(range(n,0,-1))
    normals.extend([tuple((-1 if i in pattern else 1)*a for i,a in enumerate(base))
                    for pattern in [(0,),(0,1),(0,2,3)]])
    normals.append(tuple(reversed(base)))
    for normal in normals:
        evaluations=[sum(x*y for x,y in zip(v,normal)) for v in vertices]
        assert all(t!=0 for t in evaluations)
        crossed=[0]*(n-1)
        for ids,dim in dims.items():
            if dim==n:continue
            vals=[evaluations[i] for i in ids]
            if min(vals)<0<max(vals): crossed[dim-1]+=1
        assert crossed==formula, (n,normal,crossed,formula)
    print('n=',n, 'facets=',len(facet_faces),'all_nonempty_faces=',len(seen),
          'normal_tests=',len(normals),'f=',formula,'PASS')

for n in (4,5,6):
    check(n)
print('VERIFY_OK')

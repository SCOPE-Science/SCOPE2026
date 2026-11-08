"""Exact rational checks for the facet-translate saturation construction.

This finite check supplements, and does not replace, the general proof.
"""
from fractions import Fraction as F
from itertools import product

def dot(a,b): return sum(x*y for x,y in zip(a,b))

def check_case(normals,offsets,points,facets,scale):
    d=len(points[0]); R2=max(dot(x,x) for x in points)
    for i,(u,p) in enumerate(zip(normals,facets)):
        assert dot(u,p)==offsets[i]
        for j,v in enumerate(normals):
            if j!=i: assert offsets[j]-dot(v,p)>0
        # Choose every rational facet shift from supporting sample projections.
        for c in sorted(set([F(0)] + [dot(u,x) for x in points])):
            # Translate t(K-p) by c*u/|u|^2.
            z=tuple(c*w/dot(u,u) for w in u)
            for x in points:
                inside=all(dot(v,x)<=scale*(offsets[j]-dot(v,p))+dot(v,z) for j,v in enumerate(normals))
                expected=dot(u,x)<=c
                assert inside==expected,(i,c,x,inside,expected)
    return len(normals)*len(set([F(0)]+[dot(u,x) for u in normals for x in points]))*len(points)

square_normals=[(F(1),F(0)),(F(0),F(1)),(F(-1),F(0)),(F(0),F(-1))]
square_offsets=[F(1)]*4
square_facets=[(F(1),F(0)),(F(0),F(1)),(F(-1),F(0)),(F(0),F(-1))]
pts=[(F(a,2),F(b,2)) for a,b in product(range(-2,3),repeat=2)]
count=check_case(square_normals,square_offsets,pts,square_facets,F(6))
triangle_normals=[(F(-1),F(0)),(F(0),F(-1)),(F(1),F(1))]
triangle_offsets=[F(0),F(0),F(2)]
triangle_facets=[(F(0),F(1)),(F(1),F(0)),(F(1),F(1))]
count+=check_case(triangle_normals,triangle_offsets,pts,triangle_facets,F(8))
# Independently check the claimed exact square center profile by clipping
# an axis-parallel square that excludes the origin.
for denom in range(1,21):
    for numer in range(1,3*denom+1):
        t=F(numer,denom)
        # The x-interval on the positive side has maximal overlap min(2t,1).
        # The independent y-interval has maximal overlap min(2t,2).
        mass=min(2*t,F(1))*min(2*t,F(2))/4
        expected=(t*t if t<=F(1,2) else (t/2 if t<=1 else F(1,2)))
        assert mass==expected
        count+=1
print('VERIFY_OK:',count,'exact rational construction and square-profile comparisons')

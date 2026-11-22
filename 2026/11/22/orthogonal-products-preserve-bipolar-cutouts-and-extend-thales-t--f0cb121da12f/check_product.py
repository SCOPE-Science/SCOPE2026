"""Exact rational checks for nonrectangular four-dimensional orthogonal cutouts.

This checks a concrete illustrative instance, not the dimension-independent proof.
"""
from fractions import Fraction as F
from itertools import combinations, product


def dot(a, b):
    return sum(x*y for x,y in zip(a,b))


def sub(a,b):
    return tuple(x-y for x,y in zip(a,b))


def add(a,b):
    return tuple(x+y for x,y in zip(a,b))


def scale(t,a):
    return tuple(t*x for x in a)


def proj_point_line(p,a,b):
    e=sub(b,a)
    t=dot(sub(p,a),e)/dot(e,e)
    return add(a,scale(t,e)),t


def triangle_cutouts(verts,b):
    result=[]
    for idx,v in enumerate(verts):
        incident=[]
        for j,w in enumerate(verts):
            if j==idx:
                continue
            foot,t=proj_point_line(b,v,w)
            assert F(0)<t<F(1), ('edge foot outside',idx,j,t)
            incident.append((foot,j))
        projections=[v,incident[0][0],incident[1][0],b]
        assert len(set(projections))==4
        for point in projections:
            assert dot(sub(point,v),sub(point,b))==0
            for j,w in enumerate(verts):
                assert dot(sub(point,b),sub(v,w))>=0, (idx,j,point)
        result.append(projections)
    return result


if __name__ == '__main__':
    U=[(F(0),F(0)),(F(4),F(0)),(F(0),F(3))]
    V=[(F(0),F(0)),(F(5),F(0)),(F(0),F(4))]
    b=(F(1),F(1))
    X=triangle_cutouts(U,b)
    Y=triangle_cutouts(V,b)
    checked=0
    for i,j in product(range(3),repeat=2):
        south=U[i]+V[j]
        north=b+b
        verts=[x+y for x,y in product(X[i],Y[j])]
        assert len(verts)==16
        for z in verts:
            assert dot(sub(z,south),sub(z,north))==0
            checked+=1
        # Sixteen product vertices are all extreme, since each factor's four
        # points are distinct vertices of a strictly convex cyclic quadrilateral.
    a=X[1][0]; e1=sub(X[1][1],a); e2=sub(X[1][2],a)
    assert dot(e1,e2)!=0
    print('PASS: 6 planar cutouts, 9 four-dimensional product cutouts,')
    print(f'{checked} exact sphere incidences, 16 vertices per product cell,')
    print('and a non-right angle at a south pole')

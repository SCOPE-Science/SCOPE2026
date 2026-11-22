"""Reproduce finite sample checks for an orthogonal-hull volume identity.

Requirements for the four-dimensional checks: numpy and scipy. Numerical
checks corroborate, but do not replace, the accompanying analytic proof.
"""
from fractions import Fraction
import itertools
import math


def interval_check():
    """Compute the exact planar area of a convex hull of axis intervals."""
    pairs = [((1, 2), (1, 2)), ((-2, -1), (1, 3)), ((-2, 3), (4, 5))]
    for (a, b), (c, d) in pairs:
        pts = [(a, 0), (b, 0), (0, c), (0, d)]
        def cross(o, u, v):
            return (u[0]-o[0])*(v[1]-o[1])-(u[1]-o[1])*(v[0]-o[0])
        lower, upper = [], []
        for point in sorted(set(pts)):
            while len(lower)>=2 and cross(lower[-2],lower[-1],point)<=0: lower.pop()
            lower.append(point)
        for point in reversed(sorted(set(pts))):
            while len(upper)>=2 and cross(upper[-2],upper[-1],point)<=0: upper.pop()
            upper.append(point)
        hull=lower[:-1]+upper[:-1]
        actual=Fraction(abs(sum(x*y1-y*x1 for (x,y),(x1,y1) in zip(hull,hull[1:]+hull[:1]))),2)
        v1=Fraction(b-a);v2=Fraction(d-c)
        c1=Fraction(max(b,0)-min(a,0));c2=Fraction(max(d,0)-min(c,0))
        prediction=Fraction(c1*c2-(c1-v1)*(c2-v2),2)
        assert prediction==actual, (actual,prediction)
    print('Exact interval joins: 3/3 PASS')


def polygon_deletion_check():
    import numpy as np
    from scipy.spatial import ConvexHull, QhullError
    square=[(math.cos(2*math.pi*j/4),math.sin(2*math.pi*j/4)) for j in range(4)]
    pentagon=[(math.cos(2*math.pi*j/5),math.sin(2*math.pi*j/5)) for j in range(5)]
    def area(pts):
        if len(pts)<3:return 0.
        try:return ConvexHull(np.array(pts)).volume
        except QhullError:return 0.
    layers=[]
    for poly in (square,pentagon):
        layer=[]
        for mask in range(1<<len(poly)):
            selected=[p for i,p in enumerate(poly) if mask>>i&1]
            layer.append((selected,area(selected),area(selected+[(0.,0.)])))
        layers.append(layer)
    S,T=layers
    direct=0.;derived=0.
    for s,vs,cs in S:
        for t,vt,ct in T:
            points=[[x,y,0.,0.] for x,y in s]+[[0.,0.,x,y] for x,y in t]
            observed=0.
            if len(points)>=5:
                try:observed=ConvexHull(np.array(points)).volume
                except QhullError:pass
            predicted=(cs*ct-(cs-vs)*(ct-vt))/6
            assert abs(observed-predicted)<1.e-8,(s,t,observed,predicted)
            direct+=observed
            derived+=predicted
    s1=math.sin(2*math.pi/5);s2=math.sin(4*math.pi/5)
    closed=155*s1/3072+35*s2/1536
    assert abs(direct/512-closed)<1.e-12
    assert abs(derived/512-closed)<1.e-12
    print('All 512 square–pentagon deletion subsets: PASS')
    print('Mean surviving four-volume:',format(closed,'.17g'))


if __name__=='__main__':
    interval_check()
    polygon_deletion_check()

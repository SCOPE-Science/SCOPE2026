"""Independent Euclidean projection check for the two-threshold brightness theorem.

Uses full 24-vertex three-dimensional hulls and orthogonal two-dimensional
convex hull areas, not the piecewise brightness formula to compute geometry.
"""
import math
import itertools
import random
import numpy as np
from scipy.spatial import ConvexHull


def vertices(t):
    assert 0 < t < 1
    points = {tuple(p) for signs in itertools.product((-1, 1), repeat=2)
              for p in set(itertools.permutations((signs[0], signs[1]*t, 0.0)))}
    return np.array(sorted(points), dtype=float)

def projected_area(vs, u):
    u=np.array(u,float); u/=np.linalg.norm(u)
    a=np.eye(3)[np.argmin(abs(u))]
    e1=a-u*np.dot(a,u)
    e1/=np.linalg.norm(e1)
    e2=np.cross(u,e1)
    pts=np.column_stack((vs@e1, vs@e2))
    return ConvexHull(pts).volume

def branch_brightness(t,u):
    x,y,z=sorted(map(abs,np.array(u,dtype=float)/np.linalg.norm(u)),reverse=True)
    p=2*t*t
    q=(1+2*t-2*t*t)/2
    return ((p+4*q)*x+p*(y+z)) if x>=y+z else (p+2*q)*(x+y+z)

def predicted_extrema(t):
    p=2*t*t
    q=(1+2*t-2*t*t)/2
    smallest=min(p+4*q,math.sqrt(2)*(p+2*q))
    largest=max(math.sqrt(3)*(p+2*q), math.sqrt((p+4*q)**2+2*p*p))
    return smallest,largest

def run():
    rng=random.Random(263071)
    tmax=(1+math.sqrt(7))/6
    tmin=(1+math.sqrt(3+math.sqrt(2)))/(2+math.sqrt(2))
    t_design=(math.sqrt(3)+math.sqrt(9+4*math.sqrt(3)))/(4+2*math.sqrt(3))
    assert tmax<t_design<tmin
    tested=0
    for t in [0.03,0.1,0.25,0.5,tmax,0.64,t_design,0.8,tmin,0.94,0.99]:
        v=vertices(t)
        assert v.shape==(24,3),v.shape
        l,h=predicted_extrema(t)
        p=2*t*t;q=(1+2*t-2*t*t)/2
        test_u=[(1,0,0),(1,1,0),(1,1,1),(p+4*q,p,p)]
        test_u +=[tuple(rng.gauss(0,1) for _ in range(3)) for _ in range(300)]
        for u in test_u:
            geometric=projected_area(v,u)
            predicted=branch_brightness(t,u)
            assert abs(geometric-predicted)<1e-9,(t,u,geometric,predicted)
            assert l-1e-9 <= geometric <= h+1e-9,(t,u,geometric,l,h)
            tested+=1
        bdiag=projected_area(v,(1,1,1))
        bedge=projected_area(v,(1,1,0))
        baxis=projected_area(v,(1,0,0))
        bobl=projected_area(v,(p+4*q,p,p))
        assert abs(min(bedge,baxis)-l)<1e-9
        assert abs(max(bdiag,bobl)-h)<1e-9
        if tmax<=t<=tmin:
            assert abs((h/l)-math.sqrt(1.5))<1e-10
    # Regular truncated octahedron t=1/2 rescaled 2x, confirming exact published end values.
    lo,hi=predicted_extrema(0.5)
    assert abs(4*lo-8*math.sqrt(2))<1e-12
    assert abs(4*hi-2*math.sqrt(51))<1e-12
    print('INDEPENDENT_PROJECTED_HULL_CHECKS_OK',tested)
    print('TRANSITIONS',format(tmax,'.12f'),format(tmin,'.12f'))
    print('EQUIFACIAL_T',format(t_design,'.12f'))
    print('PLATEAU_RATIO',format(math.sqrt(1.5),'.12f'))
if __name__=='__main__': run()

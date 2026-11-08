#!/usr/bin/env python3
"""Reproduce the geometric and algebraic checks for a weighted book-graph zonotope.

Python 3 standard library suffices for exact tensor cubature and spectral checks.
NumPy/SciPy provide an optional independent 3D/4D convex-hull integration check.
"""
from fractions import Fraction as F
from itertools import product
from math import sqrt


def formulas(q, t):
    t=F(t)
    D=t+F(q,2)
    a=(F(t,3)+F(2*q-1,12))/D
    third=t**3+F(3*q,2)*t**2+F(q*(3*q+1),4)*t+F(q*q*(q+1),8)
    b=third/(12*D)
    return a,b,D


def cubature(q,t):
    t=F(t)
    nodes=(F(0),F(1,2),F(1))
    weights=(F(1,6),F(4,6),F(1,6))
    denom=F(0); numer_a=F(0); numer_b=F(0)
    for inds in product(range(3),repeat=q):
        v=[nodes[i] for i in inds]
        weight=F(1)
        for i in inds:weight*=weights[i]
        length=t+sum(v)
        denom+=weight*length
        numer_a+=weight*(1-v[0])**2*length
        numer_b+=weight*length**3
    return numer_a/denom,numer_b/(12*denom),denom


def fpoly(q,t):
    t=F(t)
    return 4*t**3+6*q*t**2+(3*q*q-3*q-8)*t+F(q**3-3*q*q-6*q+4,2)


def spectral(q,t):
    a,b,D=formulas(q,t)
    high=2*b
    split=F(q+2,2)*a
    assert high-split==fpoly(q,t)/(24*D)
    assert split>a
    return high,split,a

cases=0
for q in range(2,8):
    for t in (F(0),F(1,8),F(1,4),F(1),F(2),F(7,2)):
        assert formulas(q,t)==cubature(q,t)
        spectral(q,t)
        cases+=1
for q in range(5,300):
    assert fpoly(q,0)>0 and 3*q*q-3*q-8>0
for q in (3,4):
    assert fpoly(q,0)<0 and 3*q*q-3*q-8>0
assert fpoly(2,F(0))<0
assert all(fpoly(q,1)>0 for q in range(2,300))
assert fpoly(2,F(1,2))<0 and fpoly(2,F(3,4))>0
print('EXACT_TENSOR_CUBATURE_AND_SPECTRAL_CHECKS_PASSED cases=',cases)

try:
    import numpy as np
    from scipy.spatial import ConvexHull
    from scipy.linalg import null_space
except ImportError:
    print('OPTIONAL_HULL_CHECKS_SKIPPED (numpy/scipy unavailable)')
else:
    # For dimensions 3 and 4 the facet fan gives stable, independently integrated moments.
    # High-dimensional Qhull facet degeneracies are not used as proof certificates.
    hull_cases=0
    for q in (2,3):
        for t in (0.,.25,1.,2.):
            n=q+2
            edges=[(0,j+2,1.) for j in range(q)]+[(1,j+2,1.) for j in range(q)]+[(0,1,t)]
            B=np.zeros((n,len(edges)))
            for k,(i,j,v) in enumerate(edges):
                B[i,k]=v;B[j,k]=-v
            Q=null_space(np.ones((1,n)))
            pts=np.array([Q.T@(B@np.array(s)/2) for s in product((-1,1),repeat=len(edges))])
            pts=np.unique(np.round(pts,12),axis=0)
            hull=ConvexHull(pts,qhull_options='Qx Qt')
            moment=np.zeros((n-1,n-1));vol=0.
            from math import factorial
            for face in hull.simplices:
                z=pts[face].T
                v=abs(np.linalg.det(z))/factorial(n-1)
                moment+=v*(z@z.T+np.outer(z.sum(axis=1),z.sum(axis=1)))/(n*(n+1))
                vol+=v
            moment/=vol
            a,b,_=formulas(q,F(str(t)))
            c=[np.r_[[.5,.5],-np.eye(q)[j]] for j in range(q)]
            d=np.r_[[1.,-1.],np.zeros(q)]
            expected=float(a)*sum(np.outer(z,z) for z in c)+float(b)*np.outer(d,d)
            expected_vol=2**q*(t+q/2)*sqrt(n)
            assert abs(vol-expected_vol)<1e-8
            assert np.max(np.abs(moment-Q.T@expected@Q))<1e-8
            hull_cases+=1
    print('INDEPENDENT_CONVEX_HULL_MOMENTS_PASSED cases=',hull_cases)
print('BOOK_GRAPH_ZONOTOPE_CHECKS_PASSED')

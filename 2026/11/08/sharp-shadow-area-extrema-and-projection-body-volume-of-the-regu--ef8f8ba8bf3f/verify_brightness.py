#!/usr/bin/env python3
"""Standalone numerical cross-check of the truncated-octahedron brightness theorem.
This verifies geometric formulas for many directions; the universal proof is analytic.
"""
import itertools
import math
import numpy as np
from scipy.spatial import ConvexHull

def verts():
    s=set()
    for perm in set(itertools.permutations((0,1,2))):
        inds=[j for j,x in enumerate(perm) if x]
        for sg in itertools.product((-1,1),repeat=2):
            v=list(perm)
            for i,sgn in zip(inds,sg): v[i]*=sgn
            s.add(tuple(v))
    return np.asarray(sorted(s),float)

V=verts()
assert V.shape==(24,3)

def brightness(u):
    u=np.asarray(u,float);u/=np.linalg.norm(u)
    a,b,c=sorted(abs(x) for x in u)[::-1]
    return (14*a+2*b+2*c) if (a>=b+c) else 8*(a+b+c)

def hull_area(u):
    u=np.array(u,float);u/=np.linalg.norm(u)
    # rank-two basis for plane orthogonal to u
    s=np.eye(3)[int(np.argmin(np.abs(u)))];v=s-np.dot(s,u)*u;v/=np.linalg.norm(v)
    w=np.cross(u,v)
    xy=V@np.stack((v,w),axis=1)
    return ConvexHull(xy).volume
rng=np.random.default_rng(34531)
for i in range(3000):
    u=rng.normal(size=3)
    a=brightness(u);b=hull_area(u)
    assert abs(a-b)<1e-9,(i,u,a,b)
    assert 8*math.sqrt(2)-1e-9<=a<=2*math.sqrt(51)+1e-9
for u,area in [([1,1,0],8*math.sqrt(2)),([7,1,1],2*math.sqrt(51))]:
    assert abs(brightness(u)-area)<1e-10
    assert abs(hull_area(u)-area)<1e-10
print('TRUNCATED_OCTAHEDRON_BRIGHTNESS_OK 3000')

# Exact integer determinant census for the projection zonotope.
E=((1,1,1),(1,1,-1),(1,-1,1),(-1,1,1))
G=((2,0,0),(0,2,0),(0,0,2))+tuple(tuple(3*x for x in e) for e in E)
def dot(x,y): return sum(a*b for a,b in zip(x,y))
def cross(x,y): return (x[1]*y[2]-x[2]*y[1],x[2]*y[0]-x[0]*y[2],x[0]*y[1]-x[1]*y[0])
by_axes={i:0 for i in range(4)}
for inds in itertools.combinations(range(7),3):
    x,y,z=(G[i] for i in inds)
    by_axes[sum(i<3 for i in inds)]+=abs(dot(x,cross(y,z)))
assert by_axes=={0:432,1:432,2:144,3:8},by_axes
assert 8*sum(by_axes.values())==8128
# Independent convex hull of all zonotope signed sums, for validation only.
Z=np.array([np.sum([s*np.array(g) for s,g in zip(sig,G)],axis=0)
            for sig in itertools.product((-1,1),repeat=7)],dtype=float)
assert abs(ConvexHull(Z).volume-8128)<1e-7
print('TRUNCATED_OCTAHEDRON_PROJECTION_BODY_VOLUME_OK 8128')

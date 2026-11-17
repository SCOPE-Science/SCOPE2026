#!/usr/bin/env python3
"""Independent geometric comparisons for triangle self-similarity containment.

Requires numpy and scipy. Floating-point checks illustrate, not replace, the proof.
"""
import math
import numpy as np
from scipy.spatial import ConvexHull, HalfspaceIntersection

TOL=3e-7

def normalize(vertices):
    p=np.asarray(vertices,dtype=float).copy()
    p-=p.mean(axis=0)
    a=np.linalg.det(np.stack((p[1]-p[0],p[2]-p[0])))/2
    if a<0:
        p=p[[0,2,1]]
        a=-a
    if a<=1e-9: raise ValueError('Degenerate triangle')
    return p,a

def footprint(triangle):
    p,a=normalize(triangle)
    S=[]
    for x,y in zip(p,np.roll(p,-1,axis=0)):
        e=y-x
        n=np.array([e[1],-e[0]])/(2*a)
        S.append(np.array([[n@v,n@np.array([-v[1],v[0]])] for v in p]))
    Z=np.array([v1+v2+v3 for v1 in S[0] for v2 in S[1] for v3 in S[2]])
    boundary=Z[ConvexHull(Z).vertices]
    F=np.array([np.linalg.solve(np.stack((v,w)),[1.,1.])
                for v,w in zip(boundary,np.roll(boundary,-1,axis=0))])
    return p,a,ConvexHull(F).volume,F

def containment_volume(triangle):
    p,a=normalize(triangle)
    half=[]
    for q1,q2 in zip(p,np.roll(p,-1,axis=0)):
        e=q2-q1; n=np.array([e[1],-e[0]]); h=n@q1
        for x,y in p:
            half.append([n[0]*x+n[1]*y,n[1]*x-n[0]*y,n[0],n[1],-h])
    pts=HalfspaceIntersection(np.array(half),np.zeros(4)).intersections
    return ConvexHull(pts).volume

def check(triangle):
    p,a,foot_area,v=footprint(triangle)
    four=containment_volume(p)
    assert abs(four-a*foot_area/6)<TOL*(1+four),('fiber formula',a,foot_area,four)
    assert all(q[0]>=-0.5-TOL and q[0]+math.sqrt(3)*abs(q[1])<=1+TOL for q in v),('envelope',v)
    assert four/a <= math.sqrt(3)/8+TOL,('sharp volume',four/a)
    return four/a

def main():
    checks=0
    examples=[[[0,0],[2,0],[1,math.sqrt(3)]],
              [[0,0],[2,0],[0,2]],
              [[0,0],[3,0],[0,1]],
              [[0,0],[4,0],[1,1]],
              [[0,0],[1,0],[.2,.3]]]
    for t in examples:
        check(t);checks+=3
    r0=check(examples[0]);checks+=3
    assert abs(r0-math.sqrt(3)/8)<5e-12
    print('regular triangle exact predicted ratio:',math.sqrt(3)/8)
    print('regular triangle measured ratio:',r0)
    rng=np.random.default_rng(20261111)
    max_ratio=0
    for k in range(120):
        while True:
            p=rng.normal(size=(3,2))
            if abs(np.linalg.det(np.stack((p[1]-p[0],p[2]-p[0]))))>0.1:
                break
        max_ratio=max(max_ratio,check(p));checks+=3
    # Beta(2,3) first three raw moments: E R^j=(2)_j/(5)_j.
    from scipy.special import beta
    from scipy.integrate import quad
    for j in (1,2,3,4):
        numerical=quad(lambda r:12*r**(1+j)*(1-r)**2,0,1,epsabs=1e-13)[0]
        expected=beta(2+j,3)/beta(2,3)
        assert abs(numerical-expected)<1e-12
        checks+=1
    print('120 random and 5 sample triangles checked; 4D-volume/fiber/outer-envelope tests passed.')
    print('largest random 4D volume / triangle area:',max_ratio)
    print('universal Beta(2,3) first four moments verified by quadrature.')
    print('PASSED',checks,'deterministic assertions')

if __name__=='__main__':main()

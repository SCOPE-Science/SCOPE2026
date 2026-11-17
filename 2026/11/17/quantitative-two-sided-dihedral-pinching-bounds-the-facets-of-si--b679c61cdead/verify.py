#!/usr/bin/env python3
"""Deterministic numerical cross-checks for the two-sided dihedral pinching bound.
This is diagnostic, not a substitute for the spherical-area proof.
"""
import math
import random
from itertools import combinations

PI = math.pi

def area_lh(a, b, c):
    s = (a+b+c)/2
    assert max(a,b,c) < s and s < PI
    q = math.tan(s/2)
    for t in (a,b,c): q *= math.tan((s-t)/2)
    return 4*math.atan(math.sqrt(q))

def area_girard(a,b,c):
    co=lambda x,y,z: max(-1.0,min(1.0,(math.cos(x)-math.cos(y)*math.cos(z))/(math.sin(y)*math.sin(z))))
    A=math.acos(co(a,b,c)); B=math.acos(co(b,a,c)); C=math.acos(co(c,a,b))
    return A+B+C-PI

def lower(alpha,delta):
    ell=PI/2-delta
    return 4*math.atan(math.tan(ell/4)*math.sqrt(math.tan(3*ell/4)*math.tan((alpha-2*delta)/4)))

rng=random.Random(20261111)
n=0
for delta_deg, alpha_deg in ((0.5,2),(1,5),(5,15),(5,20),(10,25),(20,60)):
    d=math.radians(delta_deg);alpha=math.radians(alpha_deg)
    ell=PI/2-d; up=PI-alpha
    assert 2*d<alpha<=PI/2+d
    L=lower(alpha,d)
    # Every tuple of side lengths in the box is a spherical triangle with perimeter <2pi
    # precisely when s<pi; we sample that admissible subset.
    for i in range(3000):
        a,b,c=[rng.uniform(ell,up) for _ in range(3)]
        s=(a+b+c)/2
        if s>=PI: continue
        val=area_lh(a,b,c)
        independent=area_girard(a,b,c)
        assert abs(val-independent)<1e-9,(delta_deg, alpha_deg,val, independent)
        assert val+1e-10>=L, (delta_deg,alpha_deg,val,L)
        n+=2
    # Check the extreme squashed spherical triangle from the proof.
    if up<2*ell:
        assert area_lh(up,ell,ell)>=L-1e-12
        n+=1

# The 3 pairwise-right exterior normals at each cube vertex have an octant normal cone.
assert abs(area_lh(PI/2,PI/2,PI/2)-PI/2)<1e-12
n+=1
# Check the claimed sqrt endpoint with epsilon decreasing by factors of 100.
d=math.radians(10);ell=PI/2-d
values=[]
for eps in (1e-3,1e-4,1e-5,1e-6):
    alpha=2*d+eps; u=PI-alpha
    values.append(area_lh(u,ell,ell)/math.sqrt(eps))
limit=2*math.tan(ell/2)*math.sqrt(math.tan(ell))
assert abs(values[-1]/limit-1)<1e-4,(values,limit)
assert all(abs(values[i]-limit)>abs(values[i+1]-limit) for i in range(3))
n+=5
print('PASS',n,'numerical cross-checks')
print('sqrt threshold coefficient:',limit,'evaluations:',values)

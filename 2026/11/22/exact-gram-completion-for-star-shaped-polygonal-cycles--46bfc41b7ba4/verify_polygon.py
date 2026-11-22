"""Finite diagnostics for radial cycle Gram completion.

Not a substitute for the proof for arbitrary vertex count.
"""
import numpy as np
from math import pi

rng=np.random.default_rng(46043)
count=0
auto_checked=0

def check(points):
    global count,auto_checked
    n=len(points)
    radii=np.linalg.norm(points,axis=1)
    dots=np.sum(points*np.roll(points,-1,axis=0),axis=1)
    cs=np.clip(dots/(radii*np.roll(radii,-1)), -1,1)
    angles=np.arccos(cs)
    assert np.all(angles>1e-8) and np.all(angles<pi-1e-8)
    assert abs(angles.sum()-2*pi)<2e-8
    phi=np.r_[0,np.cumsum(angles[:-1])]
    recovered=radii[:,None]*np.stack([np.cos(phi),np.sin(phi)],axis=1)
    gram=recovered@recovered.T
    true=points@points.T
    assert np.max(abs(gram-true))<4e-8
    count+=1
    for k in range(n):
        for sign in (+1,-1):
            perm=(k+sign*np.arange(n))%n
            same=(np.max(np.abs(radii**2-radii[perm]**2))<1e-8
                  and np.max(np.abs(dots-dots[perm if sign==1 else (perm-1)%n]))<1e-8)
            if same:
                assert np.max(np.abs(true-true[np.ix_(perm,perm)]))<4e-8
            auto_checked+=1

for n in range(3,26):
    # Affine images of regular inscribed polygons: each is strictly
    # convex, has the origin in its interior, and can be anisotropic.
    t=np.arange(n)*2*pi/n
    base=np.stack([np.cos(t),np.sin(t)],axis=1)
    for rep in range(18):
        mat=rng.normal(size=(2,2))
        if np.linalg.det(mat)<0: mat[:,0]*=-1
        if np.linalg.det(mat)<0.08: mat+=np.eye(2)
        if np.linalg.det(mat)<0: mat[:,0]*=-1
        check(base@mat.T)

for n in range(5,26):
    # General non-convex radial loops: no convexity is used in the lemma.
    for rep in range(18):
        increments=rng.uniform(0.8,1.2,size=n)
        increments*=2*pi/increments.sum()
        assert max(increments)<pi
        t=np.r_[0,np.cumsum(increments[:-1])]
        rad=rng.uniform(0.45,2.2,size=n)
        points=rad[:,None]*np.stack([np.cos(t),np.sin(t)],axis=1)
        check(points)
print('RADIAL_CYCLE_GRAM_COMPLETION_PASS cases=',count,'dihedral_checks=',auto_checked)

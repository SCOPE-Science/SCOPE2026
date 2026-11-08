"""Reproduce finite diagnostics for reflex-sector reciprocal nearest neighbors.

Requires numpy, scipy, shapely. These numerical checks supplement, but do not
replace, the planar Poisson/Palm proof and the local-score law of large numbers.
"""
import math
import numpy as np
from scipy.integrate import simpson
from scipy.spatial import cKDTree
from shapely.geometry import Polygon, Point
from shapely.affinity import translate

PI=math.pi
checks=0

def check(test, message):
    global checks
    checks += 1
    if not test:
        raise AssertionError(message)

def sector(alpha, vertices=1441):
    if abs(alpha-2*PI)<1e-12:
        return Point(0,0).buffer(1,resolution=1200)
    angles=np.linspace(-alpha/2,alpha/2,vertices)
    return Polygon([(0,0)]+[(math.cos(t),math.sin(t)) for t in angles])

def area_union(poly,theta):
    return poly.union(translate(poly,xoff=math.cos(theta),yoff=math.sin(theta))).area

def exact_density(alpha, grid_size=60):
    if alpha<=PI:return 0.0
    p=sector(alpha)
    ts=np.linspace(PI-alpha/2,alpha/2,grid_size+1)
    return float(simpson(np.array([1/area_union(p,float(t)) for t in ts]),x=ts))

def closest_sector_neighbors(coords,alpha,k=48):
    _,idx=cKDTree(coords).query(coords,k=k)
    deltas=coords[idx[:,1:]]-coords[:,None,:]
    theta=np.arctan2(deltas[:,:,1],deltas[:,:,0])
    allowed=np.abs(theta)<alpha/2
    has=np.any(allowed,axis=1)
    next_index=np.where(has,idx[np.arange(len(coords)),np.argmax(allowed,axis=1)+1],-1)
    # k-nearest truncation only; observations with no eligible neighbor are left unpaired.
    paired=(next_index>=0)&(next_index[np.maximum(next_index,0)]==np.arange(len(coords)))
    return paired.mean(),np.sum(~has)


def main():
    slope=1/(2*PI/3+math.sqrt(3)/4)
    whole=PI/(4*PI/3+math.sqrt(3)/2)
    check(0.39566<slope<0.39567,'threshold coefficient')
    check(0.62150<whole<0.62152,'full-plane endpoint')
    c=sector(PI)
    check(abs(area_union(c,PI/2)-(2*PI/3+math.sqrt(3)/4))<1e-5,'semicircular lens')
    for a in [0.8*PI,PI,PI+0.02,PI+0.1,1.5*PI,2*PI]:
        p=exact_density(a)
        check(0<=p<=1,'probability normalization')
        if a<=PI:check(p==0,'no reciprocal pair in non-reflex sector')
        if a==PI+0.02:check(abs(p/0.02-slope)<0.005,'reflex threshold slope')
        if a==1.5*PI:check(abs(p-0.39893)<0.0004,'three-quarter-plane density')
        if a==2*PI:check(abs(p-whole)<4e-5,'unconstrained-plane density')
    for a in [PI+0.1,1.5*PI,1.8*PI]:
        s=sector(a)
        for t in [0.3,PI/2,PI-0.2]:
            check(abs(area_union(s,t)-area_union(s,-t))<1e-9,'mirror symmetry')
            check(area_union(s,t)>=a/2-1e-6,'area lower bound')
    rng=np.random.default_rng(20261101)
    points=rng.uniform(size=(50000,2))
    for a,expected,tolerance in [(PI,0.,1e-9),(PI+0.1,0.0382,0.013),(1.5*PI,0.3989,0.015),(2*PI,whole,0.015)]:
        obs,unresolved=closest_sector_neighbors(points,a)
        check(abs(obs-expected)<tolerance,f'seeded finite-point comparison angle={a} observation={obs}')
        check(unresolved<100,'limited 48-neighbor truncation')
    print('All',checks,'finite diagnostics passed.')
    print('Sharp half-plane slope:',format(slope,'.12f'))
    print('Unrestricted-plane density:',format(whole,'.12f'))
    print('Density at angle 3pi/2:',format(exact_density(1.5*PI),'.12f'))

if __name__=='__main__':main()

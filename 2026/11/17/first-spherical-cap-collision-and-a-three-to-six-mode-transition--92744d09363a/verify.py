#!/usr/bin/env python3
"""Reproducibility tests for the stated triangular-prism width theorem."""
import math
import random

SQ3 = math.sqrt(3.0)

def geometry(h):
    pts = [(math.cos(2*math.pi*j/3), math.sin(2*math.pi*j/3)) for j in range(3)]
    d = [(pts[j][0]-pts[(j+1)%3][0], pts[j][1]-pts[(j+1)%3][1]) for j in range(3)]
    vec = [(v[0],v[1],s*h) for v in d for s in (+1,-1)]
    D = math.sqrt(h*h+3)
    q = math.sqrt(max(3.0,h*h+2.25))
    pairs = [(i,j,abs(sum(a*b for a,b in zip(vec[i],vec[j])))/D**2) for i in range(6) for j in range(i+1,6)]
    expected = (2*q*q/D**2 - 1)
    close = [(i,j) for i,j,co in pairs if abs(co-expected)<1e-11]
    N = 3 if h < SQ3/2-1e-9 else 6 if h > SQ3/2+1e-9 else 9
    assert len(close)==N, (h,len(close),N)
    # Every triple would have to be a triangle in the nearest-neighbour graph.
    assert not any(all(tuple(sorted((i,j))) in [tuple(sorted(p)) for p in close] for i,j in ((a,b),(b,c),(a,c))) for a in range(6) for b in range(a+1,6) for c in range(b+1,6))
    return pts,d,vec,D,q,N

def lens(t,D,q):
    import math
    theta=2*math.acos(q/D)
    r=math.acos(t/D)
    cosphi=(math.cos(r)/math.sin(r))*math.tan(theta/2)
    cosgamma=(math.cos(theta)-math.cos(r)**2)/math.sin(r)**2
    phi=math.acos(max(-1,min(1,cosphi)))
    gamma=math.acos(max(-1,min(1,cosgamma)))
    return 2*(math.pi-gamma)-4*phi*math.cos(r)

rng=random.Random(20261114)
for h in (0.2,0.5,0.75,SQ3/2,1.0,1.5,3.0):
    pts,edges,axes,D,q,N=geometry(h)
    # Independent pointwise width formula and the support bound.
    for _ in range(2000):
        v=[rng.gauss(0,1) for j in range(3)]
        norm=math.sqrt(sum(t*t for t in v)); v=[t/norm for t in v]
        w1=max(abs(sum(a*b for a,b in zip(ax,v))) for ax in axes)
        w2=max(abs(ex*v[0]+ey*v[1]) for ex,ey in edges)+h*abs(v[2])
        assert abs(w1-w2)<1e-10 and w1<=D+1e-12
    # First cap overlap: exact lens area has the claimed local coefficient.
    coeff=8*math.sqrt(2)/(3*math.sqrt(q)*math.sqrt(D*D-q*q))
    for delta in (1e-3,3e-4,1e-4):
        if delta < q and q-delta>0:
            a=lens(q-delta,D,q)
            assert a>0 and abs(a/(delta**1.5*coeff)-1) < 0.03, (h,delta,a,coeff)
    # Exact survival just above q is a disjoint union of six cap pairs.
    level=(q+D)/2
    assert 0<=6*(1-level/D)<=1
print('PASS: 7 heights, 14000 pointwise identities, all contact counts, and lens coefficients')

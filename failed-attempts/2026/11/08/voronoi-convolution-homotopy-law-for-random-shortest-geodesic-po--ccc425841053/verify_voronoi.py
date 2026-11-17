#!/usr/bin/env python3
"""Independent finite and Monte Carlo checks for random shortest-geodesic torus loops.
Only corroborates the analytic proof; not an infinite certificate.
"""
import math, random
from fractions import Fraction
from itertools import product

# Stable convolution of all uniform samples on [-1/2,1/2] evaluated at integer k.
def spline_probability(m,k):
    s=Fraction(0)
    for j in range(m+1):
        a=Fraction(2*k+m-2*j,2)
        if a>0: s+=(-1)**j*math.comb(m,j)*a**(m-1)
    return s/math.factorial(m-1)

def typeB(n,r):
    return sum((-1)**j*math.comb(n+1,j)*(2*r-2*j+1)**n for j in range(r+1))
def typeA(n,r):
    return sum((-1)**j*math.comb(n+1,j)*(r-j)**n for j in range(r+1))

for m in range(3,14):
    q={k:spline_probability(m,k) for k in range(-m,m+1)}
    assert sum(q.values())==1
    assert sum(Fraction(k*k)*x for k,x in q.items())==Fraction(m,12)
    assert q[0]>0
    for k,p in q.items():
        if m%2==0:
            assert p == Fraction(typeA(m-1,k+m//2),math.factorial(m-1))
        else:
            assert p == Fraction(typeB(m-1,k+(m-1)//2),2**(m-1)*math.factorial(m-1))
assert spline_probability(3,0)==Fraction(3,4)
assert spline_probability(4,0)==Fraction(2,3)
assert spline_probability(5,0)==Fraction(115,192)

rng=random.Random(141583)

def shortest_shift(dx,dy,cosine):
    # Lattice basis (1,0),(cosine,sqrt(1-cosine**2)).
    best=(float('inf'),None)
    for u in (-1,0,1):
        for v in (-1,0,1):
            a=dx-u;b=dy-v
            distance2=a*a+b*b+2*cosine*a*b
            if distance2<best[0]:best=(distance2,(u,v))
    return best[1]

def experiment(m,cosine,samples):
    counts={}; sx=sy=sxx=sxy=syy=0
    for _ in range(samples):
        verts=[(rng.random(),rng.random()) for _ in range(m)]
        wx=wy=0
        for j,(x,y) in enumerate(verts):
            X,Y=verts[(j+1)%m]
            u,v=shortest_shift(X-x,Y-y,cosine)
            wx-=u;wy-=v
        counts[(wx,wy)]=counts.get((wx,wy),0)+1
        sx+=wx;sy+=wy;sxx+=wx*wx;sxy+=wx*wy;syy+=wy*wy
    n=samples
    return {"p0":counts.get((0,0),0)/n,"mean":(sx/n,sy/n),"second":(sxx/n,sxy/n,syy/n)}

if __name__=='__main__':
    print('exact_1d',[(m,str(spline_probability(m,0))) for m in (3,4,5,6,7)])
    for m,c,n in [(3,0,130000),(4,0,110000),(5,0,110000),(3,.5,170000),(5,.5,170000)]:
        out=experiment(m,c,n)
        # square and hex first two coordinates in lattice basis; sqrt det shape enters in geometric map
        if c==0:
            goal=float(spline_probability(m,0)**2)
            expected=(m/12,0,m/12)
        else:
            goal=7/12 if m==3 else None
            expected=(5*m/54,-5*m/108,5*m/54)
        print('trial',m,c,n,out,'p0_target',goal,'cov_target',expected)
        for a,b in zip(out['second'],expected):
            assert abs(a-b)<0.017
        assert max(abs(a) for a in out['mean'])<.016
        if goal is not None: assert abs(out['p0']-goal)<.007
    # Covariance for fundamental hex B1=(1,0), B2=(1/2,sqrt(3)/2)
    # Voronoi inradius=1/2, in-plane per-coordinate variance=5/72.
    square_const=6/math.pi
    hex_const=18*math.sqrt(3)/(5*math.pi)
    assert abs(hex_const/square_const-3*math.sqrt(3)/5)<1e-12
    print('GEODESIC_TORUS_HOMOLOGY_AND_BSPLINE_CHECKS_OK')

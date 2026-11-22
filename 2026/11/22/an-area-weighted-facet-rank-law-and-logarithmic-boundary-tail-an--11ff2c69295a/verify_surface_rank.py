#!/usr/bin/env python3
"""Independent low-dimensional Euclidean facet/volume checks; not an infinite proof."""
import itertools, math
from functools import lru_cache
import numpy as np
from scipy.spatial import ConvexHull
from scipy.special import zeta

@lru_cache(None)
def volume(n,t):
    if n==0: return 1.0
    if n==1: return float(t)
    return sum(math.comb(n,k)*(k*t+k*(2*n-k-1)/2) * (k**(k-2))*volume(n-k,t) for k in range(1,n+1))/n

def exact_surface(n,t):
    lower=n*volume(n-1,t+1)
    upper=sum(math.comb(n,k)* math.sqrt(k)*(k**(k-2))*volume(n-k,t) for k in range(1,n+1))
    return lower+upper

def convex_hull_measures(n,t):
    vertices=set()
    for j in range(n+1):
        v=tuple([0.0]*j+[float(t+i) for i in range(j,n)])
        vertices.update(itertools.permutations(v))
    points=np.array(sorted(vertices),dtype=float)
    hull=ConvexHull(points)
    surface=0.0
    for simplex in hull.simplices:
        edge=points[simplex[1:]]-points[simplex[0]]
        surface+=math.sqrt(max(0.0,np.linalg.det(edge@edge.T)))/math.factorial(n-1)
    return hull.volume,surface

count=0
for n in (2,3,4):
    for t in (0,0.5,1,2):
        v,s=convex_hull_measures(n,t)
        assert math.isclose(v,volume(n,t),rel_tol=5e-9,abs_tol=5e-9),(n,t,'volume')
        assert math.isclose(s,exact_surface(n,t),rel_tol=5e-9,abs_tol=5e-9),(n,t,'area')
        count+=1

# Check normalization of the limiting law from a controlled Stirling/zeta tail.
# At large k, e^-k k^(k-3/2)/k! = [sqrt(2*pi)*k^2]^-1 + O(k^-3).
alpha=sum(math.exp(-k + (k-1.5)*math.log(k)-math.lgamma(k+1)) for k in range(1,1001))
alpha+=float(zeta(2,1001))/math.sqrt(2*math.pi)
beta=1/(1+alpha)
assert abs(alpha-0.6186032871609)<2e-7
assert 0<beta<1
print('SURFACE_RANK_CHECK_PASS',count,'hull comparisons; alpha',alpha,'beta',beta)

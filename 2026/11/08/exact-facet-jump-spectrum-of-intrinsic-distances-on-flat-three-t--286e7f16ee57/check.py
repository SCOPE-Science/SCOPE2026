"""Numerical checks for facet signatures of intrinsic distances on flat three-tori.
The identities are proved analytically; sampling tests are illustrative only.
"""
import math
import numpy as np
from scipy.stats import qmc

sides=np.array([1.0,1.6,2.7]); vol=float(np.prod(sides))
thresholds=sides/2

def cap(r,d):
    if r<=d: return 0.0
    e=r-d
    return math.pi*(d*e*e+2*e**3/3)

def cdf_below_first_edge(r):
    assert r<math.hypot(thresholds[0],thresholds[1])
    return (4*math.pi*r**3/3-2*sum(cap(r,d) for d in thresholds))/vol

def diff2(f,r,h): return (f(r+h)-2*f(r)+f(r-h))/h**2

for d in thresholds[:2]:
    for h in (0.004, 0.002, 0.001):
        # Compute F'' separately at points on either side of a threshold
        left=diff2(cdf_below_first_edge,d-3*h,h)
        right=diff2(cdf_below_first_edge,d+3*h,h)
        background=(8*math.pi*d)/vol
        for dj in thresholds:
            if dj<d: background-=4*math.pi*(3*d-2*dj)/vol
        expected=-(4*math.pi*d)/vol
        assert abs(right-left-expected)<0.09, (d,h,right-left,expected)
        print('facet_jump',d,h,'approx',right-left,'expected',expected)

sob=qmc.Sobol(d=3,scramble=True,seed=20261103).random_base2(m=20)
x=np.minimum(sob*sides,(1-sob)*sides)
D=np.linalg.norm(x,axis=1)
for r in (0.3,0.52,0.74,0.84,0.90):
    observed=float(np.mean(D<=r)); predicted=cdf_below_first_edge(r)
    assert abs(observed-predicted)<0.0025,(r,observed,predicted)
    print('cdf',r,'observed',observed,'exact',predicted)
print('TORUS_FACET_CHECK_OK', 'sobol_samples',len(D),'thresholds',thresholds.tolist())

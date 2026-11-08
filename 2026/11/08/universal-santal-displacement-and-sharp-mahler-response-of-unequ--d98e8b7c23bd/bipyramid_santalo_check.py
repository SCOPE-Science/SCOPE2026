"""Exact-rational and independent convex-hull checks for unequal-height bipyramids.

Run: python bipyramid_santalo_check.py (requires sympy, scipy, numpy).
The analytical argument and its dimensional quantifiers are in RESULT.md.
"""
from fractions import Fraction as F
from math import comb, sqrt, pi
from itertools import product
import sympy as S
import numpy as np
from scipy.optimize import minimize_scalar
from scipy.spatial import ConvexHull


def q_integrated(d,a,b,z):
    R=a/(a-z); T=b/(b+z)
    return (R**d-T**d)/(d*z) if z else 1/a+1/b

def q_expanded(d,a,b,z):
    lo=-1/(b+z); hi=1/(a-z)
    return sum(F(comb(d-1,k),k+1)*z**k*(hi**(k+1)-lo**(k+1)) for k in range(d))

exact=0
for d in range(2,11):
    for a,b,z in [(F(2),F(1),F(1,7)),(F(3,2),F(1),F(-1,8))]:
        assert q_integrated(d,a,b,z)==q_expanded(d,a,b,z)
        exact+=1

x=S.symbols('x')
algebra=0
for d in range(2,11):
    a=S.Rational(3,2);b=S.Rational(1)
    q=((a/(a-x))**d-(b/(b+x))**d)/(d*x)
    r=a/(a-x);v=b/(b+x)
    g=lambda y:y**d*(d+1-d*y)
    assert S.simplify((S.diff(q,x)-(g(v)-g(r))/(d*x*x)))==0
    assert S.simplify(S.limit(S.diff(q,x),x,0)-S.Rational(d+1,2)*(1/a**2-1/b**2))==0
    algebra+=2

bounds=0
for d in range(2,18):
    for a,b in [(F(2),F(1)),(F(3,2),F(1)),(F(7),F(1)),(F(11,10),F(1))]:
        c=(a-b)/(d+1); m=(a-b)/2
        R=lambda z:a/(a-z)
        T=lambda z:b/(b+z)
        g=lambda y:y**d*(d+1-d*y)
        assert g(R(c))>g(T(c)),(d,a,b,'centroid sign')
        assert g(R(m))<g(T(m)),(d,a,b,'midpoint sign')
        bounds+=2

stability=0
for d in range(2,10):
    delta=S.symbols('delta')
    z=3*delta/(d+2)
    a=1+delta;b=1-delta
    q=((a/(a-z))**d-(b/(b+z))**d)/(d*z)
    target=-S.Rational(d-1,d+2)
    assert S.simplify(S.limit((q-2)/delta**2,delta,0)-target)==0
    stability+=1

numerical=0
for d in (2,3,4,6,10):
    prev=None
    for delta in (0.05,0.15,0.3,0.6,0.9):
        a=1+delta;b=1-delta
        opt=minimize_scalar(lambda z:q_integrated(d,a,b,z),bounds=(1e-8,(a-b)/2),method='bounded',options={'xatol':1e-12})
        z=opt.x
        assert (a-b)/(d+1)<z<(a-b)/2
        if prev is not None: assert opt.fun < prev
        prev=opt.fun
        numerical+=1

# Direct Euclidean convex-hull volume of the polar, independent of the integration.
# Each horizontal section is a homothet of the chosen B-polar.
polyhedral=0
basis=[np.array([[-1.],[1.]]),
       np.array([[-1.,-1.],[-1.,1.],[1.,-1.],[1.,1.]]),
       np.array([[1.,0.],[-0.5,sqrt(3)/2],[-0.5,-sqrt(3)/2]])]
for pts in basis:
    d=pts.shape[1]+1
    basevol=ConvexHull(pts).volume if pts.shape[1]>1 else 2.0
    for a,b,z in [(2.,1.,.2),(1.4,.7,.15),(3.,2.,.1)]:
        bottom=-1/(b+z);top=1/(a-z)
        vertices=np.array([list((1+z*t)*w)+[t] for t in (bottom,top) for w in pts])
        direct=ConvexHull(vertices).volume
        analytic=basevol*q_integrated(d,a,b,z)
        assert abs(direct-analytic)<1e-10,(d,direct,analytic)
        polyhedral+=1

print('ASYMMETRIC_BIPYRAMID_CHECKS_PASSED',exact,algebra,bounds,stability,numerical,polyhedral)

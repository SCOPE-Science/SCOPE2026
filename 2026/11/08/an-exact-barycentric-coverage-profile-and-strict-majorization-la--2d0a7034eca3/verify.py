"""Numerical and symbolic checks for affine-universal side-sampled triangle coverage.
Run: python verify.py
No numerical experiment is used as a proof of the infinite-parameter theorem.
"""
from __future__ import annotations
import math
import numpy as np
import sympy as sp


def g(x: float) -> float:
    if x <= 0 or x >= 1:
        return 0.0
    return x * (1 - x) * math.log((1 - x) / x)


def coverage(v):
    return sum(g(float(x)) for x in v)


def gprime(x):
    return (1 - 2*x)*math.log((1 - x)/x)-1


def inside_triangle(px, py, side_points):
    # Orientations of the three consistently CCW sides.
    a, b, c = side_points
    return (((b[...,0]-a[...,0])*(py-a[...,1]) - (px-a[...,0])*(b[...,1]-a[...,1])) >= 0) & \
           (((c[...,0]-b[...,0])*(py-b[...,1]) - (px-b[...,0])*(c[...,1]-b[...,1])) >= 0) & \
           (((a[...,0]-c[...,0])*(py-c[...,1]) - (px-c[...,0])*(a[...,1]-c[...,1])) >= 0)


def main():
    x=sp.symbols('x',positive=True)
    g0=x*(1-x)*sp.log((1-x)/x)
    assert sp.simplify(sp.diff(g0,x) - ((1-2*x)*sp.log((1-x)/x)-1)) == 0
    assert sp.simplify(sp.diff(g0,x,3) - 1/(x*x*(1-x)*(1-x))) == 0
    assert sp.integrate(6*g0*(1-x),(x,0,1)) == sp.Rational(1,4)
    assert sp.simplify(g0.subs(x,sp.Rational(1,3))*3 - 2*sp.log(2)/3) == 0

    # Deterministic exact quadrature of the single-corner integral for several barycentric triples.
    import mpmath as mp
    mp.mp.dps=40
    triples=[(mp.mpf(1)/3,)*3,(mp.mpf(1)/10,mp.mpf(3)/10,mp.mpf(6)/10),
             (mp.mpf(1)/100,mp.mpf(33)/100,mp.mpf(66)/100),
             (mp.mpf(4)/10,mp.mpf(4)/10,mp.mpf(2)/10)]
    for a,b,c in triples:
        u0=b/(1-c)
        corner=mp.quad(lambda u:(1-c)-b*c/(u-b),[u0,1])
        closed=a-b*c*mp.log((a+b)*(a+c)/(b*c))
        assert abs(corner-closed) < mp.mpf('1e-30')

    # Pairwise balancing increases coverage for all tested positive triples.
    rng=np.random.default_rng(87032)
    for _ in range(18000):
        v=np.sort(rng.dirichlet([1,1,1]))
        a,b,c=v
        if b-a < 1e-8: continue
        t=0.25*(b-a)
        assert coverage((a+t,b-t,c)) > coverage((a,b,c))-1e-13
        assert gprime(a) > gprime(b)

    # Direct affine-coordinate simulation: exactly one uniform point on each side.
    n=480000
    u,v,w=rng.random((3,n))
    q=np.zeros((3,n,2))
    q[0,:,0]=u
    q[1,:,0]=1-v; q[1,:,1]=v
    q[2,:,1]=1-w
    # Affine transformation to a scalene triangle; barycentric containment invariant.
    affine=np.array([[1.7,-0.36],[0.24,1.11]])
    offset=np.array([0.3,-0.2])
    mapped=q@affine.T+offset
    targets=[(1/3,1/3,1/3),(.1,.3,.6),(.4,.4,.2),(.2,.5,.3),(.05,.7,.25),(.75,.14,.11),(.4,.2,.4)]
    maxerr=0.0
    for a,b,c in targets:
        pt=np.array([b,c])@affine.T+offset
        est=inside_triangle(pt[0],pt[1],mapped).mean()
        exact=coverage((a,b,c))
        err=abs(est-exact)
        maxerr=max(maxerr,err)
        assert err<0.005,(a,b,c,est,exact)
    assert abs(coverage((1/3,1/3,1/3)) - 2*math.log(2)/3)<1e-14
    for a in np.linspace(0,1,201):
        assert abs(coverage((a,1-a,0)))<3e-14
    # Corner directional first-order coefficient is binary entropy.
    for t in [.1,.3,.5,.9]:
        eps=1e-5
        f=coverage((1-eps,eps*t,eps*(1-t)))
        h=-t*math.log(t)-(1-t)*math.log(1-t)
        assert abs(f/eps-h)<0.001
    print('VERIFY_OK symbolic_derivative=3 barycentric_integral=1/4 corner_quadratures=4 balancing_pairs=18000 scalene_triangle_samples=480000 target_points=7 max_absolute_error=%.7f near_vertex_entropy_checks=4'%maxerr)

if __name__=='__main__':
    main()

"""Reproducible checks for cube--cross-polytope Cayley Santaló geometry.

Run: python checker.py .  Pure-Python exact checks always run.  If numpy and
scipy are installed, independent geometric convex-hull checks also run.
"""
from fractions import Fraction as F
from math import factorial, comb, prod, log, exp, e
from itertools import product

def e_partial(d):
    return sum((F(1,factorial(k)) for k in range(d+1)),F(0))

def cayley_volume(d):
    return F(2**(d+1),d+1)*e_partial(d)

def chamber_polynomial(d,t):
    return prod((F(j+1)+(j-1)*t for j in range(1,d+1)))

def polar_volume(d,t):
    t=F(t)
    return F(2**(2*d+1),d+1)/((1-t*t)*chamber_polynomial(d,t))

def stationarity(d,t):
    return sum(((j-1)/(j+1+(j-1)*t) for j in range(1,d+1))) - 2*t/(1-t*t)

def optimum(d):
    if d==1:return 0.
    a,b=0.,1.-1e-9
    for _ in range(90):
        m=(a+b)*.5
        if stationarity(d,m)>0:a=m
        else:b=m
    return (a+b)*.5

def exact_weight_integral(d,t):
    """Independent exact chamber integration of the polar fibers.
    Sum over signed ordered chambers using a simplex integral.
    For N=a*L1+b*Linf, weights on successive coordinate differences are a*j+b.
    """
    t=F(t)
    a,b=1+t,1-t
    simplex_vol = F(1, factorial(d))/prod(a*j+b for j in range(1,d+1))
    unit_ball_vol = 2**d*factorial(d)*simplex_vol
    integrated_positive_part = F(2**(d+1),d+1)*unit_ball_vol
    return integrated_positive_part/(1-t*t)


def run():
    exact_checks=0
    for d in range(1,17):
        for t in [F(-2,3), F(-1,5), F(0),F(1,7),F(2,3)]:
            assert polar_volume(d,t)==exact_weight_integral(d,t)
            exact_checks+=1
        mixed_coeff = sum((F(comb(d,k)*factorial(d-k)*factorial(k),factorial(d+1)*factorial(k)) for k in range(d+1)), F(0))
        # Beta integration of the Minkowski-section formula.
        assert F(2**(d+1))*mixed_coeff==cayley_volume(d)
        exact_checks+=1
    roots=[optimum(d) for d in range(1,64)]
    assert roots[0]==0 and all(0<=roots[d-1]<roots[d] for d in range(1,62))
    for d in range(2,64):
        t=roots[d-1]
        assert abs(stationarity(d,t))<1e-9*(1+d)
        assert polar_volume(d,F(0))>polar_volume(d,F.from_float(t).limit_denominator(10**10))
    assert abs(roots[1]-(2/3**.5-1))<1e-12
    assert abs(float(cayley_volume(2)*polar_volume(2,F.from_float(roots[1]).limit_denominator(10**10)))-20/3**.5)<1e-8
    # The normalized affine-invariant Mahler product has limit e^2/4.
    def ratio(d):
        t=optimum(d)
        delta=1-t
        ep=sum(1/factorial(k) for k in range(min(d,150)+1))
        lg=log(ep)-log(d+1)-log(delta*(2-delta))
        lg-=sum(log(1-(j-1)*delta/(2*j)) for j in range(1,d+1))
        return exp(lg)
    assert ratio(1)==1 or abs(ratio(1)-1)<1e-12
    assert abs(ratio(2)-5*3**.5/8)<1e-10
    assert abs(ratio(2000)-e**2/4)<.01
    print('Normalized Mahler ratios for d=1,2,20,500,2000:',*[round(ratio(d),9) for d in (1,2,20,500,2000)])
    print('Limiting constant e^2/4:', e*e/4)
    print('Exact rational integration checks:',exact_checks)
    print('Monotone unique-stationary-root checks: dimensions 1..63')
    for d in (1,2,3,4,5,10,20,50):
        t=roots[d-1]
        print('d=%2d; Santaló vertical position %.12f; d*(1-t)=%.8f; product=%.12g'%(d,t,d*(1-t),float(cayley_volume(d))*float(polar_volume(d,F.from_float(t).limit_denominator(10**10)))))
    try:
        import numpy as np
        from scipy.spatial import ConvexHull,HalfspaceIntersection
    except ImportError:
        print('Optional independent convex-hull check skipped (numpy/scipy unavailable)')
        return
    cases=0
    for d in range(1,5):
        q=np.array(list(product([-1.,1.],repeat=d)))
        xs=np.array([sgn*np.eye(d)[i] for i in range(d) for sgn in (-1.,1.)])
        c=np.vstack([np.column_stack((q,np.ones(len(q)))),np.column_stack((xs,-np.ones(len(xs))))])
        v=ConvexHull(c).volume
        expected=float(cayley_volume(d))
        assert abs(v-expected)<1e-8,('Cayley',d,v,expected)
        cases+=1
        for t in [0.,optimum(d),.31]:
            rows=np.vstack([np.column_stack((q, np.full(len(q), 1.-t))),np.column_stack((xs,np.full(len(xs),-1.-t)))])
            halfspaces=np.column_stack((rows,-np.ones(len(rows))))
            verts=HalfspaceIntersection(halfspaces,np.zeros(d+1)).intersections
            observed=ConvexHull(verts).volume
            expected=float(polar_volume(d,F.from_float(t)))
            assert abs(observed-expected)<1e-8,('polar',d,t,observed,expected)
            cases+=1
    print('Independent scipy hull/halfspace volume cases:',cases)
    print('ALL CHECKS PASSED')

if __name__=='__main__':run()

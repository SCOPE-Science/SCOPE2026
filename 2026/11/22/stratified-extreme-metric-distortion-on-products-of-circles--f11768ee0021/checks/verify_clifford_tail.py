"""Numerical diagnostics for an intrinsic/extrinsic distance tail on products of circles.

Requirements: Python >=3.10, scipy >=1.9. Mathematical proof is in RESULT.md;
finite-precision evaluations below are diagnostics, not exhaustive certification.
Run: python checks/verify_clifford_tail.py
"""
import math
from itertools import combinations
from scipy.integrate import quad
from scipy.optimize import brentq

PI=math.pi

def distortion(u,r):
    num=sum(a*a*t*t for a,t in zip(r,u))
    den=4*sum(a*a*math.sin(t/2)**2 for a,t in zip(r,u))
    return math.sqrt(num/den) if den>0 else 1.0

def coefficient(r,A):
    d=len(r); k=len(A); AA=set(A)
    s=sum(r[j]**2 for j in AA)
    denominator=PI**k*math.gamma((d+k)/2+1)*(PI**2-4)**((d-k)/2)
    denominator*=math.prod((a*a if j in AA else a) for j,a in enumerate(r))
    return 2**d*s**((d+k)/2)/denominator

def two_term(r,epsilon):
    d=len(r)
    return (sum(coefficient(r,A) for A in combinations(range(d),1))*epsilon**((d+1)/2)
            +sum(coefficient(r,A) for A in combinations(range(d),2))*epsilon**((d+2)/2))

def exact_probability_2d(r,eps):
    """Deterministic 1-D quadratures over three disjoint corner neighborhoods."""
    assert len(r)==2
    threshold=PI/2-eps; delta=1.1
    def probability_corner(A):
        if A==(0,):
            f=lambda s,y: distortion((PI-s,y),r)-threshold
        elif A==(1,):
            f=lambda s,y: distortion((y,PI-s),r)-threshold
        else:
            f=lambda s,y: distortion((PI-s,PI-y),r)-threshold
        assert f(0.,0.)>0 and f(0.,delta)<0 and f(delta,0.)<0
        y_max=brentq(lambda y: f(0,y),0,delta,xtol=1e-14)
        def horizontal_width(y):
            if y>=y_max:return 0.
            return brentq(lambda s:f(s,y),0,delta,xtol=1e-14)
        return quad(horizontal_width,0,y_max,epsabs=2e-12,epsrel=1e-10)[0]
    return sum(probability_corner(A) for A in ((0,),(1,),(0,1)))/PI**2

def run():
    checks=0
    # Independent numerical sublevel integrals, not a fit to the coefficients.
    for radii in ((1.,1.),(1.,2.),(.7,1.5)):
        prev=None
        for eps in (0.012,0.006,0.003,0.0015):
            actual=exact_probability_2d(radii,eps)
            predicted=two_term(radii,eps)
            error=abs(actual/predicted-1)
            assert error<0.05
            if prev is not None:
                assert error<prev
            prev=error
            checks+=2
    # The single-antipodal corner coefficient is minimized by equal radii.
    for radii in ((1.,1.),(1.,2.),(.7,1.5),(1.,1.,1.),(1.,2.,3.),(.5,1.,2.,4.)):
        d=len(radii)
        c1=sum(coefficient(radii,(j,)) for j in range(d))
        sharp=d*2**d/(PI*math.gamma((d+3)/2)*(PI**2-4)**((d-1)/2))
        assert c1>=sharp-1e-12
        assert (abs(c1-sharp)<1e-12)==(max(radii)==min(radii))
        checks+=2
    # Global bound and numerical approach to antipodal-coordinate corners.
    for radii in ((1.,1.),(1.,2.),(1.,2.,3.)):
        d=len(radii)
        for n in range(1,801):
            u=[(PI/2)*(1+math.sin(n*(j+1)*.79173)) for j in range(d)]
            assert 1-1e-12 <= distortion(u,radii)<=PI/2+1e-12
        checks+=800
    print(f'CLIFFORD_STRATIFIED_TAIL_CHECKS_OK {checks}')

if __name__=='__main__':run()

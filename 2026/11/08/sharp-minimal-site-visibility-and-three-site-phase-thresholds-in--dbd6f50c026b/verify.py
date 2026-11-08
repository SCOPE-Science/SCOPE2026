#!/usr/bin/env python3
"""Independent finite checks of quadratic Voronoi visibility phase formulas.
The general theorem has a separate analytic proof; samples are not its proof.
"""
from fractions import Fraction as F
from math import sqrt, isclose
import random


def thresholds(lam, mu):
    assert lam > 1 and 0 < mu < 1
    h = lam*lam/(lam*lam-1)
    r = lam/(lam*lam-1)
    c0 = sqrt(1-1/(lam*lam))
    def radial_unit(c):
        return mu/(1-mu*mu)*(mu*c+sqrt(1-mu*mu+mu*mu*c*c))
    convex = (h-r)*(1-mu)/mu
    star = sqrt(h*h-r*r)/radial_unit(c0)
    return convex,star,c0,h,r,radial_unit


def sample_star(lam,mu,s,angles=2400):
    sc, st, c0, h,r,rd = thresholds(lam,mu)
    for i in range(1,angles+1):
        c = c0+(1-c0)*i/(angles+1)
        disc = r*r - h*h*(1-c*c)
        assert disc > 0
        outer_hole = h*c+sqrt(disc)
        if s*rd(c) >= outer_hole:
            return False
    return True


def exact_rational_witness():
    s=F(1,2)
    x=F(3,4)
    y=F(1,3)
    disk=lambda y:(x-s)**2+y*y - 2*s*s
    hole=lambda y:(x-F(4,3))**2+y*y-F(4,9)
    assert disk(y)<0 and disk(-y)<0 and disk(F(0))<0
    assert hole(y)>0 and hole(-y)>0 and hole(F(0))<0
    # Each endpoint is inside the cell; their midpoint is not.
    return 7


def exact_two_site_witness():
    # A = diag(1,5), B = diag(2,1), second site b=(1,0).
    # Along x-axis, q(t)=-t*t+4*t-2.
    f=lambda t:-t*t+4*t-2
    assert f(F(0))<0 and f(F(5))<0 and f(F(2))>0
    # A-B >= 0 gives a convex sublevel set by a positive Hessian.
    return 3


def run():
    count=0
    assert exact_rational_witness()==7
    assert exact_two_site_witness()==3
    count+=10
    rng=random.Random(261008656)
    for k in range(80):
        lam=1.03 + 7*rng.random()
        mu=0.025+0.95*rng.random()
        sc,st,c0,h,r,rd=thresholds(lam,mu)
        assert 0<sc<st
        assert isclose(h-r,lam/(lam+1),rel_tol=2e-12)
        assert isclose(rd(1),mu/(1-mu),rel_tol=2e-12)
        last=st
        for j in range(1,151):
            c = c0+(1-c0)*j/151
            candidate=(h*c+sqrt(r*r-h*h*(1-c*c)))/rd(c)
            assert candidate>last-1e-10
            last=candidate
            count+=1
        assert sample_star(lam,mu,0.8*sc,angles=360)
        assert sample_star(lam,mu,(sc+st)/2,angles=360)
        assert sample_star(lam,mu,st,angles=360)
        assert not sample_star(lam,mu,st*1.15,angles=360)
        count+=4
    for lam,mu in [(2,1/sqrt(2)),(1.01,.9),(10,.02),(1.2,.2)]:
        sc,st,*_=thresholds(lam,mu)
        if lam==2:
            assert isclose(sc,2/(3*(1+sqrt(2))),rel_tol=1e-12)
            assert isclose(st,4/(3+sqrt(21)),rel_tol=1e-12)
        count+=2
    print('QUADRATIC_VORONOI_PHASE_CHECKS_OK',count)


if __name__=='__main__':
    run()

#!/usr/bin/env python3
"""Standalone exact-rational and independent-integral checks for R_1 of a cube.

All-infinite-direction assertions follow from the analytic proof in RESULT.md;
finite checks here test coefficients, boundary values, and normalization.
"""
from fractions import Fraction as F
from math import sqrt, prod
from random import Random


def s_d(s, t):
    return 1 + s * s + t * t, 6 - 2 * s - 2 * t + s * t


def h2(s, t):
    a, b = s_d(s, t)
    return a * b * b


def grad_num(s, t):
    ss, d = s_d(s, t)
    return s * d - (2 - t) * ss, t * d - (2 - s) * ss


def rho_formula(u):
    a, b, c = sorted((abs(q) for q in u), reverse=True)
    if a == 0:
        raise ValueError('zero direction')
    s, t = b/a, c/a
    ss, d = s_d(s, t)
    return d / (6*a)  # homogeneous -1 radial formula; |u|=1 in usage


def rho_quadrature(u, panels=4000):
    # Independent integration of cube covariogram by composite Simpson.
    a = max(abs(q) for q in u)
    L = 2/a
    def f(r):
        return prod(max(0.0, 1-abs(q)*r/2) for q in u)
    h = L / panels
    return h/3*(f(0)+f(L)+4*sum(f(h*j) for j in range(1,panels,2))
               +2*sum(f(h*j) for j in range(2,panels,2)))


def main():
    two_thirds=F(2,3)
    assert h2(two_thirds, two_thirds)==F(19652,729)
    assert h2(F(1),F(1))==27
    assert h2(F(0),F(0))==36
    assert h2(F(0),F(1,2))==F(125,4)
    assert F(27)-h2(two_thirds,two_thirds)==F(31,729)
    assert grad_num(two_thirds,two_thirds)==(0,0)
    assert 3*two_thirds==2

    # The critical-angle difference factor is exact at every rational grid pair.
    for i in range(17):
        for j in range(17):
            s,t=F(i,16),F(j,16)
            ss,d=s_d(s,t)
            a,b=grad_num(s,t)
            assert a-b==(s-t)*(d-ss)
            assert d-ss>=0
            if (s,t)!=(F(1),F(1)):
                assert d-ss>0
            # Closed form bounds checked, not used as a substitute for proof.
            assert h2(s,t)>=F(19652,729)
            assert h2(s,t)<=36

    # Derivative factor on the equal-coordinate line and boundary lines.
    for j in range(21):
        x=F(j,20)
        a,b=grad_num(x,x)
        assert a==b==(1-x)**2*(3*x-2)
        edge0=grad_num(F(0),x)[1]
        assert edge0==-2*(2*x-1)*(x-1)
        edge1=grad_num(F(1),x)[1]
        assert edge1==-2*(x-1)**2

    rstar=17*sqrt(17)/81
    assert abs(rstar-rho_formula(tuple(q/sqrt(17) for q in (3,2,2))))<1e-14
    assert abs(rho_formula((1,0,0))-1)<1e-14
    assert abs(rho_formula((1/sqrt(3),)*3)-sqrt(3)/2)<1e-14
    assert rstar<sqrt(3)/2<1

    rng=Random(519204)
    for _ in range(160):
        u=[rng.uniform(-1,1) for j in range(3)]
        norm=sqrt(sum(q*q for q in u))
        u=tuple(q/norm for q in u)
        actual=rho_formula(u)
        numerical=rho_quadrature(u)
        assert abs(actual-numerical)<2.1e-11,(u,actual,numerical)
        assert rstar-1e-13 <=actual<=1+1e-13
    print('CUBE_R1_EXACT_CONTACT_CHECKS_OK')

if __name__=='__main__':
    main()

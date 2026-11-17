#!/usr/bin/env python3
"""Reproducible exact-identity and numerical checks for a population map."""
from fractions import Fraction as F
from math import sqrt


def fixed(delta):
    return (F(3, 10) + F(2,45)*delta,
            F(3, 10) - F(2,45)*delta, F(2,5))


def test_exact():
    import sympy as sp
    t, v, d, y, z, rr = sp.symbols('t v d y z rr')
    tstar = sp.Rational(2,5)
    sstar = 4*d/45
    tt = 1-2*t+sp.Rational(5,4)*t**2
    ss = d*t**2-2*t*v
    Y = sp.expand(tt.subs(t,tstar+y)-tstar)
    assert sp.expand(Y+y-sp.Rational(5,4)*y*y)==0
    assert sp.expand(tt.subs(t,tstar)-tstar)==0
    assert sp.expand(ss.subs({t:tstar,v:sstar})-sstar)==0
    K = -28*d/9
    R = sp.expand(ss.subs({t:tstar+y,v:sstar+K*y+rr})-sstar-K*Y)
    assert sp.expand(R + (sp.Rational(4,5)+2*y)*rr - sp.Rational(100,9)*d*y*y)==0
    a=sp.Rational(5,4)
    YY=sp.expand((-y+a*y*y).subs(y, -y+a*y*y, simultaneous=True))
    assert sp.expand(YY-(y-2*a*a*y**3+a**3*y**4))==0
    assert sp.Rational(8,25)*sp.Rational(100,9)*sp.Rational(5,9)==sp.Rational(160,81)
    assert sp.Rational(80,81)*(-sp.Rational(9,28))==-sp.Rational(20,63)


def test_numerical():
    for delta in (F(-9,28), F(9,28)):
        cc=float((F(3,4)+delta)/2)
        dd=float((F(3,4)-delta)/2)
        x1,x2,x3=.15,.20,.65
        t=x3; s0=x1-x2
        nmax=80000
        for n in range(nmax):
            s0, t = float(delta)*t*t-2*t*s0, 1-2*t+1.25*t*t
        x1,x2,x3=(1-t+s0)/2,(1-t-s0)/2,t
        star=tuple(float(v) for v in fixed(delta))
        target=nmax*(x1-star[0] if delta<0 else x2-star[1])
        assert abs(target+20/63)<0.004, (delta,target)
        scalar=(-1)**nmax*sqrt(nmax)*(x3-float(F(2,5)))
        assert abs(scalar-4/(5*sqrt(2)))<0.007, scalar
    x1,x2,x3=.30,.30,.40
    delta=F(1,4)
    cc=float((F(3,4)+delta)/2); dd=float((F(3,4)-delta)/2)
    x1star,x2star,x3star=(float(v) for v in fixed(delta))
    for n in range(200):
        s0=x1-x2
        tt= x3
        s0, tt= float(delta)*tt*tt-2*tt*s0, 1-2*tt+1.25*tt*tt
        x1,x2,x3=(1-tt+s0)/2,(1-tt-s0)/2,tt
    assert abs(x3-float(x3star))<1e-12
    assert abs(x1-x1star)+abs(x2-x2star)<1e-10

if __name__=='__main__':
    test_exact()
    test_numerical()
    print('QUASI_NONVOLTERRA_SELECTIVE_RESONANCE_OK')

#!/usr/bin/env python3
"""Numerical and exact-rational checks for the alternating sampled-feedback theorem.
This checker is corroborative; the analytic proof is in RESULT.md.
"""
import math
import random
from fractions import Fraction


def factors(a, theta, c):
    r = math.exp(-a)
    q = math.exp(-a * theta)
    u, v, w = 1-r, 1-q, q-r
    m0 = r-u*c
    mtheta = (r-w*c)/(1+v*c)
    return r, q, u, v, w, m0, mtheta, m0*mtheta


def threshold(a, theta):
    r, q, u, v, w, *_ = factors(a, theta, 0)
    if theta == 1:
        return math.inf
    B = r*(u+w)+v
    return (B+math.sqrt(B*B+4*u*w*(1-r*r)))/(2*u*w)


def direct_cell(a, theta, c, x, t):
    q=math.exp(-a*theta)
    z=q*x/(1+c*(1-q))
    return math.exp(-a*t)*x-c*(1-math.exp(-a*t))*z


def check():
    rng = random.Random(280126)
    tests = 0
    for _ in range(1250):
        a = rng.uniform(.05, 4.5)
        th = rng.uniform(.0001, .9999)
        c = 10**rng.uniform(-2, 3)
        x = rng.uniform(-8,8)
        r,q,u,v,w,m0,mt,P=factors(a,th,c)
        assert abs(direct_cell(a,th,c,x,1)-mt*x) < 3e-10 * max(1,abs(x),abs(mt*x))
        assert abs(direct_cell(a,0,c,x,1)-m0*x) < 3e-10 * max(1,abs(x),abs(m0*x))
        assert P > -r -1e-11
        tstar = threshold(a,th)
        if c < tstar * (1-1e-9): assert P<1+1e-9
        if c > tstar * (1+1e-9): assert P>1-1e-9
        for th0 in [0,th]:
            tt = rng.uniform(0,1)
            y = direct_cell(a,th0,c,x,tt)
            h=1e-6
            dy=(direct_cell(a,th0,c,x,tt+h)-direct_cell(a,th0,c,x,tt-h))/(2*h)
            z=math.exp(-a*th0)*x/(1+c*(1-math.exp(-a*th0)))
            assert abs(dy+a*y+a*c*z) < 3e-6 * max(1,abs(y),abs(c*z))
        tests+=1
    for a in [.2,1,math.log(2),3.5]:
        phases=[0,.01,.12,.4,.85,.99,.9999]
        levels=[threshold(a,p) for p in phases]
        assert all(levels[j]<levels[j+1] for j in range(len(levels)-1))
        for th in [0,.25,.75,.95,1]:
            r,q,u,v,w, *_ = factors(a,th,0)
            c1=r/u
            assert abs(factors(a,th,c1)[-1])<1e-10
            if 0<th<1:
                c2=r/w
                assert abs(factors(a,th,c2)[-1])<1e-10
                assert c1<c2<threshold(a,th)
            for c in [.01,1,5,10000]:
                P=factors(a,th,c)[-1]
                assert P>-r-1e-9
                if th==1: assert abs(P)<1
    # Exact witness: a=log(2), q=3/4, r=1/2, c*=6.
    r,q=Fraction(1,2),Fraction(3,4)
    u,v,w=1-r,1-q,q-r
    def exact(c):
        c=Fraction(c)
        return (r-u*c)*(r-w*c)/(1+v*c)
    assert exact(0)==Fraction(1,4)
    assert exact(1)==exact(2)==0
    assert exact(6)==1
    assert exact(3)==Fraction(1,7)
    for eps in [1e-3,1e-4,1e-5]:
        a=.8; th=1-eps
        b=a*threshold(a,th)
        assert abs(b*eps/(1+math.exp(a))-1)<4*eps
    print('PASS:',tests,'random cell/derivative/boundary cases; 20 endpoint/deadbeat cases; exact rational witness; singular scaling')

if __name__=='__main__':check()

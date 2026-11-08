#!/usr/bin/env python3
"""Exact-rational checks for a two-dimensional stochastic Euler second-moment theorem."""
from fractions import Fraction as F
from math import sqrt, isclose
from random import Random

checks = 0

def eq(x, y):
    global checks
    assert x == y, (x, y)
    checks += 1

def approx(x,y,eps=1e-9):
    global checks
    assert abs(x-y) <= eps*max(1,abs(y)), (x,y)
    checks += 1

def threshold(lam,a):
    A=1.+a
    D=lam+a
    return (A+D-sqrt((A-D)**2+4*a*a))/(A*D)

def rho(lam,a,h):
    alpha=1-h*(1+a)
    beta=1-h*(lam+a)
    c=2*h*a
    d1=alpha*alpha
    d2=beta*beta
    return (d1+d2+sqrt((d1-d2)**2+4*c*c))/2

def exact_case(lam,a,h):
    A=1+a
    D=lam+a
    alpha=1-h*A
    beta=1-h*D
    c=2*h*a
    t11=alpha*alpha
    t22=beta*beta
    det=A*D*(2-h*A)*(2-h*D)-4*a*a
    eq((1-t11)*(1-t22)-c*c,h*h*det)
    eq(t11+c+2*h,1+h*h*A*A)
    eq(t22+c+2*h*lam,1+h*h*D*D)
    eq(alpha*beta-2*h*a,alpha*beta-c)
    if det>0 and 1-t11>0 and 1-t22>0:
        u=2*(D*(2-D*h)+2*a*lam)/det
        v=2*(2*a+lam*A*(2-A*h))/det
        eq((1-t11)*u-c*v,2*h)
        eq(-c*u+(1-t22)*v,2*h*lam)
        assert u>1 and v>1
        eq((1-t11)*(u-1)-c*(v-1),h*h*A*A)
        eq(-c*(u-1)+(1-t22)*(v-1),h*h*D*D)

rng=Random(314159)
lam_values=[F(1,20),F(1,4),F(1,2),F(1),F(2),F(5)]
a_values=[F(0),F(1,9),F(1),F(3),F(12)]
h_values=[F(1,1000),F(1,100),F(1,20),F(1,5),F(1,2),F(1),F(5)]
for lam in lam_values:
    for a in a_values:
        for h in h_values:
            exact_case(lam,a,h)
            t=threshold(float(lam),float(a))
            if abs(float(h)-t)>1e-11:
                assert (rho(float(lam),float(a),float(h))<1)==(float(h)<t)
                checks+=1
for k in range(1000):
    lam=F(rng.randrange(1,200),rng.randrange(1,200))
    a=F(rng.randrange(0,200),rng.randrange(1,200))
    h=F(rng.randrange(1,100),rng.randrange(1,200))
    exact_case(lam,a,h)
    threshold0=threshold(float(lam),float(a))
    r=rho(float(lam),float(a),float(h))
    if abs(threshold0-float(h))>1e-9:
        assert (r<1)==(float(h)<threshold0),(lam,a,h,r,threshold0)
        checks+=1
for lam in [0.01,0.1,0.5,1.,5.]:
    approx(threshold(lam,0),2/max(1,lam))
    for a in [100.,1000.,10000.]:
        # The stable radical suffers cancellation at huge a; compare at increasing scales.
        target=(1+lam)/(a*a)
        assert abs(threshold(lam,a)/target-1)<0.1
        checks+=1
for lam in [1e-5,1e-6,1e-7]:
    approx(threshold(lam,1),(3-sqrt(5))/2,eps=1e-4)
for a in [0,0.1,1.,10.]:
    approx(threshold(1.,a),2/(1+a)**2)
print('VERIFY_OK',checks)

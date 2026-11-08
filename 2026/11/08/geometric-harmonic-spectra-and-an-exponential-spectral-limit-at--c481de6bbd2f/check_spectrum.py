#!/usr/bin/env python3
"""Finite corroboration of explicit phase-conjugacy and power-correlation formulas.

Requires only the Python standard library. Analytic infinite-series and weak-limit
statements are proved in RESULT.md and are not certified by sampling here.
"""
import cmath
import math

R=1/math.sqrt(2)
phase=math.pi/4


def exact(a,t):
    b=abs(a-.5)
    assert b>R
    s=1 if a>.5 else -1
    delta=math.sqrt(b*b-R*R)
    k=R/(b+delta)
    z=cmath.exp(2j*s*delta*t)
    return (1-k*k)**2*z/(1-k*k*z)


def parametric(a,w):
    b=abs(a-.5)
    s=1 if a>.5 else -1
    delta=math.sqrt(b*b-R*R)
    k=R/(b+delta)
    z=cmath.exp(2j*w)
    return -s*cmath.exp(1j*phase)*(z+k)/(1+k*z)


def integrate_cov(a,t,n=12000):
    b=abs(a-.5)
    s=1 if a>.5 else -1
    delta=math.sqrt(b*b-R*R)
    k=R/(b+delta)
    mean=-s*cmath.exp(1j*phase)*k
    accum=0j
    for i in range(n):
        w=math.pi*(i+.5)/n
        start=parametric(a,w)
        finish=parametric(a,w+s*delta*t)
        accum+=(finish-mean)*(start-mean).conjugate()
    return accum/n


def check_vector_field(a,theta):
    x=math.cos(theta);y=math.sin(theta)
    q=a*(x*x+y*y)+x*y
    dx=a*x+y-q*(x+y)
    dy=a*y-q*(y-x)
    ang=(x*dy-y*dx)/(x*x+y*y)
    expect=a-.5+R*math.cos(2*theta-phase)
    assert abs(ang-expect)<1e-13
    return ang

for a in (-1.,-.21,1.21,2.):
    b=abs(a-.5)
    delta=math.sqrt(b*b-R*R)
    k=R/(b+delta)
    assert abs(1-k*k-2*delta/(b+delta))<1e-12
    for theta in (.1,.7,2.9,4.2):
        check_vector_field(a,theta)
    for t in (0.,.35,1.17):
        err=abs(integrate_cov(a,t)-exact(a,t))
        assert err<3e-8,(a,t,err)
    assert abs(exact(a,0).real-(1-k*k))<1e-12
    print('SPECTRUM_COVARIANCE_OK',a,'critical_gap=',round(delta,6))
print('GEOMETRIC_POWER_SPECTRUM_FINITE_CHECK_OK')

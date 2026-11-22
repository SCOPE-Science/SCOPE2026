#!/usr/bin/env python3
"""Finite reproducibility checks for numerical-range axial gap formulas.
The theorem is established analytically; tests here are supplementary.
Standard-library only.
"""
from math import sqrt, pi, cos, sin, atan2, log, exp
from random import Random

COUNT = 0

def check(cond, msg):
    global COUNT
    COUNT += 1
    if not cond:
        raise AssertionError(msg)

def val(p, delta, t, theta):
    a = t**p
    den = 1.0 + a
    return (delta*(1-a) + (t+t**(p-1))*cos(theta))/den + 1j * ((t-t**(p-1))*sin(theta))/den

def B(p, t):
    return abs(t-t**(p-1))/(1+t**p)

def HdivC(p, t):
    return (1-t**p)/(t+t**(p-1))

def max_golden(f, lo, hi, iterations=220):
    r=(sqrt(5)-1)/2
    c=hi-r*(hi-lo); d=lo+r*(hi-lo)
    fc=f(c); fd=f(d)
    for _ in range(iterations):
        if fc>fd:
            hi=d; d=c; fd=fc; c=hi-r*(hi-lo); fc=f(c)
        else:
            lo=c; c=d; fc=fd; d=lo+r*(hi-lo); fd=f(d)
    x=(lo+hi)/2
    return x,f(x)

def tau_and_M(p):
    t,m=max_golden(lambda x:B(p,x),1e-8,1)
    return t,m

def axial(p,delta,t):
    v=delta*HdivC(p,t)
    return B(p,t)*sqrt(max(0,1-v*v)) if abs(v)<=1 else 0

def max_axis(p,delta):
    # Find feasible t in (0,1): H/C strictly decreases from infinity to zero.
    if delta==0:
        return tau_and_M(p)[1]
    lo=0.;hi=1.
    for _ in range(90):
        mid=(lo+hi)/2
        if mid<1e-280 or abs(delta*HdivC(p,mid))>1:
            lo=mid
        else: hi=mid
    lo=max(hi,1e-12)
    x,v=max_golden(lambda t:axial(p,delta,t),lo,1)
    return v

rng=Random(20261120)
# Direct expression from the norming functional, and quartic exact top and axis.
for delta in [0, 1e-5, 0.001, 0.01, .1, .3, 1, 2, 5, 13, 100, -0.001, -.3, -3]:
    predicted=1/(2*sqrt(2*(1+2*delta*delta)))
    u=1/(3+8*delta*delta)
    k=sqrt(u)
    t=sqrt((1-k)/(1+k))
    c=-2*delta*k/sqrt(1-k*k)
    theta=atan2(sqrt(max(0,1-c*c)),c)
    z=val(4,delta,t,theta)
    check(abs(z.real)<1e-11,("axis real",delta,z))
    check(abs(z.imag-predicted)<1e-11,("axis value",delta,z,predicted))
    x,m=max_golden(lambda v: v*(1-(1+4*delta*delta)*v)/(1+v)**2,0,1/(1+4*delta*delta))
    check(abs(sqrt(m)-predicted)<1e-9,("axis scalar max",delta,x))
    check(abs(axial(4,delta,t)-predicted)<1e-11,("axis formula",delta,t))
    ttop=sqrt((1-1/sqrt(3))/(1+1/sqrt(3)))
    ztop=val(4,delta,ttop,pi/2)
    check(abs(ztop.imag-1/(2*sqrt(2)))<1e-11,("top imag",delta))
    check(abs(ztop.real-delta*sqrt(3)/2)<1e-11,("top real",delta))
    check(abs(max_axis(4,delta)-predicted)<2e-9,("optimized axis",delta))
    for i in range(150):
        rt=exp(rng.uniform(-6,6))
        th=rng.uniform(-pi,pi)
        z=val(4,delta,rt,th)
        check(z.imag <= 1/(2*sqrt(2))+1e-12,("imag cap",delta,rt,th,z))

# All-p local quadratic coefficient and asymptotic strong-diagonal tail.
for p in [1.2,1.4,1.75,2.5,3,4,5,7]:
    tau,M=tau_and_M(p)
    beta=(M/2)*HdivC(p,tau)**2
    check(0<tau<1 and M>0 and beta>0,("tau",p,tau,M,beta))
    for delta in [0.003,0.007,0.012]:
        m=max_axis(p,delta)
        ratio=(M-m)/(delta**2)
        check(abs(ratio/beta-1)<.009,("small gap",p,delta,ratio,beta))
    for delta in [80,200]:
        m=max_axis(p,delta)
        v=abs(p-2)/(2*p*delta)
        check(abs(m/v-1)<.08,("large gap",p,delta,m/v))

print('AXIAL_GAP_DIAGNOSTIC_OK',COUNT)

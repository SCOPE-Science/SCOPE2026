#!/usr/bin/env python3
"""Numerical diagnostics for the damped two-snapshot rotation frame."""
import math

COUNT = 0

def check(cond, info):
    global COUNT
    COUNT += 1
    if not cond:
        raise AssertionError(info)

def gap(alpha, t):
    q = math.exp(-alpha*t)
    return (1+q-math.sqrt((1-q)**2+4*q*math.cos(t/2)**2))/2

def F(alpha, t):
    return math.exp(-alpha*t)+math.cos(t)-(alpha*alpha-1)/(2*alpha)*math.sin(t)

def root(alpha):
    lo, hi = 0.0, math.pi
    for _ in range(100):
        mid = (lo+hi)/2
        if F(alpha,mid)>0:
            lo=mid
        else:
            hi=mid
    return (lo+hi)/2

for alpha in (0.01, 0.05, 0.1, 0.5, 1, 2, 4, 10, 30):
    tstar = root(alpha)
    check(0<tstar<math.pi, ('root range',alpha))
    check(abs(F(alpha,tstar))<2e-12, ('root residual',alpha))
    optimum = gap(alpha,tstar)
    check(optimum>math.exp(-alpha*math.pi), ('later half-turn bound',alpha))
    for k in range(100,600):
        t = 10*math.pi*k/600
        if abs(t-tstar)>1e-7:
            check(gap(alpha,t) <= optimum+1e-12, ('global grid',alpha,t))
    for k in range(1,200):
        t = math.pi*k/200
        if abs(t-tstar)>1e-7:
            diff=gap(alpha,tstar)-gap(alpha,t)
            check(diff> -2e-13,('first-half maximum',alpha,t,diff))
        # Rotation-frame matrix trace+determinant calculation.
        u=math.exp(-alpha*t/2)
        cs, ss=math.cos(t/2),math.sin(t/2)
        a11=1+u*u*cs*cs
        a12=u*u*cs*ss
        a22=u*u*ss*ss
        eig=(a11+a22-math.sqrt((a11-a22)**2+4*a12*a12))/2
        check(abs(eig-gap(alpha,t))<2e-14,('matrix eigenvalue',alpha,t))
for alpha in (20,50,100):
    v=alpha*root(alpha)
    check(abs(v-2.21771510575709)<0.008,('strong scale',alpha))
    C=2.21771510575709*(2.21771510575709-2)/4
    check(abs(alpha*alpha*gap(alpha,root(alpha))-C)<1e-4,('strong coefficient',alpha))
print('DAMPED_TWO_SNAPSHOT_CHECK_OK', COUNT)

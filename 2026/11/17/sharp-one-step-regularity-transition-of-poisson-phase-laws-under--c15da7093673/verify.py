#!/usr/bin/env python3
"""Reproduce one-step sine-kick pushforward density coefficients.
Standard library only; finite numerical checks supplement the written proof.
"""
import math
import cmath

pi=math.pi

def poisson(theta, a):
    z=complex(math.cos(theta),math.sin(theta))
    return (1-abs(a)**2)/(2*pi*abs(z-a)**2)

def f(x,s,gamma=0.,omega=0.):
    return x+omega-s*math.sin(x+gamma)

def fp(x,s,gamma=0.):
    return 1-s*math.cos(x+gamma)

def bisect(fn,lo,hi):
    flo=fn(lo)
    for _ in range(85):
        mid=(lo+hi)/2
        if fn(mid)*flo<=0:
            hi=mid
        else:
            lo=mid;flo=fn(mid)
    return (lo+hi)/2

a=0.35+0.13j
# Critical cubic: y=theta-sin(theta), density ~ 2p(0)/6**(2/3) y**(-2/3).
s=1.
C=2*poisson(0,a)/6**(2/3)
ratios=[]
for x in (0.09,0.045,0.02,0.01):
    y=f(x,s)-f(0.,s)
    dens=poisson(x,a)/fp(x,s)
    ratios.append(dens*y**(2/3)/C)
assert max(abs(v-1) for v in ratios)<0.08
# Supercritical quadratic fold: one-sided contributions of two local branches.
s=1.3
xc=math.acos(1/s)
yc=f(xc,s)
A=math.sqrt(s*s-1)
B=math.sqrt(2/A)*poisson(xc,a)
fold_ratios=[]
for dh in (3e-4,1e-4,3e-5,1e-5):
    h=math.sqrt(2*dh/A)
    r1=bisect(lambda x:f(x,s)-yc-dh,xc-3*h,xc)
    r2=bisect(lambda x:f(x,s)-yc-dh,xc,xc+3*h)
    val=(poisson(r1,a)/abs(fp(r1,s))+poisson(r2,a)/abs(fp(r2,s)))*math.sqrt(dh)/B
    fold_ratios.append(val)
assert max(abs(v-1) for v in fold_ratios)<0.02
# Critical exponents and derivative boundary, verified across phase offsets.
for s in (-2.,-1.3,-1.,-.6,0.,.4,1.,1.4,3.):
    for gamma in (-.9,0.,1.4):
        def d(x):return fp(x,s,gamma)
        for t in range(13):
            x=2*pi*t/13
            # Complex-step derivative of the original analytic lift, not the derivative formula.
            h=1e-20
            diff=(complex(x,h)-s*cmath.sin(complex(x+gamma,h))).imag/h
            assert abs(d(x)-diff)<2e-14
        if abs(s)<1:
            assert min(d(2*pi*j/5000) for j in range(5000))>0
        if abs(s)==1:
            xc=(-gamma if s==1 else pi-gamma)
            assert abs(d(xc))<1e-14
            assert abs(s*math.sin(xc+gamma))<1e-14
            assert abs(s*math.cos(xc+gamma)-1)<1e-14
        if abs(s)>1:
            xc=math.acos(1/s)-gamma
            assert abs(d(xc))<1e-13
            assert abs(abs(s*math.sin(xc+gamma))-math.sqrt(s*s-1))<1e-13
print('VERIFY_OK critical_cubic_cases=4 fold_cases=4 derivative_grid=351')
print('CRITICAL_COEFFICIENT %.12f cubic_ratios'%C,*('%.6f'%v for v in ratios))
print('FOLD_COEFFICIENT %.12f fold_ratios'%B,*('%.6f'%v for v in fold_ratios))

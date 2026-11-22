#!/usr/bin/env python3
"""Independent numerical diagnostics for the unit-base uniform-angle inradius law.

The accompanying proof is analytic; these finite tests are not proof certificates.
Uses only the Python standard library.
"""
import math
import random

PI = math.pi

def density(r):
    if r < 0 or r > 0.5:
        return 0.0
    if r == 0:
        return 8 / PI
    if r == 0.5:
        return 0.0
    a = math.acos(2*r) + 2*r*math.acosh(1/(2*r))
    return 16*a/(PI*PI*(1 + 4*r*r))

def mode_equation(r):
    a = math.acos(2*r) + 2*r*math.acosh(1/(2*r))
    ap = 2*math.acosh(1/(2*r)) - 4/math.sqrt(1-4*r*r)
    return (1+4*r*r)*ap - 8*r*a

def simpson(f,a,b,n=20000):
    assert n%2 == 0
    h=(b-a)/n
    s=f(a)+f(b)
    for k in range(1,n):
        s+=(4 if k%2 else 2)*f(a+k*h)
    return s*h/3

def original_survival(t):
    u0=2*math.atan(2*t)
    def integrand(u):
        return math.acos(max(-1.0,min(1.0,math.cos(u)+2*t*math.sin(u))))
    return 8/(PI*PI)*simpson(integrand,u0,PI/2,20000)

norm=simpson(density,0,.5,20000)
assert abs(norm-1) < 1e-7,("normalization",norm)
for t in (.01,.05,.1,.2,.35,.45):
    d=simpson(density,t,.5,20000)
    s=original_survival(t)
    assert abs(d-s)<8e-7,("two independent integral representations",t,d,s)
lo,hi=.001,.49
assert mode_equation(lo)>0 and mode_equation(hi)<0
for _ in range(75):
    mid=(lo+hi)/2
    if mode_equation(mid)>0:lo=mid
    else:hi=mid
mode=(lo+hi)/2
assert abs(mode-0.0764841973658)<1e-10,mode
assert all(mode_equation(x)>0 for x in (.005,.02,.05))
assert all(mode_equation(x)<0 for x in (.10,.2,.4))
for t in (.001,.002,.005):
    left=simpson(density,0,t,4000)
    assert abs(left/(8*t/PI)-1)<.03,("lower tail",t,left)
for h in (.0005,.001,.002):
    right=simpson(density,.5-h,.5,4000)
    predicted=64/(3*PI*PI)*h**1.5
    assert abs(right/predicted-1)<.01,("upper tail",h,right)
# Deterministic Monte Carlo on the angle simplex, used only as a diagnostic.
rng=random.Random(20261121)
n=100000
thresholds=(.05,.15,.3,.45)
counts=[0]*len(thresholds)
for _ in range(n):
    x,y,z=[-math.log(max(1e-300,rng.random())) for _ in range(3)]
    alpha=PI*x/(x+y+z); beta=PI*y/(x+y+z)
    r=1/(1/math.tan(alpha/2)+1/math.tan(beta/2))
    for i,t in enumerate(thresholds):
        counts[i]+=r<=t
for t,c in zip(thresholds,counts):
    expected=simpson(density,0,t,20000)
    assert abs(c/n-expected)<.009,("Monte Carlo diagnostic",t,c/n,expected)
print("ALL_CHECKS_PASSED")
print("density integral",norm,"mode",mode,"peak",density(mode))
print("6 independent survival comparisons; 6 endpoint comparisons; 4 seeded sampling comparisons")

"""Numerical and algebraic diagnostics for two-region Gaussian photometry.

This checker supplements, but does not replace, the analytic proof in RESULT.md.
Python 3 standard library only. Run: python CHECK.py
"""
import math
import random

COUNT = 0

def check(cond, msg):
    global COUNT
    COUNT += 1
    if not cond:
        raise AssertionError(msg)

def h(c, x):
    return -math.expm1(-c*x) + x*math.expm1(-c)

def N(c, x):
    q = -math.expm1(-c)
    return 2*x*(1-x)*(c*math.exp(-c*x)-q)-(1-2*x)*h(c, x)

def n_expanded(c, x):
    return (1+math.exp(-c))*x-1+math.exp(-c*x)*(1-2*x+2*c*x*(1-x))

def N2(c, x):
    return -c*c*math.exp(-c*x)*(2*c*x*x-(2*c+6)*x+3)

def Q(c, x):
    z=h(c,x)
    return z*z/(x*(1-x))

def root(c):
    lo = 1.e-12
    hi = .5
    check(N(c,lo)>0 and N(c,hi)<0, 'root bracket')
    for _ in range(100):
        m=(lo+hi)/2
        if N(c,m)>0: lo=m
        else:hi=m
    return (lo+hi)/2

# Symbolic structural identity tests by substitution, including boundary behavior.
for c in (0.1,0.35,1.,2.,4.,8.,25.):
    check(c-1+math.exp(-c)>0, 'left derivative sign')
    check(1-(1+c)*math.exp(-c)>0, 'right derivative sign')
    for j in range(1,100):
        x=j/100
        check(abs(N(c,x)-n_expanded(c,x))<4e-13, 'N expansion')
        check(h(c,x)>0, 'positive secant excess')
        check(Q(c,x)>0, 'positive determinant')
        # finite-difference second derivative of N, away from boundaries
        eps=1.e-4
        fd=(N(c,x+eps)-2*N(c,x)+N(c,x-eps))/(eps*eps)
        check(abs(fd-N2(c,x))<2e-3*max(1.,abs(N2(c,x))), 'N second derivative')

for c in (0.05,0.1,0.5,1.,2.,5.,10.,20.,40.,100.):
    x=root(c)
    check(0<x<.5, 'inner area fraction < half')
    check(abs(N(c,x))<1e-11, 'stationarity')
    best=Q(c,x)
    for j in range(1,1000):
        t=j/1000
        check(Q(c,t)<=best*(1+4e-12), 'global optimality grid')

# Fisher determinant computed both as a 2x2 matrix and via secant formula.
for c in (.25,1.,2.,5.,11.):
    for x in (.1,.28,.45,.63,.9):
        p1=1-math.exp(-c*x)
        p2=math.exp(-c*x)-math.exp(-c)
        a1=x
        a2=1-x
        b=2.5
        i11=p1*p1/(b*a1)+p2*p2/(b*a2)
        i22=(a1+a2)/b
        i12=(p1+p2)/b
        det=i11*i22-i12*i12
        check(abs(det-Q(c,x)/(b*b))<3e-14, '2x2 Fisher determinant')

# Radial equal-area discretization: nonradial partitions cannot beat the
# continuum optimum (these are diagnostics only, not a rearrangement proof).
rng=random.Random(24681357)
for c in (.3,2.,10.):
    x=root(c)
    mx=Q(c,x)
    width=1/80
    masses=[math.exp(-c*j*width)-math.exp(-c*(j+1)*width) for j in range(80)]
    total=sum(masses)
    for _ in range(4000):
        flags=[rng.randrange(2) for j in range(80)]
        size=sum(flags)
        if size in (0,80):continue
        area=size/80
        p=sum(v for v,f in zip(masses,flags) if f)
        val=(p-area*total)**2/(area*(1-area))
        check(val<=mx*(1+2e-13), 'discrete partition inequality')

# Small and large outer-radius limits.
for c in (0.01,0.02,0.04):
    x=root(c)
    check(abs(x-(.5-c/12)) < .03*c*c, 'small-c expansion')
y=1.2564312086261697
for c in (300.,600.):
    check(abs(c*root(c)-y)<.035, 'large-c scaling')
print(f'PASS {COUNT} deterministic diagnostics; analytic statements are proved in RESULT.md')

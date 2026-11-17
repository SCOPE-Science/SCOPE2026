#!/usr/bin/env python3
"""Deterministic consistency checks for optimal charging-clock formulas.

Uses the Python standard library only. These checks are finite diagnostics;
the mathematical statements for continuous parameter ranges rely on proof.
"""
import math

checks = 0

def check(condition, label):
    global checks
    assert condition, label
    checks += 1

def bisect_decreasing(fn, a, b, goal, n=150):
    assert fn(a) > goal > fn(b), (a, b, goal, fn(a), fn(b))
    for _ in range(n):
        m = (a+b)/2
        if fn(m) > goal:
            a = m
        else:
            b = m
    return (a+b)/2

def y_of(s):
    return -math.expm1(-s)

def logistic(v):
    return 1/(1+math.exp(-v))

def model(E, a):
    p0=logistic(-E); pa=logistic(a-E); d=pa-p0
    A=a*d
    def f(y):
        p=p0+d*y
        D=p*math.log(p/p0)+(1-p)*math.log((1-p)/(1-p0))
        return D/A
    def fp(y):
        p=p0+d*y
        return (d/A)*math.log(p*(1-p0)/(p0*(1-p)))
    def fpp(y):
        p=p0+d*y
        return (d*d/A)/(p*(1-p))
    return f, fp, fpp

def ratio_general(s, f, fp):
    u=math.exp(-s);y=1-u
    Q=y*fp(y)-f(y)
    B=f(y)-s*u*fp(y)
    return u*Q/B

def efficiency_general(s, h, f):
    return f(y_of(s))/(y_of(s)+h*s)

# The linear-response power optimum is the nonzero positive root of exp(s)=1+2s.
sp=bisect_decreasing(lambda s: 1+2*s-math.exp(s), 1, 2, 0)
yp=y_of(sp)
check(abs(math.exp(sp)-1-2*sp)<1e-13, 'power clock')
check(1.25<sp<1.26, 'power clock bracket')

def threshold_lr(s):
    return (1-math.exp(-s))/(math.exp(s)-1-2*s)

previous=1e20
for h in (1e-8,1e-6,1e-4,1e-3,0.01,0.1,1,10,100,1e4):
    s=bisect_decreasing(threshold_lr,sp+1e-9,max(20.,math.log(1/h)+10),h)
    check(s>sp, 'LR optimizer later than power clock')
    check(s<previous, 'LR clock monotonic with housekeeping')
    previous=s
    u=math.exp(-s); y=1-u
    numerator=y*(y*u+h*(2*s*u-y))
    check(abs(numerator)<1e-8, 'LR first-order condition')
    for shift in (-0.1,0.1):
        t=s+shift
        if t<=0: continue
        yt=y_of(t);ut=math.exp(-t)
        deriv=yt*(yt*ut+h*(2*t*ut-yt))
        check((deriv>0) if shift<0 else (deriv<0), 'LR unique turning sign')
    eta=y*y/(2*(y+h*s))
    check(0<eta<.5, 'LR nontrivial efficiency')
    if h<1e-3:
        L=math.log(1/h)
        check(abs(s-(L+2*h*L)) < 6*h*h*L*L+1e-8, 'LR small-cost clock expansion')
        estimate=.5-.5*h*(L+1)
        check(abs(eta-estimate)<2*h*h*L*L+1e-10, 'LR small-cost efficiency expansion')
    if h>100:
        estimate=sp+yp/(h*(2*sp-1))
        check(abs(s-estimate)<2/h**2, 'LR strong-cost clock expansion')
        check(abs(h*eta-yp*yp/(2*sp))<2/h, 'LR strong-cost efficiency')

# The derivative numerator of the LR root's threshold is strictly negative.
for i in range(1,151):
    s=.025*i
    numerator=4-math.exp(s)-(3+2*s)*math.exp(-s)
    check(numerator<0, 'LR threshold strict derivative')

for E,a in ((.2,.3),(.5,2),(1,1.5),(1,6),(2,.2),(4,1),(6,5)):
    f,fp,fpp=model(E,a)
    rho=f(1)
    check(0<rho<1, 'finite affinity long-time efficiency')
    check(abs(fp(1)-1)<1e-12, 'last derivative equals affinity work')
    for j in range(1,25):
        y=j/25
        check(fpp(y)>0 and y*fp(y)>f(y), 'convexity and secant inequality')
    for h in (.0001,.000001):
        # The root is uniquely located on the large-time branch at small housekeeping.
        approx=math.log(1/h)+math.log((1-rho)/rho)
        S=max(2.,approx-2.)
        check(ratio_general(S,f,fp)>h, 'asymptotic large-branch bracket')
        s=bisect_decreasing(lambda t:ratio_general(t,f,fp),S,25,h)
        approx=math.log(1/h)+math.log((1-rho)/rho)
        check(abs(s-approx)<.015, 'finite-affinity logarithmic clock')
        eta=efficiency_general(s,h,f)
        predicted=rho-rho*h*(approx+1)
        check(abs(eta-predicted)<.00004, 'finite-affinity efficiency deficit')
        # Numerical stationarity, not an infinite-range uniqueness proof.
        u=math.exp(-s);y=1-u
        D=u*(y*fp(y)-f(y))+h*(s*u*fp(y)-f(y))
        check(abs(D)<1e-10, 'finite-affinity stationarity')

print('PASS: %d deterministic checks (all-parameter proofs are analytic).' % checks)

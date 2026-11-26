#!/usr/bin/env python3
"""Supplementary numerical checks for a two-band depth-cost model.

Run with Python 3.10 or newer: python verify_two_band.py
The theorem is proved analytically in RESULT.md; these finite checks do not
replace the proof or establish exhaustiveness of real-parameter claims.
"""
import math
import random

checks = 0

def check(condition, message):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(message)

def f(y):
    return (y-1)*math.exp(19*y)+20*(20*y-1)

def fp(y):
    return (19*y-18)*math.exp(19*y)+400

def fpp(y):
    return (361*y-323)*math.exp(19*y)

def bisect(func, left, right, iterations=115):
    fl = func(left)
    fr = func(right)
    check(fl*fr < 0, 'root not bracketed')
    for _ in range(iterations):
        mid = (left+right)/2
        fm = func(mid)
        if fm == 0:
            return mid
        if fl*fm > 0:
            left, fl = mid, fm
        else:
            right = mid
    return (left+right)/2

def optimal_z(k):
    if k <= 1/21:
        return 0.0
    derivative = lambda z: math.exp(z)-k*math.exp(-k*z)-20*k*math.exp(-20*k*z)
    # The theoretical upper bound for all k > 1/21.
    high = math.log(21*k)/(1+k)
    check(high > 0, 'bad upper bracket')
    check(derivative(0) < 0, 'boundary derivative')
    check(derivative(high) >= -1e-10, 'upper bracket must exceed optimum')
    low = 0.0
    for _ in range(100):
        mid = (low+high)/2
        if derivative(mid) < 0:
            low=mid
        else:
            high=mid
    return (low+high)/2

def k_from_y(y):
    G = math.exp(-y)+20*math.exp(-20*y)
    h = lambda k: math.log(k)+math.log(G)-y/k
    high=1.0
    while h(high) < 0:
        high*=2
    return bisect(h, 1e-8, high)

roots=[bisect(f, a,b) for a,b in [(0,.1),(.1,.5),(.5,1)]]
expected=[(0.05695765175475504,0.18515052002851964,0.30762890509830365),
          (0.2436230469436609,1.2893711244254875,0.1889471869879306),
          (0.9999978708559953,3.591113515890582,0.2784645671686599)]
for y,(ey,ek,ez) in zip(roots,expected):
    k=k_from_y(y)
    z=optimal_z(k)
    check(abs(y-ey)<1e-10,'y critical value')
    check(abs(k-ek)<1e-9,'k critical value')
    check(abs(z-ez)<1e-9,'depth critical value')
    check(abs(k*z-y)<1e-10,'scaled depth')
    check(abs(math.exp(z)-k*(math.exp(-y)+20*math.exp(-20*y)))<1e-9,'stationarity')

check(f(0)<0 and f(.1)>0 and f(.5)<0 and f(1)>0,'four exact sign witnesses')
check(fpp(.8)<0 and fpp(.99)>0,'curvature switch')

rng=random.Random(1927)
for i in range(2500):
    # Log uniform attenuation spanning initial boundary and very opaque water.
    k=math.exp(rng.uniform(math.log(.002),math.log(1000)))
    z=optimal_z(k)
    check(z>=0,'nonnegative optimum')
    if k<=1/21:
        check(z==0,'boundary optimum')
        continue
    check(z <= math.log(21*k)/(1+k)+1e-10,'analytic upper bound')
    y=k*z
    check(abs(math.exp(z)-k*(math.exp(-y)+20*math.exp(-20*y))) < 1e-8, 'first-order equation')
    check(math.exp(z)+k*k*math.exp(-y)+400*k*k*math.exp(-20*y)>0,'strict convexity')
    # Implicit-function derivative sign outside close critical neighborhoods.
    derivk=math.exp(-y)*(y-1)+20*math.exp(-20*y)*(20*y-1)
    check(abs(derivk - math.exp(-20*y)*f(y))<1e-8,'derivative factorization')
    if abs(derivk)>1e-5:
        step=min(k*1e-5,1e-5)
        if k-step>1/21:
            finite=(optimal_z(k+step)-optimal_z(k-step))/(2*step)
            predicted=-derivk/(math.exp(z)+k*k*math.exp(-y)+400*k*k*math.exp(-20*y))
            check(abs(finite-predicted)<max(1e-5, 2e-3*abs(predicted)), 'implicit derivative')

# The single-band closed form and unimodality check.
for _ in range(800):
    a=math.exp(rng.uniform(-2,2)); b=math.exp(rng.uniform(-2,2))
    low=1/(a*b)
    k=low*(1+rng.random()*90)
    z=math.log(a*b*k)/(1+b*k)
    check(z>0,'single-band interior optimizer')
    check(abs(math.exp(z)-a*b*k*math.exp(-b*k*z))<1e-10,'single-band stationarity')
    t=b*k
    v=1+1/t-math.log(a*t)
    check(math.isfinite(v),'single-band sign function')

print('PASS: %s supplementary assertions' % checks)
for y in roots:
    k=k_from_y(y)
    print('critical y=%.15f, k=%.15f, z=%.15f' % (y,k,optimal_z(k)))

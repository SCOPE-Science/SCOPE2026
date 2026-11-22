#!/usr/bin/env python3
"""Standalone numerical diagnostics for exponential surge plus random-phase sinusoidal tide.

The proof is analytic; finite checks here are not certification of universal claims.
Python 3 standard library only: python check_tidal_exceedance.py
"""
import math
import random

PI = math.pi

def simpson(f, left, right, n=320):
    assert n % 2 == 0
    if right == left:
        return 0.0
    step = (right - left) / n
    total = f(left) + f(right)
    for i in range(1, n):
        total += (4 if i % 2 else 2) * f(left + i * step)
    return (step / 3) * total

def bessel_i0(a):
    q = a * a / 4
    term = 1.0
    answer = 1.0
    for k in range(1, 200):
        term *= q / (k * k)
        answer += term
        if term < 1e-16 * answer:
            break
    return answer

def norm_survival(a, x):
    """e**x P(S+a cos(theta)>x), S~Exp(mean=1), x>=0."""
    assert a >= 0 and x >= 0
    if x >= a or a == 0:
        return bessel_i0(a)
    upper = math.acos(x / a)
    lost = simpson(lambda theta: math.exp(x) * math.expm1(a * math.cos(theta) - x),
                   0.0, upper) / PI
    return bessel_i0(a) - lost

def direct_survival(a, x):
    assert a >= 0 and x >= 0
    if a == 0 or x >= a:
        return math.exp(-x) * bessel_i0(a)
    split = math.acos(x / a)
    return (split + simpson(lambda theta: math.exp(-x+a*math.cos(theta)),
                           split, PI)) / PI

def crossing(a, rho):
    assert a > 0 and 0 <= rho < 1
    left, right = 0.0, a
    for _ in range(65):
        x = (left + right) / 2
        if norm_survival(a, x) - norm_survival(rho*a, x) > 0:
            right = x
        else:
            left = x
    return (left+right)/2

def crossing_derivative(a, rho, x):
    if x <= 0 or x >= a:
        return 0.0
    lo = x/a
    hi = 1.0 if rho == 0 else min(1.0, x/(rho*a))
    probability = (2/PI) * (math.asin(hi)-math.asin(lo))
    return 0.5 * math.exp(x) * probability

checks = 0

def check(cond, reason):
    global checks
    if not cond:
        raise AssertionError(reason)
    checks += 1

rng = random.Random(24051)
# Endpoints and strict one-crossing comparisons; numerical evidence only.
for a in [0.08,0.22,0.5,1.0,2.5]:
    for rho in [0.0,0.2,0.5,0.9]:
        f = lambda x: norm_survival(a, x)-norm_survival(rho*a, x)
        r = crossing(a, rho)
        check(0<r<a, ('root range',a,rho,r))
        check(f(0)<0, ('negative below',a,rho))
        check(f(a)>0, ('positive above',a,rho))
        check(abs(f(r))<2e-11, ('root residual',a,rho,r,f(r)))
        check(abs(f(a+1)-f(a))<1e-10, ('tail constant',a,rho))
        for j in range(1,41):
            x=a*j/41
            check(f(x+0.0001*a)>f(x), ('strict monotonicity',a,rho,x))
        for z in [0.05*r,0.6*r,0.99*r]:
            check(f(z)<0, ('lower ordering',a,rho,z))
        for z in [r+0.01*(a-r),r+0.5*(a-r),a+0.8]:
            check(f(z)>0, ('upper ordering',a,rho,z))
        for x in [0.13*a,0.57*a,0.93*a]:
            derivative=(f(x+1e-5*a)-f(x-1e-5*a))/(2e-5*a)
            exact=crossing_derivative(a,rho,x)
            check(abs(derivative-exact)<4e-5, ('derivative identity',a,rho,x,derivative,exact))
# Two independently organized integrations of the same convolution.
for _ in range(120):
    a=rng.uniform(0.01,3.5)
    x=rng.uniform(0,4.5)
    v1=math.exp(-x)*norm_survival(a,x)
    v2=direct_survival(a,x)
    check(abs(v1-v2)<2e-10, ('direct convolution',a,x,v1,v2))
# Near-crest fractional-power boundary-layer coefficient.
for rho in [0.0,0.25,0.5,0.8]:
    c=(3*PI*(1-rho*rho)/(8*math.sqrt(2)))**(2/3)
    for a in [0.02,0.01,0.005]:
        r=crossing(a,rho)
        ratio=(a-r)/(c*a**(5/3))
        check(abs(ratio-1)<0.03, ('weak-tide coefficient',a,rho,ratio))
# Reproduce physical benchmark to a conservative numerical tolerance.
r=crossing(1.0,0.5)
check(abs(r-0.533675162945678)<3e-8, ('benchmark root',r))
for x, expected_big, expected_small in [(0.1,0.749923482659,0.829999832891),
                                         (0.75,0.555973614095,0.502353973734)]:
    check(abs(direct_survival(1,x)-expected_big)<3e-8, ('big amplitude',x))
    check(abs(direct_survival(0.5,x)-expected_small)<3e-8, ('small amplitude',x))
# The exact two-point high/low tide model gives a different crossing,
# demonstrating why that approximation does not yield the sinusoidal value.
a1,a2=0.5,1.0
r_binary=math.log(2*math.cosh(a1)-math.exp(-a2))
check(a1<r_binary<a2, ('binary tide ordering',r_binary))
check(abs(r_binary-r)>0.05, ('distinct tide phase laws',r_binary,r))
print('PASS:', checks, 'supplementary numerical assertions')
print('Sinusoidal amplitude benchmark threshold:', format(r,'.12f'))
print('Two-point tide benchmark threshold:',format(r_binary,'.12f'))

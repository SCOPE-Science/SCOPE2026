#!/usr/bin/env python3
"""Numerical checks for two-Hermite ambiguity-multiplier design.

Requires: Python 3, numpy, scipy, mpmath. No internet or input files required.
"""
import math
import numpy as np
from scipy.optimize import brentq, minimize_scalar
import mpmath as mp

COUNT = 0

def ck(condition, message):
    global COUNT
    assert bool(condition), message
    COUNT += 1

def q(s, a):
    # a is the exposure allocated to first-Hermite window.
    return math.exp(-s) * (1 + a * (s * s - 2 * s))

def radius_min(T, a):
    v = [q(0, a), q(T, a)]
    if a > 0.5:
        root = 2.0 - math.sqrt(2.0 - 1.0 / a)
        if 0.0 < root < T:
            v.append(q(root, a))
    return min(v)

def optimal(T):
    if T < 2.0:
        return 0.0, math.exp(-T), None
    if T == 2.0:
        return 0.0, math.exp(-2.0), None  # canonical among all a <= 1/2
    def eq(x):
        return 2 * (x - 1.0) * math.exp(T - x) - ((T - 1.0)**2 + 1.0 - (x - 2.0)**2)
    x = brentq(eq, 1.0, 2.0, xtol=1e-14)
    a = 1.0 / (2.0 - (x - 2.0)**2)
    return a, q(x, a), x

# Numerically integrate the actual Hermite ambiguity functions, not just polynomial values.
mp.mp.dps = 45
h0 = lambda t: mp.power(2, mp.mpf('0.25')) * mp.exp(-mp.pi * t*t)
h1 = lambda t: 2 * mp.sqrt(mp.pi) * t * h0(t)
for x, y in [(mp.mpf('0'), mp.mpf('0')),
             (mp.mpf('.25'), mp.mpf('.35')),
             (mp.mpf('.8'), mp.mpf('.13')),
             (mp.mpf('1.1'), mp.mpf('.45'))]:
    s = mp.pi*(x*x + y*y)
    for h,n in [(h0,0),(h1,1)]:
        I = mp.quad(lambda t: h(t+x/2)*h(t-x/2)*mp.exp(-2j*mp.pi*y*t), [-mp.inf,mp.inf])
        exact = mp.exp(-s/2) * (1-s if n else 1)
        ck(abs(I-exact)<mp.mpf('1e-32'), 'ambiguity integral identity')

# Check all radius and exposure regimes against dense direct sampling and
# independent scalar maximization of the exact minimized expression.
Ts = [0.01, 0.3, 0.8, 1.25, 1.95, 1.999, 2., 2.0001, 2.01, 2.1,
      2.5, 3., 4., 5., 8., 12., 18.]
for T in Ts:
    a,c,x = optimal(T)
    ck(abs(radius_min(T,a)-c)<1e-12,'computed optimal min')
    for v in np.linspace(0,1,1001):
        ck(radius_min(T,float(v)) <= c + 2e-11,'global weight max')
    ck(abs(min(q(float(s),a) for s in np.linspace(0,T,10001))-c)<3e-7,
       'dense-radius global min')
    if T<2:
        ck(a==0 and abs(c-math.exp(-T))<1e-13,'narrow disk regime')
    elif T==2:
        for v in np.linspace(0,0.5,51):
            ck(abs(radius_min(T,float(v))-math.exp(-2))<1e-12,
               'degenerate optimizer interval')
        ck(radius_min(T,0.5001)<math.exp(-2),'beyond degenerate interval')
    else:
        ck(0.5<a<1 and 1<x<2,'interior optimal exposure')
        ck(abs(q(x,a)-q(T,a))<2e-12,'equioscillation')
        ck(c>math.exp(-T),'strict Gaussian improvement')
        z=minimize_scalar(lambda v:-radius_min(T,float(v)),bounds=(0,1),method='bounded',
                          options={'xatol':1e-12})
        ck(abs(-z.fun-c)<4e-9,'independent scalar optimizer')
        ck(abs(z.x-a)<3e-5,'optimal weight uniqueness numerical check')

# Check the long-radius asymptotics for a sequence with small stable values.
for T in [14., 16., 20., 24.]:
    a,c,x=optimal(T)
    w=1-a
    predicted=math.exp(1-T)*(T-1)**2
    ck(abs(w/predicted-1)<0.006, 'weight asymptotic')
    ck(abs(c / (math.exp(-T)*(T-1)**2)-1)<0.006, 'margin asymptotic')

print(f'TWO_HERMITE_AMBIGUITY_CHECKS_PASS {COUNT}')

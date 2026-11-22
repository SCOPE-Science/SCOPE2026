#!/usr/bin/env python3
"""Numerical corroboration of the analytic gamma-maxima hazard classification.

Dependencies: mpmath. Numerical observations are not global proof.
"""
import mpmath as mp
mp.mp.dps = 55

def q(a, t):
    return mp.gammainc(a, t, mp.inf) / mp.gamma(a)

def f(a, t):
    return t**(a-1)*mp.exp(-t)/mp.gamma(a)

def mprime(a, t):
    m = q(a, t)/f(a, t)
    return -1 + m*(1-(a-1)/t)

def v(u):
    return u/(-mp.expm1(-u))

def hazard(a, lam, t):
    return lam*f(a,t)/mp.expm1(lam*q(a,t))

def derivative_sign_expression(a, lam, t):
    return f(a,t)/q(a,t)*(v(lam*q(a,t))-1-mprime(a,t))

def threshold_at(a, t):
    B=mprime(a,t)
    assert B>0
    fun=lambda u:v(u)-1-B
    high=mp.mpf('2')
    while fun(high)<0:
        high*=2
    # Monotone bisection for the unique positive inverse.
    low=mp.mpf('0')
    for _ in range(180):
        mid=(low+high)/2
        if fun(mid)<0: low=mid
        else: high=mid
    return ((low+high)/2)/q(a,t)

for a in [mp.mpf('0.4'),mp.mpf('0.5'),mp.mpf('1'),mp.mpf('1.5')]:
    for lam in [mp.mpf('0.25'),mp.mpf('2')]:
        for t in [mp.mpf('0.05'),mp.mpf('0.3'),mp.mpf('0.9'),mp.mpf('2.0'),mp.mpf('5')]:
            analytic=derivative_sign_expression(a,lam,t)
            numerical=mp.diff(lambda s: mp.log(hazard(a,lam,s)),t)
            assert abs(analytic-numerical)<mp.mpf('1e-39')

assert all(derivative_sign_expression(mp.mpf('1.5'),mp.mpf('2'),mp.mpf(v))>0 for v in ['0.05','0.9','5'])
assert all(derivative_sign_expression(mp.mpf('0.5'),mp.mpf('0.25'),mp.mpf(v))<0 for v in ['0.05','0.9','5'])
assert derivative_sign_expression(mp.mpf('0.5'),mp.mpf('2'),mp.mpf('0.01'))<0
assert derivative_sign_expression(mp.mpf('0.5'),mp.mpf('2'),mp.mpf('0.86992'))>0
assert derivative_sign_expression(mp.mpf('0.5'),mp.mpf('2'),mp.mpf('12'))<0

# A numerical grid at alpha=1/2, and a local refinement (no global certificate).
a=mp.mpf('0.5')
xs=[mp.mpf('0.2')+k*mp.mpf('0.005') for k in range(600)]
yvals=[threshold_at(a,x) for x in xs]
i=min(range(len(xs)),key=lambda j:yvals[j])
assert abs(yvals[i]-mp.mpf('1.6554326886'))<mp.mpf('0.0002')
print('PASS: derivative identities, signs and illustrative threshold grid')

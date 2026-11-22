#!/usr/bin/env python3
"""Numerical and symbolic diagnostics for the discrete Rayleigh--Weibull hazard theorem.

This is a reproducibility aid, not a proof of infinite-index assertions.
Requires mpmath and sympy. Run: python check_hazard.py
"""
from mpmath import mp
import sympy as sp

mp.dps = 65
x, t, beta = sp.symbols('x t beta', positive=True)
z = t*x**beta
phi = (sp.exp(z)-1)**2
q = sp.diff(phi, x, 2)
P = 2*t*beta*x**(beta-2)*sp.exp(z)*(sp.exp(z)-1)
g = beta*z*(2*sp.exp(z)-1)/(sp.exp(z)-1) + beta-1
assert sp.simplify(q-P*g) == 0


def F(n, tt, bb):
    def ph(v):
        if not v:
            return mp.mpf('0')
        return mp.expm1(tt*mp.power(v, bb))**2
    return ph(n+2)-2*ph(n+1)+ph(n)


def root(n, bb):
    lo = mp.mpf('1e-15')
    hi = mp.mpf('1')
    assert F(n, lo, bb) < 0
    while F(n, hi, bb) < 0:
        hi *= 2
    for _ in range(180):
        mid = (lo+hi)/2
        if F(n, mid, bb) > 0:
            hi = mid
        else:
            lo = mid
    return (lo+hi)/2


for bb in (mp.mpf('0.2'),mp.mpf('0.25'),mp.mpf('0.4')):
    roots = [root(n,bb) for n in range(25)]
    assert all(roots[k] > roots[k+1] > 0 for k in range(len(roots)-1))
    for n in (0,1,2,5,10,20):
        z0 = roots[n]
        assert F(n,z0*mp.mpf('0.95'),bb) < 0
        assert F(n,z0*mp.mpf('1.05'),bb) > 0
        assert F(n+1,z0,bb) > 0

bb=mp.mpf('0.25')
rr=[root(k,bb) for k in range(3)]
assert rr[0] > 1 and rr[1] > 1 and rr[2] < 1
assert F(0,1,bb)<0 and F(1,1,bb)<0 and F(2,1,bb)>0

for bb in (mp.mpf('0.5'),mp.mpf('0.7'),mp.mpf('2')):
    for tt in (mp.mpf('0.05'),mp.mpf('0.2'),mp.mpf('1.0'),mp.mpf('2.5')):
        for n in range(30):
            assert F(n,tt,bb) > 0

bb=mp.mpf('0.25')
def mfun(c):
    E=mp.exp(c)
    return c*(2*E-1)/(E-1)-(1-bb)/bb
c=mp.findroot(mfun,(mp.mpf('1'),mp.mpf('2')))
assert abs(mfun(c)) < mp.mpf('1e-55')
for n in (100,300,1000):
    approximate = root(n,bb)*(n+1)**bb
    assert abs(approximate-c)/c < mp.mpf('0.001')

print('symbolic second-derivative factorization: PASS')
print('positive and negative threshold checks: PASS')
print('strictly decreasing threshold samples: PASS')
print('increasing-hazard diagnostics for shapes >= 1/2: PASS')
print('beta=1/4 threshold t0,t1,t2:',*(mp.nstr(r,19) for r in rr))
print('beta=1/4 continuous curvature root:',mp.nstr(c,21))
print('test example beta=1/4 t=1: decreasing twice, then increasing: PASS')

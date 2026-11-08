#!/usr/bin/env python3
"""Independent finite diagnostics for exponential-target Brownian reset search.

Requires Python 3 and mpmath.  Mathematical asymptotic proofs are in RESULT.md;
finite checks are not substitutes for the infinite limits.
"""
import math
import mpmath as mp

mp.mp.dps = 55
checks = 0

def near(x, y, tol=mp.mpf('1e-30')):
    global checks
    checks += 1
    if abs(x-y) > tol * max(1, abs(x), abs(y)):
        raise AssertionError((x,y,abs(x-y)))

def laplace(p, r, D, s):
    z = -mp.log(p)
    q = mp.exp(-z*mp.sqrt((r+s)/r))
    return (r+s)*q/(s+r*q)

for a in (mp.mpf('0.75'), mp.mpf('1.5'), mp.mpf('2'), mp.mpf('3.2')):
    for n in (0, 1, 2, 3, 5, 10, 20):
        pmf = a*mp.beta(a+1,n+1)
        integral = mp.quad(lambda p: a*p**a*(1-p)**n, [0, 1])
        near(pmf, integral)
        surv = a*mp.beta(a,n+1)
        near(surv, a*mp.beta(a+1,n+1) + a*mp.beta(a,n+2))
    for u in (mp.mpf('0.01'), mp.mpf('0.4'), mp.mpf('2.0')):
        gamma = mp.sqrt(1+u)
        integrated = mp.quad(lambda p: a*p**(a-1)*(1+u)*p**gamma/(u+p**gamma), [0,1])
        changed = a*gamma*mp.quad(lambda w: w**(a/gamma)/(u+w), [0,1])
        near(integrated, changed)

for r,D in [(mp.mpf('1'),mp.mpf('1')),(mp.mpf('2.3'),mp.mpf('0.7'))]:
    for z in (mp.mpf('.1'),mp.mpf('1'),mp.mpf('2.5'),mp.mpf('8')):
        p=mp.exp(-z)
        f=lambda s: laplace(p,r,D,s)
        near(-mp.diff(f,0), (1/p-1)/r)
        near(mp.diff(f,0,2), (2/p**2-(z+2)/p)/r**2)
        for th in (mp.mpf('0.1'),mp.mpf('0.5')):
            # Positive exponential moment via negative Laplace argument
            moment=laplace(p,r,D,-th*r*p)
            checks+=1
            assert 1 <= moment <= 1/(1-th)+mp.mpf('1e-25')

# Concentration of scaled completion time as the target distance diverges.
for z in (mp.mpf('12'),mp.mpf('18'),mp.mpf('24')):
    p=mp.exp(-z)
    for s in (mp.mpf('.5'),mp.mpf('1.0'),mp.mpf('2.0')):
        approx=laplace(p,mp.mpf('1'),mp.mpf('1'),s*p)
        checks+=1
        assert abs(approx-1/(1+s)) < 0.002

# Critical conjugate case: explicit beta-geometric tail and pmf.
a=mp.mpf('2')
for n in (0,1,2,5,10,100,1000):
    near(a*mp.beta(a,n+1),mp.mpf(2)/((n+1)*(n+2)))
    near(a*mp.beta(a+1,n+1),mp.mpf(4)/((n+1)*(n+2)*(n+3)))

# Upper bound for conditional survival from the stopped-cycle moment formula:
# For theta=1/2, E exp(theta*r*p*T) <=2 for every p in (0,1].
for zint in range(1,31):
    p=mp.exp(-mp.mpf(zint)/2)
    checks+=1
    assert laplace(p,mp.mpf(1),mp.mpf(1),-p/2) <= 2

print('PASS:', checks, 'finite numerical/symbolic diagnostic assertions')

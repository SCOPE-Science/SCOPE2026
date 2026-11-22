#!/usr/bin/env python3
"""Deterministic numerical checks for the serotinous seed-release rate theorem.

Analytic identities and global uniqueness are proved in RESULT.md. Numerical
sampling here is only a consistency test, not an infinite-domain certificate.
"""
from __future__ import annotations
import math
import random

COUNTER = 0

def check(condition, message=''):
    global COUNTER
    COUNTER += 1
    if not condition:
        raise AssertionError(f'check {COUNTER}: {message}')

def L(k, t):
    x = k*t
    if x > 700.0:
        return 0.0
    if k == 0.0:
        return 1.0/t
    return k/math.expm1(x)

def optimum(mu, decay, maturity):
    assert mu > 0 and decay > 0 and maturity > 0
    critical = (mu+decay)*maturity/decay
    upper = critical + math.log1p(decay/mu)/decay
    def g(t):
        return (mu+decay) - mu*math.exp(decay*t-(mu+decay)*maturity) - decay*math.exp(-mu*t)
    check(g(critical)>-1e-13, 'lower bracket')
    check(g(upper)<1e-13, 'upper bracket')
    lo, hi = critical, upper
    for _ in range(75):
        mid = 0.5*(lo+hi)
        if g(mid)>0: lo=mid
        else: hi=mid
    return 0.5*(lo+hi)

def yield_rate(t, mu, decay, maturity, seed_rate=1.0):
    if t<=maturity:
        return 0.0
    if decay==0:
        if mu==0:
            return seed_rate*(t-maturity)/t
        return seed_rate*math.exp(-mu*maturity)*(-math.expm1(-mu*(t-maturity)))/(-math.expm1(-mu*t))
    if mu==0:
        return seed_rate*(-math.expm1(-decay*(t-maturity)))/(decay*t)
    return (seed_rate*mu*math.exp(-mu*maturity)/(mu+decay)
            *(-math.expm1(-(mu+decay)*(t-maturity)))
            /(-math.expm1(-mu*t)))

def direct_integral(t, mu, decay, maturity):
    # Integrate E B'(F truncated at t) = int_m^t exp(-mu u) exp(-decay(u-m)) du.
    n=500
    h=(t-maturity)/n
    s=0.0
    for i in range(n+1):
        u=maturity+i*h
        weight=1 if i in (0,n) else (4 if i%2 else 2)
        s+=weight*math.exp(-mu*u-decay*(u-maturity))
    reward=h*s/3
    duration=(-math.expm1(-mu*t))/mu
    return reward/duration

rng=random.Random(20261121)
for i in range(2500):
    mu=10**rng.uniform(-1.0,.2)
    decay=10**rng.uniform(-.5,.5)
    maturity=10**rng.uniform(-.5,.4)
    if (mu+decay)*mu*maturity/decay>14:
        continue
    t=optimum(mu,decay,maturity)
    lower=(mu+decay)*maturity/decay
    upper=lower+math.log1p(decay/mu)/decay
    check(lower<t<upper, 'strict optimizer bound')
    q=yield_rate(t,mu,decay,maturity)
    check(q+1e-12*max(1,q)>yield_rate(lower,mu,decay,maturity),'beats lower bound')
    check(q+1e-12*max(1,q)>yield_rate(upper,mu,decay,maturity),'beats upper bound')
    check(q+1e-12*max(1,q)>mu*math.exp(-mu*maturity)/(mu+decay),'beats no forced deadline')
    for f in [.0001,.001,.01,.05,.3,.6,1.4,2.5,6,20]:
        candidate=maturity+(t-maturity)*f
        if abs(candidate-t) <= 1e-12*max(1,t):
            continue
        check(q>=yield_rate(candidate,mu,decay,maturity)-1e-12,'global samples')
    for factor in [1.05,1.3]:
        check(optimum(mu*factor,decay,maturity)>=t-1e-10,'risk comparative static')
        check(optimum(mu,decay*factor,maturity)<=t+1e-10,'decay comparative static')
        check(optimum(mu,decay,maturity*factor)>=t-1e-10,'maturity comparative static')
    if i%20==0:
        check(abs(direct_integral(t,mu,decay,maturity)/q-1)<2e-8,'integral identity')

for i in range(1000):
    mu=10**rng.uniform(-1,.6)
    maturity=10**rng.uniform(-.6,.6)
    t1=maturity+0.2
    t2=maturity+0.5
    t3=maturity+3.0
    check(yield_rate(t1,mu,0,maturity)<yield_rate(t2,mu,0,maturity),'no-decay monotonicity 1')
    check(yield_rate(t2,mu,0,maturity)<yield_rate(t3,mu,0,maturity),'no-decay monotonicity 2')

for i in range(1000):
    mu=10**rng.uniform(-1,.6)
    decay=10**rng.uniform(-1,.6)
    t1=.2; t2=.5; t3=3.0
    check(yield_rate(t1,mu,decay,0)>yield_rate(t2,mu,decay,0),'no-maturity monotonicity 1')
    check(yield_rate(t2,mu,decay,0)>yield_rate(t3,mu,decay,0),'no-maturity monotonicity 2')

for i in range(1000):
    mu=10**rng.uniform(-1,.6)
    check(yield_rate(.5,mu,0,0)==1.0,'double-degenerate identity')
    check(yield_rate(3,mu,0,0)==1.0,'double-degenerate identity 2')

print('PASS:', COUNTER, 'deterministic checks')
print('Example mu=1/4, decay=1, maturity=1:')
t=optimum(.25,1,1)
print('  optimal deadline',format(t,'.12f'))
print('  reward/time',format(yield_rate(t,.25,1,1),'.12f'))
print('  unlimited-deadline reward/time',format(.25*math.exp(-.25)/1.25,'.12f'))

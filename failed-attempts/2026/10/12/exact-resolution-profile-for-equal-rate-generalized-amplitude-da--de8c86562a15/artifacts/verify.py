#!/usr/bin/env python3
import math


def probs(mu, s):
    a = math.exp(-mu*s)
    return ((1+a)**2/4, (1-a*a)/4, (1-a*a)/4, (1-a)**2/4)


def rate(mu, s):
    return -2.0*math.log2((1.0+math.exp(-mu*s))/2.0)/s

for mu in (0.2, 1.0, 3.7):
    for s in (0.01, 0.2, 1.3):
        pI,pX,pY,pZ=probs(mu,s)
        assert abs((pI+pX+pY+pZ)-1.0) < 1e-13
        a=math.exp(-mu*s)
        lamx=pI+pX-pY-pZ
        lamy=pI-pX+pY-pZ
        lamz=pI-pX-pY+pZ
        assert abs(lamx-a) < 1e-13
        assert abs(lamy-a) < 1e-13
        assert abs(lamz-a*a) < 1e-13

mu=1.7
ss=[0.02,0.05,0.1,0.3,0.8,1.5]
rr=[rate(mu,s) for s in ss]
assert all(rr[i] > rr[i+1] for i in range(len(rr)-1))
limit=mu/math.log(2.0)
assert abs(rate(mu,1e-6)-limit) < 1e-5

# Taylor check: Gamma = mu/ln2 - mu^2*s/(4 ln2) + O(s^3).
for s in (1e-3, 5e-4, 2.5e-4):
    approx=mu/math.log(2.0) - mu*mu*s/(4.0*math.log(2.0))
    assert abs(rate(mu,s)-approx) < 2.0*s**3

print('VERIFY_OK')

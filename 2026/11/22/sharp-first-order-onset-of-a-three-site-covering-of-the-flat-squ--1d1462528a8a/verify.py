#!/usr/bin/env python3
"""Reproduce the explicit logarithmic constant and numerical checks."""
from math import log, isclose
from scipy.optimize import differential_evolution
import numpy as np

def H(a):
    if a == 0 or a == .5: return 0.
    return .5*log(.5)-a*log(a)-(.5-a)*log(.5-a)

k=log(12)/4-5*log(5)/24
assert isclose(k,(H(1/12)+H(1/4))/2,rel_tol=1e-13)
assert .28592<k<.28594

def F(x):
    return (H(1/3-x)+max(H(x),H(1/6-x)))/2
for x in np.linspace(0,1/6,1001):
    assert F(float(x))>k-1.e-11
assert isclose(F(1/12),k,abs_tol=1e-13)

cent=np.arange(3)/3
for e in (.01,.003,.001):
    p=1+e
    def obj(z):
        d=np.abs(z[:,None]-cent[None,:]);d=np.minimum(d,1-d)
        return -np.min(np.sum(d**p,axis=0)**(1/p))
    r=differential_evolution(obj,[(0,1),(0,1)],seed=11,popsize=12,maxiter=180,tol=1e-10).fun
    rate=(.5+r)/e
    assert 0<rate<k
    assert abs(rate-k)<.006
    print(f"p={p:.3f}, radius={-r:.12f}, normalized loss={rate:.10f}")
print('exact coefficient:',k)
print('PASS')

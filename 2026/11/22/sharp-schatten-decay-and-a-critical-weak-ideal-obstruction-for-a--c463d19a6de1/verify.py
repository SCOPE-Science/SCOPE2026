#!/usr/bin/env python3
"""Finite reproducibility diagnostics for Aluthge iterates of power-weighted shifts.
Requires numpy and scipy. Finite checks do not prove asymptotics."""
import math
import numpy as np
from scipy.stats import binom
from scipy.special import zeta

checks = 0
for n in (3, 7, 17):
    t = .37
    probs = binom.pmf(np.arange(n+1), n, t)
    assert abs(np.sum(probs)-1) < 1e-12
    for alpha in (0.7, 1.4):
        j = np.arange(1, 41)
        a = np.exp(-alpha * (np.log(j[:,None]+np.arange(n+1)) @ probs))
        assert np.all(np.diff(a)<0)
        assert np.all(a <= j**(-alpha)*(1+1e-12))
        checks += 3
for alpha,p,t in ((1.5,2,.3),(.8,2,.7),(1,2,.5),(1.5,2,.9)):
    s = alpha*p
    target = -(1+s*t)/(2*(1+s))
    for n in (100, 250):
        m=n*t
        k = np.arange(n+1)
        probs = binom.pmf(k,n,t)
        J = np.arange(1, 2401)
        exact = np.exp(-s * (np.log(J[:,None]+k) @ probs))
        tail = zeta(s, 2401 + m)
        # The tail geometric means differ from (j+m)^-s by O(n/(j+m)^2)
        # and the resulting tail error is negligible at this precision.
        estimate = np.sum(exact) + tail
        observed = m**s*(estimate - m**(1-s)/(s-1))
        assert abs(observed-target) < .017, (n,s,t,observed,target)
        checks += 1
        op_exact = np.exp(-alpha * (np.log(1+k) @ probs))
        op_approx = m**(-alpha)*(1-alpha*(1+t)/(2*m))
        assert abs(op_exact/op_approx-1)< .002
        checks += 1
for n in (2,7,25):
    t=.4; alpha=1.25
    k=np.arange(n+1); probs=binom.pmf(k,n,t)
    j=np.array([1000.,10000.,100000.])
    a=np.exp(-alpha*(np.log(j[:,None]+k)@probs))
    critical=j**alpha*a
    assert np.all(critical<=1+1e-10)
    assert abs(critical[-1]-1)<1e-3
    checks+=2
print('VERIFY_OK',checks,'finite assertions')

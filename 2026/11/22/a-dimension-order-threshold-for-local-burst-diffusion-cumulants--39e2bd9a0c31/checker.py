#!/usr/bin/env python3
"""Standalone numerical cross-checks of source-centered local detection asymptotics."""
from math import pi, gamma, log
from scipy.integrate import quad
from scipy.special import gammainc
import numpy as np

# Units D=mu=b=1; factorial cumulants divided by E[(B)_k].
def q(d, u):
    return gammainc(d / 2., 1. / (4. * u))

def exact(d, k, eps):
    return eps ** 2 * quad(lambda u: np.exp(-k*eps**2*u) * q(d,u)**k,
                            0, np.inf, epsabs=2e-12, epsrel=1e-10, limit=350)[0]

def cdk(d, k):
    v = pi**(d/2)/gamma(d/2+1)
    return (v / (4*pi)**(d/2))**k

def leading(d, k, eps):
    if d*k < 2:
        return cdk(d,k) * gamma(1-d*k/2) * k**(d*k/2-1) * eps**(d*k)
    if d*k == 2:
        return cdk(d,k) * eps**2 * log(1/eps**2)
    C = quad(lambda u:q(d,u)**k, 0, np.inf,
             epsabs=2e-12, epsrel=1e-10, limit=350)[0]
    return eps**2 * C

cases = [(1,1),(1,2),(1,3),(2,1),(2,2),(3,1),(3,2)]
for d,k in cases:
    prev=100
    for eps in (0.2,0.08,0.02):
        ratio=exact(d,k,eps)/leading(d,k,eps)
        print(f'd={d}, k={k}, eps={eps}: ratio to leading asymptotic={ratio:.10f}')
        assert 0.65 < ratio <= 1.55, (d,k,eps,ratio)
        # The discrepancy shrinks as eps decreases, except extremely small nonmonotone errors.
        assert abs(ratio-1) < prev
        prev=abs(ratio-1)
for e in (0.1,0.3,0.8):
    assert abs(exact(1,1,e) - (1 - np.exp(-e))) < 1e-10
C22=quad(lambda u: q(2,u)**2,0,np.inf,epsabs=1e-11)[0]
C31=quad(lambda u: q(3,u),0,np.inf,epsabs=1e-11)[0]
assert abs(C22 - log(2)/2) < 1e-9
assert abs(C31 - 0.5) < 1e-9
print('PASS: 21 finite-asymptotic tests, three 1d mean resolvent tests, and two special-constant tests')

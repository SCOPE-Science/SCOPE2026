"""Finite numerical diagnostics for the two-sine level-density theorem.
This code does not replace the analytic crossing-flux proof.
"""
from math import sqrt, pi, sin
import numpy as np
from scipy.integrate import quad

def density(c, alpha=1., beta=sqrt(2)):
    lo=max(-1.,c-1.)
    hi=min(1.,c+1.)
    if not lo<hi:return 0.
    def integrand(s):
        # Endpoint singularities are integrable.
        a=alpha/sqrt(max(1.e-300,1.-(c-s)**2))
        b=beta/sqrt(max(1.e-300,1.-s*s))
        return max(a,b)/(pi*pi)
    m=(lo+hi)/2
    return quad(integrand,lo,m,epsabs=1e-8,limit=250)[0]+quad(integrand,m,hi,epsabs=1e-8,limit=250)[0]

def finite_crossings(c, R=20000., dt=.025, alpha=1., beta=sqrt(2)):
    # Numerically count sign changes in [0,R]; exact roots at sampled
    # points are not accounted for. This is a diagnostic only.
    t=np.arange(0.,R+dt,dt)
    v=np.sin(alpha*t)+np.sin(beta*t)-c
    return int(np.count_nonzero(v[:-1]*v[1:]<0))

assert abs(density(0)-sqrt(2)/pi)<1.e-8
for c in (0.,0.3,1.,1.5,1.9):
    approx=density(c)
    measured=finite_crossings(c)
    assert abs(measured/20000.-approx)<0.012, (c,measured/20000.,approx)
for delta in (1.e-2,1.e-3):
    predicted=sqrt(2.*3.)*sqrt(delta)/(pi*pi)
    assert abs(density(2.-delta)/predicted-1)<0.015
print('Finite diagnostics passed; no infinite-limit certification is inferred.')

#!/usr/bin/env python3
"""Independent numerical check of the two end-corner contribution at three spacings.
Requires numpy and scipy. This is not a calculation of the full finite-threshold tail.
"""
import numpy as np
from scipy.special import roots_legendre, beta

def rps3(e, u, v):
    d1, d2, d3 = 1-e, e*u, e*v
    return (-np.log(d1)-np.log(d2)-np.log(d3)
            -np.log(d1+d2)-np.log(d2+d3)+2*np.log(1+d2))

z, w = roots_legendre(800)
z, w = (z+1)/2, w/2
a, b = z**3, (1-z)**3
u = a/(a+b)
v = b/(a+b)
dudz = 3*z**2*(1-z)**2/(a+b)**2
A = 2*beta(1/3,1/3)
delta = .01
for t in (20., 25., 30., 35.):
    lo = np.full_like(u, 1e-80)
    hi = np.full_like(u, delta)
    saturated = rps3(hi,u,v)>t
    for _ in range(58):
        mid=(lo+hi)/2
        high=rps3(mid,u,v)>t
        lo=np.where(high,mid,lo)
        hi=np.where(high,hi,mid)
    cutoff=np.where(saturated,delta,(lo+hi)/2)
    contribution=2*np.sum(w*dudz*cutoff**2)
    print(f'{t:.0f}: {contribution*np.exp(2*t/3):.9f}, limit {A:.9f}')

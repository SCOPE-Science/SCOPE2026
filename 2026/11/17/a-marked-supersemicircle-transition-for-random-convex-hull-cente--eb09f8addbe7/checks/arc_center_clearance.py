#!/usr/bin/env python3
"""Independent finite numerical checks for the arc-center-clearance identities.

Run: python checks/arc_center_clearance.py
"""
import math
import numpy as np
from scipy.integrate import quad

pi=math.pi

def exact(n,L):
    if L <= pi: return 0.
    a=pi/L
    b=1-a
    return 1-n*a**(n-1)+(n-1)*a**n-(n-1)*b**n

def extreme_integral(n,L):
    if L<=pi:return 0.
    d=L-pi
    # density integrated over the endpoint triangle u+v<d;
    # the integrand is constant in u along a line of fixed u+v.
    near=quad(lambda s: n*(n-1)/L**n * s*(L-s)**(n-2),0,d,epsabs=1e-12)[0]
    return near-(n-1)*(d/L)**n

for n,L in [(3,3.7),(5,4.9),(7,5.8),(12,6.1),(25,4.5)]:
    assert abs(exact(n,L)-extreme_integral(n,L))<5e-11,(n,L)
for n in range(3,50):
    assert abs(exact(n,2*pi)-(1-n/2**(n-1)))<1e-12
for c in (0.15,0.8,2.,5.):
    target=1-(1+c)*math.exp(-c)
    assert abs(exact(20000,pi*(1+c/20000))-target)<4e-4,(c,target)
rng=np.random.default_rng(41907)
for n,L in [(3,3.7),(5,4.9),(9,5.8),(50,pi*(1+2.5/50))]:
    N=180000
    pts=np.sort(rng.uniform(0,L,size=(N,n)),axis=1)
    internal=np.diff(pts,axis=1)
    event=(np.max(internal,axis=1)<pi)&(2*pi-pts[:,-1]+pts[:,0]<pi)
    theory=exact(n,L)
    se=math.sqrt(max(1e-6,theory*(1-theory))/N)
    assert abs(event.mean()-theory)<6.5*se+2/N,(n,L,event.mean(),theory,se)
print('ARC_CENTER_CLEARANCE_CHECKS_OK')

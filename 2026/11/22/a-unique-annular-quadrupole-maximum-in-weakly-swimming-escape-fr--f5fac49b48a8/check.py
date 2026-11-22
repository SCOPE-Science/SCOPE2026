#!/usr/bin/env python3
"""Check the weak-propulsion angular response of absorbing-disk active diffusion."""
import numpy as np
from scipy.special import iv
from scipy.optimize import brentq

def I2prime(z): return (iv(1,z)+iv(3,z))/2

def f(r,R,D,q):
 k=np.sqrt(q/D)
 return (R*iv(1,k*r)/iv(1,k*R)-r)/(2*D*q)

def h(r,R,D,q):
 k=np.sqrt(q/D)
 return R*k/(12*D*q*q*iv(1,k*R))*(iv(2,k*r)-iv(2,k*R)*iv(2,2*k*r)/iv(2,2*k*R))

def hp(r,R,D,q):
 k=np.sqrt(q/D)
 return R*k*k/(12*D*q*q*iv(1,k*R))*(I2prime(k*r)-2*iv(2,k*R)*I2prime(2*k*r)/iv(2,2*k*R))

def eq_ratio(r,R,D,q):
 k=np.sqrt(q/D)
 return I2prime(k*r)/(2*I2prime(2*k*r))-iv(2,k*R)/iv(2,2*k*R)

for q in [0.0001,0.001,0.02,0.3,1.,10.,100.]:
 R=D=1.
 rr=np.linspace(.01,.99,99)
 k=np.sqrt(q)
 assert all(h(x,R,D,q)>0 for x in rr)
 xstar=brentq(lambda x:eq_ratio(x,R,D,q),1.e-5,R-1.e-5)
 assert abs(hp(xstar,R,D,q)) < 1e-7
 assert all(hp(x,R,D,q)>0 for x in rr if x < xstar-0.02)
 assert all(hp(x,R,D,q)<0 for x in rr if x > xstar+0.02)
 print('q=',q,'peak=',xstar,'quadrupole_at_peak=',h(xstar,R,D,q))

# ODE residual at several interior radii by analytic modified-Bessel equations
for q in [0.02,0.5,3.0,20.0]:
 R,D=1.4,1.3; k=np.sqrt(q/D)
 for r in [0.11,0.37,0.72,1.15]:
  B=R*k/(12*D*q*q*iv(1,k*R)); c=iv(2,k*R)/iv(2,2*k*R)
  hval=h(r,R,D,q)
  # L_2 I_2(k r) = k^2 I_2(k r); L_2 I_2(2kr)=4k^2 I_2(2kr)
  residual=D*B*(k*k*iv(2,k*r)-4*k*k*c*iv(2,2*k*r))-4*q*hval + (R*k*iv(2,k*r)/(4*D*q*iv(1,k*R)))
  assert abs(residual)<2e-10, (q,r,residual)
print('Second angular harmonic ODE and boundary identities checked.')

# q -> 0: h(r)=r^2(R^2-r^2)/(192D^3)
for q in [1e-3,1e-2]:
 r=.45; hlim=r*r*(1-r*r)/192
 assert abs(h(r,1.,1.,q)/hlim-1)<0.01
print('Vanishing rotational diffusion limit checked.')

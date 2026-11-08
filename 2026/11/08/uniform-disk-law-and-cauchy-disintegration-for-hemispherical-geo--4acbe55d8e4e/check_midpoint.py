#!/usr/bin/env python3
"""Numerical cross-checks of exact hemisphere geodesic-midpoint and length laws.
Run: python check_midpoint.py (requires numpy). Simulation is corroboration, not a proof.
"""
import math
import numpy as np

N=660_000
rng=np.random.default_rng(915231)
z1=rng.random(N); z2=rng.random(N)
a1=rng.uniform(0,2*math.pi,N); a2=rng.uniform(0,2*math.pi,N)
s1=np.sqrt(1-z1*z1);s2=np.sqrt(1-z2*z2)
x=np.stack((s1*np.cos(a1),s1*np.sin(a1),z1),axis=1)
y=np.stack((s2*np.cos(a2),s2*np.sin(a2),z2),axis=1)
ms=x+y;m=ms/np.linalg.norm(ms,axis=1)[:,None]
z=m[:,2]; rr=np.sum(m[:,:2]**2,axis=1)
delta=np.arccos(np.clip(np.sum(x*y,axis=1),-1,1))
assert np.max(np.abs(rr-(1-z*z)))<1e-13
for value, target, tolerance in [(np.mean(z),2/3,0.003), (np.mean(z*z),0.5,0.003),
                                  (np.mean(delta),4/math.pi,0.004), (np.mean(delta**2),2,0.009)]:
    assert abs(value-target) < tolerance, (value,target)
for p in [0.1,0.25,0.5,0.75,0.9]:
    observed=np.mean(rr <= p)
    assert abs(observed-p) < 0.004, ('disk_r2_cdf',p,observed)
for a in [0.3,0.7,1.2,2.1,2.7]:
    target=1-math.cos(a)+(a*math.cos(a)-math.sin(a))/math.pi
    observed=np.mean(delta <= a)
    assert abs(observed-target) < 0.004, ('distance_CDF',a,observed,target)
# Tangent at midpoint, relative to the meridian pointing north.
ref=(np.array([0.,0.,1.])-z[:,None]*m)/np.sqrt(1-z*z)[:,None]
v=(x-y)/np.linalg.norm(x-y,axis=1)[:,None]
cc=np.sum(v*ref,axis=1)**2
for a,b in [(0.15,0.35),(0.35,0.55),(0.55,0.75),(0.75,0.95)]:
    sel=(z>=a)&(z<b)
    # E[cos²(phi)|z]=z/(1+z).
    diff=np.mean(cc[sel]-z[sel]/(1+z[sel]))
    assert abs(diff)<0.009,(a,b,diff)
assert abs(np.mean(cc)-(2*math.log(2)-1))<0.006
# Independent disintegration sample in disc/Cauchy/uniform arc-sine coordinates.
rng=np.random.default_rng(222990)
M=340_000
rho=np.sqrt(rng.random(M)); az=2*math.pi*rng.random(M)
u=np.stack((rho*np.cos(az),rho*np.sin(az)),axis=1)
height=np.sqrt(1-rho*rho)
mm=np.column_stack((u,height));s=np.sqrt(1-height**2)
phi=np.arctan(np.tan(math.pi*(rng.random(M)-0.5))/height) + math.pi*rng.integers(0,2,M)
eref=(np.array([0.,0.,1.])-height[:,None]*mm)/s[:,None]
perp=np.cross(mm,eref)
vv=np.cos(phi)[:,None]*eref+np.sin(phi)[:,None]*perp
q=height**2/(height**2+s*s*np.cos(phi)**2)
half=np.arcsin(np.sqrt(rng.random(M)*q))
xx=np.cos(half)[:,None]*mm+np.sin(half)[:,None]*vv
yy=np.cos(half)[:,None]*mm-np.sin(half)[:,None]*vv
assert min(np.min(xx[:,2]),np.min(yy[:,2]))>=-1e-12
assert abs(np.mean(xx[:,2])-0.5)<0.004
assert abs(np.mean(yy[:,2])-0.5)<0.004
assert abs(np.mean(xx[:,2]*yy[:,2])-0.25)<0.005
assert abs(np.mean(2*half)-4/math.pi)<0.006
# Dimension-specific pole-density criterion: equality holds only for ambient d=3
for d in range(2,26):
    surface=2*math.pi**(d/2)/math.gamma(d/2)
    ball=math.pi**((d-1)/2)/math.gamma((d+1)/2)
    equal=abs(4/surface-1/ball)<1e-12
    assert equal == (d==3)
print('HEMISPHERE_GEODESIC_MIDPOINT_UNIFORM_DISK_AND_CAUCHY_OK', N, M)

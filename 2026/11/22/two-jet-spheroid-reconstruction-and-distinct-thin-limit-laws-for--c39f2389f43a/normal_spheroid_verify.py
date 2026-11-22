"""Numerical consistency checks for spheroidal radial-normal deviation laws.
This file contains only scientific calculations and deterministic tests.
Run: python normal_spheroid_verify.py
"""
import math
import numpy as np
from scipy.integrate import quad


def normalizer(r):
    if r == 1:
        return 2.0
    if r < 1:
        k = math.sqrt(1-r*r)
        return 1.0 + r*r/k*math.asinh(k/r)
    k = math.sqrt(r*r-1)
    return 1.0 + r*r/k*math.asin(k/r)


def primitive(t, r):
    if not 0 <= t <= 1:
        raise ValueError(t)
    if t == 0:
        return 0.0
    z = math.sqrt(t)
    if r == 1:
        return 2*z
    if r < 1:
        k = math.sqrt(1-r*r)
        return z*math.sqrt(r*r+k*k*t) + (r*r/k)*math.asinh(k*z/r)
    k = math.sqrt(r*r-1)
    return z*math.sqrt(max(0,r*r-k*k*t)) + (r*r/k)*math.asin(k*z/r)


def cdf_scaled(u,r):
    if u <= 0:
        return 0.
    if u >= 0.5:
        return 1.
    d = math.sqrt(1-4*u*u)
    tm=(1-d)/2
    tp=(1+d)/2
    z=normalizer(r)
    return (primitive(tm,r)+z-primitive(tp,r))/z


def cdf_from_integral(u,r):
    if u<=0: return 0.
    if u>=0.5: return 1.
    d=math.sqrt(1-4*u*u)
    a=(1-d)/2; b=(1+d)/2
    z=normalizer(r)
    return (quad(lambda x: math.sqrt(r*r+(1-r*r)*x)/math.sqrt(x),0,a,epsabs=1e-12)[0]
           +quad(lambda x: math.sqrt(r*r+(1-r*r)*x)/math.sqrt(x),b,1,epsabs=1e-12)[0])/z

count=0
for r in [0.05,0.2,0.5,0.93,1.05,1.5,3.0,10.0,200.0]:
    z=normalizer(r)
    zq=2*quad(lambda x: math.sqrt(r*r+(1-r*r)*x*x),0,1,epsabs=1e-12)[0]
    assert abs(z/zq-1)<2e-9
    count+=1
    for u in [0.01,0.1,0.24,0.4,0.49]:
        a=cdf_scaled(u,r)
        b=cdf_from_integral(u,r)
        assert abs(a-b)<1e-10,(r,u,a,b)
        count+=1
    # Cartesian normal/radial dot for a meridian point
    for th in np.linspace(0.01,math.pi/2-.01,81):
        x=math.sin(th);zz=r*math.cos(th)
        normal=np.array([math.sin(th),0,math.cos(th)/r]);pt=np.array([x,0,zz])
        delta=math.acos(np.dot(normal,pt)/(np.linalg.norm(normal)*np.linalg.norm(pt)))
        predicted=math.atan(abs(r-1/r)*abs(math.sin(th)*math.cos(th)))
        assert abs(delta-predicted)<2e-8,(r,th,delta,predicted)
        count+=1
    # Exact asymptotic coefficients using small variable values, robust at r=200.
    for u in [1e-3, 2e-3, 4e-3]:
        predicted=2*r/z*u + 1/z*u*u
        actual=cdf_scaled(u,r)
        assert abs(actual-predicted)<4*u**3*(r+1/r)/z, (r,u,actual,predicted)
        count+=1

for r,lim in [(300.,'prolate'),(0.003,'oblate')]:
    q=(r-1/r)**2
    for y in [2.1,2.5,3.,5.,10.]:
        # Y=scale*(pi/2-delta); scale = r if prolate, 1/r if oblate
        scale=r if r>1 else 1/r
        delta=math.pi/2-y/scale
        assert delta>0
        u=math.tan(delta)/math.sqrt(q)
        prob=1-cdf_scaled(u,r)  # Pr(Y <= y) = Pr(delta >= pi/2-y/scale)
        expected=(1-2/math.pi*math.asin(2/y) if r>1 else math.sqrt(1-4/y**2))
        assert abs(prob-expected)<0.025, (r,y,prob,expected)
        count+=1

print(f'PASS {count} deterministic checks')

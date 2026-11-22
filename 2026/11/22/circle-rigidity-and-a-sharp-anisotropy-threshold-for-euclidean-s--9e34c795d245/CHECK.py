#!/usr/bin/env python3
"""Finite supporting computations for the analytic antipodal-quadruple theorem.
Requires numpy and scipy; this checker is not a proof of all parameter values.
"""
import math
import numpy as np
from scipy.integrate import quad

def qprob(k):
    def f(t):
        h=(k*k-1)*abs(math.sin(2*t))/2
        r=k*k*math.cos(t)**2+math.sin(t)**2
        q=k*k*math.sin(t)**2+math.cos(t)**2
        return min(1.,2*(math.atan2(2*h,r)+math.atan2(2*h,q))/math.pi)
    # Use fourfold symmetry; split the exact saturation boundary to avoid a kink.
    if k>math.sqrt(3):
        boundary=math.asin(2*k/(math.sqrt(3)*(k*k-1)))/2
        integral=quad(f,0,boundary,epsabs=1e-9,limit=200)[0]+math.pi/4-boundary
    else:
        integral=quad(f,0,math.pi/4,epsabs=1e-9,limit=200)[0]
    return 4*integral/math.pi

def critical_fraction(k):
    if k<=math.sqrt(3):return 0.
    return 1-2*math.asin(2*k/(math.sqrt(3)*(k*k-1)))/math.pi

def kruskal_shortcut(k,phi,psi):
    p=np.array([[k*math.cos(phi),math.sin(phi)],[-k*math.cos(phi),-math.sin(phi)],
                [k*math.cos(psi),math.sin(psi)],[-k*math.cos(psi),-math.sin(psi)]])
    edges=sorted((float(np.linalg.norm(p[i]-p[j])),i,j) for i in range(4) for j in range(i+1,4))
    par=list(range(4))
    def root(i):
        while par[i]!=i:i=par[i]
        return i
    used=[]
    for wt,i,j in edges:
        ii,jj=root(i),root(j)
        if ii!=jj:
            par[ii]=jj;used.append((i,j))
        if len(used)==3:break
    return any({i,j} in ({0,1},{2,3}) for i,j in used)

def analytic_shortcut(k,phi,psi):
    a=np.array([k*math.cos(phi),math.sin(phi)])
    b=np.array([k*math.cos(psi),math.sin(psi)])
    shorter=2*min(np.linalg.norm(a),np.linalg.norm(b))
    boundary=max(np.linalg.norm(a-b),np.linalg.norm(a+b))
    return shorter<boundary

rng=np.random.default_rng(304191)
for k in [1.,1.001,1.01,1.1,1.5,math.sqrt(3),2.,5.,10.]:
    vals=[];hits=0
    for _ in range(12000):
        phi,psi=rng.uniform(0,math.pi,2)
        flag=analytic_shortcut(k,phi,psi)
        assert kruskal_shortcut(k,phi,psi)==flag,(k,phi,psi)
        hits+=flag
    p=qprob(k)
    assert abs(p-hits/12000)<0.028,(k,p,hits/12000)
assert qprob(1)==0
assert critical_fraction(math.sqrt(3))==0
assert critical_fraction(2)>0
assert critical_fraction(10)>critical_fraction(2)
for e in [1e-4,2e-4]:
    c=qprob(1+e)/e
    assert abs(c-16/math.pi**2)<0.001,(e,c)
print('ANTIPODAL_ELLIPSE_MST_CHECKS_OK')

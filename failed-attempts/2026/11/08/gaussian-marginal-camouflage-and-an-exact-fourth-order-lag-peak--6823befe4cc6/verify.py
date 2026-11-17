#!/usr/bin/env python3
"""Reproducibility checks for the Poisson-refresh OU two-time theorem.
Only standard Python, NumPy and SymPy are required.
"""
from __future__ import annotations
import math
import numpy as np
import sympy as sp
from numpy.polynomial.hermite import hermgauss

# Algebraic identities for mixed joint moments and their cumulant.
r, lam, t, v, w, rho = sp.symbols('r lam t v w rho', positive=True)
cov = v*w*rho
m22 = v**2*(1 + 2*w*rho**2)
K = sp.factor(m22-v**2-2*cov**2)
assert sp.simplify(K-2*v**2*w*(1-w)*rho**2)==0

f = sp.exp(-(r+2*lam)*t)-sp.exp(-(2*r+2*lam)*t)
A=r+2*lam
B=2*r+2*lam
texpr=sp.log(B/A)/r
assert sp.simplify(sp.diff(f,t).subs(t,texpr))==0
assert sp.simplify(sp.diff(f,t,2).subs(t,texpr)).is_negative is not False
maxexpr=sp.simplify(2*v*v *r/B * (A/B)**(A/r))
assert sp.simplify(sp.powdenest((2*v*v*f).subs(t,texpr)-maxexpr, force=True))==0
assert sp.limit(maxexpr,r,sp.oo)==v*v/2
assert sp.limit((A/r)*sp.log(A/B),r,0,dir='+')==-1
assert sp.limit(2/B,r,0,dir='+')==1/lam

# Gaussian density with covariance v[[1,c],[c,1]].
def density(x,y,c,vv):
    denom = 2*math.pi*vv*math.sqrt(1-c*c)
    q=(x*x+y*y-2*c*x*y)/(2*vv*(1-c*c))
    return np.exp(-q)/denom

def kl_quadrature(r0,lam0,t0,d0,order=50):
    # Compute D(P||Q) by integrating log p/q under BOTH Gaussian mixture components.
    vv=d0/lam0
    weight=math.exp(-r0*t0)
    rho0=math.exp(-lam0*t0)
    c=weight*rho0
    h,hw=hermgauss(order)
    u=np.sqrt(2*vv)*h[:,None]
    z=np.sqrt(2*vv)*h[None,:]
    weights=hw[:,None]*hw[None,:]/math.pi
    def expectation(c_true):
        x=np.broadcast_to(u,(order,order))
        y=c_true*x+math.sqrt(1-c_true*c_true)*np.broadcast_to(z,(order,order))
        p=weight*density(x,y,rho0,vv)+(1-weight)*density(x,y,0,vv)
        q=density(x,y,c,vv)
        return np.sum(weights*np.log(p/q))
    return weight*expectation(rho0)+(1-weight)*expectation(0)

# Process-mixture sample cross-check; not used as a proof.
for i,(r0,lam0,d0,t0) in enumerate([(0.4,1.2,2.0,.8),(3.,.7,1.5,.5),(1.5,3.,.9,.18)]):
    vv=d0/lam0
    ww=math.exp(-r0*t0)
    rho0=math.exp(-lam0*t0)
    cc=ww*rho0
    analytic=2*vv*vv*ww*rho0*rho0*(1-ww)
    rng=np.random.default_rng(481+i)
    m=650_000
    x=rng.normal(size=m)*math.sqrt(vv)
    choose=rng.uniform(size=m)<ww
    z=rng.normal(size=m)*math.sqrt(vv)
    y=np.where(choose,rho0*x+math.sqrt(1-rho0*rho0)*z,z)
    emp=np.mean(x*x*y*y)-np.mean(x*x)*np.mean(y*y)-2*np.mean(x*y)**2
    assert abs(emp-analytic)<0.055*vv*vv, (i,emp,analytic)
    assert abs(np.mean(x*y)-cc*vv)<0.015*vv
    computed=kl_quadrature(r0,lam0,t0,d0)
    assert computed>1e-8,(i,computed)
    assert abs((-.5*math.log(1-cc**2)+computed)-(-.5*math.log(1-cc**2)))>1e-8
    print(f'case {i+1}: K_theory={analytic:.10g}, K_empirical={emp:.10g}, excess_mutual_information={computed:.10g}')

# Optimal peak is unique and strictly increases with r, and has the expected endpoints.
def Kpeak(r0,lam0,vv):
    aa=r0+2*lam0
    bb=2*(r0+lam0)
    return 2*vv*vv*(r0/bb)*(aa/bb)**(aa/r0)
for ll in [.3,1.,5.]:
    vals=[Kpeak(x,ll,1.) for x in [.03,.1,.3,1.,3.,10.,100.]]
    assert all(a<b for a,b in zip(vals,vals[1:])),vals
assert Kpeak(1e7,1.,1.)>0.499999
print('PASS: exact cumulant, peak, two-time mixtures, strict positive KL checks and limits')

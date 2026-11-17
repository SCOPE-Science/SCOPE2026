#!/usr/bin/env python3
"""Reproduce exact symbolic identities and finite-energy quadrature witnesses.
The numerical tests do not certify the proved large-energy limits.
Requires sympy and scipy; runs without network or external input data.
"""
import math
from scipy.integrate import quad
from scipy.special import lambertw
import sympy as s
u,v=s.symbols('u v',positive=True)
P=u*(1-v);Q=v*(u-1)
H=u+v-s.log(u)-s.log(v)-2
Lie=lambda f:s.diff(f,u)*P+s.diff(f,v)*Q
assert s.simplify(Lie(H))==0
assert s.simplify(Lie(s.log(u))-(1-v))==0
assert s.simplify(Lie(s.log(v))-(u-1))==0
assert s.simplify(Lie(u)-(u-u*v))==0
for r in range(1,6):
 for t in range(1,6):
  assert s.integrate(s.Symbol('a')**(r-1)*(1-s.Symbol('a'))**(t-1),(s.Symbol('a'),0,1)) == s.factorial(r-1)*s.factorial(t-1)/s.factorial(r+t-1)

def demo(L):
 from math import sin,cos,pi,exp,log
 edge=-exp(-L-1)
 ul=-lambertw(edge,0).real
 uh=-lambertw(edge,-1).real
 lo,hi=log(ul),log(uh)
 def vals(theta):
  z=lo+(hi-lo)*sin(theta)**2
  dz=2*(hi-lo)*sin(theta)*cos(theta)
  u=exp(z)
  q=max(1e-14,L+1-u+z)
  branch=-exp(-q-1)
  vm=-lambertw(branch,0).real
  vp=-lambertw(branch,-1).real
  return u,vm,vp,dz
 def integ(kind):
  def integrand(theta):
   u,vm,vp,dz=vals(theta)
   t1=1/(1-vm)
   t2=1/(vp-1)
   if kind=='period': return dz*(t1+t2)
   if kind=='flux':return dz*u*(vm*t1+vp*t2)
   if kind=='flux_u':return dz*u*u/L*(vm*t1+vp*t2)
   if kind=='log_u':return dz*(-math.log(u)/L)*(t1+t2)
   raise ValueError(kind)
  return quad(integrand,1e-7,pi/2-1e-7,epsabs=1e-5,epsrel=2e-6,limit=100)[0]
 T=integ('period')
 return T/L,integ('flux')/T,integ('flux_u')/T,integ('log_u')/T
for L in (40.,80.,160.):
 t,m,x,z=demo(L)
 assert t>1 and abs(m-1)<0.005
 assert 0.4<x<1.0 and 0.4<z<0.7
 print('L=',L,'period/L=',round(t,7),'flux normalization=',round(m,7),'flux E[u/L]=',round(x,7),'time E[-log(u)/L]=',round(z,7))
print('DUAL_LOTKA_VOLTERRA_SYMBOLIC_AND_QUADRATURE_OK')

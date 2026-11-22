#!/usr/bin/env python3
"""Reproducible symbolic checks and finite diagnostics for a neutral flip in a fear map.

The infinite-orbit conclusions follow from the proof, not from these finite checks.
"""
import math
import sympy as sp

z,v=sp.symbols('z v',real=True)
K, beta, gamma, k, a, b, c, q=sp.symbols('K beta gamma k a b c q', positive=True)
p,theta,eta=sp.symbols('p theta eta',positive=True)
# The exact scalar Ricker return in the normalized coordinate z=(u-K)/K.
f=(1+z)*sp.exp(-2*z)-1
f_jet=sp.series(f,z,0,8).removeO()
g_jet=sp.series((1+f_jet)*sp.exp(-2*f_jet)-1,z,0,8).removeO().expand()
assert sp.simplify(f_jet.coeff(z,2))==0
assert sp.simplify(g_jet.coeff(z,3)+sp.Rational(4,3))==0
assert sp.simplify(g_jet.coeff(z,4))==0
assert sp.simplify(g_jet.coeff(z,5)-sp.Rational(8,15))==0
assert sp.simplify(g_jet.coeff(z,6)-sp.Rational(4,9))==0
assert sp.simplify((3*sp.Rational(4,3)**2-2*sp.Rational(8,15))/(2*sp.Rational(4,3))-sp.Rational(8,5))==0
# Derive the quadratic strong-stable graph jet without dividing by an unproved limiting quantity.
h1=-p/(1+q)
C=2*k+p*(1+theta)
h2=sp.factor((h1*(C+q*eta)+p**2/2)/(1+q**2))
# Normalized exponent through degree 2:
# E=-2*z-p*v+(2*k+p*theta)*z*v + O((|z|+v)^3).
# One-step normalized prey expansion: z'=-z-p*v+C*z*v+p^2*v^2/2+O(3).
# Predator: v'=q*v-q*eta*v^2+O(3).
identity_1=sp.expand(q*h1 + h1+p)
identity_2=sp.expand((q*q+1)*h2 - h1*(C+q*eta)-p*p/2)
assert sp.simplify(identity_1)==0 and sp.simplify(identity_2)==0
print('SYMBOLIC_OK: scalar coefficients, reciprocal log coefficient, stable graph invariance')
print('f2_jet =',g_jet)
print('h1 =',h1, 'h2 =',h2)

# Finite diagnostics (not proofs): two explicit positive-predator initial states.
params=dict(K=2.0,beta=1.1,gamma=3.,k=0.5,a=2.,b=2.8,c=3.5,alpha=0.3,d=1.)
for zz0,v0 in [(0.03,0.001),(-0.03,0.001)]:
 P=params; uu=P['K']*(1+zz0);vv=v0; values={}
 for j in range(60001):
  if j%2==0 and j//2 in {1000,5000,15000,30000}:
   n=j//2; w=uu/P['K']-1
   values[n]=1/(w*w)-8*n/3-8*math.log(n)/5
  if j<60000:
   u_next=uu*math.exp(2/(1+P['k']*vv)*(1-uu/P['K'])-P['beta']*vv/(uu+P['gamma']))
   v_next=vv*math.exp(P['alpha']-P['d']-P['a']*vv/(P['b']*uu+P['c']))
   uu,vv=u_next,v_next
 assert abs(values[30000]-values[15000])<.25, values
 print('FINITE_DIAGNOSTIC sign', '+' if zz0>0 else '-', 'renormalized clock:', values)

P=params
p0=P['beta']/(P['K']+P['gamma']); th=P['K']/(P['K']+P['gamma']); eta0=P['a']/(P['b']*P['K']+P['c']); q0=math.exp(P['alpha']-P['d'])
H1=float(h1.subs({p:p0,q:q0})); H2=float(h2.subs({p:p0,q:q0,k:P['k'],theta:th,eta:eta0}))
for vv in [1e-4,5e-5,2.5e-5]:
 zz=H1*vv+H2*vv*vv; uu=P['K']*(1+zz)
 uu1=uu*math.exp(2/(1+P['k']*vv)*(1-uu/P['K'])-P['beta']*vv/(uu+P['gamma']))
 vv1=vv*math.exp(P['alpha']-P['d']-P['a']*vv/(P['b']*uu+P['c']))
 error=uu1/P['K']-1-(H1*vv1+H2*vv1**2)
 assert abs(error)<100*vv**3
 print('GRAPH_JET_DIAGNOSTIC v=',vv,'residual/v^3=',error/vv**3)
print('VERIFY_OK')

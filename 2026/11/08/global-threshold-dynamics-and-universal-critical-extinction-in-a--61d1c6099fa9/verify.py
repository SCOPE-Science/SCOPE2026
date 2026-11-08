#!/usr/bin/env python3
"""Exact coefficient identities and illustrative numerical trajectories for a planar population model.

Requires sympy and scipy. Finite integrations are not a proof of global convergence.
"""
import sympy as sp
from scipy.integrate import solve_ivp

u, v = sp.symbols('u v', positive=True)
r, a, alpha, k, P, Q, m, eta = sp.symbols('r a alpha k P Q m eta', positive=True)
f = r/(1+alpha*u+k*v)-a*u-P*v
g = Q*u-m-eta*v
assert sp.simplify(sp.diff(f,u)/v + sp.diff(g,v)/u + (a+r*alpha/(1+alpha*u+k*v)**2)/v+eta/u) == 0

example={r:sp.Integer(2),a:sp.Integer(1),alpha:sp.Integer(1),k:sp.Integer(1),P:sp.Integer(1),Q:sp.Rational(1,2),eta:sp.Integer(1)}
U=sp.Integer(1)
assert f.subs(example).subs({u:U,v:0}) == 0
A=sp.simplify(-sp.diff(u*f,u).subs(example).subs({u:U,v:0}))
B=sp.simplify(-sp.diff(u*f,v).subs(example).subs({u:U,v:0}))
C=sp.simplify(eta+Q*B/A).subs(example)
assert (A,B,C)==(sp.Rational(3,2),sp.Rational(3,2),sp.Rational(3,2))
assert sp.simplify((A*C-B*C)-(A-B)*C)==0

def ode(t,z,mass):
 x,y=z
 return (x*(2/(1+x+y)-x-y),y*(x/2-mass-y))

critical=solve_ivp(ode,(0,10000),(0.2,2.0),args=(.5,),method='DOP853',rtol=2e-11,atol=1e-13,t_eval=[100,1000,5000,10000])
assert critical.success
assert critical.y.min()>0
assert abs(10000*critical.y[1,-1]-2/3)<.005
assert abs(10000*(1-critical.y[0,-1])-2/3)<.005

coex=solve_ivp(ode,(0,400),(0.2,2.0),args=(.25,),method='DOP853',rtol=2e-11,atol=1e-13)
assert coex.success
assert abs(coex.y[0,-1]-sp.Rational(5,6))<1e-7
assert abs(coex.y[1,-1]-sp.Rational(1,6))<1e-7

subcrit=solve_ivp(ode,(0,100),(0.2,2.0),args=(1.0,),method='DOP853',rtol=2e-11,atol=1e-13)
assert subcrit.success
assert abs(subcrit.y[0,-1]-1)<1e-6
assert subcrit.y[1,-1]<1e-10
print('VERIFY_OK exact_dulac=1 exact_critical_coefficients=3 critical_long_time=1 coexistence=1 subcritical=1')
print('critical_at_10000',critical.y[:,-1].tolist(), 'predator_t_scaled',float(10000*critical.y[1,-1]), 'prey_deficit_t_scaled',float(10000*(1-critical.y[0,-1])))

#!/usr/bin/env python3
"""Exact identities and numerical checks of the weak-forcing joint-accessibility theorem."""
from fractions import Fraction as F
from math import sqrt, sin
from scipy.optimize import minimize_scalar
from scipy.integrate import solve_ivp
import sympy as s

# Exact polynomial identities underpinning the transfer-function formula.
g,D,u,C,z=s.symbols('gamma D u C z', positive=True)
Q=(D-z)**2+g*g*z
assert s.simplify(Q/z-(z+D**2/z+g*g-2*D))==0
assert s.simplify(s.diff(Q,z)-2*(z-D+g*g/2))==0
assert s.simplify(s.diff(Q/z,z)-(1-D*D/z**2))==0
print('EXACT_IDS_OK')

# Exact source parameter values (r,K,a,b,m)=(6/5,6,11/10,8/25,9/20).
r,K,a,b,m=F(6,5),F(6,1),F(11,10),F(8,25),F(9,20)
n=m/(a*b); p=r/a*(1-n/K); gamma=r*n/K; C0=a*b*p; D0=m*r*(1-n/K); u0=n*(1-n/K)
assert D0==(a*n)*C0
from math import pi
wn=sqrt(float(D0));wp=sqrt(max(0,float(D0-gamma*gamma/F(2))))
print('SOURCE_VALUES', 'n*=',n,'p*=',p,'gamma=',gamma,'D=',D0,'C=',C0,'u=',u0)
print('RESONANCES',wn,wp,'periods',2*pi/wn,2*pi/wp)
assert wp<wn

# Sharp global minimax checked against bounded scalar optimizations for all three regimes.
def Qv(w):return (float(D0)-w*w)**2+float(gamma)**2*w*w

def model(dn,dp):
 x=float(C0)*dn/dp
 if x<=wp: wstar=wp
 elif x>=wn: wstar=wn
 else:wstar=x
 def cost(w):return sqrt(Qv(w))/float(u0)*max(dn/w,dp/float(C0))
 sol=minimize_scalar(cost,bounds=(0.000001,10),method='bounded',options={'xatol':1e-14})
 assert abs(sol.x-wstar)<1e-4,(sol.x,wstar,x)
 assert abs(sol.fun-cost(wstar))<2e-7
 return x,wstar,cost(wstar)
for xfactor in [F(1,2),F(3,4),F(49,50),F(1),F(5,4),F(3,2)]:
 dn=float(xfactor)*wn/float(C0);dp=1.
 print('JOINT',xfactor,*model(dn,dp))

# Compare first-harmonic amplitudes with the nonlinear positive periodic branch.
from numpy import array
nv=float(n);pv=float(p);aa=float(a);bb=float(b);mm=float(m);kk=float(K);rr=float(r)
for w in [0.45,wp,wn,0.9]:
 period=2*pi/w
 AN=float(u0)*w/sqrt(Qv(w));AP=float(u0)*float(C0)/sqrt(Qv(w))
 for eps in [0.02,0.01,0.005]:
  def rhs(t,xy):
   N,P=xy
   return [N*((rr+eps*sin(w*t))*(1-N/kk)-aa*P),P*(aa*bb*N-mm)]
  # long time, then sample one period, including period endpoint
  t0=150
  sol=solve_ivp(rhs,(0,t0+period),(nv,pv),rtol=3e-10,atol=3e-12,dense_output=True,max_step=0.3)
  import numpy as np
  ts=np.linspace(t0,t0+period,901,endpoint=False)
  v=sol.sol(ts)
  predN=(max(v[0])-min(v[0]))/(2*eps)
  predP=(max(v[1])-min(v[1]))/(2*eps)
  assert abs(predN-AN)<1.0*eps, (w,eps,predN,AN)
  assert abs(predP-AP)<1.0*eps, (w,eps,predP,AP)
print('VERIFY_OK exact_identities=3 minimax_regimes=6 nonlinear_amplitude_checks=24')

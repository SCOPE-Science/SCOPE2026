#!/usr/bin/env python3
"""Standalone computational regression checks for constant-curvature Itoh--Abe steps.

The analytic proof is in RESULT.md; these finite checks are diagnostics only.
Requires Python 3, NumPy, SciPy and SymPy.
"""
from math import cos, sin, cosh, sinh, sqrt, atan2, acosh, asinh, exp, pi
import numpy as np
import sympy as sp
from scipy.optimize import root

# Exact algebra for the leading transverse displacement.
c,s,r,q = sp.symbols('c s r q', real=True)
H11=c*c+q*s*s; H22=s*s+q*c*c; H12=(q-1)*s*c
B=sp.Matrix([[H11/2,0],[H12,H22/2]])
g=sp.Matrix([-r*c,r*s])
transverse=sp.expand((sp.Matrix([[s,c]])*B*g)[0])
assert sp.factor(transverse-r*(1-q)*s*c/2).subs(s*s,1-c*c).simplify()==0

R=sp.symbols('R', positive=True)
for SK in (sp.sin(R), R, sp.sinh(R)):
 Q=R*sp.diff(SK,R)/SK
 assert sp.simplify(sp.diff(R/SK,R)-(1-Q)/SK)==0
print('symbolic transverse coefficient and primitive: PASS')

def s_k(K,r):
 if K==1: return sin(r)
 if K==-1:return sinh(r)
 return r

def eval_loss(r,uv,K):
 ur,ut=uv; length=np.hypot(ur,ut)
 if K==1:
  val=cos(r)*cos(length)+sin(r)*np.sinc(length/pi)*ur
  return .5*np.arccos(np.clip(val,-1,1))**2
 if K==-1:
  fac=sinh(length)/length if length>1e-12 else 1+length**2/6
  val=cosh(r)*cosh(length)-sinh(r)*fac*ur
  return .5*acosh(max(1.,val))**2
 return .5*((r-ur)**2+ut**2)

def step(r,h,theta,K,symmetric=False):
 E=np.array([[cos(theta),-sin(theta)],[sin(theta),cos(theta)]])
 f0=.5*r*r
 def f_(a,b):return eval_loss(r,E@np.array([a,b]),K)
 def divided_difference(a,b,index):
  if index==0:
   base=f_(0,0); target=f_(a,0)
   return (target-base)/a if abs(a)>1e-9 else (f_(1e-5,0)-f_(-1e-5,0))/(2e-5)
  if index==1:
   base=f_(a,0); target=f_(a,b)
   return (target-base)/b if abs(b)>1e-9 else (f_(a,1e-5)-f_(a,-1e-5))/(2e-5)
  if index==2:
   base=f_(0,b); target=f_(a,b)
   return (target-base)/a if abs(a)>1e-9 else (f_(1e-5,b)-f_(-1e-5,b))/(2e-5)
  base=f0;target=f_(0,b)
  return (target-base)/b if abs(b)>1e-9 else (f_(0,1e-5)-f_(0,-1e-5))/(2e-5)
 def F(v):
  a,b=v
  A=divided_difference(a,b,0);B=divided_difference(a,b,1)
  if symmetric:
   A=(A+divided_difference(a,b,2))/2
   B=(B+divided_difference(a,b,3))/2
  return np.array([a+h*A,b+h*B])
 guess=E.T@np.array([h*r,0.])
 sol=root(F,guess,tol=1e-10)
 assert np.linalg.norm(F(sol.x))<1e-8, (K,h,r,sol.message)
 ur,ut=E@sol.x
 length=np.hypot(ur,ut)
 if K==1:
  x=cos(length)*sin(r)-np.sinc(length/pi)*ur*cos(r)
  y=np.sinc(length/pi)*ut
  z=cos(length)*cos(r)+np.sinc(length/pi)*ur*sin(r)
  rnew=atan2(np.hypot(x,y),z)
 elif K==-1:
  fac=sinh(length)/length if length>1e-12 else 1
  x=cosh(length)*sinh(r)-fac*ur*cosh(r)
  y=fac*ut
  rnew=asinh(np.hypot(x,y))
 else:
  x=r-ur;y=ut;rnew=np.hypot(x,y)
 return rnew,atan2(y,x)

def orbit(N,K,symmetric=False,theta=pi/4):
 r=.9;phi=0.;h=1/N
 for _ in range(N):
  r,dphi=step(r,h,theta,K,symmetric)
  phi+=dphi
 return phi,h

for K in [1,-1,0]:
 r0=.9;T=1.
 expected=.25*(r0/s_k(K,r0)-(r0*exp(-T))/s_k(K,r0*exp(-T)))
 previous_error=None
 for N in (32,64,128,256):
  phase,h=orbit(N,K)
  error=abs(phase/h-expected)
  if K==0:assert error<3e-9
  else:
   assert error<.04/N, (K,N,error)
   if previous_error is not None:assert error<.54*previous_error
  previous_error=error
 print(f'curvature {K:+d}: forward coefficient {expected:+.12f}; at N=256 observed {phase/h:+.12f}: PASS')
 if K:
  values=[]
  for N in (64,128,256):
   phase,h=orbit(N,K,True,pi/8)
   values.append(abs(phase/h))
  assert values[2]<.56*values[1]<.56*.56*values[0],(K,values)
  print(f'curvature {K:+d}: order-averaged leading drift cancels: PASS')
for K in (1,-1,0):
 for h in (.1,.5,1.):
  rnew,phi=step(.9,h,pi/4,K,True)
  exact=.9*(1-h/2)/(1+h/2)
  assert abs(rnew-exact)<2e-9 and abs(phi)<2e-9,(K,h,rnew,exact,phi)
 print(f'curvature {K:+d}: bisector order average gives exact radial midpoint: PASS')
print('All diagnostic checks passed.')

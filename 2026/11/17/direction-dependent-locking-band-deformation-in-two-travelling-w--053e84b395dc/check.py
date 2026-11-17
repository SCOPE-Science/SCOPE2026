"""Verify projective identities and perturbative locking boundaries.

Run: python check.py
Requirements: sympy, scipy, numpy.
Finite numerical checks corroborate the separate analytical arguments.
"""
import math
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

z,v,B,c,s=sp.symbols('z v B c s',real=True)
q=(2-v)*(1+z*z)+(1-z*z)+B*((1-z*z)*c+2*z*s)
a=(1-v-B*c)/2
bb=B*s
d=(3-v+B*c)/2
assert sp.simplify(q/2-(a*z*z+bb*z+d))==0
M=sp.Matrix([[bb/2,d],[-a,-bb/2]])
assert sp.trace(M)==0
assert sp.simplify(sp.det(sp.Matrix([[1,0],[0,1]])))==1
k=sp.symbols('k',integer=True,nonzero=True)
p=sp.simplify(1/(6*k)-1/(36*k*k))
lo=sp.simplify(1/(2*k)+1/(4*k*k))
width=sp.factor(p-lo)
assert sp.simplify(width+(6*k+5)/(18*k*k))==0

def orbit(y0, v0, b0, k0):
 T=2*math.pi/v0
 def rhs(t,w):
  y,der=w
  phase=y-k0*v0*t
  return [2-v0+math.cos(y)+b0*math.cos(phase),
          (-math.sin(y)-b0*math.sin(phase))*der]
 sol=solve_ivp(rhs,[0,T],[y0,1],rtol=2e-12,atol=2e-13)
 assert sol.success
 return sol.y[0,-1],sol.y[1,-1]

def fold(b0,k0,high):
 anchor=0. if high else math.pi
 v0=3. if high else 1.
 def closure(v1):return orbit(anchor,v1,b0,k0)[0]-anchor
 a,b=v0-0.07,v0+0.07
 assert closure(a)*closure(b)<0
 root=brentq(closure,a,b,xtol=1e-13)
 _,mult=orbit(anchor,root,b0,k0)
 assert abs(mult-1)<2e-8
 return root

for k0 in [-2,-1,1,2]:
 for b0 in [0.1,0.05,0.025]:
  lower=fold(b0,k0,False)
  upper=fold(b0,k0,True)
  lo_pred=1+(1/(2*k0)+1/(4*k0*k0))*b0*b0
  hi_pred=3+(1/(6*k0)-1/(36*k0*k0))*b0*b0
  # With these four frequencies, the analytic fourth-order errors are small.
  assert abs(lower-lo_pred)<2.0*b0**4
  assert abs(upper-hi_pred)<.20*b0**4
  print('FOLD',k0,b0,f'{lower:.12f}',f'{upper:.12f}',
        'width',f'{upper-lower:.12f}')
 for b0 in [0.11]:
  v0=2.
  def closure(y0):return orbit(y0,v0,b0,k0)[0]-y0
  neg=brentq(closure,-2.8,-.2,xtol=1e-13)
  pos=brentq(closure,.2,2.8,xtol=1e-13)
  mn=orbit(neg,v0,b0,k0)[1]
  mp=orbit(pos,v0,b0,k0)[1]
  assert abs(neg+pos)<1e-9
  assert abs(mn*mp-1)<1e-9
  print('RECIPROCAL',k0,'product',f'{mn*mp:.12f}')
print('VERIFY_OK symbolic_projective=1 quadratic_coefficients=1 fold_cases=12 reciprocal_pairs=4')

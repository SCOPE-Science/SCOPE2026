#!/usr/bin/env python3
"""Check exact boundary-chord moment identities for equal-ball lenses.

Run: python verify.py (requires sympy and numpy).
"""
import numpy as np
import sympy as sp

h,z=sp.symbols('h z', real=True)
E=lambda p:sp.factor(sp.integrate(p,(z,h,1))/(1-h))
rad2=1+h*h-2*h*z
M=E(rad2)
M4=E(rad2**2)
A=E((z-h)**2)
T=E((1-z**2)/2)
ch2=2*M
ch4=sp.factor(2*M4+2*M**2+4*(A**2+2*T**2))
assert sp.simplify(M-(1-h))==0
assert sp.simplify(M4-(1-h)**2*(3+h**2)/3)==0
assert sp.simplify(A-(1-h)**2/3)==0
assert sp.simplify(T-(1-h)*(2+h)/6)==0
assert sp.simplify(ch2-2*(1-h))==0
assert sp.simplify(ch4-4*(1-h)**2*(4+h**2)/3)==0
assert sp.simplify(ch4/ch2**2-(4+h**2)/3)==0

# Independently sample the geometric surface: at each point choose one of
# the two bounding spherical patches, then a uniform spherical cap coordinate.
rng=np.random.default_rng(462817)
checks=7
for R,a in [(1.,0.),(0.7,.2),(1.4,.5),(2.5,.8),(.83,.93)]:
 N=250000
 coords=[]
 for _ in (0,1):
  signed=rng.choice(np.array([-1.,1.]),size=N)
  z=R*(a+(1.-a)*rng.random(N))
  phi=2*np.pi*rng.random(N)
  pts=np.column_stack((signed*(z-R*a),np.sqrt(np.maximum(R*R-z*z,0.))*np.cos(phi),np.sqrt(np.maximum(R*R-z*z,0.))*np.sin(phi)))
  coords.append(pts)
 d2=np.square(coords[0]-coords[1]).sum(axis=1)
 observed=(d2.mean(),np.square(d2).mean())
 expected=(2*R*R*(1-a),4*R**4*(1-a)**2*(4+a*a)/3)
 # Statistical tolerances scale with standard error; this is a smoke test,
 # not a proof of exactness.
 assert abs(observed[0]/expected[0]-1)<.015, (a,observed,expected)
 assert abs(observed[1]/expected[1]-1)<.025, (a,observed,expected)
 checks+=2
print('PASS:',checks,'symbolic identities / Monte Carlo comparisons; five independent parameter pairs')

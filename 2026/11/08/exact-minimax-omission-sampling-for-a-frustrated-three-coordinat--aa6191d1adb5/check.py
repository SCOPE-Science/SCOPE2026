"""Reproducible checks for an exact three-coordinate block-selection result.
Python >=3.10; sympy and numpy only.
"""
import math
from fractions import Fraction
import numpy as np
import sympy as sp

c,d=sp.symbols('c d',positive=True)
Z=2*c*c+d*d+3*d
a=d*(1+d)/Z
b=(c*c+d)/Z
lam=(1+d)*(c*c+d)/Z
assert sp.simplify(a+2*b-1)==0
assert sp.factor(lam-b*(1+d))==0
# The symmetric two-dimensional spectral block has this characteristic polynomial.
T=sp.symbols('T')
char=(T-a)*(T-b*(1-d))-2*c*c*a*b
assert sp.simplify(char.subs(T,lam))==0
# Uniform / determinant-proportional pair sampling yields (1+d)/3.
assert sp.simplify((1+d)/3-lam-(d-c)*(c+d)*(d+1)/(3*Z))==0
assert sp.simplify((1+d)/(3*lam)-1-(d-c)*(c+d)/(3*(c*c+d)))==0
# At the balancing point the upper (symmetric) eigenvalue grows with a.
F1=2*c*c-c*(1+d)+2*d
assert sp.factor(F1.subs(d,c))==c*(c+1)
assert sp.simplify(sp.det(sp.Matrix([[1,c,c],[c,1,-d],[c,-d,1]]))-(1+d)*(1-d-2*c*c))==0

count=0
for ci in range(1,37,2):
 for di in range(ci,100,3):
  cv=ci/100;dv=di/100
  if 2*cv*cv+dv >=1:continue
  G=np.array([[1,cv,cv],[cv,1,-dv],[cv,-dv,1]],float)
  assert np.linalg.eigvalsh(G).min()>0
  av=dv*(1+dv)/(2*cv*cv+dv*dv+3*dv)
  bv=(1-av)/2
  expected=(1+dv)*(cv*cv+dv)/(2*cv*cv+dv*dv+3*dv)
  def eigmax(p):
   return np.linalg.eigvalsh(np.sqrt(p[:,None]*p[None,:])*G)[-1]
  assert abs(eigmax(np.array([av,bv,bv]))-expected)<1e-12
  assert abs(eigmax(np.ones(3)/3)-(1+dv)/3)<1e-12
  # Every symmetric competitor in a fine global mesh must be no better.
  for ai in range(201):
   aa=ai/200
   assert eigmax(np.array([aa,(1-aa)/2,(1-aa)/2]))>=expected-1e-11
   count+=1
  # In addition, test nonsymmetric choices on a triangular grid.
  for ii in range(0,101,5):
   for jj in range(0,101-ii,5):
    p=np.array([ii,jj,100-ii-jj])/100
    assert eigmax(p)>=expected-1e-11
    count+=1
print('PASS symbolic identities; tested positive-definite parameters and',count,'sampled probabilities')

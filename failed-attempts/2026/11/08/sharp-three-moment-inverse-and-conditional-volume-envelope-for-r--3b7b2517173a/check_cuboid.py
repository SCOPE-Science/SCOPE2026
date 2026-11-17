#!/usr/bin/env python3
"""Exact moment and sharp-envelope checks for the rectangular-box inverse theorem.

Usage: python3 check_cuboid.py
Requires sympy; NumPy is used only for supplementary sample checks.
"""
from fractions import Fraction as F
from math import comb, sqrt
from random import Random
import sympy as sp

m=[F(1), F(1,6), F(1,15), F(1,28)]
k2=m[2]-m[1]**2
k3=m[3]-3*m[2]*m[1]+2*m[1]**3
assert k2==F(7,180) and k3==F(11,945)
# Direct exact expansion of the first three moments of a weighted sum of squared differences.
x,y,z=sp.symbols('x y z', positive=True)
coef=[sp.Rational(1), sp.Rational(1,6), sp.Rational(1,15), sp.Rational(1,28)]
raw=[]
from math import factorial
for k in (1,2,3):
 total=0
 for i in range(k+1):
  for j in range(k-i+1):
   ell=k-i-j
   total+=sp.factorial(k)/(sp.factorial(i)*sp.factorial(j)*sp.factorial(ell))*coef[i]*coef[j]*coef[ell]*x**i*y**j*z**ell
 raw.append(sp.expand(total))
p1=x+y+z;p2=x*x+y*y+z*z;p3=x**3+y**3+z**3
assert sp.simplify(raw[0]-p1/6)==0
assert sp.simplify(raw[1]-raw[0]**2-sp.Rational(7,180)*p2)==0
assert sp.simplify(raw[2]-3*raw[1]*raw[0]+2*raw[0]**3-sp.Rational(11,945)*p3)==0
v2=sp.expand(x*y*z)
inv_v2=(p1**3-3*p1*p2+2*p3)/6
assert sp.simplify(inv_v2-v2)==0
# Reconstruct exact algebraic side squares from three even distance moments.
for vals in ((1,1,1),(1,2,3),(sp.Rational(1,4),3,9),(sp.Rational(1,9),sp.Rational(7,3),17)):
 obs=[sp.factor(o.subs({x:vals[0],y:vals[1],z:vals[2]})) for o in raw]
 s1=6*obs[0];s2=sp.Rational(180,7)*(obs[1]-obs[0]**2)
 s3=sp.Rational(945,11)*(obs[2]-3*obs[1]*obs[0]+2*obs[0]**3)
 T=sp.symbols('T')
 cp=T**3-s1*T**2+(s1**2-s2)*T/2-(s1**3-3*s1*s2+2*s3)/6
 assert sp.expand(cp-sp.prod(T-v for v in vals))==0
# A pair of noncongruent positive boxes sharing M1 and M2, with different M3.
r=sp.sqrt(3)/6
A=(2*(1-r),2*(1-r),2*(1+2*r))
B=(2*(1+r),2*(1+r),2*(1-2*r))
assert all(v>0 for v in A+B)
assert sp.simplify(sum(A)-sum(B))==0
assert sp.simplify(sum(v*v for v in A)-sum(v*v for v in B))==0
assert sp.simplify(sp.prod(A)-sp.prod(B))!=0
assert sp.simplify(sp.prod(A)-sp.prod(B))>0
# Polynomial extremizer identity, including an exact vanishing endpoint at r=1/2.
R=sp.symbols('R',real=True)
gmax=(1-R)**2*(1+2*R)/27
gmin=(1+R)**2*(1-2*R)/27
assert sp.expand(gmax-(1-3*R**2+2*R**3)/27)==0
assert sp.expand(gmin-(1-3*R**2-2*R**3)/27)==0
assert gmin.subs(R,sp.Rational(1,2))==0
rng=Random(20261104)
for _ in range(12000):
 t=[10**rng.uniform(-3,3) for j in range(3)]
 p=sum(t);q=sum(v*v for v in t)/p**2
 r=sqrt((3*q-1)/2)
 vol= t[0]*t[1]*t[2]/p**3
 upper=(1-3*r*r+2*r**3)/27
 lower=(1-3*r*r-2*r**3)/27 if r<.5 else 0.0
 assert lower-1e-13 <= vol <= upper+1e-13,(t,vol,lower,upper)
# Numerical direct point-pair simulation on selected boxes, checking moments to sampling tolerance.
import numpy as np
rg=np.random.default_rng(20261104)
for lengths in ((1.,1.,1.),(1.,2.,3.),(.7,1.3,5.)):
 vals=[x*x for x in lengths]
 exact=np.array([float(o.subs({x:vals[0],y:vals[1],z:vals[2]})) for o in raw])
 N=450000
 delta=(rg.random((N,3))-rg.random((N,3)))*np.array(lengths)
 dist2=np.sum(delta**2,axis=1)
 for k in (1,2,3):
  sample=dist2**k
  assert abs(sample.mean()-exact[k-1]) < 6.0*sample.std(ddof=1)/sqrt(N)
print('CUBOID_INVERSE_OK exact_cumulants=3 inverse_shapes=4 nonunique_pair=1 envelope_samples=12000 direct_sample_shapes=3 samples_each=450000')

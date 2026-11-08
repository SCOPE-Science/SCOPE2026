#!/usr/bin/env python3
"""Exact algebraic and finite diagnostic checks for the harmonic-triad theorem.
Universal validity relies on the accompanying proof, not on these finite tests.
"""
from itertools import product
from fractions import Fraction
from math import cos, pi
import random
import sympy as sp

A,B,C,r,x,y,z=sp.symbols('A B C r x y z', real=True)
coef={-3:C/sp.Integer(2),-2:B/sp.Integer(2),-1:A/sp.Integer(2),1:A/sp.Integer(2),2:B/sp.Integer(2),3:C/sp.Integer(2)}
q=sp.expand(sum(sp.prod(coef[k] for k in ks) for ks in product(coef, repeat=4) if sum(ks)==0))
expected=(3*(A**4+B**4+C**4)+12*(A*A*B*B+A*A*C*C+B*B*C*C)+4*A**3*C+12*A*B*B*C)/8
assert sp.simplify(q-expected)==0
assert sp.simplify(sp.expand(sp.integrate((A*sp.cos(x)+B*sp.cos(2*x)+C*sp.cos(3*x))**4,(x,0,2*sp.pi))/(2*sp.pi))-expected)==0
print('EXACT_FOURIER_ZERO_SUM_AND_DIRECT_TRIG_INTEGRATION_OK')

S=A*A+B*B+C*C
K=(4*expected/S**2)
Kminus=(sp.Rational(3,2)*(1+r**4)+6*r*r-2*r)/(1+r*r)**2
Kplus=(9+12*r*r+sp.Rational(3,2)*r**4+8*r)/(2+r*r)**2
p=3*r**3-3*r**2-3*r+1
h=3*r**3+6*r**2-3*r-4
assert sp.simplify(sp.diff(Kminus,r)+2*p/(1+r*r)**3)==0
assert sp.simplify(sp.diff(Kplus,r)+4*h/(2+r*r)**3)==0
assert sp.count_roots(p,0,1)==1 and sp.count_roots(p,1,2)==1
assert sp.count_roots(h,0,1)==1 and sp.count_roots(h,1,sp.oo)==0
assert p.subs(r,sp.Rational(1,4))>0 and p.subs(r,sp.Rational(3,10))<0
assert h.subs(r,sp.Rational(4,5))<0 and h.subs(r,sp.Rational(9,10))>0
print('EXACT_CUBIC_STURM_ROOT_COUNTS_AND_DERIVATIVES_OK')

# The min reduction is an exact coefficient identity (with t=a^2+c^2 and b^2=y).
t=x+z
Nminus=sp.Rational(3,2)*(x*x+y*y+z*z)+6*(x*y+x*z+y*z)-2*x*sp.sqrt(x*z)-6*y*sp.sqrt(x*z)
Ntwo=sp.Rational(3,2)*(x*x+z*z)+6*x*z-2*x*sp.sqrt(x*z)
assert sp.simplify(Nminus-(Ntwo+sp.Rational(3,2)*y*y+(6*t-6*sp.sqrt(x*z))*y))==0
# The inequality 6t-6sqrt(xz) >= 3t is 3(sqrt x-sqrt z)^2 >= 0.
assert sp.simplify(3*(A*A+C*C)-6*A*C-3*(A-C)**2)==0
print('EXACT_MINIMUM_DECOMPOSITION_AND_POSITIVE_CROSS_BOUND_OK')

# The upper reduction uses a^2+b^2=s; the cubic coefficient is maximal at a=b.
v,s=sp.symbols('v s',real=True,positive=True)
a=sp.sqrt(s/sp.Integer(2))*v
assert sp.simplify(sp.sqrt(2)*s**sp.Rational(3,2)-a*(3*s-2*a*a)-s**sp.Rational(3,2)/sp.sqrt(2)*(v-1)**2*(v+2))==0
# The deficit from equal first-two squared amplitudes is exact.
assert sp.factor(sp.Rational(3,4)*(A*A-B*B)**2 - (sp.Rational(3,4)*(A*A+B*B)**2-3*A*A*B*B))==0
assert sp.simplify(K.subs({A:1,B:1,C:r})-Kplus)==0
assert sp.simplify(K.subs({A:1,B:0,C:-r})-Kminus)==0
print('EXACT_MAXIMUM_SYMMETRIZATION_DEFICIT_OK')

# Resultants identify algebraic endpoints without relying on floating-point certificates.
mm,MM=sp.symbols('mm MM')
assert sp.factor(sp.resultant(p,sp.together(mm-Kminus).as_numer_denom()[0],r)/104)==208*mm**3-1224*mm**2+2268*mm-1323
assert sp.factor(sp.resultant(h,sp.together(MM-Kplus).as_numer_denom()[0],r)/418)==3344*MM**3-22644*MM**2+47736*MM-32049
print('EXACT_ALGEBRAIC_ENDPOINT_RESULTANTS_OK')

rootminus=next(float(sp.re(k)) for k in sp.nroots(p,maxsteps=200) if abs(float(sp.im(k)))<1.e-10 and 0<float(sp.re(k))<1)
rootplus=next(float(sp.re(k)) for k in sp.nroots(h,maxsteps=200) if abs(float(sp.im(k)))<1.e-10 and 0<float(sp.re(k))<1)
minval=float(Kminus.subs(r,rootminus));maxval=float(Kplus.subs(r,rootplus))
assert 1.22 < minval < 1.23 and 3.40 < maxval < 3.42
print('ENDPOINT_DIAGNOSTICS_OK',f'{rootminus:.13f}',f'{minval:.13f}',f'{rootplus:.13f}',f'{maxval:.13f}')

# Independent exact Fourier coefficient computation for complex coefficients.
rand=random.Random(1729)
def moments(u,v,w):
 fs={-3:w.conjugate()/2,-2:v.conjugate()/2,-1:u.conjugate()/2,1:u/2,2:v/2,3:w/2}
 d0=sum(aa*bb for k,aa in fs.items() for j,bb in fs.items() if k+j==0).real
 d4=sum(aa*bb*cc*dd for k,aa in fs.items() for j,bb in fs.items() for t,cc in fs.items() for t2,dd in fs.items() if k+j+t+t2==0).real
 aa,bb,cc=abs(u),abs(v),abs(w)
 proposed=(3*(aa**4+bb**4+cc**4)+12*(aa*aa*bb*bb+aa*aa*cc*cc+bb*bb*cc*cc))/8
 proposed+=(u**3*w.conjugate()).real/2+1.5*(u*w*v.conjugate()**2).real
 return d0,d4,proposed
for idx in range(240):
 u=complex(rand.uniform(-2,2),rand.uniform(-2,2))
 v=complex(rand.uniform(-2,2),rand.uniform(-2,2))
 w=complex(rand.uniform(-2,2),rand.uniform(-2,2))
 d0,d4,prop=moments(u,v,w)
 assert abs(d0-(abs(u)**2+abs(v)**2+abs(w)**2)/2)<1e-11
 assert abs(d4-prop)<1e-9*max(1,abs(d4))
 assert minval-1e-11 <= d4/d0**2 <= maxval+1e-11
print('FOURIER_COMPLEX_COEFFICIENT_RANDOM_DIAGNOSTICS_OK',240)
print('ALL_FOURIER_TRIAD_CHECKS_PASSED')

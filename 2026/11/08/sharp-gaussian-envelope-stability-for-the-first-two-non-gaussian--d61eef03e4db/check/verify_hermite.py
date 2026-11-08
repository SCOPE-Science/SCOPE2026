#!/usr/bin/env python3
"""Exact symbolic and independent integral checks for the two-Hermite envelope theorem.
Requires sympy and scipy for the optional direct-integral checks.
"""
import math
import random
import sympy as sp
from scipy.integrate import quad

T, w = sp.symbols('T w', real=True)
s5=sp.sqrt(5)
L1=1-T
L2=1-2*T+T**2/sp.Integer(2)
t0=3-s5
w0=1-1/s5
c=(s5-2)**2
F=lambda w:sp.expand(w*L1**2+(1-w)*L2**2)
P=sp.simplify((s5/sp.Integer(20))*(T-t0)**2*((T-(1+s5))**2+4))
assert sp.simplify(F(w0)-c-P)==0
assert sp.simplify(L1.subs(T,t0)-(s5-2))==0
assert sp.simplify(L2.subs(T,t0)+(s5-2))==0
assert sp.simplify(F(w).subs(T,t0)-c)==0
assert sp.simplify(sp.diff(F(w),T).subs(T,t0)-2*(s5-2)*((1-w)*(s5-1)-w))==0
assert sp.solve(sp.diff(F(w),T).subs(T,t0),w)==[w0]
assert 0<float(w0)<1 and 0<float(t0) and 0<float(c)
assert sp.discriminant(T**2-2*(1+s5)*T+10+2*s5,T)==-16

# Check the radial ambiguity formula against independent quadrature of the
# normalized Hermite functions, including non-axis-aligned phase-space points.
h0=lambda u:2**.25*math.exp(-math.pi*u*u)
h1=lambda u:2*math.sqrt(math.pi)*u*h0(u)
h2=lambda u:(4*math.pi*u*u-1)/math.sqrt(2)*h0(u)
for n,hn in enumerate([h1,h2],start=1):
 for x,y in [(0,0),(.27,.43),(.8,-.35),(1.1,0),(0,.9)]:
  real=quad(lambda t:hn(t+x/2)*hn(t-x/2)*math.cos(2*math.pi*y*t),-6,6,epsabs=2e-12)[0]
  imag=quad(lambda t:-hn(t+x/2)*hn(t-x/2)*math.sin(2*math.pi*y*t),-6,6,epsabs=2e-12)[0]
  r2=math.pi*(x*x+y*y)
  pred=math.exp(-r2/2)*float((L1 if n==1 else L2).subs(T,r2))
  assert abs(real-pred)<1e-10 and abs(imag)<1e-10,(n,x,y,real,pred,imag)

# Stress-test all weights and radii for the sharp upper/lower certificate.
rng=random.Random(20261104)
for i in range(20000):
 t=rng.random()*100
 weight=rng.random()
 twostar=float(w0)*(1-t)**2+(1-float(w0))*(1-2*t+t*t/2)**2
 assert twostar>=float(c)-1e-9
 assert abs(weight*(1-float(t0))**2+(1-weight)*(1-2*float(t0)+float(t0)**2/2)**2-float(c))<1e-10
print('TWO_HERMITE_GAUSSIAN_ENVELOPE_CHECKS_PASS 20000 10 direct_integrals')

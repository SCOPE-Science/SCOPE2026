"""Reproduce exact algebra for a noisy two-knot Brownian bridge area design.

Run: python check.py (requires SymPy and mpmath).
Finite numerical comparisons are diagnostic only; global optimality is proved in RESULT.md.
"""
import sympy as S
import mpmath as mp

x,y,z,e,u,v=S.symbols('x y z e u v', real=True)
D=x**2*(1-2*x)
T=2*x*(1-x)
F=D**2/(D+e*T+e**2)
# The derivative's sign is given by the stated polynomial for 0<x<1/2.
P=2*(1-3*x)*e**2+x*(3-12*x+8*x**2)*e + x**2*(1-2*x)*(1-3*x)
assert S.simplify(S.diff(F,x) - 2*D*x*P/(D+e*T+e**2)**2)==0
# The fixed-x stationary discriminant has a cubic factor.
q=3-12*x+8*x*x
assert S.factor(q*q-8*(1-3*x)**2*(1-2*x)) == (4*x-1)*(16*x**3-8*x**2+4*x-1)
# x=y/(1+2y); show the stationarity polynomial has one sign change.
yexpr=y/(1+2*y)
Q=S.expand((1+2*y)**3*(y*y+2*e*y*(1+y)*(1+2*y)+e**2*(1+2*y)**3))
assert S.simplify(F.subs(x,yexpr)-y**4/Q)==0
assert all(S.Poly(Q,y).coeff_monomial(y**i)!=0 for i in range(7))
assert S.Poly(4*Q-y*S.diff(Q,y),y).coeff_monomial(y**4)==0
# Covariance of the bridge observations and area information.
s,t=S.symbols('s t', real=True)
K=S.Matrix([[s*(1-s),s*(1-t)],[s*(1-t),t*(1-t)]])
assert S.simplify(K.det()-s*(t-s)*(1-t))==0
assert S.simplify(S.trace(K)-s*(1-s)-t*(1-t))==0
# For fixed outer-gap sum u and outer product v, the objective increases with v.
G=(v*(1-u))**2 / ((1-u+2*e)*v+e*u*(1-u)+e**2)
num=S.factor(S.together(S.diff(G,v)))
assert S.simplify(num.subs(e,S.Rational(1,10)).subs(u,S.Rational(3,5)).subs(v,S.Rational(1,50)))>0
# Certified locations and outward-return minimum.
mp.mp.dps=50
C=lambda xx:16*xx**3-8*xx**2+4*xx-1
r=mp.findroot(C,(mp.mpf('0.32'),mp.mpf('0.33')))
eta=-r*(3-12*r+8*r*r)/(4*(1-3*r))
assert mp.mpf('0.32389943563052') < r < mp.mpf('0.32389943563053')
assert mp.mpf('0.13592225317301') < eta < mp.mpf('0.13592225317303')
Pfun=S.lambdify((x,e),P,'mpmath')
assert abs(Pfun(r,eta))<mp.mpf('1e-45')
# Explicit strict gain over equal thirds at the maximum-displacement noise.
ff= S.lambdify((x,e),F,'mpmath')
assert ff(r,eta)>ff(mp.mpf(1)/3,eta)
# Supplementary exhaustive finite diagnostics (not a proof).
import random
rng=random.Random(1829)
for ee in [mp.mpf(0),mp.mpf('0.0001'),mp.mpf('0.01'),eta,mp.mpf('0.3'),mp.mpf(1),mp.mpf(10)]:
 if ee == 0: optimum=mp.mpf(1)/3
 else: optimum=mp.findroot(lambda xx:Pfun(xx,ee),(.32,.334))
 V=ff(optimum,ee)
 for _ in range(1000):
  a=mp.mpf(rng.random());b=mp.mpf(rng.random());s0,t0=sorted((a,b))
  d0=s0*(t0-s0)*(1-t0)
  tr=s0*(1-s0)+t0*(1-t0)
  val=d0*d0/(d0+ee*tr+ee*ee) if d0+ee*tr+ee*ee else mp.mpf(0)
  assert val<=V+mp.mpf('1e-30')
print('PASS: derivative, discriminant, covariance, monotonicity, sign-change polynomial, 7000 diagnostics')
print('optimal minimum outer spacing:',mp.nstr(r,30))
print('noise at minimum:',mp.nstr(eta,30))
print('noise-free outer spacing: 1/3; high-noise limit outer spacing: 1/3')

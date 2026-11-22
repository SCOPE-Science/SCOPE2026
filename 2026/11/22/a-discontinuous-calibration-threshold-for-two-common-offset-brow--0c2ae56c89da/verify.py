"""Reproducible exact and numerical checks for common-offset Wiener quadrature.

Requires Python 3.10+, sympy and numpy. Tests support the proof;
they are not a substitute for the all-parameter analytic arguments.
"""
import math
from fractions import Fraction
import numpy as np
import sympy as sp

s, t, eta = sp.symbols('s t eta', real=True)
c = lambda z: z-z*z/2
h = s**2*(1-s/2)**2/(s+eta)+sp.Rational(8,27)*(1-s)**3
A = s*s+(2+4*eta)*s-4*eta
B = 5*s*s+(8*eta-2)*s-8*eta
assert sp.factor(sp.diff(h,s)+A*B/(36*(s+eta)**2)) == 0
p = sp.factor(h-sp.Rational(8,27))
assert sp.factor(p+s*(32*eta*(s*s-3*s+3)+s*(5*s*s+12*s-12))/(108*(s+eta)))==0
H = s*(12-12*s-5*s*s)/(32*(s*s-3*s+3))
assert sp.factor(sp.diff(H,s)+(s*s-3*s-6)*(5*s*s-15*s+6)/(32*(s*s-3*s+3)**2))==0
sstar=(15-sp.sqrt(105))/10
etastar=(-69+7*sp.sqrt(105))/64
assert sp.simplify(H.subs(s,sstar)-etastar)==0
assert sp.simplify(B.subs({s:sstar,eta:etastar}))==0
assert sp.simplify(h.subs({s:sstar,eta:etastar})-sp.Rational(8,27))==0
assert sp.simplify(h.subs({s:sp.Rational(2,5),eta:0})-sp.Rational(8,25))==0

# The independent-increment decomposition and direct Gaussian covariance
# agree exactly for all symbolic 0 < s < t < 1 and eta >= 0.
Sigma=sp.Matrix([[s+eta,s+eta],[s+eta,t+eta]])
cv=sp.Matrix([c(s),c(t)])
general=sp.factor((cv.T*Sigma.inv()*cv)[0])
increment=sp.factor(c(s)**2/(s+eta)+(c(t)-c(s))**2/(t-s))
assert sp.factor(general-increment)==0
assert sp.factor(increment-(c(s)**2/(s+eta)+(t-s)*(1-(t+s)/2)**2))==0
# Optimizing the second observation yields an interior strict maximum.
delta=sp.symbols('delta', real=True)
g=delta*(1-s-delta/2)**2
assert sp.factor(sp.diff(g,delta)-(1-s-delta/2)*(1-s-3*delta/2))==0
assert sp.simplify(g.subs(delta,2*(1-s)/3)-sp.Rational(8,27)*(1-s)**3)==0

rng=np.random.default_rng(20261117)
max_matrix_error=0.0
max_optimality_violation=0.0
for j in range(7000):
    e=float(rng.uniform(0.00001,2))
    x=float(rng.uniform(0.0001,0.999))
    y=float(rng.uniform(x+1e-6,1))
    C=np.array([[x+e,x+e],[x+e,y+e]],dtype=float)
    v=np.array([float(c(x)),float(c(y))])
    info=float(v@np.linalg.solve(C,v))
    explicit=x*x*(1-x/2)**2/(x+e)+(y-x)*(1-(y+x)/2)**2
    max_matrix_error=max(max_matrix_error,abs(info-explicit))
    assert abs(info-explicit)<2e-10
    # Global expression against off-optimum random candidate.
    sm=(2-8*e+math.sqrt((8*e-2)**2+160*e))/10
    hi=sm*sm*(1-sm/2)**2/(sm+e)+8*(1-sm)**3/27
    hbest=max(hi,8/27)
    max_optimality_violation=max(max_optimality_violation,explicit-hbest)
    assert explicit<=hbest+5e-13

# Exact algebraic and numerical checks of two competing optimum regimes.
for e in [0.0,0.0001,0.005,0.01,0.02,0.04,float(etastar),0.05,0.2,1.0,100.0]:
    sm=(2-8*e+math.sqrt((8*e-2)**2+160*e))/10
    hi=sm*sm*(1-sm/2)**2/(sm+e)+8*(1-sm)**3/27
    hcal=8/27
    if e<float(etastar)-1e-12: assert hi>hcal
    if e>float(etastar)+1e-12: assert hi<hcal
assert abs(float(etastar)-0.04263524002683107)<1e-13
print('PASS: exact symbolic identities, critical point and 7000 independent matrix/design comparisons')
print('maximum Gaussian matrix identity discrepancy:',max_matrix_error)
print('maximum random design advantage over predicted optimum:',max_optimality_violation)
print('critical common-noise variance:',float(etastar))
print('coexisting interior design:',float(sstar),float((sstar+2)/3))

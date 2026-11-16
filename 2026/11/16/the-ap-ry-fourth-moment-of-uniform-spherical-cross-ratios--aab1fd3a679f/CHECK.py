"""Independent finite consistency checks for spherical logarithmic cross-ratio moments.

Finite arithmetic and sampling support, but do not replace, the analytic proof.
"""
from math import factorial, pi
import numpy as np
import mpmath as mp
import sympy as sp

j = sp.symbols('j', integer=True, positive=True)
f = (2*j + 1)/(16*j**4*(j+1)**4)
parts = (1/(8*j**2) - 1/(8*j**3) + 1/(16*j**4)
         - 1/(8*(j+1)**2) - 1/(8*(j+1)**3) - 1/(16*(j+1)**4))
assert sp.simplify(f-parts) == 0
exact_cycle = sp.Rational(5,16)-sp.zeta(3)/4
assert sp.simplify(sp.summation(f, (j,1,sp.oo))-exact_cycle) == 0
assert sp.simplify(4*sp.Rational(9,16) + 36*sp.Rational(1,16) + 24*exact_cycle - (12-6*sp.zeta(3))) == 0

mp.mp.dps = 55
for ell in range(1,9):
    val = mp.quad(lambda t: mp.log((1-t)/2)*mp.legendre(ell,t), [-1,0,0.75,1])
    target = -mp.mpf(2)/(ell*(ell+1))
    assert abs(val-target) < mp.mpf('1e-45'), (ell,val,target)

for n in (2,3,8,32,100,500):
    s = sum((2*k+1)/(16*k**4*(k+1)**4) for k in range(1,n+1))
    assert s < float(exact_cycle.evalf(30))
    assert abs(float(exact_cycle.evalf(30))-s) < 1/(4*n**6)

rng = np.random.default_rng(593920)
n = 400_000
p = rng.normal(size=(n,4,3))
p /= np.linalg.norm(p,axis=2,keepdims=True)
def e(a,b):
    return np.log(np.linalg.norm(p[:,a]-p[:,b],axis=1)/2) + 0.5
x13,x24,x12,x34 = e(0,2),e(1,3),e(0,1),e(2,3)
y=x13+x24-x12-x34
assert abs(float(np.mean(y))) < .012
assert abs(float(np.mean(y**2))-1) < .03
assert abs(float(np.mean(y**4)) - float((12-6*sp.zeta(3)).evalf())) < .15
assert abs(float(np.mean(x13*x24*x12*x34))-float(exact_cycle.evalf())) < .004
print('PASS: exact partial fractions, symbolic zeta evaluation, 8 Legendre integrals, 6 truncation bounds, four Monte Carlo moment checks')
print('cycle4=',float(exact_cycle.evalf(16)), 'fourth=',float((12-6*sp.zeta(3)).evalf(16)))

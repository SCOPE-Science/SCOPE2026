#!/usr/bin/env python3
"""Symbolic and finite-trajectory checks for a near-critical sigmoid flip."""
import math
import sympy as sp

x,a=sp.symbols('x a')
t=sp.series(sp.tanh(a*x/2)/2-x,x,0,7).removeO().expand()
s=sp.factor(t.coeff(x,1))
d=sp.factor(-t.coeff(x,3))
e=sp.factor(t.coeff(x,5))
assert sp.simplify(s-(a/4-1))==0
assert sp.simplify(d-a**3/48)==0
assert sp.simplify(e-a**5/480)==0
A=sp.factor(2*d/s**3)
B=sp.factor(3*d**2/s**4-2*e/s**3)
assert A.subs(a,8)==sp.Rational(64,3)
assert B.subs(a,8)==sp.Rational(1024,5)
assert sp.simplify((B/A).subs(a,8)-sp.Rational(48,5))==0

def residual(theta, n, x0):
    gain=8+theta/n
    w=x0
    for _ in range(n):
        w=math.tanh(gain*w/2)/2-w
        assert w>0 and w<=0.1
    phi= -math.expm1(-theta/2)/(theta/2) if theta!=0 else 1
    return 1/(w*w) - (64/3)*n*phi - (48/5)*math.exp(-theta/2)*math.log(n)

for theta in [-8.,-2.,0.,2.,8.]:
    for x0 in [.04,.08,.10]:
        r1=residual(theta,10000,x0)
        r2=residual(theta,100000,x0)
        assert math.isfinite(r1) and math.isfinite(r2)
        assert abs(r1-r2)<40*(1+math.exp(-theta/2))
print('SIGMOID_NEAR_FLIP_TWO_ORDER_CHECK_OK exact_coefficients=3 parameter_cases=5 initial_points=3 horizons=2')

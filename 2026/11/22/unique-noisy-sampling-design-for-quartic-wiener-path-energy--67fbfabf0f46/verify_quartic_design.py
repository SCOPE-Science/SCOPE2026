#!/usr/bin/env python3
"""Exact identities and supplementary numerical checks for one-shot quartic Wiener energy quadrature."""
import sympy as s
from math import isfinite
x, e, t, u = s.symbols('x e t u', nonnegative=True)
F = x**2*(1-s.Rational(2,3)*x)
A = x**2/s.Integer(2)-x**4/s.Integer(4)
B = x**4*(1-s.Rational(4,5)*x)
v = x+e
I = 72*A**2/v**2+24*B**2/v**4
assert s.simplify(F-(s.integrate(t**2,(t,0,x))+x**2*(1-x))) == 0
assert s.simplify(A-(s.integrate(t**3,(t,0,x))+x**2*s.integrate(t,(t,x,1)))) == 0
assert s.simplify(B-(s.integrate(t**4,(t,0,x))+x**4*(1-x))) == 0
cov2 = 2*s.integrate(s.integrate(t*u*t**2,(t,0,u)),(u,0,1))
cov4 = 2*s.integrate(s.integrate(t**4,(t,0,u)),(u,0,1))
assert s.simplify(72*cov2+24*cov4-s.Rational(38,5)) == 0
num,den = s.together(s.diff(I,x)).as_numer_denom()
P = s.cancel(num/(3*x**3)); assert s.simplify(den-25*(x+e)**5) == 0
H = s.Poly(s.cancel(P.subs(x,t/(1+t))*(1+t)**7),t)
cs = [s.factor(H.nth(i)) for i in range(8)]
expected = [
 600*e**3,
 300*e**2*(14*e+5),
 300*e*(39*e**2+30*e+4),
 300*(55*e**3+67*e**2+20*e+1),
 100*(123*e**3+204*e**2+115*e+12),
 5*(900*e**3+1785*e**2+1524*e+400),
 10*e*(60*e**2+105*e+77),
 -(75*e**2+150*e+107)
]
assert all(s.simplify(a-b)==0 for a,b in zip(cs,expected))
assert s.simplify(s.diff(A/F,x)-3*(x-2)*(x-1)/(2*(2*x-3)**2)) == 0
assert s.simplify(s.diff(B/F**2,x)-72*(x-1)/(5*(2*x-3)**3)) == 0
assert s.simplify(s.diff(2*F**2/v**2,x).subs(x,s.Rational(3,4)).subs(e,0)) == 0
assert s.simplify(s.factor(s.diff(I.subs(e,0),x)) -3*x*(993*x**4-1600*x**3+200*x**2+300)/25)==0
assert s.simplify(I.subs({x:1,e:0})-s.Rational(273,50))==0
assert s.simplify(I.subs({x:0,e:1}))==0
import mpmath as mp
mp.mp.dps=45
x0=mp.findroot(lambda z: 993*z**4-1600*z**3+200*z**2+300, (.8,.85))
assert mp.mpf('.82176036367851')<x0<mp.mpf('.82176036367852')
fun = s.lambdify((x,e),I,'mpmath')
assert abs((mp.mpf(38)/5-fun(x0,0))-mp.mpf('0.982798773160052398777799912')) <mp.mpf('1e-20')
for noise in [0,mp.mpf('0.01'),mp.mpf('.1'),1,10,100,1000]:
    z=mp.findroot(lambda z: mp.mpf(s.N(P.subs({x:z,e:noise}),30)), (.7,.95)) if noise < 2 else mp.findroot(lambda z: mp.mpf(s.N(P.subs({x:z,e:noise}),30)), (.9,.99999))
    assert 0<z<1
    # Supplementary dense samples are NOT the uniqueness proof; Descartes handles all x and e.
    for k in range(1,200):
        y=mp.mpf(k)/200
        assert fun(z,noise)>fun(y,noise)-mp.mpf('1e-24')
    q=(3-6*noise+mp.sqrt(9+60*noise+36*noise**2))/8
    assert z>q
    print('noise=',noise,'optimal_x=',mp.nstr(z,22),'quadratic_x=',mp.nstr(q,17))
print('PASS: exact rational identities, transformed Descartes certificate, risk, comparison and supplementary evaluations')

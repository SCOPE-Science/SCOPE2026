"""Exact symbolic checks for a four-compartment plankton diffusion threshold.

Requires Python 3 and SymPy (tested on SymPy 1.13.1).
All identities below are rational/polynomial, not numerical eigenvalue guesses.
The infinitude of Neumann modes is handled analytically in RESULT.md.
"""
import sympy as sp

n,p,zeta,h=sp.symbols('N P Z D', positive=True)
d,q=sp.symbols('d q', positive=True)
x=sp.symbols('x')
# Nutrient, phytoplankton, zooplankton, detritus, respectively.
f=sp.Matrix([
  -2*p*n/(1+n)+h,
   2*p*n/(1+n)-zeta*p/(1+p)-p/2,
   zeta*p/(1+p)-zeta/2,
   p/2+zeta/2-h,
])
eq={n:1,p:1,zeta:1,h:1}
assert f.subs(eq)==sp.zeros(4,1)
J=f.jacobian([n,p,zeta,h]).subs(eq)
J_expected=sp.Matrix([
 [-sp.Rational(1,2),-1,0,1],
 [sp.Rational(1,2),sp.Rational(1,4),-sp.Rational(1,2),0],
 [0,sp.Rational(1,4),0,0],
 [0,sp.Rational(1,2),sp.Rational(1,2),-1],
])
assert J==J_expected
assert sp.factor(J.charpoly(x).as_expr())==x*(16*x**3+20*x**2+12*x+5)/16

M=J-q*sp.diag(1,d,1,1)
cp=sp.Poly(M.charpoly(x).as_expr(),x)
b3,b2,b1,b0=[sp.factor(cp.coeff_monomial(x**i)) for i in (3,2,1,0)]
want_b3=(4*d*q+12*q+5)/4
want_b2=3*(4*d*q*q+2*d*q+4*q*q+3*q+1)/4
want_b1=(48*d*q**3+48*d*q*q+8*d*q+16*q**3+12*q*q+16*q+5)/16
want_b0=q*(16*d*q**3+24*d*q*q+8*d*q-4*q*q+4*q+5)/16
for actual,expected in [(b3,want_b3),(b2,want_b2),(b1,want_b1),(b0,want_b0)]:
 assert sp.cancel(actual-expected)==0
H2=sp.factor(b3*b2-b1)
H3=sp.factor(b3*b2*b1-b1*b1-b3*b3*b0)
want_H2=(48*d*d*q**3+24*d*d*q*q+144*d*q**3+120*d*q*q+34*d*q+128*q**3+156*q*q+65*q+10)/16
want_H3=((64*d*q**3+48*d*q*q+8*d*q+64*q**3+32*q*q+16*q+5)*
         (16*d*d*q**3+12*d*d*q*q+32*d*q**3+40*d*q*q+17*d*q+16*q**3+28*q*q+20*q+5))/128
assert sp.cancel(H2-want_H2)==0
assert sp.cancel(H3-want_H3)==0
r=(4*q*q-4*q-5)/(16*q**3+24*q*q+8*q)
assert sp.cancel(sp.diff(r,q)+(8*q**4-16*q**3-46*q*q-30*q-5)/(8*q*q*(q+1)**2*(2*q+1)**2))==0
assert r.subs(q,sp.Rational(9,4))==sp.Rational(25,1287)
assert r.subs(q,4)==sp.Rational(43,1440)
assert r.subs(q,sp.Rational(25,4))==sp.Rational(101,3915)
assert sp.Rational(25,1287)<sp.Rational(101,3915)<sp.Rational(43,1440)
assert want_b0.subs({q:4,d:sp.Rational(43,1440)})==0
assert want_b0.subs({q:4,d:sp.Rational(1,100)})==-sp.Rational(143,20)
assert want_b0.subs({q:4,d:1})>0
# Check that equality is simple (not a multiple zero of the quartic).
assert want_b1.subs({q:4,d:sp.Rational(43,1440)})>0
print('PASS: ecological equilibrium, Jacobian, exact quartic and Hurwitz factorizations, modal threshold and rational witness')

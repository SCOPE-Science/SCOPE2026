#!/usr/bin/env python3
"""Reproduce the symbolic contact and elimination certificates for a cyclic-six quartic family.
Run: python3 verify_hyperflex.py (requires SymPy 1.10+)."""
import sympy as S
r,t,x,y,z,h,m=S.symbols('r t x y z h m')
F=x**3*z+y**4+r*y**2*z**2+z**4
assert S.diff(F,x)==3*x**2*z
assert S.diff(F,y)==4*y**3+2*r*y*z**2
assert S.diff(F,z)==x**3+2*r*y**2*z+4*z**3
# The tangent at an affine point (x,y), x != 0, is x -> x + m*h, y -> y+h.
g=y**4+r*y**2+1
contact=S.Poly(S.expand((x+m*h)**3+g.subs(y,y+h)),h)
assert S.expand(contact.coeff_monomial(h)- (3*x**2*m+4*y**3+2*r*y))==0
assert S.expand(contact.coeff_monomial(h**2)-(3*x*m**2+6*y**2+r))==0
assert S.expand(contact.coeff_monomial(h**3)-(m**3+4*y))==0
assert contact.coeff_monomial(h**4)==1
# On C, x**3=-g, so the quadratic and cubic coefficients vanish iff A=B=0.
G=t**2+r*t+1
A=S.expand(4*t*(2*t+r)**2-3*G*(6*t+r))
B=S.expand(2*t*(2*t+r)**3-27*G**2)
f=11*r**4-1080*r**2+3888
assert S.factor(S.resultant(A,B,t))==324*(r-2)**3*(r+2)**3*f
# The system at every smooth exceptional r has one and only one value of y**2.
basis=S.groebner([A,B,f],t,r,order='lex')
assert [S.expand(p.as_expr()) for p in basis.polys]==[864*t-11*r**3+972*r,f]
T=r*(11*r**2-972)/864
assert S.rem(S.together(A.subs(t,T)).as_numer_denom()[0],f,r)==0
assert S.rem(S.together(B.subs(t,T)).as_numer_denom()[0],f,r)==0
assert S.gcd(f,S.diff(f,r))==1
assert S.gcd(f,r*(r-2)*(r+2))==1
assert S.gcd(f,S.together(T).as_numer_denom()[0])==1
num,den=S.together(G.subs(t,T)).as_numer_denom()
assert S.simplify(S.rem(num,f,r)/den-(r**2+12)/12)==0
assert S.gcd(f,r**2+12)==1
# For y=0 the cubic term vanishes automatically, and the quadratic is exactly r.
assert S.expand(contact.coeff_monomial(h**2).subs({y:0,m:0}))==r
# At x=0 the affine branch roots of y**4+r*y**2+1 are simple for r != +/-2,
# and fixing y at a root restricts the curve to x**3=0 (ordinary contact three).
assert S.factor(S.discriminant(g,y))==16*(r-2)**2*(r+2)**2
# At [1:0:0], tangent z=0 cuts the quartic as y**4=0.
assert S.expand(F.subs(z,0))==y**4
# In characteristic zero a smooth quartic has 24 total flex weight.
assert {(1,22),(4,16),(7,10)}=={(n,24-2*n) for n in (1,4,7)}
print('VERIFY_HYPERFLEX_OK')

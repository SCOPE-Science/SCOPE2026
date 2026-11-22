#!/usr/bin/env python3
"""Exact consistency check for a generic-phase (1,1,2) Lissajous surface."""
import sympy as s
x,y,z,U=s.symbols("x y z U")
lam=s.Integer(2)
twoT2=2*(2*z*z-1)
# U=t+t^{-1}, t=u_2*u_3^2, u_1=lam/t.
F=(1-lam**2)**2-U*(1-lam**2)*(U-2*lam*x)+(U-2*lam*x)**2
G=U**2-2*y*twoT2*U+4*(y*y+(twoT2/2)**2-1)
R=s.factor(s.resultant(F,G,U))
assert s.Poly(R,x,y,z).total_degree()==8
assert tuple(s.degree(R,v) for v in (x,y,z))==(4,4,8)
factors=s.factor_list(R)[1]
assert len(factors)==1 and factors[0][1]==1
partials=(R,s.diff(R,x),s.diff(R,y),s.diff(R,z))
def factor_on(var,value,extensions=()):
    opts={"extension":list(extensions)} if extensions else {}
    return s.factor(s.gcd_list([f.subs(var,value) for f in partials],**opts))
T2=2*z*z-1
for sign in (1,-1):
    assert s.expand(factor_on(x,sign*s.Rational(5,4))-4*(y-sign*T2))==0
    assert s.expand(factor_on(y,sign*s.Rational(5,4))-4*(x-sign*T2))==0
assert s.factor(factor_on(z,0))==16*x*x+40*x*y+16*y*y+9
for sign in (1,-1):
    assert s.factor(factor_on(z,sign*3*s.sqrt(2)/4,(s.sqrt(2),)))==x-y
    assert s.factor(factor_on(z,sign*s.I*s.sqrt(2)/4,(s.I,s.sqrt(2))))==x+y
print("PASS: irreducible degree-eight hypersurface and nine exact singular-curve slice factors")

"""Exact symbolic consistency checks (requires SymPy). Not a continuum certificate."""
import sympy as sp
s, r = sp.symbols('s r', positive=True)
E = sp.exp(-sp.Rational(1, 2))
m = 4 - 2*E*(sp.Rational(5,2)*sp.cosh(s)-s*sp.sinh(s))
u = 2*E*(sp.Rational(3,2)*sp.sinh(s)/s-sp.cosh(s))
k = (1+2*s)*sp.exp(-2*s)
T = 2*sp.exp(-2*s)*m/u-1-k
assert sp.simplify(sp.diff(m,s)+s*u)==0
assert sp.simplify(sp.diff(k,s)+4*s*sp.exp(-2*s))==0
assert sp.simplify(sp.diff(T,s)-2*sp.exp(-2*s)*(s-m/u*(2+sp.diff(u,s)/u)))==0
assert sp.simplify(2*sp.integrate((1-r)*(1+r)*sp.exp(-r),(r,0,1))-(8/sp.E-2))==0
ser=sp.series(T,s,0,2).removeO()
assert sp.simplify(ser.subs(s,0)-(8*sp.sqrt(sp.E)-12))==0
assert sp.simplify(sp.diff(ser,s)-(20-16*sp.sqrt(sp.E)))==0
print('PASS: exact Gaussian-mean derivatives, threshold derivative, prior variance and collision expansion')

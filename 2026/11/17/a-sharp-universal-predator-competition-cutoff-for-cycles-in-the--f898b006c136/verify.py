#!/usr/bin/env python3
"""Exact symbolic identities for the competition cutoff in a Bazykin flow.

Needs Python 3 and SymPy. Checks finite algebraic statements; the analytic
no-cycle, all-parameter realization, and Poincare-Bendixson arguments are
proved in the accompanying manuscript, not established by this program.
"""
import sympy as s
x, y, r, k, a, b, e, d, sig=s.symbols('x y r k a b e d sig',positive=True)
f=r*x*(1-x/k)-a*x*y/(x+b)
g=y*(e*a*x/(x+b)-d-sig*y)
D=s.cancel(s.diff(f/(x*y),x)+s.diff(g/(x*y),y))
assert s.simplify(D-(-r/(k*y)+a/(x+b)**2-sig/x))==0
assert s.factor((x+b)**2-4*b*x)==(x-b)**2
yp=2*r*b*(k-b)/(a*k)
dp=e*a/s.Integer(2)-sig*yp
J=s.Matrix([f,g]).jacobian([x,y]).subs({x:b,y:yp,d:dp}).applyfunc(s.factor)
T=s.factor(J.trace()); E=s.factor(J.det())
assert s.simplify(T-r/k*((k-3*b)/2-2*sig*b*(k-b)/a))==0
assert s.simplify(E-yp*(e*a**2/(8*b)-sig*r*(k-3*b)/(2*k)))==0
z={a:1,b:1,sig:s.Rational(1,5),k:30,r:s.Rational(1,100),e:s.Rational(1,2)}
assert sig.subs(z)<(a/(4*b)).subs(z)
assert dp.subs(z)==s.Rational(923,3750)>0
assert T.subs(z)==s.Rational(19,30000)>0
assert E.subs(z)==s.Rational(2233,1875000)>0
assert (r/a).subs(z)<(4*e*a*b/(sig*(k+b)**2)).subs(z)
assert (e*a*k/(k+b)-dp).subs(z)>0
assert s.simplify(f.subs({x:b,y:yp,d:dp}))==0
assert s.simplify(g.subs({x:b,y:yp,d:dp}))==0
print('VERIFY_OK symbolic_dulac=1 sharp_maximum=1 general_repeller=2 rational_witness=7')
print('rational_witness trace=19/30000 determinant=2233/1875000 d=923/3750')

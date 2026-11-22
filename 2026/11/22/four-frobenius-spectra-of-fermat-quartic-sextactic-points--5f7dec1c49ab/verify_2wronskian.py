#!/usr/bin/env python3
"""Exact symbolic check of the Fermat quartic 2-Wronskian; requires sympy."""
import sympy as s
x,y=s.symbols('x y'); js=s.symbols('u1:7'); j=[y,*js]
jetD=lambda e:s.diff(e,x)+sum(j[k+1]*s.diff(e,j[k]) for k in range(6))
f=[s.Integer(1),x,y,x*x,x*y,y*y]; rows=[]
for k in range(6):
    rows.append(f)
    f=[s.expand(jetD(t)) for t in f]
actual=s.factor(s.Matrix(rows).det(method='berkowitz'))
u1,u2,u3,u4,u5,u6=js
assert s.simplify(actual-4*u2*(45*u4*u3*u2-9*u5*u2*u2-40*u3**3))==0
# Differentiation on F(x,y)=x^4+y^4+1=0 via y'=-x^3/y^3.
D=lambda z:s.factor(s.diff(z,x)-x**3/y**3*s.diff(z,y))
yds=[y]
for _ in range(5):yds.append(D(yds[-1]))
y1,y2,y3,y4,y5=yds[1:6]
w=s.factor(4*y2*(45*y4*y3*y2-9*y5*y2*y2-40*y3**3))
expected=22680*x**5*(x**4-y**4)*(x**4+y**4)**4*(x**4+2*y**4)*(2*x**4+y**4)/y**40
assert s.cancel(w-expected)==0
print('SYMBOLIC_2WRONSKIAN_CERTIFIED_OK')

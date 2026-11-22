#!/usr/bin/env python3
"""Symbolic algebra for a piecewise-smooth jerk system's integral, balances and saltation."""
import sympy as sp
x, y, z, w, a, b, c, s = sp.symbols('x y z w a b c s', real=True)
f = sp.Matrix([y, z, -a*z-b*y+c*(x-s), x*y+y*z])
I = w - (x*x+y*y)/2
assert sp.simplify(sp.Matrix([sp.diff(I,q) for q in (x,y,z,w)]).dot(f)) == 0
p,q,r = sp.symbols('p q r', real=True)
change = sp.Matrix([x,y,z,I])
assert sp.simplify(change.jacobian([x,y,z,w]).det()) == 1
vec=sp.Matrix([y,z,-a*z-b*y+c*(x-s)])
L=lambda g: sp.expand(sp.Matrix([sp.diff(g,v) for v in (x,y,z)]).dot(vec))
# On x != 0, sign x=s and |x|=s*x, so L|x|=s*y.
identity_z=sp.expand(L(y*z)+a*L(y*y/2)-c*L(x*x/2)+c*s*y-(z*z-b*y*y))
identity_y=sp.expand(L(x*z)-L(y*y/2)+a*L(x*y)+b*L(x*x/2)-(a*y*y+c*(x*x-s*x)))
assert identity_z == 0, identity_z
assert identity_y == 0, identity_y
J = vec.jacobian([x,y,z]); assert sp.trace(J)==-a
Delta=sp.symbols('Delta',real=True)
S=sp.eye(3)+sp.Matrix([0,0,Delta])*sp.Matrix([[1,0,0]])/y
assert sp.simplify(S.det())==1
# Smooth 4x4 saltation has same unit determinant because jump is only z-component.
J4=f.jacobian([x,y,z,w]); assert sp.simplify(sp.trace(J4)+a)==0
print('PASS: exact integral; global polynomial coordinate; two stationary coboundaries; smooth divergence; unit crossing saltation determinant')

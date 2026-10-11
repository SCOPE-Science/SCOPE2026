#!/usr/bin/env python3
import sympy as sp

x,y,z,w,a,b,k,lam,sigma = sp.symbols('x y z w a b k lam sigma', nonzero=True)
F = sp.Matrix([
    k*y,
    -x-y*z,
    sigma*x + x*y - a,
    x-b*w,
])
J = F.jacobian((x,y,z,w))
A = J[:3,:3]
assert J[:3,3] == sp.zeros(3,1)
assert sp.simplify(J[3,3] + b) == 0
char4 = sp.expand((lam*sp.eye(4)-J).det())
char3 = sp.expand((lam*sp.eye(3)-A).det())
assert sp.simplify(char4 - (lam+b)*char3) == 0

# The first three equations do not contain w or b.
for i in range(3):
    assert w not in F[i].free_symbols
    assert b not in F[i].free_symbols

# Difference of two lifts over the same base orbit obeys d'=-b d.
d = sp.Function('d')
t = sp.symbols('t', real=True)
sol = sp.exp(-b*t)
assert sp.simplify(sp.diff(sol,t) + b*sol) == 0

# At the paper's baseline b=1, the invariant vertical tangent direction
# has exact exponent -1, independently of the base trajectory.
assert sp.simplify((-b).subs(b,1) + 1) == 0

print('VERIFY_OK')

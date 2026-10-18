#!/usr/bin/env python3
import sympy as sp

u,A,B,C = sp.symbols("u A B C")
P = sp.Matrix([u**4, u**2-u**5, 1+2*u**3])
cr = P.cross(P.diff(u))
expected_factor = u*(u**3+2)
Q = sp.Matrix([4*u**3-1, 2*u**2, -u**4])
assert all(sp.expand(cr[i] - expected_factor*Q[i]) == 0 for i in range(3))

F = sp.expand((B**2-4*A*C)**2 + 128*B*C**3)
sub = {A:Q[0], B:Q[1], C:Q[2]}
assert sp.expand(F.subs(sub)) == 0
assert sp.expand((B**2-4*A*C).subs(sub) - 16*u**7) == 0
assert sp.expand((B*C).subs(sub) + 2*u**6) == 0
assert sp.simplify(-((B**2-4*A*C)/(8*B*C)).subs(sub) - u) == 0

FA,FB,FC = [sp.factor(sp.diff(F,z)) for z in (A,B,C)]
assert sp.expand(FA - 8*C*(4*A*C-B**2)) == 0
assert sp.expand(FB + 4*(4*A*B*C-B**3-32*C**3)) == 0
assert sp.expand(FC - 8*(4*A**2*C-A*B**2+48*B*C**2)) == 0

b = sp.cancel(Q[1]/Q[0])
c = sp.cancel(Q[2]/Q[0])
v = sp.factor(c-b**2/4)
assert sp.factor(v + 4*u**7/(4*u**3-1)**2) == 0
assert sp.limit(b/u**2,u,0) == -2
assert sp.limit(v/u**7,u,0) == -4

W = sp.factor(sp.Matrix.hstack(P,P.diff(u),P.diff(u,2)).det())
assert W == -4*u**3*(u**3+2)**2
Wdual = sp.factor(sp.Matrix.hstack(Q,Q.diff(u),Q.diff(u,2)).det())
assert Wdual == 16*u**3*(u**3+2)
print("VERIFY_OK")

#!/usr/bin/env python3
"""Exact symbolic consistency check for a two-site quadratic map theorem."""
import sympy as s
u,w,c,d,m,g=s.symbols('u w c d mu gamma',real=True)
M=m*(1-2*u); A=M-g-1; B=M+g+1; C=M-g+1
P=s.Matrix([u+w+c+d,u-w+c-d]); Q=s.Matrix([u+w-c-d,u-w-c+d])
def F(X):return s.Matrix([m*X[0]*(1-X[0])+g*X[1],m*X[1]*(1-X[1])+g*X[0]])
E=F(P)-Q; E2=F(Q)-P
assert s.expand((E[0]+E[1]+E2[0]+E2[1])/4)==s.expand((m+g-1)*u-m*(u*u+w*w+c*c+d*d))
assert s.expand((E[0]-E[1]+E2[0]-E2[1])/4)==s.expand(A*w-2*m*c*d)
assert s.expand((E[0]+E[1]-E2[0]-E2[1])/4)==s.expand(B*c-2*m*w*d)
assert s.expand((E[0]-E[1]-E2[0]+E2[1])/4)==s.expand(C*d-2*m*w*c)
J=lambda X:s.Matrix([[m*(1-2*X[0]),g],[g,m*(1-2*X[1])]])
K=J(Q)*J(P)
expression=s.expand((s.eye(2)-K).det())
# Normal form relations substituted in exact polynomial form.
expression=s.expand(expression.subs(c*d*w,A*w*w/(2*m)))
for sym,square in [(c,A*C/(4*m*m)),(d,A*B/(4*m*m)),(w,B*C/(4*m*m))]:
 expression=s.expand(expression).subs(sym**4,square**2).subs(sym**2,square)
assert s.simplify(expression+16*M*A*B*C)==0
print('PASS: orbit equations and exact Floquet identity')

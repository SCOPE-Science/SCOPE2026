#!/usr/bin/env python3
import sympy as sp

S,I,X = sp.symbols("S I X", positive=True)
Rx,Rc,sigma,eps,c,R0 = sp.symbols("Rx Rc sigma eps c R0", positive=True)
Lam = Rx*X + Rc*I
Idot = Lam*S/(S+I) - c*I
Xdot = sigma*I - eps*X
Vdot = sp.expand(Idot + (Rx/eps)*Xdot)
target = -Lam*I/(S+I) - c*(1-R0)*I
relation = {R0:(Rc + Rx*sigma/eps)/c}
assert sp.simplify((Vdot-target).subs(relation)) == 0

lam = sp.symbols("lam")
B = sp.Matrix([[Rc-c,Rx],[sigma,-eps]])
assert sp.simplify(B.det().subs(Rc,c*R0-Rx*sigma/eps) - eps*c*(1-R0)) == 0

pi,mu,delta = sp.symbols("pi mu delta", positive=True)
A = sp.Matrix([[-pi-mu,delta],[pi,-delta-mu]])
assert sp.factor(A.det()) == mu*(delta+mu+pi)
assert sp.simplify(sp.trace(A) + pi + delta + 2*mu) == 0
print("VERIFY_OK")

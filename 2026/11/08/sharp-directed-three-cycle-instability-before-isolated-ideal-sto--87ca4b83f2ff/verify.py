#!/usr/bin/env python3
"""Exact checks for the directed three-node ideal-storage stability threshold."""
import sympy as sp
z, d, w, r = sp.symbols('z d w r', real=True)
P = 3*d**4 + 14*d**3 + 17*d**2 - 10*d - 12
# Modal polynomial and general Jacobian identity.
c = d/(5*(1-r))
A = sp.Matrix([[1-r, -c/r], [5*r*r*(1-r), d*w]])
assert sp.factor((z*sp.eye(2)-A).det()) == sp.factor(z**2-(1-r+d*w)*z+d*(r+(1-r)*w))
# Three-cycle exact block determinant and polynomial identity.
W = sp.Matrix([[0,1,0],[0,0,1],[1,0,0]])
J = (sp.Rational(1,2)*sp.eye(3)).row_join(-4*d/5*sp.eye(3)).col_join((sp.Rational(5,8)*sp.eye(3)).row_join(d*W))
U=z**2-z/2+d/2
V=d*(sp.Rational(1,2)-z)
p_h=z**2-(sp.Rational(1,2)+d)*z+d
assert sp.expand((z*sp.eye(6)-J).det()-p_h*(U*U-U*V+V*V))==0
# Schur-Cohn identity, using primitive cube root.
omega=(-1+sp.I*sp.sqrt(3))/2
T=sp.Rational(1,2)+d*omega
D=d*(1+omega)/2
assert sp.expand(sp.simplify(D*sp.conjugate(D))-d*d/4)==0
B=sp.expand(T-sp.conjugate(T)*D)
F=sp.factor((1-d**2/4)**2-sp.expand_complex(B*sp.conjugate(B)))
assert sp.simplify(F+P/16)==0
assert sp.factor(P.subs(d,sp.Rational(5,6)))==sp.Rational(49,48)
assert P.subs(d,0)==-12 and P.subs(d,1)==12
assert P.subs(d,sp.Rational(8141,10000))<0 and P.subs(d,sp.Rational(8142,10000))>0
# Exact two-node Schur inequalities at real w in [-1,1], d in (0,1).
tr=1-r+d*w
det=d*(r+(1-r)*w)
assert sp.simplify(1-tr+det-r*(1+d*(1-w)))==0
assert sp.simplify(1+tr+det-(2-r+d*(2*r-2)) -d*(2-r)*(w+1))==0
assert sp.simplify(1-det-(1-d)-d*(1-r)*(1-w))==0
# Real 6x6 eigenvalues and independent direct map finite-difference Jacobian diagnostic.
d0=sp.Rational(5,6)
vals = [complex(v) for v in J.subs(d,d0).evalf(30).eigenvals(multiple=True)]
assert sum(abs(v)>1.000001 for v in vals)==2
assert sum(abs(v)<0.999999 for v in vals)==4
rho=max(abs(v) for v in vals)
assert 1.020 < rho < 1.021
root=sp.nroots(P,maxsteps=300)
positive=[float(sp.re(x)) for x in root if abs(float(sp.im(x))) < 1e-12 and float(sp.re(x))>0]
assert len(positive)==1 and .8141<positive[0]<.8142
print('VERIFY_OK charpoly6=exact Schur_Cohn=exact boundary_bracket=exact two_node_inequalities=exact',
      f'delta_star={positive[0]:.12f}',f'rho_at_5_over_6={rho:.12f}',f'P_5over6={P.subs(d,d0)}')

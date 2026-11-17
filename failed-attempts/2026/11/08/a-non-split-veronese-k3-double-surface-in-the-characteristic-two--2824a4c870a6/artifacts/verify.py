#!/usr/bin/env python3
"""Exact checks for the Jacobian double Veronese surface (characteristic two)."""
import sympy as sp
from math import comb
A,B,C,D,E,F=sp.symbols('a b c d e f')
variables=(A,B,C,D,E,F)
M=sp.Matrix([[A,D,E],[D,B,F],[E,F,C]])

def red(p):
    return sp.Poly(sp.expand(p),*variables,modulus=2).as_expr()

det=red(M.det())
assert det == red(A*B*C + A*F**2 + B*E**2 + C*D**2)
J=[red(sp.diff(det,x)) for x in variables]
assert J==[B*C+F**2,A*C+E**2,A*B+D**2,0,0,0]
assert red(A*J[0]+B*J[1]+C*J[2]+det)==0
Q=J[:3]
G=sp.groebner(Q,*variables,order='grevlex' if False else 'grlex', modulus=2)
minors=[A*F+D*E,B*E+D*F,C*D+E*F]
for x in minors:
    for y in minors:
        assert G.reduce(red(x*y))[1]==0, (x,y)
# In the affine chart a=1, eliminate b,c to get (f+d*e)^2=0.
x,y,z=sp.symbols('x y z')
chart=sp.groebner([B+D**2,C+E**2,B*C+F**2,A+1],A,B,C,D,E,F,order='lex',modulus=2)
assert chart.reduce(red((A*F+D*E)**2))[1]==0
# Explicit overlap a=1 and b=1. In a-chart write b=d^2, c=e^2, f=de+eps,
# and verify b-chart's nilpotent e/b+(d/b)(f/b) is eps/d^3.
u,v,eps=sp.symbols('u v eps', nonzero=True)
b0=u**2; d0=u; e0=v; f0=u*v+eps
new_eps=sp.cancel(e0/b0+(d0/b0)*(f0/b0))
assert sp.Poly(sp.cancel((new_eps-eps/u**3)*u**3),u,v,eps,modulus=2).is_zero
assert sp.simplify(f0/b0-v/u-eps/u**2)==0
# Complete-intersection Hilbert function; compare independently to doubled Veronese.
for m in range(15):
    Hci=sum((-1)**i*comb(3,i)*comb(m-2*i+5,5) for i in range(4) if m-2*i>=0)
    Hred=comb(2*m+2,2)
    Hnil=comb(2*m-1,2) if m>=2 else 0  # H^0(P2,O(2m-3)) for m>=2
    assert Hci==Hred+Hnil,(m,Hci,Hred,Hnil)
for m in range(2,15):
    Hci=sum((-1)**i*comb(3,i)*comb(m-2*i+5,5) for i in range(4) if m-2*i>=0)
    assert Hci==4*m*m+2
print('JACOBIAN_IDEAL_OK')
print('CUBIC_IN_JACOBIAN_OK')
print('NILRADICAL_PRODUCTS_OK')
print('AFFINE_RIBBON_CHART_OK')
print('OVERLAP_TRANSITION_OK')
print('HILBERT_FUNCTION_AND_POLYNOMIAL_OK')
print('ALL_CHECKS_PASSED')

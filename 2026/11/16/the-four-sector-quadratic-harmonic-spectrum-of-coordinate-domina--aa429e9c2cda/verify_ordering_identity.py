#!/usr/bin/env python3
"""Exact symbolic verification of the strict-sector-ordering algebra."""
import sympy as sp
m,b0,b1,c=sp.symbols('m b0 b1 c', real=True)
d=m+1
A=sp.Rational(3,1)/d+3*m*b0+m*b1
B=1/d+m*b0-b1
D=3/d-b1-3*b0
E=1/d-2*b0+c
# Concentration eigenvalues for the antipodal union.
z=(m*m*A-2*m*m*B+m*D+m*(m-1)*E)/(2*d*m)
mu=B
identity=((m*m+4*m+1)*(b1-b0)+(m-1)*c)/(2*d)
assert sp.simplify(z-mu-identity)==0
print('Symbolic ordering comparison: PASS')

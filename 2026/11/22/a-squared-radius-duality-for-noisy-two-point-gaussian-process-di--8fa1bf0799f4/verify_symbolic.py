"""Exact algebraic checks for the two-kernel conditional-variance theorem.

Dependency: sympy (for symbolic simplification); Python 3.
Run: python3 verify_symbolic.py
"""
import sympy as s

z, c = s.symbols('z c', positive=True)
eg = s.exp
G = 2*z*eg(-z)/(c-eg(-2*z))
M = 2*z*z*eg(-2*z)/(c-(1+2*z)*eg(-2*z))
common = c*(1-z)*eg(2*z)-(1+z)
assert s.simplify(s.diff(G, z)*(c-eg(-2*z))**2*eg(3*z)/2-common) == 0
assert s.simplify(s.diff(M, z)*(c-(1+2*z)*eg(-2*z))**2*eg(4*z)/(4*z)-common) == 0
critical_c = eg(-2*z)*(1+z)/(1-z)
assert s.simplify(G.subs(c, critical_c)-(1-z)*eg(z)) == 0
assert s.simplify(M.subs(c, critical_c)-(1-z)) == 0
assert s.simplify(s.diff(s.log((1+z)/(1-z)*eg(-2*z)), z)-2*z**2/(1-z**2)) == 0
print('Symbolic identities: PASS (5)')

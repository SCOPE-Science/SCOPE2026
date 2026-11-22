"""Reproducible auxiliary checks of the arithmetic and local formulas.

The geometric irreducibility and global monodromy are proved in RESULT.md,
not inferred from this finite symbolic calculation.
"""
from sympy import Matrix, symbols, diff, solve, expand, gcd

M=Matrix([[0,3],[3,2]])
e=Matrix([1,0]); h=Matrix([0,1]); ep=3*h-e
pair=lambda u,v: int((u.T*M*v)[0])
assert pair(e,e)==0 and pair(h,h)==2 and pair(e,h)==3
assert pair(ep,ep)==0 and pair(ep,h)==3
assert gcd(pair(e,e),pair(e,h)) == 3
assert gcd(pair(ep,e),pair(ep,h)) == 3
assert 3*(3-1)**2 == 12 and 2*12 == 24
# Arbitrarily prescribed two distinct points of P1 admit independent
# quadratic restrictions; the illustrative evaluation matrix has rank 2.
s,t=symbols('s t'); forms=[s*s,s*t,t*t]
E=Matrix([[f.subs({s:1,t:0}) for f in forms],
          [f.subs({s:0,t:1}) for f in forms]])
assert E.rank()==2
# The Morse critical value is epsilon+tau^2, with two exchanging roots.
y,z,tau,eps=symbols('y z tau eps')
local=y*y+z*z+2*tau*y+2*tau*tau+eps
critical=solve([diff(local,y),diff(local,z)],(y,z),dict=True)[0]
assert expand(local.subs(critical))==tau*tau+eps
assert expand(local.subs({y:-tau,z:0,eps:-tau*tau}))==0
print('PASS: lattice, degree-24, two-parameter first-jet ranks, local simple swap')

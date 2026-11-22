#!/usr/bin/env python3
"""Symbolic identities underlying the weighted two-clique controllability theorem."""
import sympy as s
p,q,a,b,t,z=s.symbols('p q a b t z')
Q=s.Matrix([
[a,-a,0,0],
[-(p-1)*a,(p-1)*a+t,-t,0],
[0,-t,(q-1)*b+t,-(q-1)*b],
[0,0,-b,b]
])
F=s.factor(Q.charpoly(z).as_expr())
expected=z*(z**3-(p*a+q*b+2*t)*z**2+(a*b*p*q+t*(a*(p+1)+b*(q+1)))*z-a*b*t*(p+q))
assert s.expand(F-expected)==0
assert s.factor(F.subs(z,p*a)) == -a**2*p*t*(p-1)*(a*p-b*q)
assert s.factor(F.subs(z,q*b)) == b**2*q*t*(q-1)*(a*p-b*q)
A=s.expand((p-1+z)*(q-1+z)*(1+z)**2-(p-1)*(q-1))
Z=z*(z**3+(p+q)*z**2+(p*q+p+q-2)*z+2*p*q-p-q)
assert s.expand(A-Z)==0
print('PASS: quotient characteristic polynomial, both resonance evaluations, and forcing-enumerator identity')

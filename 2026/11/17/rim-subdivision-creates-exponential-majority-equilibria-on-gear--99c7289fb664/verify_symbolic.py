#!/usr/bin/env python3
"""Symbolic diagnostic of the weighted no-101 transfer identity."""
import sympy as sp
z, t, l = sp.symbols('z t l')
T = sp.Matrix([[1,z,0,0],[0,0,1,z],[1,0,0,0],[0,0,1,z]])
assert sp.expand((sp.eye(4)-t*T).det() - (1-(1+z)*t+z*t**2-z*t**3)) == 0
f = l**3-(1+z)*l**2+z*l-z
m_num = l**2-l+1
m_den = l*(3*l**2-4*l+1)
assert sp.rem(sp.expand(m_den-2*m_num),l**3-2*l**2+l-1,l)==1
roots=sp.nroots(l**3-2*l**2+l-1)
lam=max(float(sp.re(r)) for r in roots)
m=(lam**2-lam+1)/(lam*(3*lam**2-4*lam+1))
assert 0<m<0.5
print('PASS exact transfer determinant')
print('PASS density identity 1-2m=1/[lambda(3lambda^2-4lambda+1)]')
print('Perron root approx %.15f'%lam)
print('Typical one-density approx %.15f'%m)

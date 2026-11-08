#!/usr/bin/env python3
"""Build paired de Bruijn transfer matrix; exact characteristic polynomial and spectral constants."""
import sympy as S
from math import pi, sqrt
z,t=S.symbols('z t')
rule=184
f=lambda a,b,c:(rule >> (4*a+2*b+c))&1
pair=lambda q:((q>>1)&1,q&1)
T=S.zeros(16)
for u in range(4):
    for v in range(4):
        for w in range(4):
            U,V,W=pair(u),pair(v),pair(w)
            if f(U[0],V[0],W[0])==f(U[1],V[1],W[1]):
                T[4*u+v,4*v+w]=z**V[0]
D=S.factor(T.charpoly(t).as_expr())
expected=t**10*(t**2+z)*(t**4-(1+z)*t**3-z*t**2+z*(z+1)*t-2*z**2)
assert S.expand(D-expected)==0
print('CHARPOLY_OK',S.factor(D))
# Independent direct transfer trace test (not using root recursion).
traces=[S.trace(T**n).expand() for n in range(1,10)]
expected_first=[1+z,(1+z)**2,(1+z)**3,1+4*z+18*z*z+4*z**3+z**4]
for n in range(1,5):assert S.expand(traces[n-1]-expected_first[n-1])==0
print('TRANSFER_TRACE_OK first9',[(n, tr.subs(z,1)) for n,tr in enumerate(traces,1)])
# Check symmetry as exact polynomial identity for n<=9
for n,tr in enumerate(traces,1):
    assert S.simplify(tr-z**n*tr.subs(z,1/z))==0
print('REFLECTION_COMPLEMENT_OK n=1..9')
lam=.5+sqrt(5/4+sqrt(3))
var=(lam**2-1)/(4*(2*lam-1)*(lam**2-lam-1))
assert 0<var<.25
print('PF_CONSTANTS',format(lam,'.15f'),format(var,'.15f'),'unconditional_base',format(lam/4,'.15f'))

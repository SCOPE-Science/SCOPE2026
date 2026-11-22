#!/usr/bin/env python3
"""Exact algebra checks for a three-crosscap SL2 character variety.
Requires SymPy. Symbolic identities complement, rather than replace, the proof.
Run: python VERIFY.py
"""
import sympy as sp

a,b,c,s,t=sp.symbols('a b c s t')
I=sp.I
E=sp.eye(2)
F=2*a*a+2*b*b+2*c*c-a*b*c*s-8

# Every triple of pair traces (a,b,p) has a realization: vary t.
A=sp.Matrix([[a,-1],[1,0]])
B=sp.Matrix([[b-t,1],[(b-t)*t-1,t]])
assert sp.factor(A.det()-1)==0 and sp.factor(B.det()-1)==0
p=sp.factor(sp.trace(A*B))
assert sp.factor(p-((a-t)*(b-t)+2))==0
D=sp.simplify((A*A*B*B).inv())
d=sp.factor(sp.trace(D)+2)
assert sp.factor(d-(a*b*p-a*a-b*b+4))==0
assert all(sp.factor(v)==0 for v in (D+E)*(D+E)-d*D)
# With C=(D+I)/c and c^2=d, check recovered traces.
assert sp.factor(sp.trace((A*B)*(D+E))-2*p)==0
assert sp.factor(sp.trace(B*(D+E))-a*p)==0
assert sp.factor(sp.trace((D+E)*A)-b*p)==0

# Global rank-three Fricke trace relation specialized to (a,b,c,s).
P=c*s/2; Q=a*s/2; R=b*s/2
reverse=P*c+Q*a+R*b-a*b*c-s
product=a*a+b*b+c*c+P*P+Q*Q+R*R-a*b*P-b*c*Q-c*a*R+P*Q*R-4
assert sp.factor(s*reverse-product)==sp.factor((s*s-4)*F/8)

# Boundary parameterization: a^2+b^2=4, Z^2=C^2=-I.
Z=sp.diag(I,-I)
C0=sp.Matrix([[t,1],[-1-t*t,-t]])
A0=(a*E+b*Z)/2; B0=(b*E+a*Z)/2
conic=a*a+b*b-4
assert sp.simplify(C0.det()-1)==0
assert C0*C0==-E
assert Z*Z==-E

def modulo_conic(expr):
    num=sp.together(sp.expand(expr)).as_numer_denom()[0]
    return sp.Poly(num,b).rem(sp.Poly(conic,b)).as_expr().expand()
for expr in [A0.det()-1,B0.det()-1,*(A0*B0-Z),*(A0*A0*B0*B0+E)]:
    assert modulo_conic(expr)==0,expr
s0=sp.trace(A0*B0*C0)
assert modulo_conic(s0-2*I*t)==0
assert modulo_conic(sp.trace(B0*C0)-a*s0/2)==0
assert modulo_conic(sp.trace(C0*A0)-b*s0/2)==0
assert modulo_conic(sp.trace(A0*B0))==0
# Geometric smoothness: equations F=grad F=0 generate the unit ideal.
G=sp.groebner([F,*[sp.diff(F,x) for x in (a,b,c,s)]],a,b,c,s)
assert list(G)==[1]
# The coordinate conic is Gm: u=(a+i b)/2, v=(a-i b)/2, uv=1.
assert modulo_conic(((a+I*b)/2)*((a-I*b)/2)-1)==0
print('PASS: trace identities, boundary parametrization, Fricke relation, smoothness.')

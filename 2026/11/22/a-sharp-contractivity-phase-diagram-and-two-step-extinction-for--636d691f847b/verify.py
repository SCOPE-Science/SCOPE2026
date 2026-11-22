#!/usr/bin/env python3
"""Reproducible algebraic and finite checks for a nilpotent-noise theta-Maruyama test."""
import random
import sympy as sp

h,t,g,s=sp.symbols('h t g s', real=True)
N=sp.Matrix([[0,1],[0,0]])
I=sp.eye(2)
A=-I+g*N
B=s*N
D=I-t*h*A
C=sp.simplify(D.inv()*(I+(1-t)*h*A))
E=sp.simplify(D.inv()*B)
d=1+t*h
r=(1-(1-t)*h)/d
m=g*h/d**2
v=s**2*h/d**2
c=2+(2*t-1)*h
G=sp.simplify(C.T*C+h*E.T*E)
expected=sp.Matrix([[r**2,r*m],[r*m,r**2+m**2+v]])
assert all(sp.factor(e)==0 for e in G-expected)
assert sp.factor((I-G)[0,0]-h*c/d**2)==0
assert sp.factor((I-G).det()-h**2*(c**2-s**2*c-g**2)/d**4)==0
assert sp.simplify(C-r*I-m*N)==sp.zeros(2)
assert sp.simplify(E-s/d*N)==sp.zeros(2)
# The numerical step annihilates the whole state in two moves at r=0.
for t0 in [sp.Rational(0),sp.Rational(1,3),sp.Rational(1,2),sp.Rational(3,4)]:
    h0=1/(1-t0)
    b0,b1=sp.symbols('b0 b1', real=True)
    assert sp.simplify((r*I+b0*N).subs({h:h0,t:t0})*(r*I+b1*N).subs({h:h0,t:t0}))==sp.zeros(2)
# Rational sampling checks the analytic determinant and PSD phase classification.
rng=random.Random(20261120)
num=0
for _ in range(600):
    t0=sp.Rational(rng.randrange(0,9),8)
    h0=sp.Rational(rng.randrange(1,100),20)
    g0=sp.Rational(rng.randrange(0,35),10)
    s0=sp.Rational(rng.randrange(0,35),10)
    z={t:t0,h:h0,g:g0,s:s0}
    M=G.subs(z)
    C0=c.subs(z)
    # Scalar threshold can be expressed without radicals as c>=0 and c^2-s^2c-g^2>=0.
    rhs=C0>=0 and C0*C0-s0*s0*C0-g0*g0>=0
    H=I-M
    lhs=H[0,0]>=0 and H[1,1]>=0 and H.det()>=0
    assert bool(lhs)==bool(rhs), z
    num+=1
# Exact witness: Euler step can expand by factor 116 yet annihilates in two steps.
z={t:0,h:1,g:10,s:4}
assert G.subs(z)==sp.diag(0,116)
assert C.subs(z)==10*N and E.subs(z)==4*N
print('PASS: 5 general symbolic identities; 4 exact two-step identities; '
      f'{num} rational PSD comparisons; exact 116-to-zero witness')

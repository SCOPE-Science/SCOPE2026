#!/usr/bin/env python3
"""Exact algebraic checks for the sparse circular Fourier-gap theorem.

Requires Python 3.10+ and SymPy 1.12+. This checks the finite algebraic
certificate; the accompanying proof treats all positive measures.
"""
import sympy as s

x = s.symbols('x')
S = 3*s.sqrt(30)/20
h = s.sqrt(5)/10
R = s.sqrt(14)/4
c = -S+h
b = (S-R)/2
d = (S+R)/2
nodes = (c,b,d)

# The dual polynomial is nonnegative on [c,1].
P = s.expand((x*x-S*x-s.Rational(1,20))**2 *
             (x*x+2*S*x+s.Rational(5,8)))
T = s.chebyshevt
P_fourier = T(6,x)/32-s.Rational(21,640)*T(2,x)+81*s.sqrt(30)*x/8000
assert s.simplify(P-P_fourier)==0
assert s.simplify(P-(x-c)*(x+S+h)*(x-b)**2*(x-d)**2)==0

# Certified radical inequalities: e<-1<c<b<0<d<1.
e = -S-h
for val in (-1-e,c+1,b-c,-b,d,1-d):
    assert s.simplify(val).is_positive is True

# Quadrature weights solve the first three real moments.
w = []
for i in range(3):
    other = [nodes[j] for j in range(3) if i!=j]
    a,z = other
    wi = s.simplify((s.Rational(1,2)+a*z)/((nodes[i]-a)*(nodes[i]-z)))
    assert wi.is_positive is True
    w.append(wi)
for m,expected in enumerate((1,0,s.Rational(1,2))):
    assert s.simplify(sum(wi*xi**m for wi,xi in zip(w,nodes))-expected)==0
assert s.simplify(sum(wi*T(6,xi) for wi,xi in zip(w,nodes)))==0

# The odd sine Fourier constraints force reflection symmetry.
U = s.chebyshevu(5,x)
divided = s.simplify(sum(U.subs(x,nodes[i]) /
       s.prod(nodes[i]-nodes[j] for j in range(3) if j!=i)
       for i in range(3)))
expected = s.Rational(8,5)*(9*h-S)
assert s.simplify(divided-expected)==0
assert s.simplify(expected).is_positive is True

# The first two moments alone do not vanish on support {b,d}.
assert s.simplify(b*d+s.Rational(1,20))==0
assert s.simplify(s.Rational(1,2)+b*d)==s.Rational(9,20)

print('CHECK_OK Fourier_identity=exact roots=exact weights=positive '
      'moments_0_1_2_6=exact sine_rank=3')

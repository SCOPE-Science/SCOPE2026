"""Exact symbolic and sampled cross-checks for four-site natural spline stability.

Requires Python 3 and SymPy 1.14 (or a compatible version).
"""
from fractions import Fraction
import sympy as s

r, t = s.symbols('r t', positive=True)
y = s.symbols('y0:4')
M1, M2 = s.symbols('M1 M2')
h = [s.Integer(1), r, s.Integer(1)]
A = s.Matrix([[2*(1+r),r],[r,2*(1+r)]])
b = 6*s.Matrix([(y[2]-y[1])/r-(y[1]-y[0]), (y[3]-y[2])-(y[2]-y[1])/r])
assert s.factor(A.det()) == (r+2)*(3*r+2)
U = A.inv()*b
M = [s.Integer(0), U[0], U[1], s.Integer(0)]

piece = []
for j in range(3):
    g = (1-t)*y[j] + t*y[j+1] + h[j]**2/s.Integer(6)*(
        M[j]*((1-t)**3-(1-t)) + M[j+1]*(t**3-t))
    piece.append([s.factor(s.diff(g,v)) for v in y])

expected_outer = [
 (1-t)*(3*r**2+8*r+4-2*(r+1)*(t+t*t))/((r+2)*(3*r+2)),
 t*(3*r**2+4*r+1-(2*r+1)*t*t)/(r*(3*r+2)),
 t*(r+1)*(t*t-1)/(r*(3*r+2)),
 r*t*(1-t*t)/((r+2)*(3*r+2))]
for observed, expected in zip(piece[0], expected_outer):
    assert s.factor(observed-expected) == 0

expected_center_0 = -r*r*t*(1-t)*((3*r+4)-(3*r+2)*t)/((r+2)*(3*r+2))
expected_center_3 = -r*r*t*(1-t)*((3*r+2)*t+2)/((r+2)*(3*r+2))
assert s.factor(piece[1][0]-expected_center_0)==0
assert s.factor(piece[1][3]-expected_center_3)==0
assert s.factor(piece[1][0]+piece[1][3]+3*r*r*t*(1-t)/(3*r+2))==0
assert all(s.factor(sum(p)-1)==0 for p in piece)

O=1+4*(r+1)/(3*s.sqrt(3)*r*(3*r+2))
C=1+3*r*r/(2*(3*r+2))
assert s.factor(1-2*expected_outer[2].subs(t,1/s.sqrt(3))-O)==0
assert s.factor(1-2*(piece[1][0]+piece[1][3]).subs(t,s.Rational(1,2))-C)==0
assert s.simplify(s.diff(O,r)+4*s.sqrt(3)*(3*r*r+6*r+2)/(9*r*r*(3*r+2)**2))==0
assert s.factor(s.diff(C,r)-3*r*(3*r+4)/(2*(3*r+2)**2))==0
assert s.factor((C-O)*6*s.sqrt(3)*r*(3*r+2)-s.sqrt(3)*(27*r**3-8*s.sqrt(3)*(r+1))/3)==0

# Separate exact rational interpolation reconstruction at many node/gap pairs.
# This test is intentionally finite; the symbolic identities and sign proof give the theorem.
count=0
for rv in [s.Rational(1,13),s.Rational(1,3),s.Rational(1,2),s.Integer(1),s.Rational(101,100),s.Rational(3,2),s.Integer(2),s.Integer(9)]:
    for tv in [s.Rational(k,18) for k in range(19)]:
        for j in range(3):
            nodal=[s.Rational(i*i-3*i+1,7) for i in range(4)]
            full=sum(piece[j][i].subs({r:rv,t:tv})*nodal[i] for i in range(4))
            direct=((1-tv)*nodal[j]+tv*nodal[j+1]
                +h[j].subs(r,rv)**2/s.Integer(6)*(
                M[j].subs(dict(zip(y,nodal))).subs(r,rv)*((1-tv)**3-(1-tv))
                + M[j+1].subs(dict(zip(y,nodal))).subs(r,rv)*(tv**3-tv)))
            assert s.factor(full-direct)==0
            count+=1

root=s.nsolve(9*s.sqrt(3)*r**3-8*(r+1),1)
assert s.Abs(O.subs(r,root)-C.subs(r,root)) < s.Rational(1,10**12)
assert s.Abs(root-s.Float('1.01048320579748')) < s.Rational(1,10**12)
print('PASS: exact spline cardinal, sign-factor inputs, maxima and unique crossing identities')
print(f'PASS: {count} independent exact rational interpolation reconstructions')
print(f'optimal ratio: {root.evalf(16)}')
print(f'optimal norm: {C.subs(r,root).evalf(16)}')
print(f'equal-spaced norm: {O.subs(r,1).evalf(16)}')

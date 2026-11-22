#!/usr/bin/env python3
"""Exact rational certificate for a two-patch resident–traveller SVIRS threshold.

Requires Python >=3.9 and sympy. No network or external data is needed.
"""
from sympy import Matrix, Rational, eye, zeros, diag, symbols, simplify, together, factor

x = symbols('t', real=True)
q = Rational

def movement(a, b):
    return Matrix([[-a, b], [a, -b]])

MS1 = movement(q(1,10), q(2))
MV1 = movement(q(2), q(1,10))
M2 = movement(q(2), q(1,10))
assert MS1[1,0] > 0 and MS1[0,1] > 0
assert MV1[1,0] > 0 and MV1[0,1] > 0

S1 = simplify((1-x)*(eye(2)-MS1).inv()*Matrix([1,0]))
V1 = simplify(x*(eye(2)-MV1).inv()*Matrix([1,0]))
S2 = (eye(2)-M2).inv()*Matrix([0,1])
assert S1 == Matrix([30*(1-x)/31, (1-x)/31])
assert V1 == Matrix([11*x/31, 20*x/31])
assert S2 == Matrix([q(1,31), q(30,31)])

Np = [factor(S1[j]+V1[j]+S2[j]) for j in range(2)]
assert all(simplify(Np[j]-[(31-19*x)/31,(31+19*x)/31][j])==0 for j in range(2))
W = diag(2*eye(2)-MV1, 2*eye(2)-M2)
Winv = W.inv()
assert Winv[:2,:2] == Matrix([[q(21,82),q(1,82)], [q(10,41),q(20,41)]])
assert max(sum(Winv[i,j] for j in range(4)) for i in range(4)) == q(30,41)

F = zeros(4)
F0 = zeros(4)
for i in range(2):
    for k in range(2):
        for j in range(2):
            susceptibility = [S1,S2][i][j] + q(1,2)*[V1,zeros(2,1)][i][j]
            f0 = q(1,20)*susceptibility/Np[j]
            F0[2*i+j,2*k+j] = f0
            F[2*i+j,2*k+j] = (q(16) if (i,k,j)==(0,0,1) else q(1,20))*susceptibility/Np[j]

hot = (1+9*x)/(31+19*x)
assert simplify(F[1,1]-16*hot) == 0
assert simplify(F[1,1]-F0[1,1]-q(319,20)*hot) == 0
assert F[1,3] == F0[1,3]
assert all(simplify((F-F0)[i,j])==0 for i in range(4) for j in range(4) if (i,j)!=(1,1))

P=2448016069*x**3-1215675371*x**2-6337116745*x+2889002747
expected=P/(2000*(31-19*x)*(31+19*x)**2)
assert simplify((W-F).det()-expected)==0
assert P.subs(x,q(9,20)) == q(113611307281,8000)
assert P.subs(x,q(23,50)) == -q(5628471513927,125000)
assert P.diff(x).subs(x,0)<0 and P.diff(x).subs(x,1)<0
assert simplify((W-F).det().subs(x,0))>0
assert simplify((W-F).det().subs(x,q(1,2)))<0
assert 2*q(1,20)*q(30,41)==q(3,41)<1
print('PASS: exact DFE, positive-rate matrices, hotspot rank one, determinant polynomial, strict unique-root signs, and M-matrix small-contact bound')

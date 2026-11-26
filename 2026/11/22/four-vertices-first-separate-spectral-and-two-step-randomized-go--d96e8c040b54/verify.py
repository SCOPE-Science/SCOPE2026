"""Symbolic and supplementary numerical checks for finite-horizon pairwise averaging."""
from __future__ import annotations
import random
import sympy as s

I4 = s.eye(4)
W = []
for k in range(3):
    e = s.zeros(4, 1)
    e[k] = 1
    e[k + 1] = -1
    W.append(I4 - e * e.T / 2)
assert all(X * X == X for X in W)
assert all(X * s.ones(4, 1) == s.ones(4, 1) for X in W)

b, d = s.symbols('b d', real=True)
p = [(1-b)/2+d, b, (1-b)/2-d]
M2 = sum((p[i]*p[j]*W[i]*W[j]*W[i] for i in range(3) for j in range(3)),s.zeros(4))
M1 = sum((p[i]*W[i] for i in range(3)),s.zeros(4))
R = s.zeros(4)
for i in range(4): R[i,3-i]=1
D1=s.Matrix([1,-1,0,0]);D3=s.Matrix([0,0,1,-1])
C=(D1*D1.T+D3*D3.T)/2
Ms = s.simplify(M2.subs(d,0))
assert s.simplify((M2+R*M2*R)/2-Ms-d*d*C)==s.zeros(4)
assert s.simplify(M2.subs(d,-d)-R*M2*R)==s.zeros(4)

T=s.Matrix.hstack(s.Matrix([1,0,0,-1])/s.sqrt(2),s.Matrix([0,1,-1,0])/s.sqrt(2),s.Matrix([1,-1,-1,1])/2)
assert s.simplify(T.T*T)==s.eye(3)
assert s.simplify(T.T*s.ones(4,1))==s.zeros(3,1)
A=s.Matrix([[3*b*b+3*b+10,5*b*b-11*b+6],
            [5*b*b-11*b+6,7*b*b-17*b+10]])/16
S=(3*b*b+3*b+2)/8
assert s.simplify(T.T*Ms*T-s.diag(A[0,0],A[1,1],S) - s.Matrix([[0,A[0,1],0],[A[1,0],0,0],[0,0,0]]))==s.zeros(3)
assert s.simplify(A[0,0]-S-3*(1-b)*(b+2)/16)==0
assert s.simplify(A[0,0]-A[1,1]-b*(5-b)/4)==0
assert s.simplify(A[0,1]-(1-b)*(6-5*b)/16)==0
Q=29*b**4-150*b**3+281*b*b-132*b+36
F=(5*b*b-7*b+10+s.sqrt(Q))/16
assert s.simplify((A.trace()+s.sqrt((A[0,0]-A[1,1])**2+4*A[0,1]**2))/2-F)==0
assert s.diff(F,b).subs(b,0)==-s.Rational(9,8)
assert s.diff(F,b).subs(b,1)==s.Rational(9,16)
assert s.simplify(F.subs(b,s.Rational(2,5))-s.Rational(1,2)-s.sqrt(754)/100)==0
P6=116*b**6-1760*b**5+8175*b**4-18554*b**3+18203*b*b-6396*b+648
assert s.simplify(4*s.diff(A.trace(),b)**2*((A[0,0]-A[1,1])**2+4*A[0,1]**2) - s.diff((A[0,0]-A[1,1])**2+4*A[0,1]**2,b)**2 + P6/256)==0
lo, hi = s.Rational(39,100), s.Rational(2,5)
assert 7 - 10*hi > 0 and -450*hi**2+562*lo-132 > 0
assert s.expand(s.diff(Q,b)**2 - 4*(7-10*b)**2*Q - 16*P6) == 0
assert P6.subs(b,lo) < 0 < P6.subs(b,hi)

# The one-round extremal mode belongs to the antisymmetric sector.
As1=s.simplify((T.T*M1.subs(d,0)*T)[:2,:2]); S1=s.simplify((T.T*M1.subs(d,0)*T)[2,2])
assert s.simplify(As1-s.Matrix([[(b+3)/4,(1-b)/4],[(1-b)/4,3*(1-b)/4]]))==s.zeros(2)
assert s.simplify(S1-(1+b)/2)==0
F1=(3-b+s.sqrt(5*b*b-2*b+1))/4
assert s.simplify((As1.trace()+s.sqrt((As1[0,0]-As1[1,1])**2+4*As1[0,1]**2))/2-F1)==0
assert s.simplify(s.diff(F1,b).subs(b,s.Rational(2,5)))==0
assert s.simplify(F1.subs(b,s.Rational(2,5))-s.Rational(9,10))==0

# Minimality: on P3 the reflected two-round average differs by d^2 times a positive operator.
I3=s.eye(3); U=[]
for i in range(2):
 e=s.zeros(3,1);e[i]=1;e[i+1]=-1;U.append(I3-e*e.T/2)
q=[s.Rational(1,2)+d,s.Rational(1,2)-d]
N2=sum((q[i]*q[j]*U[i]*U[j]*U[i] for i in range(2) for j in range(2)),s.zeros(3))
R3=s.Matrix([[0,0,1],[0,1,0],[1,0,0]])
C3=s.simplify((N2+R3*N2*R3).subs(d,1)/2-N2.subs(d,0))
assert s.simplify((N2+R3*N2*R3)/2-N2.subs(d,0)-d*d*C3)==s.zeros(3)
assert C3.eigenvals()=={s.Rational(9,8):1,s.Rational(3,8):1,s.Integer(0):1}

# Numerics are supplemental: compare the nine ordered two-draw outcomes with the analytic factor.
import numpy as np
from scipy.optimize import brentq
Ws=[np.array(X,dtype=float) for X in W]
J=np.ones((4,4))/4
FN=s.lambdify(b,F,'numpy'); FPN=s.lambdify(b,s.diff(F,b),'numpy')
root=brentq(FPN,0.39,0.4,xtol=5e-15)
assert abs(root-0.3943218483533838)<1e-12
assert abs(FN(root)-0.774552853191494)<1e-12
assert FN(.4)>FN(root)
for _ in range(300):
    pp=np.random.default_rng(_).dirichlet(np.ones(3))
    direct=sum(pp[i]*pp[j]*Ws[i]@Ws[j]@Ws[i] for i in range(3) for j in range(3))
    factors=np.linalg.eigvalsh(direct-J)
    assert factors[0]>-1e-12
    assert factors[-1]>=FN(root)-1e-11
    bb=float(pp[1]); dd=float((pp[0]-pp[2])/2)
    symm=sum(v*Ws[i]@Ws[j]@Ws[i] for i in range(3) for j in range(3)
              for v in [([((1-bb)/2),bb,((1-bb)/2)][i])*([((1-bb)/2),bb,((1-bb)/2)][j])])
    assert np.linalg.eigvalsh(symm-J)[-1] >= FN(root)-1e-11
print('PASS symbolic identities, P3 minimality, one-step contrast and 300 randomized two-round checks')
print('two-round unique center probability:', format(root,'.15f'))
print('sharp two-round expected squared disagreement:', format(FN(root),'.15f'))
print('one-round-optimized two-round error:',format(FN(.4),'.15f'))

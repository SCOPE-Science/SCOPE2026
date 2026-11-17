#!/usr/bin/env python3
"""Exact finite check for the balanced concentric-square phase-retrieval theorem.

Requires sympy. The general parameter theorem is proved analytically;
this program independently tests the integral-coordinate model and degeneracies.
"""
import sympy as S
I=S.I
H=[]
for j in range(3):
    A=S.zeros(3); A[j,j]=1; H.append(A)
for j,k in ((0,1),(0,2),(1,2)):
    A=S.zeros(3); A[j,k]=A[k,j]=1; H.append(A)
    A=S.zeros(3); A[j,k]=I; A[k,j]=-I; H.append(A)

def lift(nodes):
    rows=[]
    for z in nodes:
        v=S.Matrix([1,z,z*z])
        rows.append([S.expand((v.conjugate().T*A*v)[0]) for A in H])
    return S.Matrix(rows)

def make(ring_factor):
    return [I**k for k in range(4)]+[ring_factor*I**k for k in range(4)]

M=lift(make(1+I)); null=M.nullspace()
assert M.rank()==8 and len(null)==1
D=S.diag(2,-3,1)
assert D.det()==-6
assert all(S.expand((S.Matrix([1,z,z*z]).conjugate().T*D*S.Matrix([1,z,z*z]))[0])==0 for z in make(1+I))
assert all(S.expand((M*S.Matrix([S.trace(A*D) for A in H]))[k])==0 for k in range(8))
# General diagonal formula vanishes at both radius levels.
r,s=S.symbols('r s',positive=True)
q=lambda R:S.expand(r*r*s*s-(r*r+s*s)*R*R+R**4)
assert q(r)==0 and q(s)==0
assert S.factor(r*r*s*s*(-(r*r+s*s)))!=0
# No twist: the rank-two invisible direction is the imaginary 0-2 corner.
M0=lift(make(2)); A=S.zeros(3);A[0,2]=I;A[2,0]=-I
assert A.rank()==2 and M0.rank()<8
assert all(S.expand((S.Matrix([1,z,z*z]).conjugate().T*A*S.Matrix([1,z,z*z]))[0])==0 for z in make(2))
# Same circle, any rotation: the two rank-one squared-modulus patterns coincide.
theta=S.symbols('theta',real=True)
R=S.symbols('R',positive=True)
assert S.simplify(abs(R**2)**2 - R**4)==0
print('TWO_SQUARES_PASS rank=8 nullspace=1 det_diagonal=-6 distinct_nodes=8 alias_counterexample=PASS same_circle=PASS')

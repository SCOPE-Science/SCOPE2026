#!/usr/bin/env python3
"""Exact arithmetic checks for the two-row relaxed Kaczmarz horizon theorem.

Uses Python's standard library only. The universal statement is established by
its analytic proof, not by this finite collection of checks.
"""
from fractions import Fraction as F

Z=F(0); O=F(1)

def add(A,B):
    return tuple(tuple(A[i][j]+B[i][j] for j in range(2)) for i in range(2))

def sub(A,B):
    return tuple(tuple(A[i][j]-B[i][j] for j in range(2)) for i in range(2))

def mul(A,B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)) for i in range(2))

def scale(A,v):
    return tuple(tuple(v*A[i][j] for j in range(2)) for i in range(2))

def trans(A):
    return tuple(tuple(A[j][i] for j in range(2)) for i in range(2))

def qform(A,x):
    return sum(x[i]*A[i][j]*x[j] for i in range(2) for j in range(2))

def M2(U,V):
    T=(U,V)
    return scale(sum_matrices(tuple(mul(trans(mul(B,A)),mul(B,A)) for A in T for B in T)),F(1,4))

def sum_matrices(mats):
    R=((Z,Z),(Z,Z))
    for A in mats:R=add(R,A)
    return R

def model(c,s,d):
    assert c>0 and s>0 and c*c+s*s==1 and 0<d<1
    U=((s*s,-c*s),(-c*s,c*c))
    V=((-d,Z),(Z,O))
    V0=((Z,Z),(Z,O))
    Mdelta=M2(U,V); Mbase=M2(U,V0)
    D=sub(Mdelta,Mbase)
    formula=scale(((d*d*(s*s*(1+s*s)+d*d), c*s*d*(1-s*s*d)),
                   (c*s*d*(1-s*s*d),c*c*s*s*d*d)),F(1,4))
    assert D==formula,(D,formula)
    determinant=D[0][0]*D[1][1]-D[0][1]**2
    assert determinant==-c*c*s*s*d*d*(1-2*s*s*d-s*s*d*d-d**4)/16
    assert D[0][0]+D[1][1]==d*d*(2*s*s+d*d)/4
    # Directly check the exact one-step identity for independent sampling.
    Qdelta=scale(add(mul(U,U),mul(V,V)),F(1,2))
    Qbase=scale(add(mul(U,U),mul(V0,V0)),F(1,2))
    assert sub(Qdelta,Qbase)==((d*d/2,Z),(Z,Z))
    return D,determinant

cases=0; indefinite=0; nonnegative=0
for den in range(2,15):
    for num in range(1,den):
        t=F(num,den)
        c=(1-t*t)/(1+t*t)
        s=2*t/(1+t*t)
        for j in range(1,20):
            d=F(j,20)
            D,det=model(c,s,d)
            cases+=1
            if det<0: indefinite+=1
            else: nonnegative+=1

c=F(3,5);s=F(4,5);d=F(1,4)
D,det=model(c,s,d)
assert det==-F(36639,64000000)
e=(-O,O)
assert qform(D,e)==-F(18831,640000)
U=((s*s,-c*s),(-c*s,c*c))
V=((-d,Z),(Z,O));V0=((Z,Z),(Z,O))
Mbase=M2(U,V0);Mdelta=M2(U,V)
assert qform(Mbase,e)==F(629,625)
assert qform(Mdelta,e)==F(125053,128000)
Qdelta=scale(add(mul(U,U),mul(V,V)),F(1,2))
Qbase=scale(add(mul(U,U),mul(V0,V0)),F(1,2))
assert qform(Qbase,e)==F(37,25)
assert qform(Qdelta,e)==F(1209,800)
print('VERIFY_OK exact_two_step_matrix_cases=%d indefinite_cases=%d nonnegative_cases=%d witness_determinant=true witness_first_step=true witness_second_step=true' %(cases,indefinite,nonnegative))

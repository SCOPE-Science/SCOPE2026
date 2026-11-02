#!/usr/bin/env python3
from fractions import Fraction

def matvec(A, x):
    return [sum(a*b for a,b in zip(row,x)) for row in A]

def dot(x,y):
    return sum(a*b for a,b in zip(x,y))

def sub_outer(A, u, tau):
    n=len(A)
    return [[A[i][j]-u[i]*u[j]/tau for j in range(n)] for i in range(n)]

def check_cov(A):
    n=len(A)
    one=[Fraction(1) for _ in range(n)]
    u=matvec(A,one)
    tau=dot(one,u)
    assert tau>0
    beta=[v/tau for v in u]
    assert sum(beta)==1
    C=sub_outer(A,u,tau)
    assert matvec(C,one)==[0]*n
    return u,beta,C

A=[
    [Fraction(2),Fraction(-1,2),Fraction(1,4)],
    [Fraction(-1,2),Fraction(3),Fraction(1,4)],
    [Fraction(1,4),Fraction(1,4),Fraction(2)]
]
u,beta,C=check_cov(A)
assert all(x>0 for x in u)

B=[
    [Fraction(1),Fraction(-3,2)],
    [Fraction(-3,2),Fraction(4)]
]
uB,betaB,CB=check_cov(B)
assert uB==[Fraction(-1,2),Fraction(5,2)]
assert betaB[0]==Fraction(-1,4)
assert betaB[1]==Fraction(5,4)

rho=Fraction(-2,5)
E=[
    [Fraction(1) if i==j else rho for j in range(3)]
    for i in range(3)
]
uE,betaE,CE=check_cov(E)
assert uE==[Fraction(1,5)]*3
assert betaE==[Fraction(1,3)]*3
assert [sum(E[i][j] for j in range(3) if j!=i) for i in range(3)] == [Fraction(-4,5)]*3
assert 1+2*rho == Fraction(1,5) > 0
assert 1-rho == Fraction(7,5) > 0

print(
    "VERIFY_OK "
    f"equicorr_beta={float(betaE[0]):.12f} "
    f"negative_row_beta={float(betaB[0]):.12f}"
)

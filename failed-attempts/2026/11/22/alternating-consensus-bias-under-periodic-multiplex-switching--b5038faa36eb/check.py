"""Exact rational checks for periodic two-layer averaging (public scientific reproduction)."""
from fractions import Fraction as F

W1=((0,1,1),(1,0,1),(1,1,0))
W2=((0,2,1),(2,0,1),(1,1,0))

def transition(W):
    return [[F(x,sum(row)) for x in row] for row in W]

def prod(A,B):
    return [[sum((A[i][t]*B[t][j] for t in range(len(A))),F(0)) for j in range(len(A))] for i in range(len(A))]

def power(A,k):
    n=len(A);R=[[F(int(i==j)) for j in range(n)] for i in range(n)]
    for _ in range(k):R=prod(R,A)
    return R

def left(u,P):
    return [sum((u[i]*P[i][j] for i in range(len(u))),F(0)) for j in range(len(u))]

def invariant(p,P):
    assert left(p,P)==p
    assert all(v>=0 for v in p) and sum(p)==1

A=transition(W1);B=transition(W2)
u=[F(1,3)]*3
invariant(u,A)
invariant([F(3,8),F(3,8),F(1,4)],B)
for k in range(1,32):
    r=F(-1,2)**k
    C=prod(B,power(A,k))
    expected=[[F(1,3)+r*(B[i][j]-F(1,3)) for j in range(3)] for i in range(3)]
    assert C==expected
    pi=[F(2)+r,F(2)+r,F(2)]
    pi=[pi[0]/(2*(3+r)),pi[1]/(2*(3+r)),F(1)/(3+r)]
    invariant(pi,C)
    assert (pi[2]>F(1,3))==(k%2==1)
    assert F(1,4)<pi[2]<F(1,2)
    assert (pi[2]>F(1,3)) if k%2 else (F(1,4)<pi[2]<F(1,3))
print('PASS: exact identities and all parity comparisons for 31 switching periods; per-layer stationary laws verified')

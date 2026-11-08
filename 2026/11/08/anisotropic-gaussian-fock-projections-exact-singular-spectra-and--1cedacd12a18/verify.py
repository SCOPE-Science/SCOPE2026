#!/usr/bin/env python3
"""Exact, self-contained arithmetic checks for Gaussian covariance and lattice identities."""
from fractions import Fraction as F
from math import gcd

def mat_mul(X,Y):
    return [[sum(X[i][k]*Y[k][j] for k in range(2)) for j in range(2)] for i in range(2)]

def inv2(M):
    a,b=M[0]; c,d=M[1]
    det=a*d-b*c
    return [[d/det,-b/det],[-c/det,a/det]]

def det2(M):
    return M[0][0]*M[1][1]-M[0][1]*M[1][0]

def trace2(M):
    return M[0][0]+M[1][1]

A=[[F(1),F(1,2)],[F(1,2),F(1)]]
B=[[F(3),F(1)],[F(1),F(5)]]
t=F(2)
H=[[2*t*F(i==j)-A[i][j] for j in range(2)] for i in range(2)]
D=[[t*t*e for e in row] for row in mat_mul(inv2(B),inv2(H))]
assert H==[[F(3),F(-1,2)],[F(-1,2),F(3)]]
assert det2(A)==F(3,4)
assert det2(B)==F(14)
assert det2(H)==F(35,4)
assert D==[[F(116,245),F(-4,245)],[F(-12,245),F(68,245)]]
assert trace2(D)==F(184,245)
assert det2(D)==F(32,245)
kappa_sq=t**4/(det2(A)*det2(H))
assert kappa_sq==F(256,105)
IminusD=[[F(i==j)-D[i][j] for j in range(2)] for i in range(2)]
assert kappa_sq/det2(IminusD)==F(1792,279)
assert 0<trace2(D)<1 and 0<det2(D)<1
assert D[0][1]!=D[1][0]
checks=11
for p,q in [(1,1),(1,2),(2,3),(3,4),(3,5),(4,7),(1,7),(5,8)]:
    assert gcd(p,q)==1
    for N in range(1,18):
        R=p*q*N
        observed=sum(1 for m in range(q*N+1) for n in range(p*N+1) if p*m+q*n<R)
        formula=F(p*q*N*N+(p+q-1)*N,2)
        assert observed==formula,(p,q,N,observed,formula)
        boundary=sum(1 for m in range(q*N+1) for n in range(p*N+1) if p*m+q*n==R)
        assert boundary==N+1
        checks+=2
print('ANISOTROPIC_GAUSSIAN_FOCK_EXACT_OK',checks)

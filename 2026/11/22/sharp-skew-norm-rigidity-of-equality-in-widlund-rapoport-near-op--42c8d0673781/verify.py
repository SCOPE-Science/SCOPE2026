#!/usr/bin/env python3
"""Exact finite corroboration of the canonical Jacobi extremizer; analytic proof in RESULT.md."""
import sympy as S
checks=0
for k in range(1,6):
    n=k+1
    J=S.zeros(n)
    for j in range(1,n):
        J[j-1,j]=j
        J[j,j-1]=j
    A=S.eye(n)+S.I*J
    b=S.zeros(n,1);b[0,0]=1
    D0=S.Integer(1)
    D1=S.Integer(1)
    for j in range(1,n):
        Dj=S.factor(A[:j,:j].det())
        assert Dj==S.factorial(j)
        checks+=1
        y=A[:j,:j].inv()*b[:j,:]
        x=S.zeros(n,1);x[:j,:]=y
        r=S.simplify(b-A*x)
        assert S.simplify((r.conjugate().T*r)[0])==1
        checks+=1
    eig=J.eigenvals()
    assert all(val.is_real for val in eig)
    checks+=1
assert S.simplify(S.det(S.Symbol('t')*S.eye(2)-S.Matrix([[0,1],[1,0]]))-(S.Symbol('t')**2-1))==0
checks+=1
print('VERIFY_OK',checks)

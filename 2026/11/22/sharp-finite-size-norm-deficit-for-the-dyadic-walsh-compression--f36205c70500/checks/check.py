#!/usr/bin/env python3
"""Independent finite and symbolic checks for the weighted Walsh-truncation norm.
Requires sympy and scipy; does not substitute for the all-N proof.
"""
import math
import sympy as s
from scipy.linalg import eigh_tridiagonal

rt2=s.sqrt(2)
x=s.Symbol('x')


def matrices(N):
    w=[s.Integer(1)] + [s.Integer(2)**(j-1) for j in range(1,N+1)]
    C=s.Matrix(N+1,N+1,lambda i,j: s.sqrt(w[i]*w[j])/s.sqrt(s.Integer(2)**N) if i+j<=N else s.Integer(0))
    B=s.Matrix(N+1,N+1,lambda i,j: (rt2 if min(i,j)==0 else s.Integer(2)) if i+j==N else (-rt2 if i+j==N+1 else s.Integer(0)))
    J=s.diag(2,*([6]*(N-1)),4)
    for i in range(N):
        J[i,i+1]=J[i+1,i]=-2 if i==0 else -2*rt2
    return C,B,J

def polynomial(N):
    pprev=s.Integer(1)
    pcur=2-x
    pnext=s.expand((6-x)*pcur-4)
    pprev,pcur=pcur,pnext
    for k in range(3,N+1):
        pprev,pcur=pcur,s.expand((6-x)*pcur-8*pprev)
    return s.expand((4-x)*pcur-8*pprev)

def symbolic():
    count=0
    for N in range(2,13):
        C,B,J=matrices(N)
        eye=s.eye(N+1)
        assert C*B==eye, ('inverse',N)
        assert B*B==J, ('Jacobi',N)
        assert s.expand(J.charpoly(x).as_expr()-(-1)**(N+1)*polynomial(N))==0, ('charpoly',N)
        count+=3
    t0=6-4*rt2
    h0=rt2*(3+2*rt2)
    for N in range(2,13):
        _,_,J=matrices(N)
        h=s.Matrix([h0]+[j+3+2*rt2 for j in range(1,N+1)])
        resid=(J-t0*s.eye(N+1))*h
        assert all(s.simplify(resid[j])==0 for j in range(N)),N
        assert s.simplify(resid[N]-((2*rt2-2)*(N+3+2*rt2)+2*rt2))==0,N
        count+=2
    print('exact symbolic identities:',count)

def numerics():
    L0=1+1/math.sqrt(2)
    c=5+3*math.sqrt(2)
    coef=math.sqrt(2)*math.pi**2*L0**3
    for N in [4,6,10,20,40,80,200,500,1000]:
        diag=[2.]+[6.]*(N-1)+[4.]
        off=[-2.]+[-2*math.sqrt(2)]*(N-1)
        val=float(eigh_tridiagonal(diag,off,eigvals_only=True,select='i',select_range=(0,0))[0])
        assert 6-4*math.sqrt(2) < val < 6
        sharp=val**(-0.5)
        asym=L0-coef/(N+c)**2
        assert abs(sharp-asym)< 6000/(N+c)**4, (N,sharp,asym)
        print(f'N={N:4d} norm={sharp:.12f} correction-error={(sharp-asym):.4g}')
    print('all supplemental checks passed')

if __name__=='__main__':
    symbolic()
    numerics()

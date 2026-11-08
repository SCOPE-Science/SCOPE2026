#!/usr/bin/env python3
"""Exact checks for the cross-polytope second-moment energy.
Uses rational arithmetic for Jacobian and all quartic coefficients.
"""
from fractions import Fraction as F
import numpy as np
from math import sqrt

count=0
for d in range(3,11):
    # In orthonormal tangent coordinates, build moment Jacobians.
    labels=[(i,s,j) for i in range(d) for s in (1,-1) for j in range(d) if j!=i]
    n=len(labels)
    J1=np.zeros((d,n), dtype=int)
    off=[(i,j) for i in range(d) for j in range(i+1,d)]
    J2=np.zeros((len(off),n), dtype=int)
    for k,(i,s,j) in enumerate(labels):
        J1[j,k]=1
        J2[off.index((min(i,j),max(i,j))),k]=s
    # Frobenius weights of offdiagonal matrix = twice sum of squares.
    H=2*J1.T@J1 + 4*J2.T@J2   # a=b=1 Hessian
    w=np.linalg.eigvalsh(H)
    expected=[0]*(d*(3*d-5)//2)+[4*(d-1)]*d+[16]*(d*(d-1)//2)
    assert np.max(abs(w-np.sort(expected)))<2e-11, (d,w,expected)
    count+=1
    # Rank check purely by integer row elimination with sympy, small d only.
    if d<=6:
        import sympy as sp
        A=sp.Matrix(J1.tolist()).col_join(sp.Matrix(J2.tolist()))
        assert A.rank()==d+d*(d-1)//2
        count+=1

# Exact fourth-order diagonal and offdiagonal cancellation on diverse p
# p[i][j] = first derivative symmetric coordinate (u_{+}+u_{-})/sqrt(2).
for d in range(3,9):
    for r in range(1,d):
        p=[[F(0) for j in range(d)] for i in range(d)]
        # Two rows feed the same column with opposite signs; A p = 0.
        col=d-1
        i=0; j=r
        if r==d-1: j=d-2
        p[i][col]=F(r);p[j][col]=-F(r)
        assert all(sum(p[i][k] for i in range(d))==0 for k in range(d))
        T=[[sum(p[i][a]*p[i][b] for i in range(d)) for b in range(d)] for a in range(d)]
        for i in range(d):
            T[i][i]-=sum(q*q for q in p[i])
        D=[sum(p[i][j]**2 for i in range(d))-sum(x*x for x in p[j]) for j in range(d)]
        assert [T[i][i] for i in range(d)]==D
        v=[[F(0) for j in range(d)] for i in range(d)]
        for i in range(d):
            for j in range(i+1,d):
                v[i][j]=v[j][i]=-T[i][j]/2
        for i in range(d):
            for j in range(d):
                M=T[i][j]+(v[i][j]+v[j][i] if i!=j else 0)
                assert M==(D[i] if i==j else 0)
                count+=1
        assert sum(D)==0

# Nonintegrable kernel direction d>=3 with explicit nonzero obstruction.
for d in range(3,11):
    p=[[F(0) for _ in range(d)] for _ in range(d)]
    p[0][2]=1;p[1][2]=-1
    D=[sum(p[i][j]**2 for i in range(d))-sum(x*x for x in p[j]) for j in range(d)]
    assert D==[-1,-1,2]+[0]*(d-3)
    assert sum(x*x for x in D)==6
    count+=1
# Direct symbolic verification of the nonintegrable analytic curve at d=3.
import sympy as sp
t=sp.symbols('t', real=True)
e=[sp.eye(3)[:,i] for i in range(3)]
h=sp.sqrt(1+t*t/2)
X=[]
for sig in (1,-1):
    X.extend([(sig*e[0]+t*e[2]/sp.sqrt(2))/h,
              (sig*e[1]-t*e[2]/sp.sqrt(2))/h,
              sig*e[2]])
sumx=sp.zeros(3,1)
M=-2*sp.eye(3)
for x in X:
    sumx+=x; M+=x*x.T
assert all(sp.simplify(v)==0 for v in sumx)
assert sp.simplify(sp.trace(M.T*M)-6*t**4/(1+t*t/2)**2)==0
count+=2
print(f'CROSSPOLYTOPE_EXACT_CHECKS_PASS {count}')

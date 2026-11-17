#!/usr/bin/env python3
"""Exact rational and symbolic checks for finite difference-penalty smoothing."""
from fractions import Fraction as Q
import sympy as sp


def diff_matrix(n, order):
    D = sp.zeros(n-order, n)
    for i in range(n-order):
        for j in range(order+1):
            D[i, i+j] = (-1)**(order-j)*sp.binomial(order,j)
    return D


def grad(n):
    B = sp.zeros(n-1,n)
    for i in range(n-1): B[i,i]=-1; B[i,i+1]=1
    return B


def step_basis(n):
    R=sp.zeros(n,n-1)
    for j in range(n-1):
        for i in range(j+1,n):R[i,j]=1
    return R


t=sp.Symbol('t', positive=True)
for n in (2,3,4):
    for p in (1,2):
        if n<=p: continue
        D=diff_matrix(n,p)
        S=(sp.eye(n)+t*D.T*D).inv()
        A=(grad(n)*S*step_basis(n)).applyfunc(sp.factor)
        assert sp.simplify(A*sp.ones(n-1,1)-sp.ones(n-1,1))==sp.zeros(n-1,1) if p==2 else True
        if n==3 and p==2:
            expected=sp.Matrix([[1+3*t,3*t],[3*t,1+3*t]])/(1+6*t)
            assert (A-expected).applyfunc(sp.simplify)==sp.zeros(2)
        if n==4 and p==2:
            den=(1+2*t)*(1+10*t)
            a=(6*t*t+9*t+1)/den
            b=3*t/(1+10*t)
            c=t*(6*t-1)/den
            d=4*t/(1+10*t)
            e=(1+4*t)/(1+10*t)
            expected=sp.Matrix([[a,d,c],[b,e,b],[c,d,a]])
            assert (A-expected).applyfunc(sp.simplify)==sp.zeros(3)
            central=sp.factor(d+e+d)
            assert sp.factor(central - (1+12*t)/(1+10*t))==0
            outer_low=sp.factor(a+b-c-central)
            outer_high=sp.factor(a+b+c-central)
            assert sp.factor(outer_low + t*(18*t+1)/den)==0
            assert sp.factor(outer_high + 3*t/(1+10*t))==0
print('SYMBOLIC_N3_AND_N4_PATH_VARIATION_IDENTITIES_PASSED')


def inverse_rational(A):
    n=len(A)
    work=[list(row)+[Q(int(i==j)) for j in range(n)] for i,row in enumerate(A)]
    for j in range(n):
        k=next(i for i in range(j,n) if work[i][j])
        work[j],work[k]=work[k],work[j]
        d=work[j][j]
        work[j]=[v/d for v in work[j]]
        for i in range(n):
            if i!=j:
                d=work[i][j]
                work[i]=[a-d*b for a,b in zip(work[i],work[j])]
    return [row[n:] for row in work]


def operator_gradient(n,p,t):
    # K = D_p^T D_p, with integer differences.
    from math import comb
    D=[[Q(0) for _ in range(n)] for _ in range(n-p)]
    for i in range(n-p):
        for j in range(p+1):D[i][i+j]=Q((-1)**(p-j)*comb(p,j))
    K=[[sum(D[k][i]*D[k][j] for k in range(n-p)) for j in range(n)] for i in range(n)]
    S=inverse_rational([[Q(i==j)+t*K[i][j] for j in range(n)] for i in range(n)])
    A=[]
    for i in range(n-1):
        A.append([sum(S[i+1][r]-S[i][r] for r in range(j+1,n)) for j in range(n-1)])
    return A,S

count=0
for n in range(2,13):
    for t0 in [Q(1,1000),Q(1,7),Q(1),Q(13,3),Q(100)]:
        for p in [1,2]:
            if n<=p:continue
            A,S=operator_gradient(n,p,t0)
            columns=[sum(abs(A[i][j]) for i in range(n-1)) for j in range(n-1)]
            assert all(sum(S[i])==1 for i in range(n))
            if p==1:
                assert max(columns)<1
            elif n==3:
                assert max(columns)==1
            else:
                assert max(columns)>1
                # A monotone 0-1 step has output endpoint span >1.
                assert max(sum(A[i][j] for i in range(n-1)) for j in range(n-1))>1
            if n==4 and p==2:
                assert max(columns)==(1+12*t0)/(1+10*t0)
            count+=1
print('EXACT_RATIONAL_DIMENSIONS_PARAMETERS_AND_STEP_WITNESSES_PASSED',count)
print('ALL_WHITTAKER_PATH_VARIATION_CHECKS_PASSED')

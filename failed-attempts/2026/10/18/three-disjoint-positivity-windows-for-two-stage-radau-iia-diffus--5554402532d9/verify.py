#!/usr/bin/env python3
"""Exact checks for Radau IIA endpoint diffusion on unit stars.
Scientific reproducibility only; requires Python standard library.
"""
from fractions import Fraction as F
from math import isqrt

def stability(t):
    return (F(6)-2*t)/(t*t+4*t+6)

def closed(m,h):
    r=stability(h); s=stability((m+1)*h)
    center_center=(1+m*s)/F(m+1)
    center_leaf=(1-s)/F(m+1)
    leaf_diag=F(1,m+1)+F(m-1,m)*r+s/F(m*(m+1))
    leaf_off=F(1,m+1)-r/F(m)+s/F(m*(m+1))
    return center_center,center_leaf,leaf_diag,leaf_off

def matmul(A,B):
    return [[sum((v*B[k][j] for k,v in enumerate(row)),F(0))
             for j in range(len(B[0]))] for row in A]

def solve(A,B):
    n=len(A); w=[A[i][:]+B[i][:] for i in range(n)]
    for j in range(n):
        p=next(k for k in range(j,n) if w[k][j])
        w[j],w[p]=w[p],w[j]
        d=w[j][j];w[j]=[t/d for t in w[j]]
        for i in range(n):
            if i!=j and w[i][j]:
                d=w[i][j];w[i]=[t-d*s for t,s in zip(w[i],w[j])]
    return [row[n:] for row in w]

def direct(m,h):
    n=m+1
    L=[[F(0) for j in range(n)] for i in range(n)]
    L[0][0]=F(m)
    for i in range(1,n):
        L[0][i]=L[i][0]=F(-1)
        L[i][i]=F(1)
    L2=matmul(L,L)
    Q=[[F(i==j)+F(2,3)*h*L[i][j]+h*h*L2[i][j]/6 for j in range(n)] for i in range(n)]
    N=[[F(i==j)-h*L[i][j]/3 for j in range(n)] for i in range(n)]
    return solve(Q,N)

def P(m,h):
    return ((m+1)*h**4+(-2*m*m+2*m+10)*h**3+
            (6*m*m+4*m+16)*h*h+(24*m+12)*h+36)

def Q(m,h):
    return (m+1)*h*h+(4-2*m)*h+6

assert stability(F(0))==1
assert stability(F(3))==0
assert stability(F(9))<0
assert Q(11,F(1,2))==Q(11,F(1))==0
for m in range(11,1001):
    assert P(m,F(8))<0
    assert Q(m,F(1))<=0
    assert Q(m,F(2))==18
    assert 3*(m-2)<3*(m+1)
assert all(P(m,F(8))>0 for m in range(1,11))

steps=[F(0), F(1,10), F(1,2), F(3,4), F(1), F(3,2),F(2),F(3),F(4),F(8),F(15),F(100)]
cnt=0
for m in range(1,17):
    for h in steps:
        cc,cl,ld,lo=closed(m,h)
        matrix=direct(m,h)
        n=m+1
        assert matrix[0][0]==cc
        assert all(matrix[0][i]==matrix[i][0]==cl for i in range(1,n))
        assert all(matrix[i][i]==ld for i in range(1,n))
        assert all(matrix[i][j]==lo for i in range(1,n) for j in range(1,n) if i!=j)
        assert all(sum(row)==1 for row in matrix)
        assert lo>=0 and cl>=0
        if m<=10:
            assert min(z for row in matrix for z in row)>=0
        cnt+=1
for m in (11,12,13,25,100):
    assert closed(m,F(3,4))[0]<0
    assert closed(m,F(8))[2]<0
    assert closed(m,F(2))[0]>0 and closed(m,F(2))[2]>0
    assert closed(m,F(10000))[0]>0 and closed(m,F(10000))[2]>0
print('PASS: exact matrix identity, mass, sign tests:',cnt,'star/step combinations')
print('PASS: negative signs at separated times for m=11,12,13,25,100')
print('PASS: analytic coefficient identities at integer m=11,...,1000')

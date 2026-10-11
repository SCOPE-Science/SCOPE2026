#!/usr/bin/env python3
import math


def matmul(A,B):
    n=len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def data(r):
    s=math.sqrt(1.0-r*r)
    D=math.sqrt(2.0+r*r+2.0*s)
    alpha=(1.0+r*r+s)/D
    beta=math.sqrt(2.0)*r/D
    delta=(1.0+s)/D
    a=0.5*(alpha+s)
    e=0.5*(alpha-s)
    b=beta/math.sqrt(2.0)
    S=[[a,b,e],[b,delta,b],[e,b,a]]
    return s,D,a,b,e,delta,S


def check_algebra(r):
    s,D,a,b,e,delta,S=data(r)
    G=matmul(S,S)
    target=[[1.0,r,r*r],[r,1.0,r],[r*r,r,1.0]]
    err=max(abs(G[i][j]-target[i][j]) for i in range(3) for j in range(3))
    assert err < 2e-12, (r,err)
    gap=a-delta
    assert b>0.0 and gap>0.0
    deriv=(2.0/3.0)*b*gap
    closed=r*s/(3.0*D)*(1.0-(1.0+s)/D)
    assert abs(deriv-closed) < 2e-14 and closed>0.0


def check_rotation(r,theta=1e-4):
    _,_,a,b,_,delta,_=data(r)
    ct,st=math.cos(theta),math.sin(theta)
    p0=(a*a+delta*delta+a*a)/3.0
    amp1=a*ct+b*st
    amp2=-b*st+delta*ct
    p=(amp1*amp1+amp2*amp2+a*a)/3.0
    assert p>p0, (r,p-p0)

for r in (1e-4,0.01,0.1,0.25,0.5,0.8,0.95,0.9999):
    check_algebra(r)
for r in (0.25,0.5,0.8,0.95,0.9999):
    check_rotation(r)
print('VERIFY_OK')

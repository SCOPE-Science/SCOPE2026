#!/usr/bin/env python3
"""Standalone exact-rational and floating diagnostics for projection trace bounds."""
from fractions import Fraction as F
from math import isfinite

def matmul(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
def trace(a):
    return a[0][0]+a[1][1]
def power(a,n):
    z=[[F(1),F(0)],[F(0),F(1)]]
    for _ in range(n): z=matmul(z,a)
    return z

def constants(p):
    a=p*(2**(p-1)-2)/4
    b=p*(p-1)/2
    return min(a,b),max(a,b)

count=0
P=[[F(1),F(0)],[F(0),F(0)]]
for k in range(1,101):
    z=F(k,101)
    t=(1-z*z)/(1+z*z)
    s=2*z/(1+z*z)
    Q=[[t*t,t*s],[t*s,s*s]]
    assert matmul(Q,Q)==Q
    for p in (3,4,5):
        pq=matmul(P,Q)
        qp=matmul(Q,P)
        c=[[pq[i][j]-qp[i][j] for j in range(2)] for i in range(2)]
        comm2=sum(c[i][j]*c[i][j] for i in range(2) for j in range(2))
        total=[[P[i][j]+Q[i][j] for j in range(2)] for i in range(2)]
        delta=trace(power(total,p))-2-(2**p-2)*t**p
        assert delta==(1+t)**p+(1-t)**p-2-(2**p-2)*t**p
        assert comm2==2*t*t*(1-t*t)
        lower,upper=constants(p)
        assert F(str(lower))*comm2<=delta<=F(str(upper))*comm2,(p,k,t,float(delta/comm2),lower,upper)
        if p==4: assert delta==6*comm2
        count+=1
for p in (3.125,3.25,3.5,3.75,3.875,4.125,4.25,4.5,4.75,4.875):
    lower,upper=constants(p)
    for k in range(1,2001):
        t=k/2001
        delta=(1+t)**p+(1-t)**p-2-(2**p-2)*t**p
        comm2=2*t*t*(1-t*t)
        ratio=delta/comm2
        assert isfinite(ratio) and lower-1e-8 <=ratio <=upper+1e-8,(p,t,ratio,lower,upper)
        count+=1
print('PROJECTION_MCCARTHY_DIAGNOSTIC_OK',count)

#!/usr/bin/env python3
from fractions import Fraction as F
from math import cos, pi, sqrt

def q0(K,c):
    return K*K*(1-c*c)-2*K*(c-1)*(3*c+1)-3*(c-1)*(3*c-1)
def q1(K,c):
    return K*K*(1-c*c)-2*K*(3*c*c+1)-(9*c*c-1)
def q2(K,c):
    return K*K*(1-c*c)-2*K*(c+1)*(3*c-1)-3*(c+1)*(3*c+1)
def t0(K,c):
    return -(c-1)*(K+3)*((K+3)*c+K-1)
def t1(K,c):
    return -((K+3)*c-(K-1))*((K+3)*c+(K-1))
def t2(K,c):
    return -(c+1)*(K+3)*((K+3)*c-(K-1))

for K in [F(2),F(5,2),F(7),F(13,3),F(29)]:
    for c in [F(-4,5),F(-1,3),F(0),F(2,7),F(9,10)]:
        assert q0(K,c)==t0(K,c)
        assert q1(K,c)==t1(K,c)
        assert q2(K,c)==t2(K,c)
        assert q1(K,c)==t1(K,c)  # j=3 repeats j=1
        lhs=F(1)-((K-F(1))/(K+F(3)))**2
        rhs=F(8)*(K+F(1))/(K+F(3))**2
        assert lhs==rhs

def r(k): return (k*k-1.0)/(k*k+3.0)
def f(k,s): return cos(k)-s*r(k)
def bisect(a,b,s):
    fa,fb=f(a,s),f(b,s)
    if fa==0: return a
    if fb==0: return b
    assert fa*fb<0,(a,b,s,fa,fb)
    for _ in range(100):
        m=(a+b)/2
        fm=f(m,s)
        if fa*fm<=0: b,fb=m,fm
        else: a,fa=m,fm
    return (a+b)/2

target=2*sqrt(2)
for n in [8,13,21,34]:
    N=n*pi
    s=1 if n%2==0 else -1
    width=4.0/N
    left=bisect(N-width,N,s)
    right=bisect(N,N+width,s)
    a=N*(left-N); b=N*(right-N)
    assert abs(a+target)<0.12
    assert abs(b-target)<0.12
print('VERIFY_OK')

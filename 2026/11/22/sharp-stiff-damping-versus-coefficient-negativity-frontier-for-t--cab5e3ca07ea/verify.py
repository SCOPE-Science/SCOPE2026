#!/usr/bin/env python3
"""Exact-arithmetic supplementary checks for a two-stage RK damping/negativity frontier.

Standard library only. Finite checks corroborate, not replace, the analytic proof.
"""
from fractions import Fraction as F
from math import sqrt

COUNT = 0

def check(condition, message='identity failed'):
    global COUNT
    assert condition, message
    COUNT += 1

def tableau(u, t):
    u = F(u); t = F(t)
    p = 1 / (1 + 12*u*u)
    q = 1-p
    return p,q,((p/2+t*q/6, q*(3-t)/6-u),
                (p*(3-t)/6+1/(12*u), q/2+t*p/6))

def mul(A, x):
    return tuple(sum(A[i][j]*x[j] for j in range(2)) for i in range(2))

def delta(u,t):
    u=F(u);t=F(t)
    return u - 2*(3-t)*u*u/(1+12*u*u)

def R(z,t):
    z=F(z);t=F(t)
    return (1+(3-t)*z/6+(1-t)*z*z/12) / (1-(3+t)*z/6+(1+t)*z*z/12)

def test_tableau(u,t):
    p,q,A=tableau(u,t)
    b=(p,q)
    c=mul(A,(F(1),F(1)))
    check(c==(F(1,2)-u,F(1,2)+1/(12*u)))
    check(sum(b)==1)
    check(sum(b[i]*c[i] for i in range(2))==F(1,2))
    check(sum(b[i]*c[i]*c[i] for i in range(2))==F(1,3))
    Ac=mul(A,c)
    check(sum(b[i]*Ac[i] for i in range(2))==F(1,6))
    M=tuple(tuple(b[i]*A[i][j]+b[j]*A[j][i]-b[i]*b[j] for j in range(2)) for i in range(2))
    factor=t*p*q/3
    check(M==((factor,-factor),(-factor,factor)))
    check(sum(A[i][i] for i in range(2))==(3+t)/6)
    check(A[0][0]*A[1][1]-A[0][1]*A[1][0]==(1+t)/12)
    check(A[0][1]==-delta(u,t))
    # Scalar test equation's exact step from a 2x2 inversion.
    for z in [F(-1,3),F(-2),F(-7,2)]:
        G=((1-z*A[0][0], -z*A[0][1]),(-z*A[1][0],1-z*A[1][1]))
        det=G[0][0]*G[1][1]-G[0][1]*G[1][0]
        v=((G[1][1]-G[0][1])/det, (G[0][0]-G[1][0])/det)
        check(1+z*(p*v[0]+q*v[1])==R(z,t))

for denom in range(2,37):
    for numer in range(1,denom):
        u=F(numer,denom)
        if not F(1,6)<=u<=F(1,2):
            continue
        for t in [F(0), F(1,11), F(1,3), F(3,5), F(1), F(3), F(7,2)]:
            test_tableau(u,t)

# Exact boundary derivatives and the restricted-optimum envelope.
for rho in [F(0),F(1,10),F(1,4),F(1,2)]:
    t=(1-rho)/(1+rho)
    u=F(1,6)
    check(delta(u,t)==1/(12*(1+rho)))
    check((3*t-1)/8>=0)
    for k in range(0,1001):
        u2=F(1,6)+F(k,3000)
        check(delta(u2,t)>=delta(u,t))

for rho in [F(3,5),F(3,4),F(9,10),F(99,100)]:
    t=(1-rho)/(1+rho)
    def deriv(u):
        return 1-4*(3-float(t))*u/(1+12*u*u)**2
    lo=1/6;hi=1/2
    for _ in range(100):
        mid=(lo+hi)/2
        if deriv(mid)>0: hi=mid
        else:lo=mid
    u=(lo+hi)/2
    check(1/6 < u < 1/2)
    check(abs((1+12*u*u)**2-4*(3-float(t))*u)<1e-13)
    minimum=float(delta(F(u).limit_denominator(10**12), t))
    for k in range(0,1001):
        v=float(F(1,6)+F(k,3000))
        check(float(delta(F(v).limit_denominator(10**12),t))>=minimum-2e-12)

# The L-stable corner is the two-stage Radau IIA method.
p,q,A=tableau(F(1,6),F(1))
check((p,q)==(F(3,4),F(1,4)))
check(A==((F(5,12),-F(1,12)),(F(3,4),F(1,4))))
check(R(-2,1)==F(1,9))
print(f'PASS: {COUNT} supplementary checks; exact order, algebraic stability, stability function, and frontier samples')

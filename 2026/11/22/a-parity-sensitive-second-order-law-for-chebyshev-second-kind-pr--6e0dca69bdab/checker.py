#!/usr/bin/env python3
"""Consistency tests for the sharp semicircle-weight Chebyshev residual asymptotics.
The infinite-dimensional and asymptotic assertions require the proof in RESULT.md.
"""
import math
from fractions import Fraction
PI = math.pi

def residual(n, theta):
    u = (theta - math.sin(2*theta)/2)/PI
    return u*(1-u)-sum(((math.sin(k*theta)/k-math.sin((k+2)*theta)/(k+2))/PI)**2 for k in range(1,n+1))

def tail(n, theta, high=180000):
    s=0.0
    for m in range(n+2,high+1):
        a=2*(math.cos(theta)*math.sin(m*theta)-m*math.sin(theta)*math.cos(m*theta))/(PI*(m*m-1))
        s+=a*a
    return s

def curvature_exact(n):
    ev = n//2
    odds = [k for k in range(1,n+1,2)]
    q=Fraction(-1-ev,1)+sum((Fraction((k+1)**2,k*(k+2)) for k in odds), Fraction(0,1))
    return q*8 # coefficient of 1/pi^2

def curvature_closed(n):
    if n%2: return 4*(Fraction(1,1)-Fraction(1,n+2))
    return -4*(Fraction(1,1)+Fraction(1,n+1))

assert residual(0,PI/2)==0.25
for n in range(0,100):
    assert curvature_exact(n)==curvature_closed(n),n
    assert (curvature_exact(n)>0)==bool(n%2)
for n in [0,1,2,3,5,10,24,60]:
    for t in [0.15,0.35,0.79,1.25,PI/2,2.17,2.8]:
        lhs=residual(n,t);rhs=tail(n,t)
        assert abs(lhs-rhs)<3e-6,(n,t,lhs,rhs)
for n in [20,21,40,41,80,81,160,161,320,321]:
    th=PI/2 if n%2==0 else PI/2+PI/(2*(n+2))
    predicted=2/(PI**2*n)-2/(PI**2*n*n)
    error=abs(residual(n,th)-predicted)
    assert error < 3/n**3, (n,error)
    if n%2:
        assert residual(n,th)>residual(n,PI/2)
        centered_pred=2/(PI**2*n)-4/(PI**2*n*n)
        assert abs(residual(n,PI/2)-centered_pred)<3/n**3
# Confirm sample global bounds by dense probes, not as exhaustive certificates.
for n in [4,7,16,25,60,101]:
    best=max(residual(n,PI*j/1200) for j in range(1,1200))
    selected=PI/2 if n%2==0 else PI/2+PI/(2*(n+2))
    assert best < residual(n,selected)+0.5/n**3,(n,best,residual(n,selected))
print('PASS: 100 exact curvature identities, 56 Parseval-tail probes, 10 asymptotic probes, 6 dense-grid checks.')

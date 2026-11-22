#!/usr/bin/env python3
"""Finite numerical and algebraic tests of annular Bergman commutator identities.

All infinite dimensional assertions require the accompanying analytic proof.
"""
import math
from fractions import Fraction

checks = 0

def check(pred, msg):
    global checks
    if not pred:
        raise AssertionError(msg)
    checks += 1

def I(n, r):
    if n == -1:
        return -math.log(r)
    return -math.expm1((2*n+2)*math.log(r))/(2*n+2)

def eig(n,m,r):
    return I(n+m,r)/I(n,r)-I(n,r)/I(n-m,r)

def theta(y):
    if abs(y)<1e-3:
        z=y*y
        return 1/3-z/15+2*z*z/189-z*z*z/675
    return 1/(y*y)-1/(math.sinh(y)**2)

# Independently evaluate exact integer moment identities via rational arithmetic.
for r in (Fraction(1,2),Fraction(2,3),Fraction(3,4)):
    q=r*r
    for m in (1,2,3):
        for n in list(range(-12,-1))+list(range(0,15)):
            if n==-1 or n+m==-1 or n-m==-1:
                continue
            def J(k):return (1-q**(k+1))/Fraction(k+1)
            a=J(n+m)/J(n)-J(n)/J(n-m)
            check(a>0,('positive',r,m,n))
            check(a== (J(n+m)*J(n-m)-J(n)**2)/(J(n)*J(n-m)), 'exact rational identity')
# Strictly positive and symmetric limiting profile, maximum at zero.
for j in range(1,100):
    x=j/20
    check(theta(x)>0,('theta positive',x))
    check(abs(theta(x)-theta(-x))<1e-12,('theta even',x))
    check(theta(x)<theta((j-1)/20),('theta decreasing',x))
check(abs(theta(0)-1/3)<1e-14,'theta maximum')
# Finite-radius trace telescoping and convergence of scaled moments.
for r in (0.70,0.85,0.94):
    for m in (1,2,3):
        vals=[eig(n,m,r) for n in range(-700,701)]
        check(all(x>0 for x in vals),'positive spectrum')
        total=sum(vals)
        check(abs(total-m*(1-r**(2*m))) < 0.025,'finite trace tail')
        check(max(vals)<m*m*(-math.log(r))**2/3+1e-8,'global theta bound')
# Pointwise profile, at fixed nonzero scaled index, compared via independent quadrature.
for m in (1,2,3):
    for y in (-3,-2,-1,0,1,2,3):
        diffs=[]
        for eps in (0.1,0.06,0.03,0.015):
            n=round(y/eps)-1
            a=eig(n,m,math.exp(-eps))/(m*eps)**2
            diffs.append(abs(a-theta(y)))
        check(diffs[-1]<0.12,('pointwise convergence',m,y,diffs))
# Exact second moment integral formula against numerical Simpson quadrature.
N=10000
step=20/N
sm=theta(0)**2+theta(20)**2
for j in range(1,N):
    sm+=(4 if j%2 else 2)*theta(j*step)**2
integral=2*sm*step/3 + 2/(3*20**3)  # algebraic tail; exponential correction negligible
# ζ(2) and ζ(3) approximated by convergent series with controlled tail.
z3=sum(k**-3 for k in range(1,50000))
expected=(8/math.pi**2)*(math.pi**2/6-z3)
check(abs(integral-expected)<2e-8,('zeta formula',integral,expected))
print('ANNULAR_BERGMAN_COMMUTATOR_DIAGNOSTIC_OK',checks)

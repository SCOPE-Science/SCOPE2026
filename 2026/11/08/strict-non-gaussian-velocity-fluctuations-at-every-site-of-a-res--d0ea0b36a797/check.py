#!/usr/bin/env python3
"""Standalone exact checks for the ordered fourth cumulant and chain transfer.
Run: python check.py. Requires sympy. The analytic arguments in RESULT.md,
not finite tests, establish the all-parameter statements.
"""
from math import factorial
from fractions import Fraction
import sympy as s

checks=0

def certify(expr, expected=0):
    global checks
    assert s.simplify(expr-expected)==0, (expr,expected)
    checks+=1

r,D,a,A,B,C=s.symbols('r D a A B C', positive=True)
# A,B,C denote exp(-r*(successive gaps)), and a=t2-t1.
m2=2*D/r
m4=24*D**2/r**2
# Nested Markov calculation: P_t(x)=e^(-rt)x;
# P_t(x^2)=e^(-rt)x^2 + (2D/r)(1-e^(-rt));
# P_t(x^3)=e^(-rt)(x^3+6Dt*x).
E4=C*(B*A*(m4+6*D*a*m2)+m2*(1-B)*A*m2)
Wick=m2**2*(A*C+2*A*B**2*C)
connected=s.factor(E4-Wick)
answer=(4*D**2/r**2)*A*B*C*(5+3*r*a-2*B)
certify(connected,answer)
certify(connected.subs({A:1,B:1,C:1,a:0}),12*D**2/r**2)
certify(E4.subs({A:1,B:1,C:1,a:0}),m4)
certify(Wick.subs({A:1,B:1,C:1,a:0}),3*m2**2)
# Unequal times, independent of the absolute origin.
for rr in (s.Rational(1,3),s.Rational(3,2),s.Integer(4)):
    for dd in (s.Rational(2,5),s.Integer(1),s.Integer(3)):
        for aa,bb,cc in ((0,0,0),(s.Rational(1,2),1,0),
                          (1,s.Rational(1,3),2),(2,3,1)):
            ea=s.exp(-rr*aa);eb=s.exp(-rr*bb);ec=s.exp(-rr*cc)
            val=connected.subs({r:rr,D:dd,a:aa,A:ea,B:eb,C:ec})
            val2=answer.subs({r:rr,D:dd,a:aa,A:ea,B:eb,C:ec})
            certify(val,val2)
            assert float(val)>0
            checks+=1

# Exact state-space Taylor coefficients and resolvent response for multiple
# short chains. These independently reconstruct two critical proof inputs:
# nonzero local response and positive Laplace transform at positive arguments.
for N in range(2,7):
    m=s.Rational(2); k=s.Rational(3); gamma=s.Rational(5,2)
    K=s.zeros(N)
    for i in range(N):
        K[i,i]=2
        if i+1<N: K[i,i+1]=-1;K[i+1,i]=-1
    boundary=s.zeros(N);boundary[0,0]=1;boundary[N-1,N-1]=1
    Mat=s.zeros(2*N)
    for i in range(N):
        Mat[i,N+i]=1
    for i in range(N):
        for j in range(N):
            Mat[N+i,j]=-k*K[i,j]/m
            Mat[N+i,N+j]=-gamma*boundary[i,j]/m
    inp=s.zeros(2*N,1); inp[N,0]=k/m
    powers=[];v=inp
    for p in range(2*N+3):
        powers.append(v);v=Mat*v
    for ell in range(1,N+1):
        degree=2*(ell-1)
        for p in range(degree):
            certify(powers[p][N+ell-1])
        certify(powers[degree][N+ell-1],(k/m)**ell)
        for rr in (s.Rational(1,2),s.Integer(1),s.Rational(5,2)):
            M=(m*rr**2)*s.eye(N)+k*K+gamma*rr*boundary
            lap=k*rr*M.inv()[ell-1,0]
            assert lap>0
            checks+=1
print('PASS', checks,'exact symbolic, rational and transfer checks')

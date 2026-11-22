"""Reproducible checks for the all-chain Euler--Maruyama stability identity.
Python 3 with sympy and numpy; no external data or network operations.
These finite checks supplement the separate analytic proof.
"""
from math import comb
from fractions import Fraction
import sympy as sp
import numpy as np

identities=0
for n in range(1,9):
    z=sp.symbols('z')
    polynomial=sum(comb(n,j)**2*z**j for j in range(n+1))
    lhs=sum(comb(n+k,n)**2*z**k for k in range(20))
    rhs=sp.series(polynomial/(1-z)**(2*n+1),z,0,20).removeO()
    assert sp.expand(lhs-rhs)==0
    identities+=1

cov_checks=0
spectrum_checks=0
for m in range(2,8):
    n=m-1
    for h in [sp.Rational(1,2),sp.Rational(3,4),sp.Rational(1),sp.Rational(5,4),sp.Rational(3,2)]:
        T=(1-h)*sp.eye(m)+h*sp.Matrix(m,m,lambda i,j: int(j==i+1))
        P=sp.zeros(m)
        P[m-1,m-1]=1
        acc=sp.zeros(m)
        for k in range(850):
            acc+=P
            P=T*P*T.T
            if max(abs(float(P[i,j])) for i in range(m) for j in range(m))<1e-40:
                break
        closed=h**(2*n)*sum(comb(n,j)**2*(1-h)**(2*j) for j in range(n+1))/(1-(1-h)**2)**(2*n+1)
        assert abs(float(acc[0,0]-closed))<1e-9
        cov_checks+=1
        if m<=4:
            e=sp.zeros(m)
            e[m-1,0]=1
            for sigma2 in [sp.Rational(1,2),sp.Rational(2),sp.Rational(5)]:
                Phi=sp.kronecker_product(T,T)+h*sigma2*sp.kronecker_product(e,e)
                rad=max(abs(np.linalg.eigvals(np.array(Phi,dtype=float))))
                test=float(h*sigma2*closed)
                if abs(test-1)>1e-9:
                    assert (rad<1)==(test<1),(m,h,sigma2,rad,test)
                spectrum_checks+=1

for n in range(1,10):
    z=sp.symbols('z')
    P=sum(comb(n,j)**2*z**j for j in range(n+1))
    assert sp.expand(P.subs(z,1)-comb(2*n,n))==0

print('BINOMIAL_IDENTITIES_OK',identities)
print('COVARIANCE_RESPONSE_CHECKS_OK',cov_checks)
print('KRONECKER_SPECTRAL_CHECKS_OK',spectrum_checks)
print('CENTRAL_BINOMIAL_LIMITS_OK',9)
print('VERIFICATION_PASS; analytic proof required for the infinite-domain claim')

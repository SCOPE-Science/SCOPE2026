"""Numerical and exact-rational checks of the transverse log-cocycle correlation formula.
Only tests finite computations; proofs of all-m statements are in RESULT.md.
"""
from fractions import Fraction
from math import pi,cos,sin,isclose

def b2(x):
    x=x%1
    return x*x-x+Fraction(1,6)

def gamma_coefficient(phi,m):
    return (b2((2**m+1)*phi)+b2((2**m-1)*phi))/2**m

def fourier_covariance(phi,m,cutoff=100000):
    p=float(phi)
    return sum(2*cos(2*pi*(2**m)*k*p)*cos(2*pi*k*p)/((2**m)*k*k) for k in range(1,cutoff+1))

def verify():
    # Exact formulas for two geometrically natural roots.
    for m in range(0,19):
        c=gamma_coefficient(Fraction(1,3),m)
        assert c==Fraction(1,9*2**m)
        d=gamma_coefficient(Fraction(1,4),m)
        assert d==(Fraction(1,12) if m==0 else Fraction(-1,24*2**m))
    print('Exact Bernoulli/rational covariance cases: PASS (38 identities)')
    for p in (Fraction(1,4),Fraction(1,3),Fraction(2,5)):
        for m in (0,1,2,3):
            direct=fourier_covariance(p,m)
            analytic=float(gamma_coefficient(p,m))*pi*pi
            assert abs(direct-analytic)<1.2e-4,(p,m,direct,analytic)
    print('Independent 100000-mode Fourier correlation comparisons: PASS (12)')
    for n in range(1,19):
        a=sum((n-m)*gamma_coefficient(Fraction(1,3),m) for m in range(1,n))
        v=n*gamma_coefficient(Fraction(1,3),0)+2*a
        assert v==Fraction(3*n-4,9)+Fraction(4,9*2**n)
        b=sum((n-m)*gamma_coefficient(Fraction(1,4),m) for m in range(1,n))
        w=n*gamma_coefficient(Fraction(1,4),0)+2*b
        assert w==Fraction(2,12)-Fraction(1,12*2**(n-1))
    print('Exact finite-n variance identities: PASS (36)')
    theta=.123456789
    for n in range(1,13):
        p=1.; q=1.
        for j in range(n):
            x=sin(pi*(2**j)*theta)**2
            p*=4*x-2
            q*=4*x-4
        expected_p=(-1)**n*sin(pi*2**(n+1)*theta)/sin(2*pi*theta)
        expected_q=(-1)**n*(sin(pi*2**n*theta)/sin(pi*theta))**2
        assert isclose(p,expected_p,rel_tol=1e-8,abs_tol=1e-8),(n,p,expected_p)
        assert isclose(q,expected_q,rel_tol=1e-8,abs_tol=1e-8),(n,q,expected_q)
    print('Exact-cocycle telescoping numerical diagnostics: PASS (24)')
if __name__=='__main__': verify()

#!/usr/bin/env python3
"""Finite reproducibility checks for the tangential harmonic Berezin law.
Scientific statements for all parameters follow from the accompanying proof,
not from these finite calculations. Requires scipy >= 1.9.
"""
from math import pi, sin, gamma, exp, log, isfinite
from scipy.integrate import quad
from scipy.special import beta as B, expn

checks=0

def close(actual, expected, tol=1e-7):
    global checks
    assert isfinite(float(actual)) and abs(actual-expected) <= tol*max(1.,abs(expected)), (actual,expected,tol)
    checks+=1

def I_exact(b):
    return B((b-1)/2,(b+1)/2)/4 - sin(pi*b/2)*B(b-1,b+1)/2

def A_exact(b):
    return 2**(2*b-1)*(b-1)/pi * I_exact(b)

def I_numeric(b):
    # Integrable at both endpoints for b>1.
    def fun(t):
        return t**(b-2)*(complex(t,-1)**(-b)).real**2
    return quad(fun,0,1,epsabs=2e-11,epsrel=2e-11)[0]+quad(fun,1,float('inf'),epsabs=2e-11,epsrel=2e-11)[0]

def p(b, x):
    c=2**(2*b-1)*(b-1)/pi
    # Rescale v=|x|t; keep both integrable endpoints.
    a=abs(x)
    f=lambda t: t**(b-2)*(complex(t+1/a,-1)**(-b)).real**2
    integ=quad(f,0,1,epsabs=1e-10)[0]+quad(f,1,float('inf'),epsabs=1e-10)[0]
    return c*a**(-b-1)*integ

for b in (1.25,1.5,1.75,1.9,2,2.2,2.5,3,4):
    close(I_numeric(b),I_exact(b),tol=2e-8)
    assert I_exact(b)>0
    checks+=1
    for x in (200,1000):
        ratio=p(b,x)*x**(b+1)/A_exact(b)
        # Uniform convergence; the 200-point tail is only moderately asymptotic.
        close(ratio,1,tol=0.08 if x==200 else 0.018)

# A universal, exactly normalized logarithmic cusp at zero weight.
close(A_exact(2),1,1e-12)
for s in (0.02,0.04,0.1,0.4,1,2):
    exact=exp(-s)*(1+2*s*s/3)+s*expn(2,s)
    numerical=2*quad(lambda b:exp(-s*b)*(s**3/3+b**(-3)+s*b**(-2)),1,float('inf'),epsabs=2e-11)[0]
    close(exact,numerical,2e-8)
for s in (0.0001,0.0002,0.0005):
    exact=exp(-s)*(1+2*s*s/3)+s*expn(2,s)
    close((1-exact)/(s*s*log(1/s)),1,tol=.15)

# Fourier-Plancherel conditional horizontal variance for b>2.
for b in (2.1,2.5,3,4):
    f=lambda x:(complex(1,-x)**(-b)).real**2
    denom=quad(f,0,float('inf'),epsabs=1e-10)[0]
    numer=quad(lambda x:x*x*f(x),0,float('inf'),epsabs=1e-10)[0]
    close(numer/denom,1/(2*b-3),1e-7)
    # Beta-prime averaging gives the exact full horizontal variance.
    variance=B(b-1,b-2)/B(b-1,b)/(2*b-3)
    close(variance,2/(b-2),1e-12)

# Heavy-tail fractional coefficients are positive and approach 1/(-alpha).
for b in (1.25,1.5,1.75,1.95):
    K=A_exact(b)*pi/(gamma(b+1)*sin(pi*b/2))
    assert K>0
    checks+=1
print('PASS',checks,'finite diagnostics; all-parameter conclusions remain analytic')

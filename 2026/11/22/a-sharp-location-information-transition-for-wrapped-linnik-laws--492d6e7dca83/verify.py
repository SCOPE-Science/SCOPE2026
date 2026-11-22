#!/usr/bin/env python3
"""Numerical checks for the square-root Hellinger cusp in wrapped Linnik laws.
No external files or network are required. Finite checks do not replace proofs.
"""
import math
import mpmath as mp
mp.mp.dps=35
checks=0

def close(x,y,tol=mp.mpf('1e-10')):
    global checks
    checks+=1
    assert abs(x-y)<tol, (x,y)

def fvals(alpha,sigma,x,K=6000):
    a=mp.mpf(str(alpha)); s=mp.mpf(str(sigma)); x=mp.mpf(str(x))
    c=s**(-a)
    # r_k = (1+(sigma*k)^alpha)^-1 - sigma^-alpha*k^-alpha
    rr=[1/(1+(s*k)**a)-c/k**a for k in range(1,K+1)]
    f0=(1+2*(c*mp.zeta(a)+sum(rr)))/(2*mp.pi)
    d=(c*(mp.zeta(a)-mp.re(mp.polylog(a,mp.exp(1j*x))))
        +sum(rr[k-1]*(1-mp.cos(k*x)) for k in range(1,K+1)))/mp.pi
    fp=-(c*mp.im(mp.polylog(a-1,mp.exp(1j*x)))
         +sum(k*rr[k-1]*mp.sin(k*x) for k in range(1,K+1)))/mp.pi
    return f0, f0-d, fp

for a in (1.25,1.5,1.75,2.0):
    for sigma in (.7,1.4):
        b=a-1
        B=mp.mpf(str(sigma))**(-a)/(2*mp.gamma(a)*mp.sin(mp.pi*b/2))
        for x in (0.003,0.001):
            f0,fx,fp=fvals(a,sigma,x)
            # B and B*b are exact power-law coefficients, with asymptotic convergence.
            assert f0>fx>0 and fp<0
            checks+=3
            rel1=abs((f0-fx)/x**b/B-1)
            rel2=abs(-fp/(B*b*x**(b-1))-1)
            assert rel1 < (.24 if a==1.25 else .09), (a,sigma,x,'cusp',rel1)
            assert rel2 < (.14 if a==2 else .10), (a,sigma,x,'derivative',rel2)
            checks+=2

for b in (.2,.4):
    J=mp.quad(lambda u: ((abs(u+1)**b)-(abs(u)**b))**2, [-mp.inf,-1,0,mp.inf])
    assert J>0 and mp.isfinite(J)
    checks+=1

# Exact Fourier coefficients of wrapped Linnik follow from an exponential mixture
# of wrapped symmetric stable Fourier coefficients.
for a in (1.2,1.5,2.0):
    for sigma in (.5,1.7):
        for k in (1,2,5,11):
            target=1/(1+(sigma*k)**a)
            integral=mp.quad(lambda t:mp.exp(-t)*mp.exp(-t*(sigma*k)**a),[0,mp.inf])
            close(integral,target)

print('PASS:',checks,'individual numerical assertions; analytic proof is in RESULT.md')

#!/usr/bin/env python3
"""Reproduce finite-dimensional Gaussian XNysTrace second moments.
Purely deterministic algebra and seeded experiments, no external files or network.
"""
import math
import numpy as np
import sympy as S
from fractions import Fraction

t = S.symbols('t', positive=True)
r = (t-1)/(t+1)
X = t*(1+t**2)/2
Y = t**2*(1+r**4)/4
V = X+Y
H = 1+t**4
D = S.factor(S.Rational(5,8)*H-V)
G = S.factor(X-4*Y)
assert S.simplify(D - (t-1)**2*(5*t**6+26*t**5+57*t**4+80*t**3+57*t**2+26*t+5)/(8*(t+1)**4)) == 0
assert S.simplify(G - t*(t-1)**2*(t**4+2*t**3+10*t**2+2*t+1)/(2*(t+1)**4)) == 0
print('SYMBOLIC: optimal 5/8 Gaussian-Hutch risk ratio and maximal 5/3 self-error underestimation certified by positive polynomial factorizations.')
assert V.subs(t,1)==S.Rational(5,4)
assert (X-Y).subs(t,1)==S.Rational(3,4)
assert S.simplify(V.subs(t,2)-S.Rational(487,81))==0
print('RATIONAL BENCHMARKS: identity eigenspectrum V=5/4, expected self-error-square=3/4; spectrum 1,4 gives V=487/81.')

# Independent high-accuracy numerical angular quadrature for the residual Fourier moments.
import scipy.integrate as it
for a,b in [(1.,1.), (1.,4.), (1.,25.), (.25,1.), (3.,7.)]:
    q=math.sqrt(a*b)
    rr=(math.sqrt(b)-math.sqrt(a))/(math.sqrt(a)+math.sqrt(b))
    tau=lambda th: a*b/(a*math.cos(th)**2+b*math.sin(th)**2)
    integ=lambda fun:it.quad(fun,0,2*math.pi,epsabs=1e-11,epsrel=1e-11)[0]/(2*math.pi)
    out=(integ(tau),integ(lambda th:tau(th)**2),integ(lambda th:tau(th)*math.cos(4*th)))
    target=(q,q*(a+b)/2,q*rr**2)
    assert max(abs(u-v) for u,v in zip(out,target))<2e-10, (a,b,out,target)
print('QUADRATURE: 5 independent angular Fourier moment identities verified to 2e-10.')

# Direct random sample of the original two leave-one-out estimators, with no analytical simplifications.
rng=np.random.default_rng(20261105)
n=180000
w=rng.normal(size=(n,2,2))
g1=w[:,0,:];g2=w[:,1,:]
for a,b in [(1.,1.), (1.,4.), (1.,25.), (.25,1.), (3.,7.)]:
    A=np.array([a,b]);
    Q1=np.einsum('ni,i,ni->n',g1,A,g1); Q2=np.einsum('ni,i,ni->n',g2,A,g2)
    cross=np.einsum('ni,i,ni->n',g1,A,g2)
    trN1=np.einsum('ni,i,ni->n',g1,A*A,g1)/Q1
    trN2=np.einsum('ni,i,ni->n',g2,A*A,g2)/Q2
    T1=trN2+np.einsum('ni,i,ni->n',g1,A,g1)-cross*cross/Q2
    T2=trN1+np.einsum('ni,i,ni->n',g2,A,g2)-cross*cross/Q1
    TT=(T1+T2)/2
    ERR2=(T1-T2)**2/4
    q=math.sqrt(a*b); rr=(math.sqrt(b)-math.sqrt(a))/(math.sqrt(b)+math.sqrt(a))
    X=q*(a+b)/2;Y=a*b*(1+rr**4)/4
    var=X+Y; eerr=X-Y
    actualvar=np.mean((TT-a-b)**2); actualerr=np.mean(ERR2)
    assert abs(np.mean(TT)-(a+b))<.065*math.sqrt(var), (a,b,'bias',np.mean(TT)-a-b)
    assert abs(actualvar/var-1)<.065, (a,b,'variance',actualvar,var)
    assert abs(actualerr/eerr-1)<.065, (a,b,'posterior',actualerr,eerr)
    print(f'MONTE_CARLO: eigenvalues=({a:g},{b:g}), variance calc={var:.8f}, estimate={actualvar:.8f}; reported-square expectation calc={eerr:.8f}, sample={actualerr:.8f}')
print('ALL CHECKS PASS: symbolic sharpness, quadrature and independent Gaussian leave-one-out simulation.')

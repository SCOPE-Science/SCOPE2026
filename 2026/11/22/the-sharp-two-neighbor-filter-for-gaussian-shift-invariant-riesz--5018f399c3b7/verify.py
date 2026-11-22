#!/usr/bin/env python3
"""Reproduce the sharp two-neighbor Gaussian translate Riesz-bound calculation.

Uses independent Jacobi series and numerical one-variable optimization.
Requires Python 3, numpy, scipy and mpmath.
"""
import math
import mpmath as mp
from scipy.optimize import minimize_scalar

mp.mp.dps=65


def theta(u,q):
    # Direct theta series, no Jacobi-product factors used.
    z=mp.acos(mp.mpf(u))
    n=1
    total=mp.mpf(1)
    while True:
        term=2*mp.power(q,n*n)*mp.cos(n*z)
        total+=term
        if 2*mp.power(q,n*n)<mp.mpf('1e-60'):break
        n+=1
        if n>500:raise RuntimeError('theta series did not converge')
    return total


def t_opt(q):
    h=mp.sqrt(theta(1,q)); j=mp.sqrt(theta(-1,q))
    return (h-j)/(h+j)


def spect(u,q,t):
    return theta(u,q)*(1+t*t-2*t*u)


def exact_ratio(q,t):
    # SciPy bounded max, endpoint min follows from log concavity.
    ff=lambda u: float(spect(mp.mpf(u),q,t))
    r=min(ff(-1),ff(1))
    sol=minimize_scalar(lambda u:-ff(u),bounds=(-1,1),method='bounded',options={'xatol':1e-13})
    M=max(ff(-1),ff(1),ff(sol.x))
    return M/r,sol.x


count=0
for sig in (0.55,0.8,1.,1.5,2.,3.,4.,6.,8.):
    q=mp.exp(-mp.pi*sig/2)
    t=t_opt(q)
    R,u=exact_ratio(q,t)
    baseline=float(theta(1,q)/theta(-1,q))
    assert 0<t<1 and -1<u<1
    assert abs(float(spect(-1,q,t)/spect(1,q,t))-1)<2e-12
    assert R<baseline
    count+=4
    # both perturbation sides and far-away tests including reciprocal form
    for x in (0.,0.15,0.5,0.85,0.98):
        for xp in (float(t)*x,float(t)+(1-float(t))*x):
            if abs(xp-float(t))<1e-13:continue
            Rp,_=exact_ratio(q,mp.mpf(xp))
            assert Rp>R-2e-11,(sig,xp,Rp,R)
            count+=1
    print('sigma={:.2f} q={:.9g} optimal_t={:.12f} max_u={:+.9f} optimal_B/A={:.12f} plain_B/A={:.12f}'.format(sig,float(q),float(t),u,R,baseline))

# Verify Poisson versus Fourier-series gram multiplier for several frequencies
for sig in (0.7,1.,2.,4.):
    q=mp.exp(-mp.pi*sig/2)
    for xi in (0.,1/8,1/4,3/8,1/2):
        a=mp.nsum(lambda n:mp.exp(-2*mp.pi*(n+xi)**2/sig)/sig,[-mp.inf,mp.inf])
        b=theta(mp.cos(2*mp.pi*xi),q)/mp.sqrt(2*sig)
        assert abs(a/b-1)<mp.mpf('1e-45')
        count+=1
# Stronger high-precision small-q asymptotics without float subtraction.
def theta_derivative(u,q):
    total=mp.mpf(0)
    for n in range(1,100):
        term=2*mp.power(q,n*n)*n*mp.chebyu(n-1,u)
        total+=term
        if abs(term)<mp.mpf('1e-60'):break
    return total
for sig in (6,8,10,12):
    q=mp.exp(-mp.pi*sig/2)
    t=t_opt(q)
    F=lambda u: theta_derivative(u,q)/theta(u,q)-2*t/(1+t*t-2*t*u)
    u=mp.findroot(F, (mp.mpf('-0.1'), mp.mpf('0.1')))
    R=spect(u,q,t)/spect(-1,q,t)
    assert abs((R-1)/(4*q*q)-1)<mp.mpf('0.0002')
    assert abs(t/q-1)<mp.mpf('0.0002')
    count+=2
print('PASS',count,'numerical assertions; infinite-dimensional assertions use the analytical argument')

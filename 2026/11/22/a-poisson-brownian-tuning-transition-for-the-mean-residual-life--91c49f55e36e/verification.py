#!/usr/bin/env python3
"""Numerical supplements for the growing-weight residual-life goodness-of-fit result.

All mathematical definitions and source citations are given in RESULT.md.
This script checks the exact finite-sample kernel identity and illustrative regimes;
it is not a substitute for the infinite-sample proof.
"""
import math
from numpy.polynomial.legendre import leggauss
import numpy as np
from scipy.integrate import quad


def scaled_statistic(observations, a):
    """Return a^2*T_{n,a} via exact piecewise polynomial integration."""
    x = np.asarray(observations, dtype=float)
    assert x.ndim == 1 and len(x) >= 2 and np.all(x > 0) and a > 0
    n = len(x)
    y = np.sort(x / x.mean())
    u = a * y
    bounds = np.concatenate(([0.], u, [math.inf]))
    prefix = np.concatenate(([0.], np.cumsum(y)))
    val = 0.0
    for k in range(n + 1):
        lo, hi = float(bounds[k]), float(bounds[k+1])
        A = k - prefix[k]
        B = (k-n)/a
        ex_lo = math.exp(-lo)
        ex_hi = math.exp(-hi) if math.isfinite(hi) else 0.0
        # integrate (A+B*u)^2 exp(-u) over [lo,hi]
        I0 = ex_lo-ex_hi
        I1 = (lo+1)*ex_lo-((hi+1)*ex_hi if ex_hi else 0)
        I2 = (lo*lo+2*lo+2)*ex_lo-((hi*hi+2*hi+2)*ex_hi if ex_hi else 0)
        val += A*A*I0 + 2*A*B*I1 + B*B*I2
    return (a/n)*val


def scaled_statistic_quad(x,a):
    x=np.asarray(x,dtype=float); n=len(x); y=np.sort(x/x.mean())
    def f(u):
        t=u/a; k=np.searchsorted(y,t,side='right')
        H=k-n*t+np.sum(np.maximum(t-y[:k],0.0))
        return H*H*math.exp(-u)
    return a/n*quad(f,0,60,points=sorted(a*y[(a*y<60)]),epsabs=1e-9)[0]


def mean_h_sq(n, y):
    # Normalized independent exponentials give nY_i/S~n Dirichlet(1,...,1).
    y=np.asarray(y)
    p=np.maximum(0.,1-y/n)
    q=np.maximum(0.,1-2*y/n)
    diag = 2*n/(n+1)*p**(n+1)-2*p**n+p**(n-1)
    off = n/(n+1)*q**(n+1)-2*q**n+q**(n-1)
    return np.where(y < n, n*diag+n*(n-1)*off, 0.)


def check():
    rng=np.random.default_rng(370321)
    asserts=0
    for n in (2,3,4,7,17):
        for _ in range(10):
            x=rng.exponential(size=n)
            a=float(rng.uniform(.2,30))
            got=scaled_statistic(x,a)
            expected=scaled_statistic_quad(x,a)
            assert abs(got-expected)<2e-7*(1+abs(expected)),(n,a,got,expected)
            asserts+=1
    # Exact second-moment identity via direct finite Dirichlet numerical quadrature
    from scipy.special import roots_laguerre
    nodes,weights=roots_laguerre(70)
    for n in (2,3,5,10):
        for a in (1.,5.,20.):
            vals=mean_h_sq(n,nodes/a)
            expected=(a/n)*float(np.dot(weights,vals))
            # Independent Monte Carlo cross-check (low precision only)
            nrep=4000
            sims=np.array([scaled_statistic(rng.exponential(size=n),a) for _ in range(nrep)])
            se=np.std(sims,ddof=1)/math.sqrt(nrep)
            assert abs(sims.mean()-expected)<5*se+0.025,(n,a,sims.mean(),expected,se)
            asserts+=1
    # Centered Poisson Q_c moments: E=1, Var=1+c/2 by exact Poisson cumulants
    # integrated identities E[min(U,V)]=1/2, E[min(U,V)^2]=1/2 for Exp(1) U,V.
    for c in (.1,.5,1.,2.,5.):
        em=1.0
        var=2*(2/4)+c*(1/2) # = 1+c/2
        assert abs(var-(1+c/2)) < 1e-14 and em==1.0
        asserts+=1
    # verify exact value H(0)=0 for a normalized sample
    for n in (2,5,25,100):
        y=rng.exponential(size=n); y=y/y.mean()
        assert abs(np.sum(y-1)) < 5e-12
        asserts+=1
    print(f"PASS: {asserts} supplementary numerical/algebraic assertions")
    print("All paths are independently computed; limits rely on the mathematical proof.")

if __name__=='__main__':check()

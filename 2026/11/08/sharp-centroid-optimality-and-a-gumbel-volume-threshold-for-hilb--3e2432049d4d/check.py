#!/usr/bin/env python3
"""Independent numerical checks of exact Euclidean simplex Hilbert-ball masses.

Requires Python 3, NumPy, SciPy. Simulations check implications, not proofs.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import betaln


def hilbert_distances(anchor, y):
    z = np.log(y) - np.log(np.asarray(anchor)[None, :])
    return np.max(z, axis=1) - np.min(z, axis=1)


def analytic_mass(x, r):
    x = np.asarray(x, dtype=float)
    c = math.expm1(r)
    # Transform s=z/(1-z) to make integration finite without large s;
    # alternative to a signed inclusion-exclusion sum.
    def integrand(u):
        s = u/(1-u)
        return (1+c)/c*math.exp(-s)*math.prod(-math.expm1(-c*xi*s) for xi in x)/(1-u)**2
    return quad(integrand, 0, 1, epsabs=2e-12, epsrel=1e-10, limit=400)[0]


def center_mass_beta(n, r):
    c = math.expm1(r)
    a = n/c
    return math.exp(math.log(a) + betaln(a,n))


def main():
    rng=np.random.default_rng(20261105)
    trials=[([.5,.5],.8),([.2,.8],1.5),([.2,.3,.5],1.2),([.6,.3,.1],.8),([.1,.15,.2,.25,.3],2.0)]
    for x,r in trials:
        expected=analytic_mass(x,r)
        n=len(x)
        m=300000
        y=rng.exponential(size=(m,n))
        y=y/np.sum(y,axis=1,keepdims=True)
        actual=np.mean(hilbert_distances(x,y)<=r)
        sigma=math.sqrt(max(1e-12,expected*(1-expected))/m)
        assert abs(actual-expected)<6*sigma+0.0008, (x,r,expected,actual,sigma)
        print('MC',n,r,'mass',round(expected,9),'simulated',round(actual,9))
    for n in range(2,11):
        x=[1/n]*n
        for r in [.3,1.,2.5]:
            q=analytic_mass(x,r)
            b=center_mass_beta(n,r)
            assert abs(q-b)<8e-10, (n,r,q,b)
    print('EXACT_CENTER_BETA_OK n=2..10 radii=3')
    for x,y in [([.6,.3,.1],[.45,.45,.1]),([.45,.45,.1],[1/3]*3),([.55,.25,.1,.1],[.4,.4,.1,.1])]:
        for r in [.2,1.,2.]:
            a,b=analytic_mass(x,r),analytic_mass(y,r)
            assert b>a+1e-12, (x,y,r,a,b)
    print('STRICT_BALANCING_CHECK_OK')
    for x in [[.2,.8],[.2,.3,.5],[.1,.15,.2,.25,.3]]:
        n=len(x)
        for r in [0.01,.004]:
            leading=math.factorial(n)*r**(n-1)*math.prod(x)
            observed=analytic_mass(x,r)
            assert abs(observed/leading-1)<0.1, (x,r,observed,leading)
    print('SHORT_RADIUS_COEFFICIENT_OK')
    # High-dimensional centering of Hilbert radius at barycenter.
    for n in [1000,10000]:
        for s in [-1.,0.,1.]:
            r=math.log(n)+math.log(math.log(n))+s
            q=center_mass_beta(n,r)
            g=math.exp(-math.exp(-s))
            assert abs(q-g)<.09,(n,s,q,g)
            print('GUMBEL_CENTER',n,s,round(q,6),round(g,6))
    print('HILBERT_SIMPLEX_EUCLIDEAN_BALL_MASS_OK')

if __name__=='__main__':
    main()

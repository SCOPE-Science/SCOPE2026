#!/usr/bin/env python3
"""Check finite Hilbert-distance laws against independently sampled simplex pairs.

Requires Python 3, NumPy and SciPy. All calculations are non-certifying
numerical sanity checks; the analytic proof is in RESULT.md.
"""
from math import exp, log, gamma, lgamma, pi
import numpy as np
from scipy.integrate import quad
from scipy.special import beta, betainc, hyp2f1


def law_cdf(n, alpha, r):
    """Integrate the exact beta-prime range law in the beta-coordinate."""
    assert n >= 2 and alpha > 0 and r >= 0
    q = exp(r)
    B = beta(alpha, alpha)
    def integrand(u):
        if not (0 < u < 1):
            return 0.
        v = q*u/(1-u+q*u)
        delta = max(0., betainc(alpha, alpha, v) - betainc(alpha, alpha, u))
        return u**(alpha-1)*(1-u)**(alpha-1)*delta**(n-1)/B
    val = n*quad(integrand,0,1,epsabs=2e-11,epsrel=2e-11, limit=200)[0]
    return val


def uniform_closed(n,r):
    a = np.expm1(r)
    return n*a**(n-1)*beta(n,n)*hyp2f1(n-1,n,2*n,-a)


def direct_pairs(n,alpha,count,rng):
    """Apply the metric to independent *normalized* gamma barycentric vectors."""
    X = rng.gamma(alpha,1,(count,n))
    Y = rng.gamma(alpha,1,(count,n))
    X /= X.sum(axis=1)[:,None]
    Y /= Y.sum(axis=1)[:,None]
    L = np.log(X)-np.log(Y)
    return L.max(axis=1)-L.min(axis=1)


def harmonic(k):
    return sum(1/i for i in range(1,k+1))


def main():
    rng=np.random.default_rng(2026110515)
    configurations=((2,1.),(3,1.),(5,1.),(4,2.),(8,.5))
    N=100000
    for n,alpha in configurations:
        d=direct_pairs(n,alpha,N,rng)
        for r in (1.,2.,4.):
            v=law_cdf(n,alpha,r)
            observed=float(np.mean(d<=r))
            assert abs(v-observed)<0.012,(n,alpha,r,v,observed)
            if alpha==1:
                assert abs(v-uniform_closed(n,r))<1e-9,(n,r,v,uniform_closed(n,r))
        if alpha==1:
            assert abs(float(d.mean())-2*harmonic(n-1))<0.045,(n,d.mean())
        print(f"FINITE n={n} alpha={alpha}: CDF, direct metric, exact-mean checks OK")
    for alpha in (.5,1.,2.):
        n=1200; N=6000
        d=direct_pairs(n,alpha,N,rng)
        c=exp(lgamma(2*alpha)-2*lgamma(alpha))/alpha
        target_mean=(2/alpha)*(log(n*c)+0.57721566490153286)
        target_var=pi*pi/(3*alpha*alpha)
        assert abs(float(d.mean())-target_mean)<0.38/alpha,(alpha,d.mean(),target_mean)
        assert abs(float(d.var())-target_var)<0.30/(alpha*alpha),(alpha,d.var(),target_var)
        print(f"EXTREME alpha={alpha}: centered mean/variance, n=1200 consistency OK")
    for n,alpha in ((2,1.),(3,1.),(2,2.)):
        coeff = n*beta(n*alpha,n*alpha)/beta(alpha,alpha)**n
        for r in (.01,.02):
            ratio = law_cdf(n,alpha,r)/(r**(n-1))
            assert abs(ratio/coeff-1)<0.07,(n,alpha,r,ratio,coeff)
    print("HILBERT_DIRICHLET_RANGE_VERIFIED_FINITE_CDF_AND_LIMIT_SANITY")

if __name__=='__main__':
    main()

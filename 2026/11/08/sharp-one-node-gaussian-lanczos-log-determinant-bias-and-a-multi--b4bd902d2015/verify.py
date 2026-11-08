"""Reproduce one-node Gaussian Lanczos log-determinant bias calculations.

Python 3 standard library only. These finite checks supplement analytic proofs.
"""
from math import sin,cos,pi,log,log1p,lgamma,exp,sqrt,cosh
from random import Random
from itertools import product


def b_exact(n, j, kappa, intervals=4096):
    """Beta-law integral, transformed to a smooth angular quadrature."""
    assert n >= 2 and 1 <= j < n and kappa > 1 and intervals % 2 == 0
    a, b = j/2.0, (n-j)/2.0
    inv_beta = exp(lgamma(a+b)-lgamma(a)-lgamma(b))
    def fun(theta):
        s,c=sin(theta),cos(theta)
        return 2.0*inv_beta*s**(j-1)*c**(n-j-1)*log1p((kappa-1)*s*s)
    h=(pi/2)/intervals
    integral=h/3*(fun(0)+fun(pi/2)+4*sum(fun(h*i) for i in range(1,intervals,2))+2*sum(fun(h*i) for i in range(2,intervals-1,2)))
    return n*integral - j*log(kappa)


def bias_monte_carlo(eigs, rng, samples=30000):
    n=len(eigs)
    total=0.0
    for _ in range(samples):
        g=[rng.gauss(0,1) for _ in eigs]
        weights=[v*v for v in g]
        norm=sum(weights)
        total+=norm*log(sum(a*w for a,w in zip(eigs,weights))/norm)-sum(log(a) for a in eigs)
    return total/samples


def verify():
    checks=0
    for k in [1.01,1.1,1.5,2,4,10,50,1000]:
        analytic=4*log(cosh(log(k)/4))
        numeric=b_exact(2,1,k)
        assert abs(analytic-numeric) < 3e-9,(k,analytic,numeric)
        checks+=1
    # Deterministic endpoint theorem stress test on all 2^n endpoint spectra,
    # and 1,000 arbitrary nonendpoint spectra; no finite test establishes the theorem.
    rng=Random(20261103)
    for n in [2,3,4,5,6,7]:
        for k in [1.25,2,6,30]:
            entries=[b_exact(n,j,k,2048) for j in range(1,n)]
            maximum=max(entries)
            assert maximum>=0
            checks+=1
            for bits in product([1,k],repeat=n):
                if min(bits)==max(bits):
                    assert 0 <= maximum
                else:
                    assert b_exact(n,sum(a>1 for a in bits),k,512) <= maximum+1e-8
                checks+=1
            # Gaussian spectra trial of the proposed sharp extremizers
            for _ in range(120):
                x=[rng.random()*log(k) for _ in range(n)]
                l=[exp(z) for z in x]
                # Expected n*log of random sphere quadratic via a finite direction sample.
                # Tolerance is Monte Carlo; this is a weak numerical stress test only.
                sample=0.0
                for __ in range(800):
                    w=[rng.gauss(0,1)**2 for i in range(n)]
                    sample+=n*log(sum(a*v for a,v in zip(l,w))/sum(w)) -sum(x)
                sample/=800
                assert sample < maximum+0.55,(n,k,sample,maximum)
                checks+=1
    # The asymptotic and small condition-number multiplicity phase distinction.
    for n in [4,5,6,7,8]:
        near=[b_exact(n,j,1.04,8192) for j in range(1,n)]
        far=[b_exact(n,j,1e7,8192) for j in range(1,n)]
        assert 1+near.index(max(near)) == n//2,(n,near)
        assert 1+far.index(max(far)) == 1,(n,far)
        checks+=2
    # Monte Carlo is only a cross-check of the exact expectation law.
    for n,j,k in [(2,1,3),(4,1,50),(4,2,10),(5,2,2)]:
        target=b_exact(n,j,k)
        mc=bias_monte_carlo([k]*j+[1]*(n-j),rng)
        assert abs(mc-target) < 0.17,(n,j,k,mc,target)
        checks+=1
    print('VERIFY_OK',checks)
    for n,k in [(2,2),(4,2),(4,50),(5,50),(8,1000)]:
        vals=[b_exact(n,j,k) for j in range(1,n)]
        print('n',n,'kappa',k,'maximizing_j',vals.index(max(vals))+1,'max_bias',format(max(vals),'.12f'))

if __name__=='__main__':
    verify()

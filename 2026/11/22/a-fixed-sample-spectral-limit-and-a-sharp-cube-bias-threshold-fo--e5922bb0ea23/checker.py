#!/usr/bin/env python3
"""Reproducible numerical checks for a fixed-sample spherical spectral test.

The mathematical arguments in RESULT.md, not these finite checks, prove the limits.
Requires numpy and scipy. Run with: python checker.py
"""
import itertools
import math

import numpy as np
from scipy.stats import beta, binom, norm


def t_from_gram(u):
    """Source beta=2 statistic via a Gram matrix, for d>=2n."""
    n, d = u.shape
    assert d >= 2 * n
    gram = u @ u.T
    lam = np.linalg.eigvalsh(gram)[-1]
    return (lam - n / d) ** 2 / n


def t_from_full_covariance(u):
    n, d = u.shape
    scatter = u.T @ u / n
    delta = scatter - np.eye(d) / d
    return n * np.linalg.norm(delta, ord=2) ** 2


def critical_abs_inner(d, alpha):
    return math.sqrt(beta.ppf(1.0 - alpha, 0.5, (d - 1) / 2))


def exact_n2_power(d, alpha, mu):
    c = d * critical_abs_inner(d, alpha)
    p = (1 + mu * mu) / 2
    # Exact finite binomial sum, with strict rejection for a discontinuous alternative.
    return sum(binom.pmf(k, d, p) for k in range(d+1) if abs(2*k-d)>c)


def n2_limit_power(c, alpha=0.05):
    q = norm.ppf(1-alpha/2)
    return norm.sf(q-c*c) + norm.cdf(-q-c*c)


def enumerate_edge_covariances(n, mu):
    """Exhaustive finite algebraic moments for all sign configurations."""
    edges = list(itertools.combinations(range(n), 2))
    r = len(edges)
    mean = np.zeros(r)
    second = np.zeros((r,r))
    for signs in itertools.product((-1,1), repeat=n):
        s = np.array(signs, dtype=float)
        p = math.prod((1 + mu * int(x))/2 for x in signs)
        e = np.array([s[i]*s[j] for i,j in edges])
        mean += p*e
        second += p*np.outer(e,e)
    return edges,mean,second-np.outer(mean,mean)


def main():
    rng = np.random.default_rng(20261117)
    assertions = 0
    # Exact finite Gram-vs-full scatter formula for both sign and sphere directions.
    for n,d in ((2,4),(2,7),(3,6),(3,10),(4,8),(4,12)):
        for _ in range(5):
            u = rng.normal(size=(n,d));u /= np.linalg.norm(u,axis=1)[:,None]
            assert np.isclose(t_from_gram(u),t_from_full_covariance(u),rtol=1e-9,atol=1e-10)
            assertions += 1
    # Special exact two-observation formula, including extreme pairings.
    for d in (4,5,8,17,64):
        for _ in range(40):
            u=rng.choice([-1.,1.],size=(2,d))/math.sqrt(d)
            r=float(u[0]@u[1]);direct=t_from_gram(u)
            assert np.isclose(direct,(1+abs(r)-2/d)**2/2,atol=1e-12)
            assertions += 1
    # Entire edge covariance for nonzero bias: identity, shared, and disjoint edges.
    for n in (3,4,5):
        for mu in (0.0,0.15,0.4):
            edges,means,cov=enumerate_edge_covariances(n,mu)
            assert np.allclose(means,mu*mu,atol=1e-13)
            assertions+=len(means)
            for a,e in enumerate(edges):
                for b,f in enumerate(edges):
                    expected=(1-mu**4 if a==b else (mu*mu-mu**4 if set(e)&set(f) else 0.0))
                    assert abs(cov[a,b]-expected)<1e-12
                    assertions+=1
    # Exact null Beta quantile, exact binomial power and Gaussian local limit.
    alpha=.05
    for d in (64,256,1024,4096):
        q=critical_abs_inner(d,alpha)
        assert abs(beta.cdf(q*q,.5,(d-1)/2)-(1-alpha))<1e-11
        assertions+=1
        mu=d**(-.25)
        power=exact_n2_power(d,alpha,mu)
        assert 0 < power < 1
        assertions+=1
        print(f'd={d}: critical |r|={q:.12f}, local c=1 exact power={power:.12f}')
    limiting=n2_limit_power(1.,alpha)
    assert abs(limiting-0.17007504575308752)<1e-12
    assertions+=1
    assert abs(n2_limit_power(0,alpha)-alpha)<1e-14
    assertions+=1
    for c in (0,.1,.5,1,1.5,2,3):
        power=n2_limit_power(c,alpha)
        assert 0 <= power <= 1
        assertions+=1
    # Fixed-n, high-d Gram CLT: compare independent off-diagonal covariance empirically.
    n=3;d=512;rep=3000
    # Pairwise biased-product signs, in the local regime.
    mu=d**(-.25)
    u=rng.choice([-1.,1.],size=(rep,d,n),p=[(1-mu)/2,(1+mu)/2])
    edges=((0,1),(0,2),(1,2))
    x=np.column_stack([np.sum(u[:,:,i]*u[:,:,j],axis=1)/math.sqrt(d) for i,j in edges])
    theoretical_cov=np.eye(3)*(1-mu**4)+(np.ones((3,3))-np.eye(3))*(mu*mu-mu**4)
    assert np.max(abs(x.mean(axis=0)-math.sqrt(d)*mu*mu))<0.07
    assertions+=3
    assert np.max(abs(np.cov(x,rowvar=False)-theoretical_cov))<0.08
    assertions+=9
    print(f'n=2, alpha=0.05, c=1: limiting power={limiting:.12f}')
    print(f'{assertions} deterministic assertions passed; simulation is supplementary only.')

if __name__=='__main__':
    main()

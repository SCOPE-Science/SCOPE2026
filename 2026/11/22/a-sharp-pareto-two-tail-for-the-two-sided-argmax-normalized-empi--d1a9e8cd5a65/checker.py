"""Standalone reproducibility checks for two-sided argmax-weighted uniform EDF tails.
Run: python3 checker.py
Requires Python 3.9+ standard library. All random checks have fixed seed.
"""
import itertools
import math
import random


def alpha(n, x):
    # Stable small root of (1/n-u)^2 = x^2 u(1-u).
    return (2.0 / (n*n)) / (x*x + 2.0/n + x*math.sqrt(x*x + 4.0*(n-1)/(n*n)))


def two_sided_score(points):
    u = sorted(points)
    n = len(u)
    ds = [max((j+1)/n-z, z-j/n) for j,z in enumerate(u)]
    r = max(range(n), key=lambda j: ds[j])
    return ds[r]/math.sqrt(u[r]*(1-u[r])), r


def corner_probability(n, x):
    a = alpha(n, x)
    assert 0 < a < 1/(2*n)
    # Stable evaluation: n! times integral_0^a (1/n-2u)^(n-1) du
    # via a binomial expansion to avoid cancellation at large x.
    v = 0.0
    from math import comb
    for k in range(n):
        v += comb(n-1,k) * (1/n)**(n-1-k) * (-2.0)**k * a**(k+1)/(k+1)
    return math.factorial(n)*v


def run():
    checks = 0
    for n in range(2, 10):
        c = 2*math.factorial(n-1)/(n**n)
        for x in (15, 30, 60, 120, 250):
            a = alpha(n,x)
            lhs = (1/n-a)**2
            rhs = x*x*a*(1-a)
            assert abs(lhs/rhs-1) < 1e-11, (n,x,lhs,rhs)
            checks += 1
            p = corner_probability(n,x)
            # corners account for all leading tail; relative difference is O(x^-2).
            assert abs((2*p*x*x)/c-1) < 0.08, (n,x,2*p*x*x,c)
            checks += 1
        assert c > 0
        checks += 1
    # Exact categorical count for limiting corner geometry: one observation
    # in each of bins 2,...,n; no points in bin 1.
    for n in range(2, 7):
        count = sum(1 for tup in itertools.product(range(n), repeat=n-1)
                    if sorted(tup) == list(range(1,n)))
        assert count == math.factorial(n-1), (n,count)
        checks += 1
    # Independent direct simulation of the complete statistic; noncorner
    # configurations contribute at order x^-4 and simulations have noise.
    rng = random.Random(13579)
    for n,x,m,tol in ((2,10.0,500_000,0.13), (3,10.0,700_000,0.20),
                      (4,10.0,1_000_000,0.27)):
        hit = 0
        for _ in range(m):
            val,rank = two_sided_score([rng.random() for _ in range(n)])
            hit += (val>x)
        est = hit/m
        asymptotic = 2*math.factorial(n-1)/(n**n*x*x)
        assert abs(est/asymptotic-1) < tol, (n,hit,m,est,asymptotic)
        checks += 1
        print('Monte Carlo n=%d, threshold=%.1f, observed=%.8g, tail-equivalent=%.8g, hits=%d' %
              (n,x,est,asymptotic,hit))
    print('%d checks passed' % checks)

if __name__ == '__main__':
    run()

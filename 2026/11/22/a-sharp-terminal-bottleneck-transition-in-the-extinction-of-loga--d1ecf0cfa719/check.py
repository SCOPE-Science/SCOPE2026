#!/usr/bin/env python3
"""Reproduce finite-state and numerical checks for the equal-domain erosion theorem.
Uses only the Python standard library. Finite checks are NOT an infinite proof.
"""
from fractions import Fraction
import math
import random


def poisson_cdf_le(k, mu):
    if k < 0:
        return 0.0
    if mu == 0:
        return 1.0
    p = math.exp(-mu + k*math.log(mu) - math.lgamma(k+1))
    out = p
    for j in range(k, 0, -1):
        p *= j/mu
        out += p
    return min(1.0, out)


def poisson_tail_ge(k, mu):
    if k <= 0:
        return 1.0
    if mu == 0:
        return 0.0
    if k <= mu:
        return max(0.0, 1.0-poisson_cdf_le(k-1, mu))
    p = math.exp(-mu + k*math.log(mu) - math.lgamma(k+1))
    out, j = p, k
    for _ in range(10000):
        j += 1
        p *= mu/j
        out += p
        if p < out*1e-15:
            break
    return min(1.0, out)


def domain_survival(n, t):
    assert n >= 2 and t >= 0
    if t == 0:
        return 1.0
    k = n-1
    return poisson_cdf_le(k-1, 2*t) + math.exp(k*math.log(2)-t)*poisson_tail_ge(k, t)


def rate(x):
    assert x > 0.5
    return 2*x-1-math.log(2*x) if x <= 1 else x-math.log(2)


def predicted(alpha):
    assert alpha > 0
    if alpha >= 1-math.log(2):
        return alpha+math.log(2)
    lo, hi = .5, 1.
    for _ in range(70):
        mid = (lo+hi)/2
        if rate(mid) < alpha:
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2


def hitting_laplace(initial, s):
    """Exact independent-rate-1 clocks, arbitrary binary ring state (1=down)."""
    memo = {}
    N = len(initial)
    def rec(state):
        if sum(state) == 0:
            return Fraction(1)
        if state in memo:
            return memo[state]
        live = [j for j in range(N) if state[j] and (not state[(j-1)%N] or not state[(j+1)%N])]
        assert live
        ans = Fraction(0)
        for j in live:
            nxt = list(state)
            nxt[j] = 0
            ans += rec(tuple(nxt))
        ans /= (s+len(live))
        memo[state] = ans
        return ans
    return rec(tuple(initial))


def test():
    checks = 0
    # Independent proof-path verification on the true finite-state generator.
    for n in range(2,8):
        for s in [Fraction(1,2),Fraction(1),Fraction(3)]:
            got = hitting_laplace([0]+[1]*n+[0],s)
            want = Fraction(1,1)/(1+s)*(Fraction(2,1)/(2+s))**(n-1)
            assert got == want,(n,s,got,want)
            checks += 1
    # Exact 2-spin expression, and monotone normalized survivals.
    for t in [0.01,0.1,0.5,1.0,2.0,6.0,10.0]:
        assert abs(domain_survival(2,t)-(2*math.exp(-t)-math.exp(-2*t))) < 2e-13
        checks += 1
    for n in [2,3,5,12,50,200]:
        ts = [j*(n+1)/12 for j in range(1,41)]
        a = [domain_survival(n,t) for t in ts]
        assert all(0 <= z <= 1+1e-10 for z in a)
        assert all(a[j] >= a[j+1]-1e-11 for j in range(len(a)-1))
        checks += 1
    # Probability is exactly a product for noninteracting separated domains.
    for n in [2,3,4]:
        for m in [1,2,5]:
            t = n/2+1
            cdf = (1-domain_survival(n,t))**m
            assert 0 <= cdf <= 1
            checks += 1
    # The finite-n exponential-rate estimates converge toward the derived LDP.
    for x in [0.7,0.85,1.0,1.1,1.5]:
        err = []
        for n in [50,100,200,400]:
            val = domain_survival(n,n*x)
            assert val > 0
            err.append(abs(-math.log(val)/n-rate(x)))
            checks += 1
        assert err[-1] < 0.008 and all(err[j] > err[j+1] for j in range(3)),(x,err)
        checks += 1
    # Unique tail-rate optimizer, two regimes and their matching boundary.
    crit = 1-math.log(2)
    assert abs(predicted(crit)-1) < 2e-14
    for alpha in [.05,.1,.2,crit,.4,.6,.9]:
        x = predicted(alpha)
        assert abs(rate(x)-alpha) < 3e-13
        assert (x >= 1) == (alpha >= crit)
        gstar, estar = min(x,1.),max(0.,x-1.)
        def J(g,e):
            return 2*g-1-math.log(2*g)+e
        # Check the joint-rate minimum over g+e=x on a grid.
        assert abs(J(gstar,estar)-alpha) < 3e-13
        for q in range(1,1000):
            g = x*q/1000
            e = x-g
            assert J(g,e) >= alpha-1e-12
        checks += 1
    # Simulated finite-domain survival versus independent analytic convolution.
    rng=random.Random(4412)
    for n,t in [(2,1.0),(4,2.5),(7,4.0),(12,6.3)]:
        trials=25000
        exceed = 0
        for _ in range(trials):
            v = sum(rng.expovariate(2) for i in range(n-1))+rng.expovariate(1)
            exceed += (v > t)
        assert abs(exceed/trials-domain_survival(n,t)) < .023,(n,t,exceed/trials,domain_survival(n,t))
        checks += 1
    print('PASS',checks,'finite generator, distribution, LDP-rate and sampling checks')
    print('critical alpha',crit,'critical c',1/crit)
    for alpha in [.1,.2,crit,.5,.8]:
        x=predicted(alpha)
        print('alpha',round(alpha,9),'limit',round(x,9),'bulk',round(min(x,1),9),'last',round(max(x-1,0),9))

if __name__ == '__main__':
    test()

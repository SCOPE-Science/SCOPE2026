#!/usr/bin/env python3
"""Standalone finite checks for a single-resource contribution-fairness theorem.

All scientific outputs are recomputed from formulas; simulations only corroborate
analytic identities and do not certify any infinite-population limit.
"""
import itertools
import math
import random
from fractions import Fraction


def via_spacings(vals):
    v = sorted(vals)
    n = len(v)
    v0 = 0
    shapley = []
    a = 0.0
    for j, x in enumerate(v):
        a += (x-v0)/(n-j)
        shapley.append(a)
        v0 = x
    return sum(shapley[j]/v[j] for j in range(n))


def via_pairs(vals):
    v = sorted(vals)
    n = len(v)
    h = sum(1.0/j for j in range(1, n+1))
    return h-sum(v[r]/v[j]/((n-r-1)*(n-r))
                 for r in range(n-1) for j in range(r+1,n))


def by_permutations(vals):
    n = len(vals)
    sh = [0.0]*n
    for p in itertools.permutations(range(n)):
        best=0
        for i in p:
            incr=max(best,vals[i])-best
            sh[i]+=incr/math.factorial(n)
            best=max(best, vals[i])
    return sum(sh[i]/vals[i] for i in range(n))


def uniform_exact(n):
    # For ordered uniform samples E[U_(r)/U_(j)] = r/j.
    h = sum((Fraction(1,j) for j in range(1,n+1)), Fraction())
    return h-sum((Fraction(r,j*(n-r)*(n-r+1))
                  for r in range(1,n) for j in range(r+1,n+1)),Fraction())


def power_exact(n,s):
    # E[(U_(r)/U_(j))^s] = product_{h=r}^{j-1} h/(h+s).
    h = sum(1.0/j for j in range(1,n+1))
    q = 0.0
    for r in range(1,n):
        ratio = 1.0
        for j in range(r+1,n+1):
            ratio *= (j-1)/(j-1+s)
            q += ratio/((n-r)*(n-r+1))
    return h-q


def limiting(s):
    # positive series C_s = sum_{m>=1} s/[m(m+s-1)]
    # Use the digamma form when available for high precision.
    import mpmath as mp
    return float(s*(mp.digamma(s)+mp.euler)/(s-1)) if s != 1 else math.pi**2/6


def main():
    checks=0
    for n in range(1,8):
        for k in range(12):
            vals=[(3+((i*13+k*17+i*k*5)%67))/67 for i in range(n)]
            a=via_spacings(vals)
            b=via_pairs(vals)
            assert abs(a-b)<3e-12,(n,k,a,b)
            if n<=6:
                c=by_permutations(vals)
                assert abs(a-c)<3e-12,(n,k,a,c)
            checks+=2 if n<=6 else 1
    for n in range(1,101):
        h2 = sum((Fraction(1,j*j) for j in range(1,n+1)),Fraction())
        assert uniform_exact(n)==h2
        assert abs(power_exact(n,1.0)-float(h2))<3e-12
        checks+=2
    for s in [0.25,0.5,1,1.5,2,3,5,12]:
        assert abs(power_exact(2,s)-(1.5-0.5/(s+1)))<1e-12
        checks+=1
    rng=random.Random(14021211)
    for n in [2,3,4,5,8,12,20,35]:
        for rep in range(35):
            u=sorted(rng.random() for _ in range(n))
            ff=[via_pairs([x**s for x in u]) for s in [0.25,0.5,1,2,4]]
            assert all(ff[i]<ff[i+1] for i in range(4))
            assert 1<=ff[0] and ff[-1]<sum(1/j for j in range(1,n+1))+1e-12
            checks+=2
    for n in range(1,101):
        assert abs(power_exact(n,2)-2*n/(n+1))<5e-12
        assert abs(power_exact(n,3)-3*n*(3*n+5)/(4*(n+1)*(n+2)))<5e-12
        checks+=2
    for s in [0.5,1,2,3]:
        # Precomputed analytic values for the power-law limiting curve.
        target={0.5:2*math.log(2),1:math.pi**2/6,2:2.0,3:2.25}[s]
        assert abs(limiting(s)-target)<3e-12
        checks+=1
    # Seeded simulations check expected finite-n values, with explicit tolerances.
    for n, reps in [(5,30000),(25,10000),(80,6000)]:
        for s in [0.5,1,2]:
            sm = 0.0
            for _ in range(reps):
                sm += via_spacings([rng.random()**s for _ in range(n)])
            empirical=sm/reps
            exact=power_exact(n,s)
            assert abs(empirical-exact)<0.03,(n,s,empirical,exact)
            print('sample', n,s,'empirical',round(empirical,6),'exact_mean',round(exact,6), 'limit',round(limiting(s),6))
            checks+=1
    print('PASS',checks,'checks; finite comparisons are not a proof of asymptotic convergence')

if __name__=='__main__':
    main()

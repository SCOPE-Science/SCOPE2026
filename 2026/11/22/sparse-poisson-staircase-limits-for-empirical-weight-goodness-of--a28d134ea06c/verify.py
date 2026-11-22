"""Numerical and exact algebraic consistency checks for sparse Poisson-weight limits.

This script checks finite-count formulas and distribution approximations. It does not
substitute for the analytical proof of the triangular-array theorems.
"""
from __future__ import annotations
import math
from itertools import product

CHECKS = 0

def check(condition, detail=''):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(detail or f'check {CHECKS}')

def poisson_prob(lam, k):
    return math.exp(-lam) * lam**k / math.factorial(k)

def distance_from_counts(counts, p, a=1., weight='fixed'):
    n = sum(counts)
    lhat = sum(k*c for k,c in enumerate(counts)) / n
    assert lhat > 0
    m = len(counts)-1
    while m>0 and counts[m]==0: m-=1
    empirical = [x/n for x in counts]
    fitted = [poisson_prob(lhat,k) for k in range(len(counts))]
    # The tail is EXACT for fixed and fitted weights, not truncated.
    terms = []
    for k in range(m+1):
        w = empirical[k]/fitted[k]
        g = math.exp(-a*k) if weight=='fixed' else fitted[k] if weight=='fitted' else empirical[k]
        terms.append((g, abs(w-1)))
    if weight=='fixed':
        tail_sum=math.exp(-a*(m+1))/(1-math.exp(-a))
        tail_sup=math.exp(-a*(m+1))
    elif weight=='fitted':
        tail_sum=1-sum(fitted[:m+1]);tail_sup=poisson_prob(lhat,m+1)
        check(tail_sum >= -1.e-12)
    else:
        tail_sum=0.;tail_sup=0.
    return {
        1:sum(g*d for g,d in terms)+tail_sum,
        2:math.sqrt(sum(g*d*d for g,d in terms)+tail_sum),
        math.inf:max([g*d for g,d in terms]+[tail_sup])
    }

def critical_limit(z,r,c,a=1.):
    val=math.factorial(r)*z/c
    tail=math.exp(-a*(r+1))/(1-math.exp(-a))
    return {1:math.exp(-a*r)*abs(val-1)+tail,
            2:math.sqrt(math.exp(-a*r)*(val-1)**2+tail),
            math.inf:max(math.exp(-a*r)*abs(val-1),math.exp(-a*(r+1)))}

# Exact missing-cell tail identity, across all low-maximum possibilities.
for a in [0.4,1.0,2.0]:
    for m in range(1,11):
        exact=math.exp(-a*(m+1))/(1-math.exp(-a))
        partial=sum(math.exp(-a*k) for k in range(m+1,m+401))
        check(abs(exact-partial)<2e-13)

# Critical n*lambda^2 -> 2; the rare count in cell two has Poisson(1) law.
for n in [5000,50000,500000]:
    lam=math.sqrt(2/n)
    q2=poisson_prob(lam,2)
    for z in range(7):
        exact=math.comb(n,z)*q2**z*(1-q2)**(n-z)
        limit=poisson_prob(1.,z)
        check(abs(exact-limit) < 0.035 if n==5000 else abs(exact-limit)<0.015 if n==50000 else abs(exact-limit)<0.005)
    check(abs(n*q2-1.)<0.04)

# Construct representative histograms with all counts <= 2 and fixed rare-cell count.
# Bulk counts use the Poisson expectation and automatically refit the mean.
for r,c in [(2,2.),(3,6.)]:
    n=3_000_000
    lam=(c/n)**(1/r)
    expect=[n*poisson_prob(lam,k) for k in range(r+1)]
    for z in range(5):
        ns=[round(e) for e in expect]
        ns[-1]=z
        ns[0]=n-sum(ns[1:])
        check(ns[0]>0)
        for a in [0.7,1.,1.5]:
            actual=distance_from_counts(ns,math.inf,a,'fixed')
            target=critical_limit(z,r,c,a)
            for p in [1,2,math.inf]:
                check(abs(actual[p]-target[p])<0.02, f'{r=} {z=} {a=} {p=} {actual[p]=} {target[p]=}')
            for w in ['fitted','empirical']:
                adaptive=distance_from_counts(ns,math.inf,a,w)
                for p in [1,2,math.inf]:
                    check(adaptive[p]<0.02,f'{r=} {z=} {w=} {p=} {adaptive[p]=}')

# The centered rare-cell law has a real atom; explicit representative probabilities.
check(abs(sum(poisson_prob(1,z) for z in range(30))-1)<1e-12)
check(abs(critical_limit(1,2,2)[1]-math.exp(-3)/(1-math.exp(-1)))<1e-14)
check(abs(poisson_prob(1,1)-math.exp(-1))<1e-14)

print(f'passed {CHECKS} formula/finite-array checks')
print('r=2, c=2, a=1: floor',format(critical_limit(1,2,2)[1],'.15g'))
print('rare-cell atom P(Z=1)',format(poisson_prob(1,1),'.15g'))

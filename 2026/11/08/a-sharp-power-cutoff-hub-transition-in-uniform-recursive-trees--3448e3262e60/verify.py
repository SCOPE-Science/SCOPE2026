#!/usr/bin/env python3
"""Finite exact diagnostics for power-cutoff recursive-tree degrees.

All asymptotic and localization statements require their analytic proof;
this script checks finite stochastic identities and the defining phase equations.
"""
from fractions import Fraction
from itertools import product
from math import floor, log, isclose

checks = 0

def test(condition, message):
    global checks
    assert condition, message
    checks += 1


def allowed(m, gamma):
    return tuple(range(max(1, floor(m**gamma)), m+1))


def exact_tree_degree_distribution(n, gamma):
    sets = [allowed(m, gamma) for m in range(1, n)]
    denominator = 1
    for z in sets:
        denominator *= len(z)
    degree_vectors = {}
    for choices in product(*sets):
        d = [0] * n
        for parent in choices:
            d[parent - 1] += 1
        d = tuple(d)
        degree_vectors[d] = degree_vectors.get(d, 0) + 1
    test(sum(degree_vectors.values()) == denominator, 'complete enumeration')
    return degree_vectors, denominator


for gamma in (0.2, 0.5, 0.8):
    for n in range(2, 9):
        dist, total = exact_tree_degree_distribution(n, gamma)
        test(all(sum(ds) == n-1 for ds in dist), 'each tree has n-1 edges')
        means = [sum(Fraction(count*ds[v],total) for ds,count in dist.items())
                 for v in range(n)]
        for v in range(1,n+1):
            p = sum((Fraction(1,len(allowed(m,gamma)))
                    for m in range(v,n) if v in allowed(m,gamma)),Fraction())
            test(means[v-1] == p, 'exact mean from independent parent choices')
        for u in range(n):
            for v in range(u+1,n):
                maxu = max(x[u] for x in dist)
                maxv = max(x[v] for x in dist)
                for a in range(1,maxu+1):
                    pa = sum((count for ds,count in dist.items() if ds[u] >= a),0)
                    for b in range(1,maxv+1):
                        pb = sum((count for ds,count in dist.items() if ds[v] >= b),0)
                        pab = sum((count for ds,count in dist.items()
                                   if ds[u] >= a and ds[v] >= b),0)
                        test(pab*total <= pa*pb, 'negative quadrant dependence')


gamma_critical = 1-1/(2*log(2))
t0 = 1/log(2)

def rate(t,c):
    if c == 0:
        return float('inf') if t > 0 else 0.
    return t*log(t/c)-t+c


def coefficient(gamma):
    if gamma <= gamma_critical:
        return t0
    low, high = 2*(1-gamma), t0
    for i in range(150):
        mid = (low+high)/2
        if rate(mid,1-gamma) < gamma:
            low = mid
        else:
            high = mid
    return (low+high)/2


def profile(a,gamma):
    return min(1.,a/gamma)-a

for gamma in (0.02,0.10,0.25,gamma_critical,0.3,0.5,0.7,0.9,0.99):
    t = coefficient(gamma)
    hub = max(gamma,gamma_critical)
    test(isclose(rate(t,profile(hub,gamma)),hub,abs_tol=1e-10),
         'root of variational equation')
    for j in range(1,2000):
        a = j/2000
        test(a-rate(t,profile(a,gamma)) < 2e-8,
             'rate balance nonpositive at the solved threshold')
    test(isclose(t,t0,abs_tol=1e-12) if gamma<=gamma_critical else t<t0,
         'piecewise maximum-degree coefficient')

test(isclose(coefficient(0.5), 0.5*2.718281828459045, rel_tol=1e-12),
     'half-power coefficient e/2')
print('CHECKS_PASSED',checks)
print('GAMMA_CRITICAL',format(gamma_critical,'.15f'))
for gamma in (0.1,0.3,0.5,0.8):
    print('GAMMA',gamma,'MAX_DEGREE_COEFFICIENT',format(coefficient(gamma),'.12f'),
          'HUB_EXPONENT',format(max(gamma,gamma_critical),'.12f'))

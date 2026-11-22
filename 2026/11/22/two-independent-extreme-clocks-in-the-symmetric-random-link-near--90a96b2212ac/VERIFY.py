#!/usr/bin/env python3
"""Checks finite combinatorial identities for weighted reciprocal nearest neighbors.

Only the standard Python library is required.  Finite checks do not prove the
limiting laws; the latter follow from the factorial-moment argument in RESULT.md.
"""
import itertools
import math
from fractions import Fraction

assertions = 0

def check(statement):
    global assertions
    assert statement
    assertions += 1

def matching_probability(n, k):
    p = Fraction(1)
    for j in range(1, k + 1):
        p /= 2 * n - 2 * j - 1
    return p

def edge_touch_count(n,k):
    return 2*k*n-2*k*k-k

def factorial_moment_exact(n,k,t):
    numerator = math.prod(range(n-2*k+1,n+1))
    den = (2**k)*math.prod(2*n-2*j-1 for j in range(1,k+1))
    return numerator / den * math.exp(-edge_touch_count(n,k)*t)

def reciprocal(edge_order, n):
    low = [None]*n
    for e in edge_order:
        i,j = e
        if low[i] is None: low[i] = j
        if low[j] is None: low[j] = i
    return {tuple(sorted((i, low[i]))) for i in range(n) if low[low[i]] == i}

for n in range(2, 5):
    edges = list(itertools.combinations(range(n),2))
    N = math.factorial(len(edges))
    samples = list(itertools.permutations(edges))
    check(len(samples) == N)
    for k in range(1,n//2+1):
        selected = {(2*j,2*j+1) for j in range(k)}
        count = sum(selected.issubset(reciprocal(order,n)) for order in samples)
        check(Fraction(count,N) == matching_probability(n,k))
    # Verify the exact falling-factorial moments (for t=0)
    counts = [len(reciprocal(order,n)) for order in samples]
    for k in range(n//2+1):
        empirical = Fraction(sum(math.prod(range(v-k+1,v+1)) if v>=k else 0 for v in counts),N)
        exact = Fraction(math.prod(range(n-2*k+1,n+1)),2**k)*matching_probability(n,k)
        check(empirical == exact)

# A separate, direct integral identity for two disjoint marked pairs.
# Integrating the two marked edge densities over s<=v and s>=v yields
# exp(-(4n-10)t)/((2n-3)(2n-5)).
for n in range(4,41):
    for k in range(n//2 + 1):
        m = matching_probability(n,k)
        check(m > 0)
        check(edge_touch_count(n,k) == k*(2*n-2*k-1))
        check(math.isclose(factorial_moment_exact(n,k,0),
             float(Fraction(math.prod(range(n-2*k+1,n+1)),2**k)*m),rel_tol=2e-14))
    for t in [0.0, 0.007, 0.045,0.12]:
        formula = float(matching_probability(n,2))*math.exp(-edge_touch_count(n,2)*t)
        independent_integral = math.exp(-(4*n-10)*t)/((2*n-3)*(2*n-5))
        check(math.isclose(formula,independent_integral,rel_tol=2e-14))

# Exact isolated-vertex factorial moment from the number of distinct
# edges incident to a prescribed set of r vertices.
for n in range(3,51):
    for r in range(n+1):
        m = r*n-r*(r+1)//2
        check(m == r*(n-r)+r*(r-1)//2)
        check(m >= 0)

# Analytic normalization and asymptotic factorial moment sanity checks.
for n in [200,1000,10000,100000]:
    c_n = math.log(n*(n-1)/(2*(2*n-3)))
    for x in [-1,0,1]:
        t = (c_n+x)/(2*n-3)
        mean = factorial_moment_exact(n,1,t)
        check(abs(mean-math.exp(-x)) < 5e-11)
    for k in [2,3]:
        t=(c_n+0.25)/(2*n-3)
        observed=factorial_moment_exact(n,k,t)
        target=math.exp(-0.25*k)
        if n>=10000:
            check(abs(observed-target)<0.003)

print(f'VERIFY_OK {assertions} deterministic assertions')

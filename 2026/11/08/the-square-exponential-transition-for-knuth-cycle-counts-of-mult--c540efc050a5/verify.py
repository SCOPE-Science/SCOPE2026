#!/usr/bin/env python3
"""Reproducible arithmetic checks for multiset cycle-increment laws.

No finite check is used as a proof of the asymptotic theorem.
"""
from fractions import Fraction
from math import comb, ceil, exp, log, sqrt
from itertools import combinations

checks = 0

def require(condition, message):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(message)

def pmf(m, n):
    # The first symbol (m=0) creates n singleton cycles.
    if m == 0:
        return [Fraction(int(k == n)) for k in range(n + 1)]
    normalizer = comb(m + n, n)
    return [Fraction(comb(m - 1 + n - k, n - k), normalizer)
            for k in range(n + 1)]

def exact_moments(m, n):
    p = pmf(m, n)
    avg = sum(k * pk for k, pk in enumerate(p))
    var = sum((k - avg)**2 * pk for k, pk in enumerate(p))
    return avg, var

def independent_urn_counts(m, n):
    # Count all binary words with m successful objects and n failed objects.
    total = m + n
    counts = [0] * (n + 1)
    for positions in combinations(range(total), m):
        first_success = positions[0]
        counts[first_success] += 1
    return [Fraction(a, comb(total, m)) for a in counts]

for m in range(0, 9):
    for n in range(1, 9):
        p = pmf(m, n)
        require(sum(p) == 1, 'PMF normalization')
        if m:
            require(p == independent_urn_counts(m, n), 'independent binary-word count')
        avg, var = exact_moments(m, n)
        require(avg == Fraction(n, m + 1), 'mean identity')
        expected_var = (Fraction(n * (m+n+1) * m, (m+1)**2 * (m+2))
                        if m else Fraction(0))
        require(var == expected_var, 'variance identity')

# Independently convolve marginal probabilities and compare the sum of exact
# means and variances to product-polynomial logarithmic derivatives.
for mult in ([1,1,1], [2,1,3], [3,2,4], [1,4,2,3]):
    joint = [Fraction(1)]
    m = 0
    sum_mu = Fraction(0)
    sum_var = Fraction(0)
    for n in mult:
        p = pmf(m, n)
        new_joint = [Fraction(0)] * (len(joint)+len(p)-1)
        for i, u in enumerate(joint):
            for j, v in enumerate(p):
                new_joint[i+j] += u*v
        joint = new_joint
        mu, var = exact_moments(m, n)
        sum_mu += mu
        sum_var += var
        m += n
    mu = sum(k*u for k,u in enumerate(joint))
    var = sum((k-mu)**2*u for k,u in enumerate(joint))
    require(sum(joint)==1, 'joint normalization')
    require(mu==sum_mu, 'convolution mean')
    require(var==sum_var, 'convolution variance')

# The Laplace-product law of S=sum_{k>=0}q^k E_k has the moments
# (1-q)^{-1} and (1-q^2)^{-1}; check finite truncations numerically.
for q in [0.08, 0.3, 0.6, 0.9]:
    mean = sum(q**j for j in range(2000))
    var = sum(q**(2*j) for j in range(2000))
    require(abs(mean - 1/(1-q)) < 1e-10, 'critical mean series')
    require(abs(var - 1/(1-q*q)) < 1e-10, 'critical variance series')
    for s in [0.01,0.1,1.0,5.0]:
        laplace = 1.0
        for j in range(2000):
            laplace /= (1+s*q**j)
        require(0<laplace<=1, 'Laplace transform bounds')
        require(abs(laplace - exp(-s/(1-q))) <= s*s*10, 'Jensen second order sanity')

# Numerical end-point Laplace estimates: g_j=c(j^beta-(j-1)^beta),
# a_j=exp(g_j). The output is diagnostic; it does not certify limits.
def asymptotic_variance_ratio(beta, c, t):
    gs = [c*(j**beta - (j-1)**beta) for j in range(2, t+1)]
    top = gs[-1]
    return sum(exp(2*(x-top)) for x in gs)

for beta, c, t in [(1.4,.2,60000),(1.5,.4,700),(1.8,.3,1200),
                   (2.0,.4,100),(2.0,1.0,40),(2.5,.2,70),(3.0,.2,30)]:
    ratio = asymptotic_variance_ratio(beta,c,t)
    if beta < 2:
        prediction = t**(2-beta)/(2*c*beta*(beta-1))
    elif beta == 2:
        prediction = 1/(1-exp(-4*c))
    else:
        prediction = 1
    require(abs(ratio/prediction - 1)<.20,
            'variance phase diagnostic for beta=%s: %.4f / %.4f'%(beta,ratio,prediction))

# Exact large-integer moment checks for the critical sequence n_j=2^(j^2).
# The proposed limiting variable has mean 4/3 and variance 16/15.
N = 0
mean = Fraction(0)
variance = Fraction(0)
for j in range(1, 13):
    n = 2**(j*j)
    mean += Fraction(n, N+1)
    variance += Fraction(n*(N+n+1)*N, (N+1)**2*(N+2))
    if j >= 9:
        a = Fraction(n, N)
        require(abs(float(mean/a)-4/3)<0.001, 'exact critical mean')
        require(abs(float(variance/a**2)-16/15)<0.001,
                'exact critical variance')
    N += n

print('PASS', checks, 'exact and diagnostic assertions')

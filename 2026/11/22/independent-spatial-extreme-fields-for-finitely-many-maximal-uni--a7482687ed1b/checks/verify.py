#!/usr/bin/env python3
"""Deterministic finite tests for extreme consecutive-spacing calculations.

Requires only Python 3 standard library. This does not certify an asymptotic limit.
"""
import math
from fractions import Fraction

checks = 0

def check(condition, message):
    global checks
    assert condition, message
    checks += 1

def erlang_tail(k, x):
    if k == 0:
        return float(x < 0)
    if x <= 0:
        return 1.0
    return math.exp(-x)*sum(x**j/math.factorial(j) for j in range(k))

def gamma_density(k, x):
    if x < 0:
        return 0.0
    return x**(k-1)*math.exp(-x)/math.factorial(k-1)

def threshold(n, k, offset=0):
    return math.log(n)+(k-1)*math.log(math.log(n))-math.log(math.factorial(k-1))+offset

def midpoint_integral(fn, lo, hi, slices=12000):
    if hi <= lo:
        return 0.0
    step = (hi-lo)/slices
    return step*sum(fn(lo+(j+0.5)*step) for j in range(slices))

def overlapping_tail(k, ell, overlap, a, b):
    """Numerically integrate the exact shared-Erlang decomposition.
    A = shared + exclusive(k-overlap), B = shared + exclusive(ell-overlap).
    """
    assert 1<=overlap<=min(k,ell)
    def integrand(t):
        return gamma_density(overlap,t)*erlang_tail(k-overlap,a-t)*erlang_tail(ell-overlap,b-t)
    upper=max(a,b)
    cutpoints=sorted({0.0, max(0.0,min(a,upper)),max(0.0,min(b,upper)),upper})
    integral=sum(midpoint_integral(integrand,lo,hi) for lo,hi in zip(cutpoints,cutpoints[1:]))
    return integral+erlang_tail(overlap,upper)

# Erlang survival and convolution sanity checks against symbolic identities.
for k in range(1,7):
    for x in (0.1,0.5,1.0,2.0,5.0,9.0,18.0):
        check(0<erlang_tail(k,x)<1, ('tail range',k,x))
        if k>1:
            check(erlang_tail(k,x)>erlang_tail(k-1,x),('stochastic order',k,x))
for k in range(1,6):
    for j in range(10,35):
        x=j/4
        eps=1e-5
        slope=(erlang_tail(k,x+eps)-erlang_tail(k,x-eps))/(2*eps)
        check(abs(slope+gamma_density(k,x))<1e-8,('gamma tail derivative',k,x))

# Distinct overlapping windows always lose at least half a log-power.
for k in range(1,9):
    for ell in range(1,9):
        for h in range(1,min(k,ell)+1):
            if k==ell==h:
                continue
            exponent=(k+ell)/2-h
            check(exponent>=0.5,('overlap exponent',k,ell,h))

# Integral formula is exactly solvable for these nested/shifted pairs.
for n in (100,1000,10000,100000):
    a,b=threshold(n,1),threshold(n,2)
    exact=math.exp(-b)*(1+b-a)
    via_integral=overlapping_tail(1,2,1,a,b)
    check(abs(exact-via_integral)<2e-8,('1/2 nested',n,exact,via_integral))
    a,b=threshold(n,2),threshold(n,3)
    exact=erlang_tail(2,b)+math.exp(-b)*(b*b-a*a)/2
    via_integral=overlapping_tail(2,3,2,a,b)
    check(abs(exact-via_integral)<2e-8,('2/3 nested',n,exact,via_integral))
    a=threshold(n,2)
    exact=2*math.exp(-a)-math.exp(-2*a)
    via_integral=overlapping_tail(2,2,1,a,a)
    check(abs(exact-via_integral)<2e-8,('2/2 shifted',n,exact,via_integral))

# Verify predicted rare pair rates decrease along a large-n sequence.
for (k,ell,h) in ((1,2,1),(2,2,1),(2,3,2),(2,3,1),(3,4,3)):
    values=[]
    for n in (10000,100000,1000000):
        values.append(n*overlapping_tail(k,ell,h,threshold(n,k),threshold(n,ell)))
    check(values[2]<values[0],('rare-overlap decay',k,ell,h,values))

# The exact one-window tail normalization tends to unit exceedance intensity.
for k in range(1,7):
    ns=(10**8,10**14,10**24)
    vals=[n*erlang_tail(k,threshold(n,k)) for n in ns]
    check(max(abs(v-1) for v in vals)<1e-12 if k==1 else abs(vals[-1]-1)<abs(vals[0]-1),('intensity normalization',k,vals))

# Exhaustive combinatorial count: placing q disjoint intervals of length k
# on N independent coordinates has binomial(N-(k-1)q,q) choices.
from itertools import combinations
for N in range(3,11):
    for k in range(1,5):
        if k>N:
            continue
        starts=range(N-k+1)
        for q in range(1,min(4,len(starts))+1):
            exact=sum(all(b>=a+k for a,b in zip(ix,ix[1:])) for ix in combinations(starts,q))
            predicted=math.comb(N-(k-1)*q,q) if N-(k-1)*q>=q else 0
            check(exact==predicted,('disjoint windows',N,k,q,exact,predicted))

print(f'PASS: {checks} deterministic assertions; Erlang tails, overlap exponents, exact paired-tail identities, rare-pair decay and disjoint-window enumeration.')

#!/usr/bin/env python3
"""Standalone exact-rational checks for geometric-lag edge-count identities.

The mathematical proof uses independent geometrics and boundary-flow conservation;
these finite checks corroborate its algebra and finite-dimensional definitions.
"""
from fractions import Fraction as F
from itertools import product
from math import comb

checks = 0

def verify(statement):
    global checks
    if not statement:
        raise AssertionError('An exact identity failed')
    checks += 1

def poisson_binomial(probabilities):
    law = [F(1)]
    for p in probabilities:
        nxt = [F(0)] * (len(law) + 1)
        for k, a in enumerate(law):
            nxt[k] += a * (1 - p)
            nxt[k + 1] += a * p
        law = nxt
    return law

def moments(law):
    mu = sum(k * v for k, v in enumerate(law))
    var = sum((k-mu)**2 * v for k,v in enumerate(law))
    return mu, var

# Derive the stationary indegree covariance directly by summing independent
# categorical trials at each later source, then compare with the formula.
for r in [F(1,2), F(1,3), F(2,3), F(3,4)]:
    for m in [1, 2, 3]:
        p = lambda h: (1-r)*r**(h-1)
        verify(sum(p(h) for h in range(1, 81)) == 1-r**80)
        # The geometric tails here are evaluated symbolically, not numerically.
        var_one = m*(1-(1-r)**2/(1-r*r))
        verify(var_one == 2*m*r/(1+r))
        for d in range(1, 9):
            cov = -m*(1-r)**2 * r**d/(1-r*r)
            verify(cov == -m*(1-r)*r**d/(1+r))
        for L in range(1, 19):
            var_cov = L*var_one - 2*m*(1-r)/(1+r)*sum((L-d)*r**d for d in range(1,L))
            rhs = 2*m*r*(1-r**L)/(1-r*r)
            verify(var_cov == rhs)
            # Source-level outgoing/incoming cut probabilities.
            p_out = [r**(t-1) for t in range(1,L+1)]
            out_mean = m*sum(p_out)
            out_var = m*sum(v*(1-v) for v in p_out)
            in_mean = m*(1-r**L)/(1-r)
            in_var = m*((1-r**L)/(1-r) - (1-r**L)**2/(1-r*r))
            verify(out_mean == in_mean)
            verify(out_var + in_var == rhs)

# A finite, independent enumeration of edge choices versus the boundary rule.
# The graph uses one edge per new vertex; all parent choices are enumerated.
# X_j(H) is the number of edges entering vertex j by time H, and
# identity sum_{j=a}^b X_j(H)- (b-a+1) = in_future - out_block
# holds when H>=b, with the block's own sources a,...,b.
for H in range(3,7):
    parents = [tuple(range(n)) for n in range(1,H+1)]
    for choices in product(*parents):
        for a in range(1,H):
            for b in range(a,H+1):
                inside = sum(a <= choices[n-1] <= b for n in range(1,H+1))
                out = sum(choices[n-1] < a for n in range(a,b+1))
                inc = sum(a <= choices[n-1] <= b for n in range(b+1,H+1))
                verify(inside-(b-a+1) == inc-out)

# Exact finite distribution of crossing edge counts for the stationary model:
# direct convolution and mean/variance comparison.  Incoming tail is cut at T,
# and its omitted mean is exactly m*(1-r**L)*r**T/(1-r).
for r in [F(1,2), F(2,3)]:
    for m in [1, 2]:
        for L in [1, 2, 3, 5]:
            out_probs = [r**(t-1) for t in range(1,L+1) for _ in range(m)]
            in_probs = [r**(s-1)*(1-r**L) for s in range(1,13) for _ in range(m)]
            law_out = poisson_binomial(out_probs)
            law_in = poisson_binomial(in_probs)
            verify(sum(law_out) == sum(law_in) == 1)
            o_mean, o_var = moments(law_out)
            i_mean, i_var = moments(law_in)
            verify(o_mean == m*(1-r**L)/(1-r))
            verify(i_mean == m*(1-r**L)*(1-r**12)/(1-r))
            verify(o_var + i_var <= 2*m*r*(1-r**L)/(1-r*r))
            verify(2*m*r*(1-r**L)/(1-r*r) - (o_var+i_var) <= m*(1-r**L)*r**12/(1-r))

print('PASS:', checks, 'exact-rational identities and finite enumerations')

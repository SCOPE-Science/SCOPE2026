#!/usr/bin/env python3
"""Standalone finite checks for the matching/edge-count coupling of threshold graphs.

Run: python3 verify.py
Uses only the Python standard library. Exact finite checks do not certify infinite limits.
"""
from itertools import product
from functools import lru_cache
from fractions import Fraction
from math import comb, isclose, pi, sqrt
import random

checks = 0

def demand(cond, msg):
    global checks
    checks += 1
    if not cond:
        raise AssertionError(msg)


def adjacency(n, creation):
    # A 1 creates a dominating vertex, a 0 an isolated vertex.
    adj = [0] * n
    for j, bit in enumerate(creation, start=1):
        if bit:
            for i in range(j):
                adj[j] |= 1 << i
                adj[i] |= 1 << j
    return tuple(adj)


def independent_matching_number(adj):
    n = len(adj)
    @lru_cache(None)
    def solve(mask):
        if not mask:
            return 0
        low = mask & -mask
        i = low.bit_length() - 1
        remaining = mask ^ low
        ans = solve(remaining)
        neighbors = adj[i] & remaining
        while neighbors:
            jbit = neighbors & -neighbors
            neighbors ^= jbit
            ans = max(ans, 1 + solve(remaining ^ jbit))
        return ans
    return solve((1 << n) - 1)


def metrics(n, creation):
    # Read creation bits right to left (newest to oldest).
    w = 0
    h = 0
    for bit in reversed(creation):
        w += 1 - 2 * bit
        h = max(h, w)
    deficiency = n - 2 * ((n - h) // 2)
    edge_sum = sum(j * bit for j, bit in enumerate(creation, start=1))
    return deficiency, edge_sum, h

# Independent maximum-matching recursion for every creation word through 10 vertices.
for n in range(2, 11):
    for word in product((0, 1), repeat=n - 1):
        adj = adjacency(n, word)
        d, edges, h = metrics(n, word)
        e_direct = sum((x.bit_count()) for x in adj) // 2
        nu = independent_matching_number(adj)
        demand(edges == e_direct, (n, word, 'edge count'))
        demand(d == n - 2 * nu, (n, word, 'matching number'))
        demand(d - h in (0, 1), (n, word, 'discretization'))

# Exhaustive exact covariance over all binary creation words for even orders.
# This is an independent finite-size sanity check of sign/scaling, not an asymptotic proof.
ratios = []
for n in range(2, 17, 2):
    N = 1 << (n-1)
    ds = es = de = 0
    for word in product((0, 1), repeat=n-1):
        d, e, h = metrics(n, word)
        ds += d
        es += e
        de += d * e
        demand(d == 2*((h+1)//2), (n, word, 'even-order formula'))
    cov = Fraction(de*N - ds*es, N*N)
    demand(cov < 0, (n, 'strict negative covariance'))
    ratios.append((n, float(cov/(n*n)), str(cov)))

# Reflection-principle matching numbers from Ross (2011), a separately checked baseline.
for n in range(2, 15):
    hist = [0] * (n//2 + 1)
    for word in product((0, 1), repeat=n-1):
        d, e, h = metrics(n, word)
        hist[(n-d)//2] += 1
    for k in range(n//2):
        demand(hist[k] == comb(n,k), (n,k,'Ross matching pmf'))
    if n%2 == 0:
        demand(hist[n//2] == comb(n-1,(n-1)//2), (n,'perfect matching pmf'))

# The exact Brownian-maximum/integrated-Brownian covariance is 5/16;
# the edge-centering factor is -1/2, so the target covariance is -5/32.
assert Fraction(1, 2) - Fraction(3, 8)/2 == Fraction(5,16)
assert -Fraction(1,2)*Fraction(5,16) == -Fraction(5,32)
limiting_correlation = (-5/32)/sqrt((1-2/pi)/12)
assert -1 < limiting_correlation < 0
print('PASS', checks, 'exact finite assertions')
print('normalized finite covariance values:', ratios)
print('asymptotic covariance:', -Fraction(5,32))
print('asymptotic correlation:', round(limiting_correlation, 12))

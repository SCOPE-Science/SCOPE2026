#!/usr/bin/env python3
"""Supplementary rational arithmetic checks for an ordinal C0 affine-shift calculation.

This tests only finite-coordinate binomial identities and does not establish
continuity on ordinal spaces or any infinite-dimensional statement.
"""
from fractions import Fraction
from math import comb, floor

cases = 0
for a,b in [(1,2),(1,3),(2,3),(3,5),(7,11)]:
    t = Fraction(a,b)
    for n in range(41):
        # The first n+1 coordinates of A_t**n e_0.
        c = [Fraction(comb(n,k),1)*t**k*(1-t)**(n-k)
             for k in range(n+1)]
        assert sum(c) == 1
        mode = (n+1)*a//b
        assert c[mode] == max(c)
        # Explicit binomial recurrence for the prior probability vector.
        if n:
            prev = [Fraction(comb(n-1,k),1)*t**k*(1-t)**(n-1-k)
                    for k in range(n)]
            for k in range(n+1):
                expected = (1-t)*(prev[k] if k<n else 0) + \
                           t*(prev[k-1] if k else 0)
                assert c[k] == expected
        residual = t*max(c)
        assert residual > 0
        cases += 1
print('passed', cases, 'exact rational binomial residual checks')

#!/usr/bin/env python3
"""Finite diagnostics for q-numerical-radius witnesses and exact endpoint identity."""
from fractions import Fraction as F
from math import sqrt

count = 0
for t in (1.01, 1.10, 1.30, 1.40):
    for q in (.10, .50, .90, .99, .9999):
        # Real geometric unit vector: x_j=sqrt(1-r*r)*r**j.
        # For the shift with first weight t, <Tx,x>=r*(t+(1-t)*r*r).
        def expectation(r):
            return r * (t + (1.0-t)*r*r)
        lo, hi = 0., 1.
        assert expectation(lo) < q < expectation(hi)
        for _ in range(120):
            mid = (lo+hi)/2
            if expectation(mid) < q:
                lo = mid
            else:
                hi = mid
        r = (lo+hi)/2
        a = expectation(r)
        b2 = t*t*(1-r*r)+r*r
        assert abs(a-q) < 3.e-14
        assert b2 > 1
        radius_witness = q*abs(a) + sqrt(1-q*q)*sqrt(b2-a*a)
        assert radius_witness > 1
        count += 4
# Verify endpoint identity with rational finite-support vectors.
for t in (F(1),F(7,5),F(3,2)):
    for raw in ((F(1), F(2), F(-1), F(3)),
                (F(0), F(1), F(1), F(1), F(0)),
                (F(2), F(-2), F(0))):
        x = list(raw) + [F(0)]
        norm2 = sum(v*v for v in x)
        xtx = t*x[0]*x[1] + sum(x[j]*x[j+1] for j in range(1,len(x)-1))
        rhs = (sum((x[j+1]-x[j])**2 for j in range(1,len(x)-1))/2
               + x[0]**2 + x[1]**2/2 - t*x[0]*x[1])
        assert norm2-xtx == rhs
        count += 1
print(f'{count} finite diagnostic assertions passed; universal proof is analytical.')

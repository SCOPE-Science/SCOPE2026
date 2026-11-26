#!/usr/bin/env python3
"""Exact finite checks of a one-link one-dimensional lattice-gas identity.

These computations supplement, and do not substitute for, the all-length proof.
"""
from fractions import Fraction
import itertools
import sympy as sp

z, a = sp.symbols('z a')
P = [sp.Integer(1), 1 + z]
for n in range(2, 21):
    P.append(sp.expand(P[n-1] + z*P[n-2]))

identity_cases = 0
for m in range(2, 11):
    Z = sp.expand(P[m]**2 + (a-1)*z**2*P[m-2]**2)
    # Independent combinatorial coefficient construction (does not use factorization).
    accum = {}
    for mask in range(1 << (2*m)):
        # Only the central edge can join two simultaneously occupied sites.
        if any((mask >> j & 3) == 3 for j in range(2*m-1) if j != m-1):
            continue
        k = mask.bit_count()
        has_central_pair = bool((mask >> (m-1) & 3) == 3)
        key=(k, int(has_central_pair))
        accum[key]=accum.get(key,0)+1
    direct=sp.Poly.from_dict({(k,r):num for (k,r),num in accum.items()},(z,a)).as_expr()
    assert sp.expand(Z-direct)==0, (m,Z,direct)
    identity_cases += 1

count_cases = 0
for m in range(2, 10):
    d=(m+1)//2
    for rate in [sp.Rational(0),sp.Rational(1,4),sp.Rational(1,2),sp.Rational(3,4),sp.Rational(1),sp.Rational(5,4),sp.Rational(2),sp.Rational(5)]:
        f=sp.Poly(sp.expand(P[m]**2+(rate-1)*z*z*P[m-2]**2),z)
        expected_distinct=(m if rate == 0 else 2*d) if rate < 1 else (d if rate == 1 else 0)
        num=f.count_roots(-sp.oo,sp.oo)
        assert num==expected_distinct,(m,rate,num,expected_distinct)
        if rate == 1:
            assert sp.gcd(f.as_expr(),sp.diff(f.as_expr(),z)) == P[m]
        count_cases+=1

# Explicit near-threshold nonzero splitting coefficients: every zero of P_m is simple,
# and P_m has no common factor with z P_{m-2}.
for m in range(2,20):
    assert sp.gcd(P[m],z*P[m-2]) == 1
    assert sp.gcd(P[m],sp.diff(P[m],z)) == 1

# Demonstrate the small instance directly.
assert sp.expand(P[3]**2+(a-1)*z*z*P[1]**2 - (a*z**4 + (2*a+4)*z**3 +(a+10)*z**2+6*z+1)) == 0
print('SOFT_LINK_EXACT_VERIFICATION_PASSED',identity_cases,count_cases,18)

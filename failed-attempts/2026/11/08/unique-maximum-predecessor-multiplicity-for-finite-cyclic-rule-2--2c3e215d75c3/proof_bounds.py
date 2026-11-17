#!/usr/bin/env python3
"""Exact rational checks for the inequalities used in the analytic proof.
The symbolic three by three identities appear explicitly in RESULT.md.
No floating-point arithmetic or third-party packages are used.
"""
from fractions import Fraction
lo = Fraction(146557, 100000)
hi = Fraction(146558, 100000)
p = lambda t: t**3 - t**2 - 1
assert p(lo) < 0 < p(hi)
assert lo**2 > 2
# For four or more 1-bits: 2 L^(n-2)+L^(-4) < L^n, n>=4.
assert lo**4 - 2 * hi**2 - lo**-4 > 0
# For up to three 1-bits: L^-1/2(1+4L^-8)<1, squared.
assert (1+4*lo**-8)**2 < lo
# Frobenius squares of the residual blocks at powers 3,4,5 are <1.
assert 3 - lo**2 < 1
assert 3*hi**2 - 8*lo + 6 < 1
assert 6*hi**2 - 12*lo + 5 < 1
print('EXACT_RATIONAL_INEQUALITIES_PASS', str(lo),str(hi))

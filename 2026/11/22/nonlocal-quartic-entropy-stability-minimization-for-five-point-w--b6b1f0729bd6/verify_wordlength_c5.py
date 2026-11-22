"""Exact rational certificate for a five-point word-length Fourier deficit.

Uses only the Python standard library. It certifies the specified rational
witness and strict comparison to 19/40; no numerical optimization is used.
"""
from fractions import Fraction as F
from math import isqrt


def sqrt_interval(q, scale=10**12):
    q = F(q)
    assert q >= 0
    m = isqrt(q.numerator * scale**2 // q.denominator)
    lo, hi = F(m, scale), F(m+1, scale)
    assert lo**2 <= q < hi**2
    return lo, hi


def log_interval(x, terms=24):
    """Positive x>1; atanh series and exact geometric tail majorant."""
    x = F(x)
    assert x > 1
    t = (x-1)/(x+1)
    partial = sum((2*t**(2*j+1)/F(2*j+1) for j in range(terms)), F(0))
    upper_tail = 2*t**(2*terms+1) / ((2*terms+1)*(1-t*t))
    return partial, partial + upper_tail

r5lo, r5hi = sqrt_interval(F(5))
r7lo, r7hi = sqrt_interval(F(7, 10))
L2, U2 = log_interval(2)
L3, U3 = log_interval(3)
L75, U75 = log_interval(F(7,5))
# Entropy of (3,1,1,3,6), divided by sqrt(56/5), is
# (27/14) log 3 -(12/7) log 2 - log(7/5).
ent_lo = F(27,14)*L3 - F(12,7)*U2 - U75
ent_hi = F(27,14)*U3 - F(12,7)*L2 - L75
# Word-length Fourier energy = 9/20 -(2/35) sqrt(5).
energy_lo = F(9,20) - F(2,35)*r5hi
energy_hi = F(9,20) - F(2,35)*r5lo
# Squared L2 distance to 1 is 2(1-sqrt(7/10)).
den_lo = 4*(1-r7hi)**2
den_hi = 4*(1-r7lo)**2
deficit_lo, deficit_hi = 2*energy_lo-ent_hi, 2*energy_hi-ent_lo
assert den_lo > 0 and deficit_lo > 0
assert deficit_hi < F(19,40)*den_lo
assert F(19,40) < F(1,2)
print('exact rational witness certified')
print('deficit interval:',float(deficit_lo),float(deficit_hi))
print('denominator interval:',float(den_lo),float(den_hi))
print('ratio interval:',float(deficit_lo/den_hi),float(deficit_hi/den_lo))
print('strict upper bound: 19/40 < 1/2')

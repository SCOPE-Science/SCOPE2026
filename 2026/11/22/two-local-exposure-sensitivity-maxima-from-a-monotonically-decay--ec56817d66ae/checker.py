"""Exact rational certificates for a two-timescale transient exposure benchmark.

Only Python standard library. Run: python flare_snr_check.py
"""
from fractions import Fraction as Q
from math import factorial

def eneg_bounds(x):
    """Rational lower/upper bounds on exp(-x), x >= 0."""
    assert x >= 0
    y = x / 128
    assert y <= Q(1, 4)
    # Alternating series bounds for exp(-y) at degree 16/17.
    def partial(n):
        return sum(((-y) ** k) / factorial(k) for k in range(n + 1))
    hi, lo = partial(16), partial(17)
    assert 0 < lo <= hi <= 1
    return lo**128, hi**128

def N_bounds(t):
    u0,u1=eneg_bounds(t)
    v0,v1=eneg_bounds(30*t)
    # N= 2t(e^-t+5e^-30t) -[1-e^-t+(1-e^-30t)/6]
    #  = (2t+1)e^-t +(10t+1/6)e^-30t -7/6
    return ((2*t+1)*u0+(10*t+Q(1,6))*v0-Q(7,6),
            (2*t+1)*u1+(10*t+Q(1,6))*v1-Q(7,6))

checks=[(Q(1,20),1),(Q(1,8),-1),(Q(1,3),1),(Q(1),-1)]
for t,sign in checks:
    lo,hi=N_bounds(t)
    assert lo > 0 if sign==1 else hi<0
    print('verified_sign',str(t),sign, 'midapprox',float((lo+hi)/2), 'bound_width',float(hi-lo))

if __name__ == '__main__':
    print('PASS: four exact rational interval signs; proof provides root bound')

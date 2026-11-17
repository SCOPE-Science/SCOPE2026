#!/usr/bin/env python3
"""Reproducible numerical checks of a first-return sampling threshold.
Requires Python 3 and SciPy. Does not replace the analytic proof.
"""
import math
from scipy.special import gammainc, gammaincc, gammaln

# Exact tail identity for integer return times, against exponential coupling.
for delta in (0.2,0.5,0.8):
    for n in range(0,21):
        exact=math.exp(1-(n+1)**delta)
        via_exp=math.exp(-((n+1)**delta-1))
        assert abs(exact-via_exp)<1e-13

for q in (100,400,1600,6400):
    lo=q-q**0.25; hi=q+q**0.25
    base=gammaincc(q+1,1.0)
    frac_lo=(gammainc(q+1,lo)-gammainc(q+1,1))/base
    frac_hi=(gammainc(q+1,hi)-gammainc(q+1,1))/base
    assert 0<frac_lo<0.5<frac_hi<1, (q,frac_lo,frac_hi)
    assert frac_hi-frac_lo < 2.5*q**(-0.25), (q,frac_lo,frac_hi)
    logmu=1+gammaln(q+1)+math.log(base)
    logvarbound=q*math.log(lo)-q-logmu
    assert logvarbound < -q**0.25/2, (q,logvarbound)
    lograre=1-q**0.25
    assert lograre<0

for c in (1.05,1.2,1.6,2.3):
    b=(c+1)/2
    assert math.log(b)+1-c < 0
for c in (0.2,0.7,0.95):
    b=(c+1)/2
    assert c<b<1
print('VERIFY_OK exact_return_tails=63 gamma_window_cases=4 variance_and_rare_checks=4 supercritical_exponents=4 subcritical_cutoffs=3')

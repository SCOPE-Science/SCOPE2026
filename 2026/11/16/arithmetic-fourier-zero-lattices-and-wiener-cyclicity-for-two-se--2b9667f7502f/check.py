"""Supplementary finite checks for two-interval Fourier-zero arithmetic.

This script tests exact modular membership against direct complex Fourier
transforms on rational test grids. Infinite completeness is proved analytically.
"""
from fractions import Fraction as Q
from math import pi, sin
from cmath import exp
from itertools import product


def zero_predicate(a,b,d,t):
    if t==0: return False
    return ((t*a).denominator==1 and (t*b).denominator==1) or ((t*(a+b)).denominator==1 and (t*d).denominator==1) or ((t*(a-b)).denominator==1 and (2*t*(d+b)).denominator==1 and ((2*t*(d+b)).numerator%2==1))


def Fourier_num(a,b,d,t):
    a,b,d,t=map(float,(a,b,d,t))
    # 2 pi i t times the transform: sum of four endpoint exponentials.
    return 1-exp(-2j*pi*t*a)+exp(-2j*pi*t*(a+d))-exp(-2j*pi*t*(a+d+b))

count=0
for a,b,d in product([Q(1,2),Q(2,3),Q(1),Q(3,2),Q(2)],repeat=3):
    for k in range(-36,37):
        if not k:continue
        t=Q(k,12)
        pred=zero_predicate(a,b,d,t)
        norm=abs(Fourier_num(a,b,d,t))
        assert (norm<1e-10)==pred,(a,b,d,t,pred,norm)
        count+=1
# Test exact simultaneous-root multiplicity for equal widths.
a=Q(1); b=Q(1); d=Q(1,2)
# h=3/2: odd sine zeros t=odd integers are also cos zeros.
for t in (Q(1),Q(3),Q(-1)):
    assert zero_predicate(a,b,d,t)
    assert (t*a).denominator==1 and (2*t*(d+a)).numerator%2==1
# Two examples of three distinct mechanisms.
assert zero_predicate(Q(1),Q(2),Q(1,3),Q(1))  # both sine factors vanish
assert zero_predicate(Q(1),Q(2),Q(1,3),Q(3))
assert zero_predicate(Q(1),Q(2),Q(1,2),Q(2))  # sum/gap resonance
assert zero_predicate(Q(3),Q(1),Q(2),Q(1,2))  # difference/parity resonance
print('CHECK_OK finite_rational_frequency_tests=',count,' plus exact overlap checks')

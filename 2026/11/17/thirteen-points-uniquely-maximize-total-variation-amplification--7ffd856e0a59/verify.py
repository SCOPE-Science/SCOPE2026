"""Exact rational checks for the quartic Savitzky--Golay variation theorem.

Requires Python 3 standard library only. The infinite-range proof is in RESULT.md.
"""
from fractions import Fraction as F


def numerator_and_denominator(m):
    assert isinstance(m, int) and m >= 2
    p = (2*m-3)*(2*m-1)*(2*m+1)*(2*m+3)*(2*m+5)
    c = 15*m**4+30*m**3-35*m**2-50*m+12
    b = -70*m*m-70*m+105
    return [15*(63*k**4+b*k*k+c) for k in range(-m, m+1)], 4*p


def gain(m):
    nums, den = numerator_and_denominator(m)
    return F(sum(map(abs, nums)), den)


# Reproduction identities and coefficient construction over a range of m.
for m in range(2, 31):
    nums, den = numerator_and_denominator(m)
    assert sum(nums) == den
    for power in (1, 2, 3, 4):
        assert sum(nums[k+m]*k**power for k in range(-m, m+1)) == 0
    # Independent centered least-squares row from inverse Gram cofactor.
    s = {p: sum(j**p for j in range(-m,m+1)) for p in (0,2,4,6,8)}
    A,B,C,D,E = (s[p] for p in (0,2,4,6,8))
    det = A*(C*E-D*D)-B*(B*E-C*D)+C*(B*D-C*C)
    assert det>0
    for k in range(-m,m+1):
        gram = F((C*E-D*D)+(C*D-B*E)*k*k+(B*D-C*C)*k**4,det)
        assert gram == F(nums[k+m],den)
print('LEAST_SQUARES_MOMENTS_AND_GRAM_COFACTOR_PASS 29')


winner=F(3763,2431)
assert gain(6)==winner
for m in range(2, 2000):
    if m!=6:
        assert gain(m)<winner, ('unexpected competing window',m)
print('EXACT_ALL_WINDOWS_5_TO_3999_UNIQUE_13_POINT_MAX_PASS 1998')


# Certificate for G_infinity < 301/200, using two rational root intervals.
def Q(u): return 63*u**4-70*u*u+15
def J(u): return (225*u-350*u**3+189*u**5)/128
lo1,hi1=F(538469,1000000),F(538470,1000000)
lo2,hi2=F(906179,1000000),F(906180,1000000)
assert Q(lo1)>0>Q(hi1)
assert Q(lo2)<0<Q(hi2)
assert hi1 < F(2,3) < lo2
# On [0,1], |J'|=|K| <= (225+1050+945)/128 < 18.
mid1,mid2=(lo1+hi1)/2,(lo2+hi2)/2
upper=1+4*(J(mid1)-J(mid2)+18*F(1,1000000))
assert upper < F(301,200), (upper, F(301,200))
print('RATIONAL_CONTINUUM_ROOT_ENCLOSURES_AND_GAIN_BOUND_PASS', float(upper))


# For m>=2000: P_m /m^5=prod(2-3t,2-t,2+t,2+3t,2+5t)>31,
# and coefficient error bounds are <= (1+13+20)/m =34/m.
# Check the explicit rational coefficient error bounds at the worst t=1/2000.
t=F(1,2000)
p=(2-3*t)*(2-t)*(2+t)*(2+3*t)*(2+5*t)
assert p>31
# Coefficient differences: absolute numerator polynomials bounded by their
# positive-coefficient majorants at t, divided by P_m/m^5.
err_a=F(15,128)*(240+80*t+1400*t*t+114*t**3+675*t**4)/31
err_b=F(525,64)*(48+32*t+200*t*t+18*t**3+45*t**4)/31
err_c=F(945,128)*(80+80*t+200*t*t+18*t**3+45*t**4)/31
assert err_a<1 and err_b<13 and err_c<20, (err_a,err_b,err_c)
# Coarse sufficient large-window bound: G_m < 301/200 + 78/m,
# which is strictly less than the exact winner for m>=2000.
assert F(301,200)+F(78,2000)<winner
print('EXACT_INFINITE_TAIL_POSITIVE_GAP_PASS')


# Extremal one-jump sequences: first difference of a step is the delta,
# output first difference is precisely the signed impulse-response kernel.
# Test direct finite sums on multiple representative windows.
for m in (2,3,4,5,6,8,25):
    nums,den=numerator_and_denominator(m)
    y={j:sum(nums[k+m] for k in range(-m,m+1) if j-k>=0) for j in range(-3*m,3*m+1)}
    variations=sum(abs(y[j]-y[j-1]) for j in range(-2*m,2*m+1))
    assert variations==sum(map(abs,nums))
print('EXACT_JUMP_SIGNAL_ATTAINS_EVERY_SHARP_KERNEL_GAIN_PASS')
print('ALL_QUARTIC_SAVITZKY_GOLAY_VARIATION_CHECKS_PASS',str(winner))

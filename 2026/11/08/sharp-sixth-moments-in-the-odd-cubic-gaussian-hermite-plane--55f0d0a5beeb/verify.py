#!/usr/bin/env python3
"""Exact self-contained rational verification for the odd-cubic Gaussian L6 theorem.
Python 3 standard library only. No random sampling or external dependencies.
"""
from math import comb
from fractions import Fraction


def poly_mul(a, b):
    result = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            result[i + j] += x * y
    return result


def gauss_even_moment(degree):
    if degree % 2:
        return 0
    out = 1
    for k in range(1, degree, 2):
        out *= k
    return out


def evaluate(p, x):
    acc = 0
    for c in reversed(p):
        acc = acc * x + c
    return acc


# Gaussian sixth moment of (a*Z + b*(Z^3-3Z)). For a=1, b=t.
# Use an independently generated expansion in t and z, not the displayed formula.
coeff = []
for k in range(7):
    # z^(6-k) (z^3 - 3z)^k = sum_j binom(k,j) (-3)^(k-j) z^(6+2j)
    v = sum(comb(k,j)*(-3)**(k-j)*gauss_even_moment(6+2*j)
            for j in range(k+1))
    coeff.append(comb(6,k)*v)
expected = [15, 360, 6750, 86400, 769500, 4315680, 11608920]
assert coeff == expected, (coeff, expected)
print('EXACT_GAUSSIAN_SIXTH_MOMENT_POLYNOMIAL_OK')

# Orthogonality of H1 and H3; variance a^2+6 b^2.
h3 = [0,-3,0,1]
var_h3 = sum(h3[i]*h3[j]*gauss_even_moment(i+j)
             for i in range(4) for j in range(4))
cross = sum(h3[i]*gauss_even_moment(i+1) for i in range(4))
assert var_h3 == 6 and cross == 0
print('EXACT_HERMITE_ORTHOGONALITY_OK')

# Check the derivative identity of K(t)=N(t)/(1+6t^2)^3.
p = [-1,-36,-690,-8100,-55620,-167832,71928]  # ascending
nprime = [i*coeff[i] for i in range(1,7)]
left = poly_mul(nprime,[1,0,6])
right = poly_mul(poly_mul(coeff,[0,36]),[1])
left += [0]*max(0,len(right)-len(left))
right += [0]*max(0,len(left)-len(right))
assert [a-b for a,b in zip(left,right)] == [-360*z for z in p]+[0]
print('EXACT_DERIVATIVE_IDENTITY_OK')

# P(-u) has exactly one positive u-root: at u>=1/8 all coefficients
# of Q(1/8+v) are positive. At 0<u<1/8 the Mobius transform has one
# sign change, hence precisely one root by Descartes and endpoint signs.
q = [((-1)**i)*p[i] for i in range(7)]
scale = 8**6
shift = []
for j in range(7):
    shifted = sum(Fraction(q[i]*comb(i,j),8**(i-j)) for i in range(j,7))
    shift.append(shifted*scale//8)
assert shift == [11671,874896,22102080,305510400,2167050240,7267221504,2356936704]
trans = [0]*7
for i in range(7):
    for k in range(7-i):
        trans[i+k] += q[i]*comb(6-i,k)*8**(6-i)//8
assert trans == [-32768,-49152,-107520,-75520,-26400,-39336,11671]
assert all(z>0 for z in shift) and all(z<0 for z in trans[:-1]) and trans[-1]>0
# P(t) also has exactly one positive root by Descartes: plus then minus.
assert p[-1]>0 and all(z<0 for z in p[:-1])
print('EXACT_TWO_REAL_CRITICAL_ROOT_CERTIFICATE_OK')

# Exact rational isolation; the monotonicity proof is the degree-6
# Descartes transform above, not just these finite brackets.
neg_lo,neg_hi = Fraction(-102,1000),Fraction(-101,1000)
pos_lo,pos_hi = Fraction(2642,1000),Fraction(2643,1000)
assert evaluate(p,neg_lo)>0 and evaluate(p,neg_hi)<0
assert evaluate(p,pos_lo)<0 and evaluate(p,pos_hi)>0

def bisect(lo,hi):
    sign_lo = 1 if evaluate(p,lo)>0 else -1
    for _ in range(95):
        mid = (lo+hi)/2
        sign_mid = 1 if evaluate(p,mid)>0 else -1
        if sign_mid==sign_lo:
            lo=mid
        else:
            hi=mid
    return (lo+hi)/2

tmin,tmax=bisect(neg_lo,neg_hi),bisect(pos_lo,pos_hi)
def moment_ratio(t):
    return evaluate(coeff,t)/(1+6*t*t)**3
rmin,rmax = moment_ratio(tmin),moment_ratio(tmax)
assert rmin<15 and rmax>53745
assert moment_ratio(Fraction(0))==15
assert Fraction(coeff[-1],216)==53745
assert Fraction(4)<rmin<Fraction(5)
assert Fraction(57613)<rmax<Fraction(57615)
print('EXACT_ROOT_ISOLATION_AND_ENDPOINT_COMPARISONS_OK')
print('ROOTS',f'{float(tmin):.15f}',f'{float(tmax):.15f}')
print('SIXTH_POWER_BOUNDS',f'{float(rmin):.12f}',f'{float(rmax):.12f}')
print('ALL_ODD_CUBIC_GAUSSIAN_CHECKS_PASSED')

#!/usr/bin/env python3
"""Exact rational checks for the degree-four double-cap concentration theorem.

Requires only the Python standard library.  The inequalities for every real
cutoff are justified in RESULT.md by signs of the factored differences.
"""
from fractions import Fraction as F
from math import sqrt


def trim(p):
    p = list(map(F, p))
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def add(a, b):
    return trim([(a[i] if i < len(a) else 0) +
                 (b[i] if i < len(b) else 0)
                 for i in range(max(len(a), len(b)))])


def scale(a, k):
    return trim([k * v for v in a])


def neg(a):
    return scale(a, -1)


def sub(a, b):
    return add(a, neg(b))


def mul(a, b):
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, u in enumerate(a):
        for j, v in enumerate(b):
            out[i+j] += u*v
    return trim(out)


def power(a, k):
    out = [F(1)]
    for _ in range(k):
        out = mul(out, a)
    return out


def diff(a):
    return trim([i*a[i] for i in range(1, len(a))] or [0])


def integral(a):
    return [F(0)] + [a[i] / (i+1) for i in range(len(a))]


def evaluate(a, x):
    out = F(0)
    for v in reversed(a):
        out = out*x+v
    return out


def even_coeffs(coeffs):
    """Compose the coefficient list in s with s=t^2."""
    out = [F(0)] * (2*len(coeffs)-1)
    for i, value in enumerate(coeffs):
        out[2*i] = F(value)
    return trim(out)

x = [F(0), F(1)]
one = [F(1)]
s = power(x, 2)
a = sub(one, s)
P4 = [F(3,8), F(0), F(-30,8), F(0), F(35,8)]

# Full-sphere norm cancels against the two identical antipodal caps.
eigen = []
for m in range(5):
    dm = P4[:]
    for _ in range(m):
        dm = diff(dm)
    q = mul(power(a, m), power(dm, 2))
    integ = integral(q)
    z = evaluate(integ, F(1))
    assert z > 0
    eigen.append(scale(sub([z], integ), 1/z))

expected = [
    [1,F(-81,64),0,F(135,16),0,F(-999,32),0,F(675,16),0,F(-1225,64)],
    [1,0,0,F(-135,16),0,F(459,16),0,F(-585,16),0,F(245,16)],
    [1,F(-45,32),0,F(15,2),0,F(-351,16),0,F(45,2),0,F(-245,32)],
    [1,0,0,F(-105,16),0,F(189,16),0,F(-135,16),0,F(35,16)],
    [1,F(-315,128),0,F(105,32),0,F(-189,64),0,F(45,32),0,F(-35,128)]
]
assert all(eigen[m] == trim(expected[m]) for m in range(5))
print('EXACT_FIVE_LEGENDRE_CAP_EIGENVALUE_POLYNOMIALS_OK')

seven_s_minus_three = even_coeffs([-3,7])
seven_s_minus_one = even_coeffs([-1,7])
fac = mul(x, a)

def factors(*xs):
    out = one
    for h in xs:
        out = mul(out, h)
    return out

factor_claims = {
 (0,1): scale(factors(fac, seven_s_minus_three, even_coeffs([3,-30,35])), F(9,64)),
 (0,2): scale(factors(fac, seven_s_minus_three, even_coeffs([-1,-10,35])), F(3,64)),
 (0,3): scale(factors(fac, even_coeffs([-27,293,-625,455])), F(3,64)),
 (0,4): scale(factors(fac, even_coeffs([51,271,-935,805])), F(3,128)),
 (1,2): scale(factors(x, power(a,2), seven_s_minus_three, seven_s_minus_one),F(15,32)),
 (1,3): scale(factors(power(x,3), power(a,2), seven_s_minus_one),F(15,8)),
 (1,4): scale(factors(x,power(a,2),even_coeffs([21,-58,133])),F(15,128)),
 (2,3): scale(factors(x,power(a,3),seven_s_minus_one),F(45,32)),
 (2,4): scale(factors(x,power(a,3),even_coeffs([1,7])),F(135,128)),
 (3,4): scale(factors(x,power(a,4)),F(315,128)),
}
for pair, claimed in factor_claims.items():
    i,j=pair
    assert sub(eigen[i],eigen[j]) == claimed, pair
print('EXACT_ALL_TEN_EIGENVALUE_DIFFERENCE_FACTORIZATIONS_OK')

# Purely rational root separation for the unique cubic threshold:
# P'(s) = 1365*s^2-1250*s+293 is positive on all real s
# since its discriminant is -37280 and leading coefficient > 0.
assert 1250**2 - 4*1365*293 == -37280
P = [F(-27),F(293),F(-625),F(455)]
assert evaluate(P,F(0)) < 0 < evaluate(P,F(1,7))
assert evaluate(P,F(120330,1000000)) < 0
assert evaluate(P,F(120332,1000000)) > 0

# The other three transition cutoffs are in strict order.
beta_sq = (5+2*sqrt(15))/35
gamma_sq = 3/7
delta_sq = (15+2*sqrt(30))/35
assert 1/7 < beta_sq < gamma_sq < delta_sq < 1
alpha_sq_lower=F(120330,1000000)
alpha_sq_upper=F(120332,1000000)
assert 0 < alpha_sq_lower < alpha_sq_upper < 1/7
print('FOUR_EXACT_TRANSITION_THRESHOLDS_ORDERED_OK')

# At t=sqrt(3/7), m=0,1,2 are equal and strictly larger than m=3,4.
# The common value and the two smaller values follow by rational reduction.
z=F(3,7)
for m, coeff in enumerate([
    F(-243,2401),F(-243,2401),F(-243,2401),
    F(-423,2401),F(-513,2401)]):
    # eigen_m(t) = 1 + t * polynomial_m(t^2).
    assert eigen[m][0] == 1
    q=sum(eigen[m][2*k+1]*z**k for k in range(5))
    # t * q = sqrt(21) * (q/7) since t=sqrt(21)/7
    assert q/7 == coeff
print('EXACT_FIVE_DIMENSIONAL_MAXIMUM_EIGENSPACE_RESONANCE_OK')

# Positivity of all m-4 differences follows from the factorizations:
# m=0: 51+s*(805s^2-935s+271) >= 51-1605/3220 >0 on [0,1].
# m=1: discr(133s^2-58s+21)<0.
assert F(51)-F(1605,3220)>0
assert 58**2-4*133*21<0
for i in range(4):
    for t in [F(1,100), F(1,7), F(2,7), F(1,2), F(4,7), F(4,5), F(99,100)]:
        assert evaluate(sub(eigen[i],eigen[4]),t)>0
print('STRICT_LEAST_CONCENTRATED_ORDER_FOUR_CERTIFICATE_OK')

# Independent numerical integral check without special-function libraries.
# Composite Simpson for a few interior cutoffs, normalization independently
# obtained by quadrature and compared against the exact polynomial.
import math

def simpson(f, lo, hi, n=1000):
    h=(hi-lo)/n
    val=f(lo)+f(hi)
    for i in range(1,n):
        val+=(4 if i%2 else 2)*f(lo+i*h)
    return val*h/3

def leg_deriv(m,z):
    # Independent closed expressions for derivatives of P_4.
    return [(35*z**4-30*z**2+3)/8,
            (35*z**3-15*z)/2,
            (105*z*z-15)/2,
            105*z,105][m]

for m in range(5):
    f=lambda y:(1-y*y)**m*leg_deriv(m,y)**2
    for t in (0.13,0.42,0.73):
        q=simpson(f,t,1)/simpson(f,0,1)
        val=float(evaluate(eigen[m],F(t)))
        assert abs(q-val)<2e-9,(m,t,q,val)
print('INDEPENDENT_NUMERICAL_ASSOCIATED_LEGENDRE_INTEGRALS_OK 15')
print('ALL_DEGREE_FOUR_DOUBLE_CAP_CHECKS_OK')

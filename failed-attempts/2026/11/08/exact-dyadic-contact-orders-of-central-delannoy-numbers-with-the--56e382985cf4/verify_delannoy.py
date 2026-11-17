"""Exact rational certificate and finite checks for a central Delannoy valuation theorem."""
from fractions import Fraction
from math import comb

J = 16
M = 16

def v2int(n):
    if n == 0:
        raise ValueError('zero has infinite valuation')
    return (abs(n) & -abs(n)).bit_length() - 1

def v2q(q):
    if q == 0:
        return None
    return v2int(q.numerator) - v2int(q.denominator)

# a_j(N) = (-2)^j prod_{i=0}^{j-1}(N-i(i+1))/(j!)^2
coeff = [Fraction(0) for _ in range(M + 1)]
a = [Fraction(0) for _ in range(M + 1)]
a[1] = Fraction(-2)
for j in range(1, J + 1):
    for m in range(M + 1):
        coeff[m] += a[m]
    if j < J:
        a = [Fraction(0)] + [
            Fraction(2*j*(j+1),(j+1)**2)*a[m] - Fraction(2,(j+1)**2)*a[m-1]
            for m in range(1, M + 1)
        ]
# Modulo 2 on coefficients of the normalized 4-adic polynomial.
expected = [0,1,7,3,5,5,10,8,10,9,13,12,14,12]
actual = [v2q(coeff[m] * Fraction(4**m,64)) for m in range(3,17)]
assert actual == expected, (actual, expected)
assert actual[0] == 0 and all(v >= 1 for v in actual[1:])

# Derivation-independent direct Delannoy definition.
for n in range(1,601):
    d = sum((2**j)*comb(n,j)**2 for j in range(n+1))
    N = n*(n+1)
    t = v2int(N)
    predicted = 2 if t == 1 else 3*t
    actual_v = v2int(d - (-1)**n)
    assert actual_v == predicted, (n, predicted, actual_v)

# Tail polynomial coefficient norm calculation at the finite critical frontier.
for j in range(17,513):
    S = sum(max(0, v2int(i*(i+1))-2) for i in range(1,j))
    assert 2*S <= j, (j,S)
    assert j-4-v2int(j)-S >= 1, (j,S)

# Independent exact finite evaluation of the j=1..16 coefficient via elementary symmetric polynomials.
elem = [Fraction(1)] + [Fraction(0)]*15
coeff_ind = [Fraction(0)]*17
for j in range(1,17):
    if j > 1:
        i=j-1
        u=Fraction(1,i*(i+1))
        for r in range(min(j-1,15),0,-1):
            elem[r] += u*elem[r-1]
    for m in range(1,j+1):
        coeff_ind[m] += Fraction((-1)**m*2**j,j)*elem[m-1]
assert coeff_ind == coeff
print('VERIFY_OK rational_coefficient_valuations=' + ','.join(map(str,actual)) + ' direct_n=1..600 tail_j=17..512 independent_recurrence=PASS')

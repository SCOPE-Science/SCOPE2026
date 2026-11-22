"""Exact rational certificate for the five-cycle nonlocal quartic entropy witness.
All comparisons use Python integers/Fractions; no floating point in assertions.
"""
from fractions import Fraction as F
from math import isqrt
from decimal import Decimal, localcontext

X = (1090, 1025, 925, 925, 1025)
S = F(sum(x*x for x in X), 5)
assert S == 1000120 and F(sum(X), 5) == 998


def sqrt_bounds(p, places=30):
    # Positive rational p, integer-square bounds with absolute width 10^-places.
    a, b = p.numerator, p.denominator
    scale = 10**places
    floor = isqrt((a*scale*scale)//b)
    return F(floor, scale), F(floor+1, scale)


def log_lower(t, terms=18):
    # log(t) = 2 artanh((t-1)/(t+1)); an exact absolute remainder bound.
    y = (t-1)/(t+1)
    s = F(0)
    for j in range(terms):
        s += 2*y**(2*j+1)/F(2*j+1)
    tail = 2*abs(y)**(2*terms+1)/((2*terms+1)*(1-y*y))
    return s-tail

s5lo, s5hi = sqrt_bounds(F(5))
sSlo, sShi = sqrt_bounds(S)
assert s5lo*s5lo <=5 <=s5hi*s5hi
assert sSlo*sSlo <=S <=sShi*sShi
mu_inverse_upper = (5+s5hi)/10
energy_upper = F(5690, 1)/S * mu_inverse_upper
entropy_lower = sum((F(x*x)/S)*log_lower(F(x*x)/S) for x in X)/5
d2_lower = 2*(1-F(998)/sSlo)
assert d2_lower > 0
ratio_threshold = F(119,200)
assert 2*energy_upper - entropy_lower < ratio_threshold*d2_lower*d2_lower
# sqrt5 < 56/25 gives (7-sqrt5)/8 > (7-56/25)/8 = 119/200.
assert s5hi < F(56,25)
assert ratio_threshold < (7-s5hi)/8

with localcontext() as c:
    c.prec=44
    def dec(f): return Decimal(f.numerator)/Decimal(f.denominator)
    print('S =', S)
    print('D_upper =', dec(2*energy_upper-entropy_lower))
    print('d2_lower^2 =', dec(d2_lower*d2_lower))
    print('R_upper =', dec((2*energy_upper-entropy_lower)/(d2_lower*d2_lower)))
    print('threshold =', dec(ratio_threshold))
    print('L5_lower =', dec((7-s5hi)/8))
    print('exact rational inequalities PASS')

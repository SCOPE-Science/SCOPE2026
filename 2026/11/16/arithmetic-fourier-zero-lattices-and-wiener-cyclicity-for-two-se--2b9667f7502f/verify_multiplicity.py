"""Exact rational test: reduce the endpoint polynomial and its frequency derivatives."""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from math import lcm
from sympy import Poly, cyclotomic_poly, symbols

x = symbols('x')


@lru_cache(None)
def powers(L):
    p = Poly(cyclotomic_poly(L,x),x)
    return [Poly(x**i,x).rem(p) for i in range(L)]


def test(a,b,d,xi):
    A, B, D = xi*a, xi*b, xi*d
    integer = lambda z: z.denominator == 1
    families = (integer(A) and integer(B), integer(A+B) and integer(D),
                integer(A-B) and integer(2*(D+B)) and (2*(D+B)).numerator%2 == 1)
    ends = (F(0),A,A+D,A+D+B)
    L = lcm(*(v.denominator for v in ends))
    vals = [powers(L)[int(L*v)%L] for v in ends]
    order = 0
    for j in range(3):
        v = sum(s*e**j*w for s,e,w in zip((1,-1,1,-1),ends,vals))
        if not v.is_zero:
            break
        order += 1
    expected = int(any(families)) + int(a==b and families[0] and families[2])
    assert order == expected, (a,b,d,xi,order,families)
    if order:
        one, u, v, w = vals
        origin_scaled_slope = a*u-(a+d)*v+(a+d+b)*w
        branch_slopes = (a*one+b*v, (a+b+d)*one-d*u, (a+d)*one-(b+d)*u)
        for occurs, slope in zip(families,branch_slopes):
            if occurs:
                assert (origin_scaled_slope-slope).is_zero
        if order == 2:
            endpoint_square = -a*a*u+(a+d)**2*v-(a+b+d)**2*w
            assert (endpoint_square-2*a*(a+d)*one).is_zero
    return order, families


freqs = [F(i,j) for i in (1,2,3,6) for j in (2,3,5)]
params = [F(1,2),F(1),F(4,3),F(3,2),F(2),F(5,2)]
counts = [0,0,0]
families_seen = set()
for a,b,d,xi in product(params,params,params,freqs):
    order, families = test(a,b,d,xi)
    counts[order] += 1
    families_seen.add(families)
assert all(counts)
assert {(True,False,False),(False,True,False),(False,False,True)} <= families_seen
print(f"Exact endpoint/derivative tests by order (0, 1, 2): {counts}")

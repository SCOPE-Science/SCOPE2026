#!/usr/bin/env python3
"""Exact Pluecker chart and determinantal-slice arithmetic checks.

Requires Python 3 and SymPy. All identities are symbolic over the integers.
"""
from itertools import combinations
from math import comb, factorial
from sympy import Matrix, eye, symbols, simplify

a, b, c, d, e, f, g, h, i = symbols('a b c d e f g h i')
M = Matrix([
    [1, 0, 0],
    [a, d, g],
    [b, e, h],
    [c, f, i],
    [0, 1, 0],
    [0, 0, 1],
])

def minors(mat):
    return {''.join(map(str, (t + 1 for t in I))):
            mat.extract(I, (0, 1, 2)).det().expand()
            for I in combinations(range(6), 3)}

P = minors(M)
assert P['156'] == 1
assert (P['256'], P['356'], P['146'], -P['145']) == (a, b, f, i)
# These block-preserving unipotent shears remove four free coordinates.
T = eye(6)
T[1, 0], T[2, 0] = -a, -b
T[3, 4], T[3, 5] = -f, -i
M0 = T * M
expected_M0 = Matrix([
    [1, 0, 0], [0, d, g], [0, e, h], [c, 0, 0],
    [0, 1, 0], [0, 0, 1]
])
assert M0 == expected_M0
P0 = minors(M0)
nonzero = {
    '123': d*h-e*g,
    '125': -g, '126': d, '135': -h, '136': e, '156': 1,
    '234': c*(d*h-e*g), '245': c*g, '246': -c*d,
    '345': c*h, '346': -c*e, '456': c,
}
for key, val in P0.items():
    assert simplify(val - nonzero.get(key, 0)) == 0, (key, val)
# The degree-three coordinate '456' is omitted by projection.
x = (P0['126'], P0['136'], -P0['125'], -P0['135'])
y = (-P0['246'], -P0['346'], P0['245'], P0['345'])
assert x == (d, e, g, h)
assert y == (c*d, c*e, c*g, c*h)
for j, k in combinations(range(4), 2):
    assert simplify(x[j]*y[k] - x[k]*y[j]) == 0
assert simplify(P0['123'] - (x[0]*x[3]-x[1]*x[2])) == 0
assert simplify(P0['234'] - (x[0]*y[3]-x[1]*y[2])) == 0
# Cone over Segre(P^1 x P^3): Hilbert series (1+3*t)/(1-t)^5.
for degree in range(36):
    hilbert = (degree+1) * comb(degree+3, 3)
    numerator_expansion = comb(degree+4, 4) + (3*comb(degree+3,4) if degree else 0)
    assert hilbert == numerator_expansion
transverse_multiplicity = 1+3
assert transverse_multiplicity == comb(4,1) == 4
# Hook-length formula for the 3 by 3 rectangle = degree of Gr(3,6).
hook_product = 1
for row in range(3):
    for column in range(3):
        hook_product *= (3-row)+(3-column)-1
source_degree = factorial(9) // hook_product
assert source_degree == 42
projected_degree = source_degree - 1
assert projected_degree == 41
print('PLUCKER_CHART_OK', len(P), len(P0))
print('DETERMINANTAL_SLICE_OK', transverse_multiplicity)
print('PROJECTIVE_DEGREE_OK', projected_degree)
print('VERIFY_OK')

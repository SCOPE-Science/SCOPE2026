#!/usr/bin/env python3
"""Exact arithmetic checks for the finite inequalities in the stated theorem.

The infinite tail relies on the independently published Nagura prime-interval
inequality plus the analytic estimates in the proof, not on finite search.
"""
from fractions import Fraction as F
from functools import reduce

P = [2, 3, 5, 7]
next_five = {
    11: [13, 17, 19, 23, 29],
    13: [17, 19, 23, 29, 31],
    17: [19, 23, 29, 31, 37],
    19: [23, 29, 31, 37, 41],
    23: [29, 31, 37, 41, 43],
}

def factor(p):
    return F(p**3 + 1, p**3)

for p, qs in next_five.items():
    assert reduce(lambda a, q: a*factor(q), qs, F(1)) > factor(p), p

h = F(125, 216)
coefficient = h/(1-h) - F(1, 2*29**3) * h**2/(1-h**2)
assert coefficient == F(2079146625, 1513630118) > 1

H = sum((F(1, p**3) for p in [11, 13, 17, 19, 23, 29]), F(0)) \
    + F(1, 31**3) + F(1, 4*31**2)
assert H == F(6873910901010396038995101, 3484482229214561906464984708)
assert H < F(1,500)

heads = [(reduce(lambda a, p: a*factor(p),
                 (p for j,p in enumerate(P) if mask & (1<<j)), F(1)), mask)
         for mask in range(16)]
heads.sort()
assert len({x for x, _ in heads}) == 16
assert [mask for _, mask in heads] == [0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15]
ratios = [heads[i+1][0]/heads[i][0] for i in range(15)]
assert min(ratios) == F(344,343)
assert F(500,499) < min(ratios)
assert heads[-1][0] == reduce(lambda a,p: a*factor(p), P, F(1))
print('VERIFY_OK finite_prime_checks=5 head_coefficients=16 disjoint_gaps=15')
print('minimum_consecutive_ratio=344/343 upper_tail_bound=500/499')
print('Nagura_tail_coefficient=', coefficient)

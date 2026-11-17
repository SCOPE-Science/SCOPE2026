#!/usr/bin/env python3
"""Exact rational certificate for the stated productive-crown theorem.

Requires Python 3 standard library only. No approximate numerical claims.
"""
from fractions import Fraction as Q
n = 12
m = 10000
h = 100
a = Q(3, 4)
r = Q(97, 100)
alpha = Q(9999, 10000)
assert alpha == Q(m - 1, m)
assert Q(11101, 1000) ** 2 < (n - 1)**2 + 4*a*a
assert Q(1802, 1000) ** 2 < 1 + 4*a*a
assert 30 * 97**33 < 11 * 100**33
assert 400 * 11**6 < 30**6
assert r**198 < Q(1,400)
S = 1 + a*a*(1-r**(2*h))/(1-r*r)
T = a*a*r*(1-r**(2*(h-1)))/(1-r*r)
root_lower = (Q(11101,1000)+(n-1)*Q(1802,1000))/n
L = root_lower + 2*alpha*T
D = L - 2*S
assert D > 0
assert root_lower - 2 == Q(6923,12000)
D_bound = Q(6923,12000) - Q(9,8)*((1-alpha*r)+r*(alpha-r)*Q(1,400))/(1-r*r)
assert D_bound == Q(496253,189120000)
assert D > D_bound > 0
assert L/S > 2
print('PASS: exact finite Schur-norm lower certificate')
print('strict rational lower bound for L - 2S:', D_bound)
print('strict positivity of L-2S confirmed:', D > D_bound)

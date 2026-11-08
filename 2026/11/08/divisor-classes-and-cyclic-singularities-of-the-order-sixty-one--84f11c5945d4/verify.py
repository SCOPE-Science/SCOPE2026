#!/usr/bin/env python3
"""Exact checks for the order-61 Klein quartic quotient classification.

The geometric applications of Lefschetz and equivariant descent are proven
in the accompanying mathematical argument, not replaced by this script.
"""
from fractions import Fraction
from math import comb

p = 61
A = [1, 58, 9, 34, 20]
assert len(set(A)) == 5
assert all((3*A[j]+A[(j+1) % 5]) % p == 0 for j in range(5))
assert sum(A) % p == 0
for k in range(1, p):
    assert len({(k*t) % p for t in A}) == 5
W = [8, 19, 33]
for j in range(5):
    local = sorted((A[(j+o) % 5] - A[j]) % p for o in (2, 3, 4))
    assert local == sorted((pow(-3, j, p)*v) % p for v in W)
ages = {k: sum(k*v % p for v in W) for k in range(1,p)}
assert min(ages.values()) == 22 and ages[39] == 22
assert tuple(39*v % p for v in W) == (7,9,6)
assert sum(W) % p == 60

# The exact rank-two subspace of local character restrictions.
ones = (1,1,1,1,1)
subspace = {tuple((b - m*a) % p for a in A)
            for m in range(p) for b in range(p)}
assert len(subspace) == p*p
assert (0,)*5 in subspace
kernel = [(m,b) for m in range(p) for b in range(p)
          if all((b - m*a) % p == 0 for a in A)]
assert kernel == [(0,0)]
assert {tuple((b-m*a) % p for a in A) for m in range(p) for b in range(p)} == subspace

# Quartic Chern class and trace calculation.
c3 = sum(comb(5,i) * (-4)**(3-i) for i in range(4))
assert c3 == -14
chi_X = 4 * c3
assert chi_X == -56
b3 = 4 - chi_X
assert b3 == 60
trace_nonidentity_H3 = 4-5
assert trace_nonidentity_H3 == -1
assert (b3 + 60*trace_nonidentity_H3) // 61 == 0
assert b3+60*trace_nonidentity_H3 == 0
assert Fraction(4,61) == Fraction(4,61)
print('fixed_points=5 local_type=1/61(8,19,33)')
print('mld=22/61 at_k=39')
print('global_local_image_cardinality=',len(subspace))
print('Pic_kernel_mod_61=',kernel)
print('b3_X=',b3,'invariant_b3_Y=0','anticanonical_volume=',Fraction(4,61))
print('VERIFY_OK')

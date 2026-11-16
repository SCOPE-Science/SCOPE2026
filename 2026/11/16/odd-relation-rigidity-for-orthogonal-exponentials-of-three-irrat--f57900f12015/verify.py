#!/usr/bin/env python3
"""Exact supplementary checks for a three-factor Bernoulli Fourier example.

This finite check verifies the example, not the theorem's universal upper bound.
Uses only the Python standard library.
"""
from fractions import Fraction as F
from itertools import product


def add(x, y):
    return x[0] + y[0], x[1] + y[1]


def mul(x, y):
    return x[0]*y[0] + 2*x[1]*y[1], x[0]*y[1] + x[1]*y[0]


def scale(x, q):
    return x[0]*q, x[1]*q


def sub(x, y):
    return add(x, scale(y, F(-1)))


zero = F(0), F(0)
a = F(-1), F(1)
b = F(0), F(1,2)
c = F(1), F(0)
A = F(1), F(1)
B = F(0), F(1)
C = F(1), F(0)

assert mul(a, A) == (F(1),F(0))
assert mul(b, B) == (F(1),F(0))
assert mul(c, C) == (F(1),F(0))
assert sub(A, B) == C
atoms = [add(add(scale(a,F(i)),scale(b,F(j))),scale(c,F(k)))
         for i,j,k in product((0,1),repeat=3)]
assert len(atoms) == len(set(atoms)) == 8

frequencies = (zero, scale(A,F(1,2)), scale(B,F(1,2)))
scales = (a,b,c)
for i in range(3):
    for j in range(i+1,3):
        gap = sub(frequencies[i], frequencies[j])
        witness = [mul(length, gap) for length in scales]
        assert any(v[1]==0 and (2*v[0]).denominator == 1 and
                   (2*v[0]).numerator % 2 for v in witness)

# The unique primitive integer relation is A-B-C=0.
assert sub(sub(A,B),C) == zero
print('CHECK_OK exact_atoms=8 exact_frequency_pairs=3 primitive_relation=1')

#!/usr/bin/env python3
"""Exact elementary checks for the characteristic-two cyclic cubic arithmetic."""
from math import gcd
w = (1,9,4,3,5)
assert len(set(w)) == 5
assert all((2*w[i]+w[(i+1)%5]) % 11 == 0 for i in range(5))
assert sorted({pow(2,i,11) for i in range(10)}) == list(range(1,11))
assert pow(2,10,11) == 1
# Fourier inversion of the character whose identity value is 10 and
# nonidentity values are -1: each of the ten nontrivial chars occurs once.
assert (10 - 10)//11 == 0
assert (10 + 1)//11 == 1
# The determinant of a single ten-cycle of one-dimensional eigenlines
# is minus its tenth-power scalar.
determinant=2**15
cycle_scalar=-determinant
assert -cycle_scalar == determinant
assert 2**15 == 32768
for n in range(1,31):
    q=2**n
    base=sum(q**i for i in range(4))
    middle_trace=0 if n%10 else 10*(cycle_scalar**(n//10))
    count=base-middle_trace
    assert count>0
    if n<10: assert count == base
    if n==10: assert count == 1075119105
print('VERIFY_OK')

#!/usr/bin/env python3
"""Exact finite-mask verification of a quadratic consecutive non-coprimality bound."""
from itertools import combinations, product
from math import gcd

def zero_masks(p, length=8):
    return {sum(1 << j for j in range(length) if ((a+j)**2+1)%p == 0)
            for a in range(p)}

# If a prime other than 2,5 hits two positions i,j in 0..7,
# it divides (j-i)^2+4, and is therefore 13,29, or 53.
# Other odd primes have at most one hit. Three independent wildcard
# copies represent ANY THREE different singleton-hit primes, a superset
# of all remaining possibilities.
classes={p:zero_masks(p) for p in (2,5,13,29,53)}
for wildcard in range(3):
    classes[1000000+wildcard]={0}|{1<<i for i in range(8)}

count=0
for primes in combinations(classes,3):
    for masks in product(*(classes[p] for p in primes)):
        count+=1
        if masks[0] | masks[1] | masks[2] == (1<<8)-1:
            raise AssertionError(('eight-position covering',primes,masks))
print('Exact local-mask combinations checked:',count)
assert all(gcd(n*n+1,1010)>1 for n in range(7,14))
for r in (13,17,29,37,41,53,61,73,89,97,101,109):
    t=next(t for t in range(r) if (t*t+1)%r==0)
    a=next(a for a in range(7,10*r+7,10) if (a+3-t)%r==0)
    assert all(gcd((a+i)**2+1,10*r)>1 for i in range(7))
print('Seven-position example and 12 CRT specializations: PASS')

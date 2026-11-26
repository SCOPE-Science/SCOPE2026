#!/usr/bin/env python3
"""Finite checks for the eventual-power witness and source operation table."""
from itertools import product
from math import factorial

NEG = {0:1, 1:0, 2:2}
DISJ = {
 (0,0):{0}, (0,1):{1}, (0,2):{2},
 (1,0):{1}, (1,1):{1}, (1,2):{1,2},
 (2,0):{2}, (2,1):{1,2}, (2,2):{2}
}
assert all(len(DISJ[a,b])>=1 for a in range(3) for b in range(3))
assert DISJ == {(b,a):vals for (a,b),vals in DISJ.items()}
assert {NEG[NEG[a]] for a in range(3)}=={0,1,2}
assert NEG[NEG[1]]==1
assert DISJ[1,2]=={1,2}
assert 1 in DISJ[1,2] and 2 in DISJ[1,2]

def iterate(f,x,n):
    for _ in range(n):
        x=f[x]
    return x

count=0
for d in range(1,5):
    for f in product(range(d), repeat=d):
        count+=1
        for x in range(d):
            assert iterate(f,x,2*d)==iterate(f,x,2*(d+factorial(d)))
assert count==1+4+27+256
print('FINITE_NEGATION_WITNESS_OK',count,'endofunctions',4,'carrier_sizes','dynamic_split_1_k')

#!/usr/bin/env python3
"""Checks for the seven-adic derangement residue theorem."""
from collections import Counter

p=7
v=[0]*7
w=[0]*7
for a in range(7):
    f=0; df=0; prod=1; dprod=0
    for j in range(14):
        if j:
            dprod=(dprod*(a-j+1)+prod)%p
            prod=(prod*(a-j+1))%p
        if j<7:
            f=(f+(-1)**j*prod)%p
        df=(df+(-1)**j*dprod)%p
    v[a],w[a]=f,df
assert v==[1,0,1,5,2,5,6],v
assert w==[1,5,4,1,5,1,3],w
count=Counter()
for sign in (1,-1):
    for residue in v:
        count[(sign*residue)%p]+=1
assert [count[r] for r in range(7)]==[2,3,3,0,0,3,3]
for k in range(1,5):
    modulus=7**k
    count=Counter(); d=1;count[d]+=1
    for n in range(1,2*modulus):
        d=(n*d+(-1)**n)%modulus
        count[d]+=1
    assert len(count)==5*7**(k-1)
    for residue in range(modulus):
        want={0:2,1:3,2:3,3:0,4:0,5:3,6:3}[residue%7]
        assert count[residue]==want,(k,residue,count[residue],want)
print('VERIFY_OK derivative_table=7 residue_classes=7 complete_levels=4')

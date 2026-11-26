#!/usr/bin/env python3
"""Exact independent extension-field check of the rank-one idempotent word law."""
from itertools import product
from collections import Counter
from fractions import Fraction
Q=4
N=2
ADD=lambda a,b:a^b
# GF(4)=GF(2)[x]/(x^2+x+1), with elements (0,1,x,x+1).
def mul(a,b):
    z=0
    for i in range(2):
        for j in range(2):
            if (a>>i)&1 and (b>>j)&1:z^=1<<(i+j)
    if z&4:z^=7  # x^2=x+1
    return z

def dot(x,y):
    v=0
    for a,b in zip(x,y):v^=mul(a,b)
    return v

def mm(a,b):
    return tuple(mul(a[2*i],b[j])^mul(a[2*i+1],b[2+j]) for i in range(2) for j in range(2))

inv={a:next(b for b in range(1,4) if mul(a,b)==1) for a in range(1,4)}
lines={tuple(mul(x,inv[next(t for t in u if t)]) for x in u) for u in product(range(4),repeat=2) if any(u)}
assert len(lines)==5
E=set()
for u in lines:
    for v in product(range(4),repeat=2):
        if dot(u,v)==1:E.add(tuple(mul(u[i],v[j]) for i in range(2) for j in range(2)))
assert len(E)==20
Z=(0,0,0,0)
assert all(mm(a,a)==a for a in E)
d=Counter({a:1 for a in E})
for k in range(1,6):
    if k>1:
        nex=Counter()
        for a,c in d.items():
            for b in E:nex[mm(a,b)]+=c
        d=nex
    assert sum(d.values())==20**k
    s=Fraction(4,5); C=s**k+Fraction(4,20**k); D=Fraction(1,5**(k-1))
    expected={1:(C-D)/3+D,2:(C-D)/3,3:(C-D)/3}
    for t,p in expected.items():
        actual=Fraction(sum(c for a,c in d.items() if a[0]^a[3]==t),20**k)
        assert actual==p,(k,t,actual,p)
    zero=Fraction(d[Z],20**k)
    assert zero==1-s**(k-1)
    print(f'GF4 n=2 k={k} trace_1={expected[1]} trace_alpha={expected[2]} trace_alpha+1={expected[3]} zero={zero}')
print('VERIFY_OK')

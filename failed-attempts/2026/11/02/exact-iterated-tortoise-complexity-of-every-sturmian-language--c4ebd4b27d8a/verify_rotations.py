#!/usr/bin/env python3
"""Enumerate rational mechanical factors and iterated tortoise images.
All arithmetic describing slopes and words is exact integer arithmetic.
For primitive period q, lengths n<q avoid any endpoint coincidences.
"""
from math import gcd


def T(w):
    i=w.find('1')
    return w if i<0 else w[:i]+w[i+1:]+'1'


def cyclic_factors(p,q,n):
    base = ''.join(str(((i+1)*p)//q - (i*p)//q) for i in range(q))
    ss=base+base
    return {ss[i:i+n] for i in range(q)}

cases=0
for q in range(3,97):
    for p in range(1,q):
        if gcd(p,q)!=1:continue
        for n in range(1,min(q,31)):
            F=cyclic_factors(p,q,n)
            assert len(F)==n+1, (p,q,n,len(F))
            cur=set(F)
            for k in range(1, min(12,q)+1):
                cur={T(w) for w in cur}
                expected=n+1-min(n-1,(k*q)//p)
                assert len(cur)==expected, (p,q,n,k,len(cur),expected)
                cases+=1
print(f'PASS exact_rational_mechanical_cases={cases}')

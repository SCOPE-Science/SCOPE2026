#!/usr/bin/env python3
"""Independent labelled-mask deletion recursion on the crown graph."""
from fractions import Fraction
from functools import lru_cache

@lru_cache(None)
def jam(n, left, right):
    assert left.bit_count()==right.bit_count()
    edges=[(i,j) for i in range(n) for j in range(n)
           if i!=j and (left>>i)&1 and (right>>j)&1]
    if not edges:
        return Fraction(int(left!=0),1)
    return sum((jam(n,left^(1<<i),right^(1<<j)) for i,j in edges),Fraction(0))/len(edges)

reference={2:'0',3:'1/3',4:'4/21',5:'4/21',6:'172/1029',7:'4870/31899',8:'8840593/63096222'}
for n,ref in reference.items():
    q=jam(n,(1<<n)-1,(1<<n)-1)
    assert q==Fraction(ref), (n,q,ref)
    print(n, q, 'states',jam.cache_info().currsize)
print('PASS independent labelled-mask exact dimer RSA n=2..8')

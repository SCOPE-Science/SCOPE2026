#!/usr/bin/env python3
"""Direct F2 matrix enumeration and independent orbit-stabilizer identities."""
from itertools import product
from math import prod

def mul(A,B):
    return tuple(__import__('functools').reduce(lambda a,b: a^b,(B[k] for k in range(4) if A[i]>>k&1),0) for i in range(4))

def rank(A):
    basis={}; r=0
    for a in A:
        v=a
        while v:
            j=v.bit_length()-1
            if j in basis:v^=basis[j]
            else:basis[j]=v; r+=1; break
    return r

mats=(tuple(x) for x in product(range(16),repeat=4))
sq=[M for M in mats if mul(M,M)==(0,0,0,0)]
byrank={r:[M for M in sq if rank(M)==r] for r in range(3)}
assert tuple(len(byrank[r]) for r in range(3))==(1,105,210)
total=zero=nonzero=0
for X in sq:
    for Y in sq:
        XY=mul(X,Y); YX=mul(Y,X)
        if XY==YX:
            total+=1
            if XY==(0,0,0,0):zero+=1
            else:nonzero+=1
assert (total,zero,nonzero)==(10816,8296,2520),(total,zero,nonzero)
for q in (2,3,4,5,7):
    n1=(q**3+q**2+q+1)*(q**3-1)
    gaussian_42=(q**2+1)*(q**2+q+1)
    n2=gaussian_42*(q**2-1)*(q**2-q)
    S=1+n1+n2
    F1=q**5+q**4-q**2
    F2=2*q**4-q**2
    total_formula=S+n1*F1+n2*F2
    nprod=n2*q**2*(q**2-1)
    GL4=prod(q**4-q**i for i in range(4))
    assert nprod==GL4//(q**3*(q-1))
    assert total_formula-nprod>0
    if q==2: assert (total_formula,nprod)==(10816,2520)
    print(f'q={q}: square-zero={S}, rank1={n1}, rank2={n2}, pairs={total_formula}, product_nonzero={nprod}')
print('ALL_EXTERIOR_4X4_PAIR_TESTS_PASS')

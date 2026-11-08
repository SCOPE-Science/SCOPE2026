#!/usr/bin/env python3
"""Independent binary embedded-coordinate Hilbert polynomial checks."""
from itertools import combinations,combinations_with_replacement
from math import comb

def poly_mul(a,b):
    z=0
    while b:
        bit=b & -b
        z ^= a<<(bit.bit_length()-1)
        b-=bit
    return z

def coords(q,n):
    seq=[q**i for i in range(n)]
    return [sum(1<<sum(u) for u in combinations(seq,j)) for j in range(n+1)]

def rank(vectors):
    basis={}
    for v in vectors:
        while v:
            d=v.bit_length()
            if d not in basis:
                basis[d]=v
                break
            v^=basis[d]
    return len(basis)

for n in (2,3,4):
    q=2; D=sum(q**i for i in range(n)); fs=coords(q,n)
    M={}
    for k in range(1,9):
        products=[]
        for tup in combinations_with_replacement(range(n+1),k):
            v=1
            for i in tup:v=poly_mul(v,fs[i])
            products.append(v)
        h=rank(products)
        M[k]=h
    if n==2: pa=1
    elif n==3: pa=4
    else:pa=10
    stable=[k for k,h in M.items() if h==D*k+1-pa]
    assert stable and 8 in stable, (n,M)
    print(f'q=2 n={n} degree={D} predicted_p_a={pa} hilbert_dimensions={M} agrees_at_degrees={stable}')
print('ALL_HILBERT_REPLAYS_PASSED')

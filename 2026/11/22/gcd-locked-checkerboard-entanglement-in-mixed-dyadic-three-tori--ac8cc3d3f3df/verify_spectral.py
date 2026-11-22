"""Separate full-adjacency power-rank and Jordan-kernel verification."""
from itertools import product
from math import gcd

def rank_xor(vectors):
    basis={}
    for v in vectors:
        while v:
            p=(v & -v).bit_length()-1
            b=basis.get(p)
            if b is None:
                basis[p]=v
                break
            v ^= b
    return len(basis)

def neighbor_masks(lengths):
    coords=list(product(*(range(a) for a in lengths)))
    ids={c:j for j,c in enumerate(coords)}
    masks=[]
    for x in coords:
        mask=0
        for axis in range(3):
            for shift in (-1,1):
                y=list(x)
                y[axis]=(y[axis]+shift)%lengths[axis]
                mask |= (1 << ids[tuple(y)])
        masks.append(mask)
    return masks

def multiply(mask, adjacency):
    v=0
    while mask:
        low=mask & -mask
        i=low.bit_length()-1
        v ^= adjacency[i]
        mask ^= low
    return v

def verify():
    cases=[(4,6,6),(8,6,6),(4,6,10),(8,6,10),
           (4,10,10),(4,6,14),(4,6,18),(4,10,30),
           (8,6,14),(16,6,6)]
    for sizes in cases:
        m,u,v=sizes
        n=m*u*v
        h=m//2
        chains=16*gcd(u//2,v//2)-8
        stable=n-chains*h
        adj=neighbor_masks(sizes)
        cols=[1<<i for i in range(n)]
        assert rank_xor(cols)==n
        for time in range(1,h+2):
            cols=[multiply(column,adj) for column in cols]
            got=rank_xor(cols)
            expect=stable+chains*max(h-time,0)
            assert got==expect,(sizes,time,got,expect)
        print(f'PASS lengths={sizes} binary_Jordan_chains={chains}, length={h}, invertible_dimension={stable}')
    print(f'PASS {len(cases)} full-adjacency power-rank tests')

if __name__=='__main__':verify()

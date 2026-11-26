"""Direct exact binary checkerboard-cut rank verification."""
from itertools import product
from math import gcd

def binary_rank(rows):
    pivots = {}
    for v in rows:
        while v:
            j = v.bit_length()-1
            if j not in pivots:
                pivots[j]=v
                break
            v ^= pivots[j]
    return len(pivots)

def cut_rank(lengths):
    coords=list(product(*(range(t) for t in lengths)))
    whites=[c for c in coords if sum(c)%2]
    black=[c for c in coords if not sum(c)%2]
    pos={c:i for i,c in enumerate(whites)}
    rows=[]
    for c in black:
        mask=0
        for j in range(3):
            for e in (-1,1):
                d=list(c)
                d[j]=(d[j]+e)%lengths[j]
                mask ^= 1 << pos[tuple(d)]
        rows.append(mask)
    return binary_rank(rows)

def verify():
    cases=[(4,6,6),(8,6,6),(4,6,10),(8,6,10),
           (4,10,10),(4,6,18),(4,10,30),(4,6,14),
           (8,6,14),(4,18,18),(16,6,6),(4,14,14),
           (4,6,22),(8,10,14),(4,14,18),
           (4,6,30),(4,10,18)]
    for sizes in cases:
        m,u,v=sizes
        g=gcd(u//2,v//2)
        expected=m*u*v//2-8*g+4
        observed=cut_rank(sizes)
        assert observed==expected,(sizes,observed,expected)
        print(f'PASS lengths={sizes} cut_rank={observed} gcd={g}')
    print(f'PASS {len(cases)} physical-graph rank tests')

if __name__=='__main__':verify()

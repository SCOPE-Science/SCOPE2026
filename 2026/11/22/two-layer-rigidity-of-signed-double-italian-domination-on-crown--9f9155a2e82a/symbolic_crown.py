"""Independent coefficient construction for crown-graph low-weight layers."""
from collections import defaultdict
from itertools import product
from math import comb

ALPHABET=(-1,1,2,3)
def sum_counts(n):
    d={0:1}
    for _ in range(n):
        next_d=defaultdict(int)
        for s,c in d.items():
            for label in ALPHABET:
                next_d[s+label]+=c
        d=next_d
    return d

def low_coefficients(n):
    if n<4:raise ValueError('n must be >= 4')
    d=sum_counts(n)
    dsmall=sum_counts(n-1)
    return d.get(1,0),2*n*(dsmall.get(0,0)+dsmall.get(-1,0))

for n in range(4,11):
    c2,c3=low_coefficients(n)
    print(f'n={n} weight2={c2} weight3={c3}')

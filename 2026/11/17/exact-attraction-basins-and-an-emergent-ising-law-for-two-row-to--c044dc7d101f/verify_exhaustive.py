#!/usr/bin/env python3
"""Independent direct-state exhaustive check for a width-two NEC-majority torus."""
from collections import Counter
from itertools import product
from math import comb

def maj(x,y,z):
    return int(x+y+z >= 2)

def step(x):
    n=len(x)
    return tuple((maj(x[i][0], x[i][1], x[(i+1)%n][0]),
                  maj(x[i][1], x[i][0], x[(i+1)%n][1])) for i in range(n))

def predicted(y):
    n=len(y)
    k=sum(y[i]!=y[(i+1)%n] for i in range(n))
    return 3**n-2**n if k==0 else 3**(n-k)

for n in range(3,9):
    hist=Counter()
    nonequal=0
    max_entry=0
    codes=((0,0),(0,1),(1,0),(1,1))
    for x in product(codes,repeat=n):
        seeds=[i for i in range(n) if x[i][0]==x[i][1]]
        if not seeds:
            nonequal+=1
            assert step(x)==x[1:]+x[:1]
            continue
        y=tuple(x[next((i+d)%n for d in range(n) if (i+d)%n in seeds)][0] for i in range(n))
        z=x
        entry=0
        while z!=step(z):
            z=step(z)
            entry+=1
            assert entry<n
        assert z==tuple((t,t) for t in y)
        hist[y]+=1
        max_entry=max(max_entry,entry)
    assert nonequal==2**n
    assert sum(hist.values())==4**n-2**n
    assert len(hist)==2**n
    for y in product((0,1),repeat=n):
        assert hist[y]==predicted(y),(n,y,hist[y],predicted(y))
    assert max_entry==n-1
    print(f'n={n} fixed={len(hist)} absorbing={sum(hist.values())} shifting={nonequal} max_entry={max_entry} homogeneous_basin={hist[(0,)*n]}')
print('ALL_DIRECT_CHECKS_PASS')

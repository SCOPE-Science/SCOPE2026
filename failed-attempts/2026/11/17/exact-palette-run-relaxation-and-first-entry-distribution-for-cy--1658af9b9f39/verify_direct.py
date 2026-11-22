#!/usr/bin/env python3
"""Direct independent state enumeration for synchronous cyclic successor contact on K_n."""
from collections import Counter
from itertools import product

def step(x,q):
    # An occupied successor color guarantees a distinct neighbor on K_n.
    occupied=set(x)
    return tuple((v+1)%q if (v+1)%q in occupied else v for v in x)

def support_clock(x,q):
    occupied=set(x)
    if len(occupied)==q: return 0,q
    r=0
    for c in range(q):
        if c in occupied:
            length=0
            while (c+length)%q in occupied:
                length+=1
            r=max(r,length)
    return r-1,1

def orbit_clock(x,q):
    seen={};z=x
    while z not in seen:
        seen[z]=len(seen)
        z=step(z,q)
    return seen[z],len(seen)-seen[z]

cases=0;states=0
for q in range(4,8):
    for n in range(2,7):
        hist=Counter()
        for x in product(range(q),repeat=n):
            prediction=support_clock(x,q)
            actual=orbit_clock(x,q)
            assert prediction==actual,(q,n,x,prediction,actual)
            hist[actual]+=1
            states+=1
        cases+=1
        print(f'q={q} n={n} total={q**n} clocks={dict(sorted(hist.items()))}')
print(f'PASS direct cases={cases}, states={states}')

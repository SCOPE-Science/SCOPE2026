#!/usr/bin/env python3
"""Direct exhaustive independent-time census for ternary successor chasing on ordered tournaments."""
from collections import Counter
from itertools import product
from math import comb

def advance(state):
    out=[]
    for i, color in enumerate(state):
        out.append((color + int(((color+1)%3) in state[i+1:])) % 3)
    return tuple(out)

def stabilizing_time(state, limit=50):
    for t in range(limit):
        nxt=advance(state)
        if nxt==state:return t
        state=nxt
    raise AssertionError('nonfixing trajectory')

def predicted(n,t):
    # independent rational polynomial coefficient by integer recursion
    h=[1]
    for m in range(2,n+1):
        b=[0]*m
        for j,v in enumerate(h):
            b[j]+=2*v
            b[j+1]+=v
        if m>=3:
            b[0]-=m-2
            b[2]+=m-2
        h=b
    return 3*h[t]

for n in range(1,10):
    hist=Counter(stabilizing_time(x,n+2) for x in product(range(3),repeat=n))
    got=[hist[t] for t in range(n)]
    expect=[predicted(n,t) for t in range(n)]
    assert got==expect,(n,got,expect)
    assert sum(got)==3**n
    print(f'n={n}: {got}')
print('PASS: direct ternary-state enumeration agrees with all-n recurrence through n=9')

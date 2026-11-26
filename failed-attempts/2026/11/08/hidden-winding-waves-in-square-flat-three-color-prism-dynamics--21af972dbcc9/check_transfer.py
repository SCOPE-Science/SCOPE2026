#!/usr/bin/env python3
"""Exact square-flat prism coloring counts and winding distributions (stdlib)."""
from collections import Counter
from math import isclose, sqrt, pi

def step(a,b):
    return ((b-a+1)%3)-1

STATES = [(a,b) for a in range(3) for b in range(3)]
EDGES = [[] for _ in STATES]
for i,(a,b) in enumerate(STATES):
    for j,(c,d) in enumerate(STATES):
        if step(a,c) + step(c,d) - step(b,d) - step(a,b) == 0:
            EDGES[i].append((j,step(a,c)))


def census(n):
    counts=Counter()
    for start in range(9):
        dp = {(start,0):1}
        for _ in range(n):
            nxt={}
            for (s,h),v in dp.items():
                for t,inc in EDGES[s]:
                    key=(t,h+inc)
                    nxt[key]=nxt.get(key,0)+v
            dp=nxt
        for (state,h),v in dp.items():
            if state==start:
                counts[h]+=v
    return counts

def total_closed(n):
    a,b=3,7  # eigenvalues satisfy x^2=7x-4
    v0,v1=2,7
    for _ in range(n):
        v0,v1=v1,7*v1-4*v0
    return v0+3*2**n+4*(-1)**n

def run():
    print('row_sums', [len(e) for e in EDGES])
    for n in range(3,13):
        c=census(n)
        assert all(h%3==0 for h in c)
        total=sum(c.values())
        assert total==total_closed(n),(n,total,total_closed(n))
        assert c[0] > 0
        assert (total-c[0]) > 0
        print(f'n={n} total={total} zero={c[0]} nonzero={total-c[0]} maxwind={max(map(abs,c))}')
    print('TRANSFER_OK')

if __name__=='__main__':run()

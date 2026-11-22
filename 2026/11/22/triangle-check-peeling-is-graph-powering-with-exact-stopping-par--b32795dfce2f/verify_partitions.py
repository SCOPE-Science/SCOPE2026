#!/usr/bin/env python3
"""An independent partition enumerator and connected-graph recurrence."""
from collections import Counter
from math import comb

def partitions(n):
    # canonical restricted-growth strings encode each set partition uniquely
    if n==0:
        yield ();return
    def rec(prefix,k):
        if len(prefix)==n:
            yield tuple(prefix);return
        for x in range(k+1):
            prefix.append(x)
            yield from rec(prefix,max(k,x+1))
            prefix.pop()
    yield from rec([0],1)

def polynomial(n):
    c=Counter()
    for p in partitions(n):
        blocks={b:p.count(b) for b in set(p)}
        weight=comb(n,2)-sum(comb(a,2) for a in blocks.values())
        c[weight]+=1
    return dict(sorted(c.items()))

def successes(n):
    # count connected labelled graphs by the component containing vertex 0.
    connected=[0]*(n+1);connected[1]=1
    for size in range(2,n+1):
        connected[size]=2**comb(size,2)-sum(
          comb(size-1,k-1)*connected[k]*2**comb(size-k,2)
          for k in range(1,size))
    return connected[n]

if __name__=='__main__':
    for n in range(3,8):
        c=polynomial(n)
        print(n,c,'Bell',sum(c.values()),'connected_labeled_graphs',successes(n))

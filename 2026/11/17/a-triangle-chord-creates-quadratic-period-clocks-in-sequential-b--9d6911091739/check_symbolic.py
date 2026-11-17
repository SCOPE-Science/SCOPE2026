#!/usr/bin/env python3
"""Check the explicit invariant orbit for sequential (1,3) hysteresis."""
from collections import Counter

def graph_masks(b):
    L = 2*b+1
    n = 2*L
    adj = [(1 << i) for i in range(n)]
    edges = ([(i,i+1) for i in range(L-1)]
        + [(L+i,L+i+1) for i in range(L-1)]
        + [(b,L+b),(0,2)])
    for u,v in edges:
        adj[u] |= 1 << v
        adj[v] |= 1 << u
    return adj

def sweep(bits, masks):
    for i,mask in enumerate(masks):
        occupied = (bits & mask).bit_count()
        if (bits >> i) & 1:
            if occupied < 3:
                bits &= ~(1 << i)
        elif occupied >= 1:
            bits |= 1 << i
    return bits

def encode(b,r,q):
    # q=0 denotes an empty lower row, q>0 denotes a pulse starting at q-1.
    L = 2*b+1
    lo = 0 if q==0 else ((1 << (b+1))-1) << (q-1)
    return ((1 << r)-1) | (lo << L)

def predicted(b,r,q):
    L=2*b+1
    if r==b+1 and q==0:
        return ((b if b>=3 else L), 0 if b>=3 else b+1)
    if r==3 and q==0:
        return (L,b+1)
    if r> b+1:
        return (r-1,(q-1)%(b+2))
    if r==b+1:
        return (L,(q-1)%(b+2))
    # On the inserted chain, the lower row is empty.
    assert q==0 and 4<=r<=b
    return (r-1,0)

def run(max_b=70):
    checked=0
    for b in range(2,max_b+1):
        masks=graph_masks(b)
        states=[(r,q) for r in range(b+1,2*b+2) for q in range(b+2)]
        states += [(r,0) for r in range(3,b+1)]
        observed=set()
        for r,q in states:
            expected=predicted(b,r,q)
            got=sweep(encode(b,r,q),masks)
            assert got==encode(b,*expected),(b,r,q,expected,got)
            checked+=1
        start=(b+1,0)
        x=start
        for t in range(b*(b+4)):
            assert x not in observed,(b,t,x)
            observed.add(x)
            x=predicted(b,*x)
        assert x==start and len(observed)==len(states)==b*(b+4)
        assert observed==set(states)
    print(f"PASS symbolic graph-update transitions beta=2..{max_b}; {checked} states")
    print("PASS one primitive orbit of length beta*(beta+4) for every tested beta")
    for b in (2,3,4,5,10,20,70):
        print(f"beta={b} vertices={4*b+2} period={b*(b+4)}")

if __name__=='__main__':
    run()

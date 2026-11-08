#!/usr/bin/env python3
"""Independent finite verification of a rank-two inverse involution formula."""
from math import comb

def theta(t):
    k,a,b=t
    if a <= k < b:
        return t
    if k < a:
        return (b-1,k,a)
    return (a,b,k+1)

def map_tuple(n,t):
    k,a,b=t
    return tuple(a if j<=k else b for j in range(1,n+1))

def compose(f,g):
    return tuple(f[z-1] for z in g)  # f after g

def reversal(n,t):
    k,a,b=t
    return (n-k,n+1-b,n+1-a)

def run():
    total=0
    for n in range(2,17):
        ts=[(k,a,b) for k in range(1,n) for a in range(1,n+1) for b in range(a+1,n+1)]
        seen=set()
        fixed=0
        pairs=0
        for t in ts:
            v=theta(t)
            assert v in ts and theta(v)==t
            f=map_tuple(n,t);g=map_tuple(n,v)
            assert compose(compose(f,g),f)==f
            assert compose(compose(g,f),g)==g
            assert theta(reversal(n,t))==reversal(n,v)
            idem=(compose(f,f)==f)
            assert (v==t)==idem
            if v==t: fixed+=1
            else:
                pairs+=1
                assert v!=t
            seen.add(v)
        assert set(ts)==seen
        assert fixed==comb(n+1,3)
        assert pairs//2==comb(n,3)
        assert len(ts)==(n-1)*comb(n,2)
        total+=len(ts)
        print('n=%d elements=%d fixed=%d transpositions=%d reversal=PASS inverse=PASS' % (n,len(ts),fixed,pairs//2))
    print('VERIFY_OK n=2..16 elements=%d' % total)
if __name__=='__main__': run()

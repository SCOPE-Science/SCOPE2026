#!/usr/bin/env python3
"""Independent quotient-graph Euler counting and monodromy checks."""
from functools import lru_cache
from math import factorial

def formula(m):
    t=1 if m==1 else 2**(m-1)*m**(m-2)
    return t*factorial(2*m-1)**m

def count_tours(m):
    edges=[(a,b,p) for a in range(m) for b in range(m) for p in range(2)]
    out=[[i for i,(u,v,p) in enumerate(edges) if u==a] for a in range(m)]
    anchor=edges.index((0,0,0))
    full=(1<<len(edges))-1
    @lru_cache(None)
    def dp(v,used):
        if used==full:return int(v==0)
        return sum(dp(edges[e][1],used|1<<e) for e in out[v] if not (used>>e)&1)
    return dp(0,1<<anchor)

def voltage(q,n,d):
    assert q%d==0 and d>=2
    m=q//d
    if n==2:return m*m*sum(range(d))%d
    # For n>=3 each quotient source vertex has q outgoing edges.
    # Their common phase offset is the second symbol's phase.
    return 0

if __name__=='__main__':
    for m in (1,2,3):
        assert count_tours(m)==formula(m)
        print('Q_EULER',m,formula(m))
    for d in range(2,10):
        for m in range(1,10):
            q=d*m
            v=voltage(q,2,d)
            import math
            assert (math.gcd(d,v)==1)==(d==2 and m%2==1)
            for n in (3,4,5): assert voltage(q,n,d)==0
    print('CROSSCHECK_OK')

#!/usr/bin/env python3
"""Finite independent tests of optimal induced two-regular completion counts.

The infinite-size statements require the mathematical proof, not this checker.
"""
from itertools import combinations
from collections import defaultdict


def path_union(k, i):
    """Build k disjoint 2-vertex paths and i isolated vertices."""
    n = 2 * k + i
    edges = {(2*j, 2*j+1) for j in range(k)}
    return n, edges


def required_additions(k, i):
    r = k + i
    return 2 if (k,i) == (0,1) else r


def predicted_labelled(k, i):
    r=required_additions(k,i)
    if (k,i)==(0,1):return 1
    degs = (1,)*(2*k) + (2,)*i
    s=len(degs)
    if r==0:return 1
    dp={ (0,)*s:1 }
    for _ in range(r):
        nd=defaultdict(int)
        for state,count in dp.items():
            for u,v in combinations(range(s),2):
                if state[u]<degs[u] and state[v]<degs[v]:
                    vstate=list(state);vstate[u]+=1;vstate[v]+=1
                    nd[tuple(vstate)]+=count
        dp=nd
    return dp.get(degs,0)


def brute_completion_counts(k,i,m):
    n, original=path_union(k,i)
    candidates=[(a,b) for a in range(n) for b in range(n,n+m)]
    candidates += list(combinations(range(n,n+m),2))
    count=0
    for bits in range(1<<len(candidates)):
        deg=[0]*(n+m)
        for a,b in original:deg[a]+=1;deg[b]+=1
        # Early degree pruning independent of any claimed theorem.
        valid=True
        for j,(a,b) in enumerate(candidates):
            if bits>>j&1:
                deg[a]+=1;deg[b]+=1
                if deg[a]>2 or deg[b]>2:
                    valid=False;break
        if valid and all(x==2 for x in deg):count+=1
    return count


def main():
    cases=[(0,0),(0,1),(0,2),(0,3),(1,0),(1,1),(1,2),(2,0),(2,1)]
    for k,i in cases:
        r=required_additions(k,i)
        assert r<=3
        observed=[brute_completion_counts(k,i,m) for m in range(r+1)]
        expected=predicted_labelled(k,i)
        assert not any(observed[:-1]),(k,i,observed)
        assert observed[-1]==expected,(k,i,observed,expected)
        print('paths=%d isolated=%d min_new=%d labelled_optima=%d verified' % (k,i,r,expected))
    print('ALL_CHECKS_OK')

if __name__=='__main__':main()

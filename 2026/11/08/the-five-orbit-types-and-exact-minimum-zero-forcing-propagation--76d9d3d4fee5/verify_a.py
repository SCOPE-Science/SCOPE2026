#!/usr/bin/env python3
"""Independent explicit-state enumerator for a minimum zero-forcing family."""
from itertools import combinations
from collections import Counter

def neighbours(n):
    N=2*n
    return [((v-1)%N,(v+1)%N,(v+n)%N) for v in range(N)]

def rounds(n, subset, adj):
    blue=set(subset)
    for t in range(2*n+1):
        if len(blue)==2*n:
            return t
        nxt=set()
        for v in blue:
            white=[u for u in adj[v] if u not in blue]
            if len(white)==1:
                nxt.add(white[0])
        if not nxt:
            return None
        blue.update(nxt)
    raise AssertionError('nontermination')

def expected(n):
    if n%2==0:
        h=n//2
        return Counter({h-1:n,h:8*n,h+1:4*n})
    h=(n-1)//2
    return Counter({h:3*n,h+1:6*n,h+2:4*n})

def canonical_orbit(n,subset):
    N=2*n
    return min(tuple(sorted((sgn*v+k)%N for v in subset))
               for sgn in (1,-1) for k in range(N))

def main():
    for n in range(4,19):
        adj=neighbours(n)
        profile=Counter(); orbits={}
        if n<=11:
            for subset in combinations(range(2*n),3):
                assert rounds(n,subset,adj) is None, ('three-set forces',n,subset)
        for subset in combinations(range(2*n),4):
            t=rounds(n,subset,adj)
            if t is not None:
                profile[t]+=1
                o=canonical_orbit(n,subset)
                if o not in orbits:
                    orbits[o]=[0,t]
                assert orbits[o][1]==t
                orbits[o][0]+=1
        assert profile==expected(n), ('wrong spectrum',n,profile,expected(n))
        assert sorted(v[0] for v in orbits.values())==sorted([n,2*n,2*n,4*n,4*n]), (n,orbits)
        assert len(orbits)==5
        print(f'n={n}: {sum(profile.values())} minimum sets, profile={sorted(profile.items())}, five orbits',flush=True)
    print('PY_EXHAUSTIVE_PASS')
if __name__=='__main__': main()

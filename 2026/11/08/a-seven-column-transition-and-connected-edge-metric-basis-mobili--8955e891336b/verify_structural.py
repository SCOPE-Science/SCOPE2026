#!/usr/bin/env python3
"""Configuration generator and independent token-move census."""
from itertools import combinations
from math import comb
from collections import Counter,deque

def generate(n):
    ans=[]
    for hole in range(n):
        cols=[j for j in range(n) if j!=hole]
        for k in range(3,n-3):
            for first in combinations(cols,k):
                ff=set(first)
                ans.append(sum(1<<j for j in first)+sum(1<<(n+j) for j in cols if j not in ff))
    return ans

def moves(mask,n,slide):
    used=[i for i in range(2*n) if mask>>i&1]
    empty=[i for i in range(2*n) if not(mask>>i&1)]
    for a in used:
        for b in empty:
            if slide and not(a//n==b//n or a%n==b%n):continue
            yield mask^(1<<a)^(1<<b)

def check(n):
    states=generate(n)
    assert len(set(states))==len(states)
    expected=n*(2**(n-1)-2*(1+n-1+comb(n-1,2)))
    assert len(states)==expected
    index=set(states)
    for slide in (True,False):
        graph={s:set(moves(s,n,slide))&index for s in states}
        assert all(s in graph[t] for s,neigh in graph.items() for t in neigh)
        q=deque([states[0]]);seen={states[0]}
        while q:
            for v in graph[q.popleft()]:
                if v not in seen:seen.add(v);q.append(v)
        assert len(seen)==len(states)
        deg=Counter(map(len,graph.values()))
        print(f'n={n} slide={slide} bases={len(states)} edges={sum(map(len,graph.values()))//2} degree_hist={sorted(deg.items())} connected=yes')
    if n==7:
        assert all(len(list(moves(s,n,True)))>=6 for s in states)
        assert all(len(set(moves(s,n,True))&index)==6 for s in states)
        assert all((set(moves(s,n,True))&index)==(set(moves(s,n,False))&index) for s in states)
    print(f'PASS structural counting and reconfiguration n={n}')

if __name__=='__main__':
    for n in range(7,11):check(n)

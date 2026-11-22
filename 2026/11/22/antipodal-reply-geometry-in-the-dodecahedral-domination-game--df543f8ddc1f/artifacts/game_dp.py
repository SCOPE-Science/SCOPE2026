#!/usr/bin/env python3
"""Exact minimax on the dodecahedral graph GP(10,2); standard library only."""
from collections import Counter, deque
from functools import lru_cache

N = 20
adj = [set() for _ in range(N)]
def edge(u,v):
    adj[u].add(v); adj[v].add(u)
for i in range(10):
    edge(i, (i+1)%10)
    edge(i, 10+i)
    edge(10+i, 10+(i+2)%10)
assert sum(map(len,adj)) == 60 and all(len(x)==3 for x in adj)
closed = [sum(1<<x for x in (adj[v]|{v})) for v in range(N)]
FULL = (1<<N)-1

def distances(x):
    d = [-1]*N;d[x]=0;q=deque([x])
    while q:
        v=q.popleft()
        for w in adj[v]:
            if d[w]<0:d[w]=d[v]+1;q.append(w)
    return d

@lru_cache(None)
def solve(covered,turn):
    """Number of future selected vertices; turn 0=minimizer, 1=maximizer."""
    if covered == FULL: return 0
    nxt=(covered|a for a in closed if (a&~covered))
    vals=[1+solve(mask,1-turn) for mask in nxt]
    return min(vals) if turn==0 else max(vals)

assert solve(0,0)==9 and solve(0,1)==8
assert all(sorted(Counter(distances(v)).items())==[(0,1),(1,3),(2,6),(3,6),(4,3),(5,1)] for v in range(N))

for u in range(N):
    du=distances(u)
    assert all(1+solve(closed[u],1)==9 for _ in [0])
    assert 1+solve(closed[u],0)==8
    for v in range(N):
        if u==v:continue
        a=closed[u]|closed[v]
        # If Dominator chose u, Staller chooses v, then Dominator plays.
        dscore=2+solve(a,0)
        # If Staller chose u, Dominator chooses v, then Staller plays.
        sscore=2+solve(a,1)
        assert dscore==(9 if du[v] in (1,5) else 8), (u,v,dscore)
        assert sscore==(8 if du[v]==3 else 9), (u,v,sscore)
print('graph: GP(10,2), vertices=20 edges=30, distance profile=1,3,6,6,3,1')
print('game values: Dominator-start=9, Staller-start=8')
print('all 20 first choices equivalent by explicitly checked score')
print('after D first, S response: distance 1/5 -> final 9; distance 2/3/4 -> final 8')
print('after S first, D response: distance 3 -> final 8; distance 1/2/4/5 -> final 9')
print('first-two-move positions verified=760')
print('reachable memoized states='+str(solve.cache_info().currsize))

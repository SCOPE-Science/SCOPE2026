#!/usr/bin/env python3
"""Direct state-space verification of optimal monitoring and local relocation.
Uses graph-neighborhood propagation, not the row/column criterion, to decide feasibility.
"""
from collections import Counter, deque
from itertools import combinations


def rook(n):
    adj = [set() for _ in range(n*n)]
    for i in range(n*n):
        for j in range(n*n):
            if i != j and (i//n == j//n or i%n == j%n):
                adj[i].add(j)
    return adj


def monitor(seed, adj):
    seen = set(seed)
    for x in seed: seen.update(adj[x])
    while True:
        new = set()
        for x in seen:
            residual = adj[x] - seen
            if len(residual) == 1: new.update(residual)
        if not new: break
        seen |= new
    return len(seen) == len(adj)


def states(n):
    adj = rook(n)
    for k in range(1,n):
        valid = [tuple(x) for x in combinations(range(n*n), k) if monitor(x,adj)]
        if valid: return k,valid,adj
    raise AssertionError('No feasible optimum')


def graph(states,adj):
    lookup = {v:i for i,v in enumerate(states)}
    graph = [set() for _ in states]
    for i, ss in enumerate(states):
        seed = set(ss)
        for u in ss:
            for v in adj[u]-seed:
                new = tuple(sorted((seed-{u}) | {v}))
                if new in lookup: graph[i].add(lookup[new])
    assert all(i in graph[j] for i,neighbors in enumerate(graph) for j in neighbors)
    return graph


def bfs(graph, start):
    dist = [-1]*len(graph)
    dist[start] = 0
    q = deque([start])
    while q:
        v=q.popleft()
        for w in graph[v]:
            if dist[w] == -1:
                dist[w]=dist[v]+1
                q.append(w)
    assert min(dist)>=0
    return dist


def canonical_pairs(n,idx):
    expected=set()
    for r in range(n):
        for c in range(n):
            a=tuple(sorted(i*n+c for i in range(n) if i != r))
            b=tuple(sorted(r*n+j for j in range(n) if j != c))
            expected.add(tuple(sorted((idx[a],idx[b]))))
    return expected


def main():
    for n in (3,4,5):
        k,ss,adj=states(n)
        assert k == n-1, (n,k)
        g=graph(ss,adj)
        v=len(g); edges=sum(map(len,g))//2
        assert v == 2*n**n-n*n*__import__('math').factorial(n-1)
        assert edges == n*(n-1)*(n**n-__import__('math').factorial(n))
        idx={s:i for i,s in enumerate(ss)}
        canon=canonical_pairs(n,idx)
        observed=set()
        # For n=5 only one source per canonical destination pair plus 20 other probes.
        starts=range(v) if n<=4 else sorted({a for a,b in canon})[:25] + list(range(0,v,283))
        for a in starts:
            d=bfs(g,a)
            assert max(d)<=2*(n-1)
            for b,cost in enumerate(d):
                if cost == 2*(n-1):observed.add(tuple(sorted((a,b))))
        if n<=4: assert observed == canon, (n, len(observed),len(canon))
        if n==5: assert observed<=canon and observed, (n,observed-canon)
        print('direct:', 'n=',n,'minimum=',k,'states=',v,
              'slides=',edges,'diameter pairs examined=',len(starts),
              'observed extremals=',len(observed), 'predicted=',len(canon),flush=True)
    print('DIRECT_VERIFY_OK')


if __name__=='__main__': main()

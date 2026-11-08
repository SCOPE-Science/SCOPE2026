#!/usr/bin/env python3
"""Enumerate actual shortest paths as sequences of Johnson vertices; no Cayley implementation."""
from itertools import permutations
from collections import deque, Counter
from math import factorial, comb

for d in range(1,5):
    A=set(range(d)); B=set(range(d,2*d))
    paths=[]
    for remove_order in permutations(A):
      for add_order in permutations(B):
        current=A.copy(); sequence=[frozenset(current)]
        for out,into in zip(remove_order,add_order):
          assert out in current and into not in current
          current.remove(out);current.add(into)
          sequence.append(frozenset(current))
        assert current==B
        paths.append(tuple(sequence))
    assert len(paths)==factorial(d)**2
    adj=[set() for _ in paths]
    for i in range(len(paths)):
      for j in range(i):
        if sum(paths[i][t]!=paths[j][t] for t in range(1,d))==1:
          adj[i].add(j);adj[j].add(i)
    assert all(len(v)==3*(d-1) for v in adj)
    N=len(paths)
    assert sum(map(len,adj))//2==N*3*(d-1)//2
    # Count ALL triangles directly from the graph, not from a predicted structure.
    triangles=sum(len(adj[u]&adj[v]) for u in range(N) for v in adj[u] if u<v)//3
    assert triangles==N*(d-1)
    dist={0:0}; queue=deque([0])
    while queue:
      u=queue.popleft()
      for v in adj[u]:
        if v not in dist:
          dist[v]=dist[u]+1; queue.append(v)
    assert len(dist)==N and max(dist.values())==comb(d,2)
    print('DIRECT_PASS d=%d paths=%d edges=%d triangles=%d diameter=%d'%(d,N,sum(map(len,adj))//2,triangles,max(dist.values())))
print('DIRECT_ALL_PASS')

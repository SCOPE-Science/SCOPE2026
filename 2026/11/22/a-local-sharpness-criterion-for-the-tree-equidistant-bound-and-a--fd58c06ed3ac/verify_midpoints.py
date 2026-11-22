"""Reproduce the midpoint and class criterion by an independent Python implementation.
Run with: python3 verify_midpoints.py
"""
from itertools import product
from collections import deque

def tree(code):
    n=len(code)+2
    deg=[1]*n
    for x in code:deg[x]+=1
    adj=[set() for _ in range(n)]
    for x in code:
        y=next(y for y in range(n) if deg[y]==1)
        adj[x].add(y);adj[y].add(x);deg[x]-=1;deg[y]-=1
    x,y=[i for i in range(n) if deg[i]==1]
    adj[x].add(y);adj[y].add(x)
    return adj

def witness_distances(adj):
    n=len(adj); dd=[]
    for s in range(n):
        d=[-1]*n;d[s]=0;q=deque([s])
        while q:
            v=q.popleft()
            for w in adj[v]:
                if d[w]<0:d[w]=d[v]+1;q.append(w)
        dd.append(d)
    return dd

def check(adj):
    n=len(adj)
    dist=witness_distances(adj)
    side=[None]*n;side[0]=0;q=deque([0])
    while q:
        x=q.popleft()
        for y in adj[x]:
            if side[y] is None:side[y]=1-side[x];q.append(y)
    classes=[{x for x in range(n) if side[x]==i} for i in range(2)]
    def eq(s):
        o=set(range(n))-s
        return all(any(dist[w][x]==dist[w][y] for w in s) for x in o for y in o if x<y)
    for i in range(2):
        pred=all(len(adj[v])!=2 or any(len(adj[u])==1 for u in adj[v]) for v in classes[1-i])
        assert eq(classes[i])==pred
    if all(len(adj[v])!=2 or any(len(adj[u])==1 for u in adj[v]) for v in range(n)):
        for mask in range(1<<n):
            s={v for v in range(n) if mask>>v&1}
            assert eq(s) == (classes[0]<=s or classes[1]<=s)

count=0
for n in range(2,7):
    for code in product(range(n),repeat=n-2):
        check(tree(code));count+=1
# deterministic mixed-degree trees of greater order, including long subdivisions
for n in range(7,12):
    for k in range(35):
        code=[(j*j+3*j*k+5*k+7)%n for j in range(n-2)]
        check(tree(code));count+=1
print('TREE_MIDPOINT_INDEPENDENT_OK',count)

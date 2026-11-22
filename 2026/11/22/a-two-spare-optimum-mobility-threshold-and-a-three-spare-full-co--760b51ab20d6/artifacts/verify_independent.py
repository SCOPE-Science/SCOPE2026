#!/usr/bin/env python3
"""Independent construction: shortest-path DFS, subset enumeration, union-find."""
from collections import defaultdict, Counter, deque
from itertools import combinations

V = tuple(range(16))
NBR = {u:tuple(v for v in V if (u ^ v).bit_count() == 1) for u in V}
# Construct shortest paths by graph distance, not coordinate permutations.
def paths_to(s,t):
    queue = deque([s])
    depth = {s:0}
    while queue:
        x=queue.popleft()
        for y in NBR[x]:
            if y not in depth:
                depth[y] = depth[x]+1
                queue.append(y)
    out=[]
    def dfs(u,history):
        if u==t:
            out.append(sum(1<<v for v in history))
        else:
            for v in NBR[u]:
                if depth[v]==depth[u]+1 and depth[v]+(v^t).bit_count()==depth[t]:
                    dfs(v,history+[v])
    dfs(s,[s]);return out

P=[]
for u in V:
    for v in V:
        if u<v and (u^v).bit_count()==4:
            pv=paths_to(u,v)
            assert len(pv)==24
            P.extend(pv)
assert len(P)==192 and len(set(P))==192

# A separate equivalent algorithm: a feasible set has no disjoint diametral path.
feasible=set()
minimum=[]
for k in range(16+1):
    for comb in combinations(V,k):
        m=sum(1<<v for v in comb)
        if not any(m&p==0 for p in P):
            feasible.add(m)
            if k==6:minimum.append(m)
assert len(feasible)==22499 and len(minimum)==40
assert Counter(x.bit_count() for x in feasible)==Counter({
    6:40,7:560,8:2910,9:5920,10:6376,11:4176,12:1820,
    13:560,14:120,15:16,16:1})

# Union-find is independent of the first checker's breadth-first components.
for cap, target in [(6,{1:40}),(7,{1:160,11:40}),
                    (8,{1:260,3250:1}),(9,{9430:1})]:
    S={x for x in feasible if x.bit_count()<=cap}
    parent={x:x for x in S};rank={x:1 for x in S}
    def root(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]];x=parent[x]
        return x
    def unite(x,y):
        x=root(x);y=root(y)
        if x!=y:
            if rank[x]<rank[y]:x,y=y,x
            parent[y]=x;rank[x]+=rank[y]
    for s in S:
        for v in range(16):
            if not(s>>v &1):
                t=s|(1<<v)
                if t in S:unite(s,t)
    classes=Counter(root(s) for s in S)
    assert Counter(classes.values())==Counter(target)
    if cap==8:
        assert len({root(s) for s in minimum})==1
    if cap==7:
        assert len({root(s) for s in minimum})==40
    if cap==9:
        assert len(classes)==1
# Independent removal minimality.
minim={s for s in feasible if all((s&~(1<<v)) not in feasible for v in V if (s>>v)&1)}
assert Counter(s.bit_count() for s in minim)==Counter({6:40,7:160,8:260})
# Shortest path search in a graph implicitly generated from valid add/removal neighbors.
allowed={s for s in feasible if s.bit_count()<=8}
pairdist=Counter()
for i,a in enumerate(minimum):
    q=deque([a]);d={a:0}
    while q:
        x=q.popleft()
        for j in V:
            y=x^(1<<j)
            if y in allowed and y not in d:
                d[y]=d[x]+1;q.append(y)
    assert len(d)==3250
    for b in minimum[i+1:]:pairdist[d[b]]+=1
assert pairdist==Counter({4:60,6:160,8:480,12:80})
print('INDEPENDENT_PATH_DFS_OK 192')
print('INDEPENDENT_ALL_SUBSETS_OK 65536')
print('INDEPENDENT_UNION_FIND_OK 6:40 7:200 8:261 9:1')
print('INDEPENDENT_DISTANCE_PROFILE_OK')
print('VERIFY_INDEPENDENT_OK')

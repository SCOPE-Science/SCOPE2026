#!/usr/bin/env python3
"""Independent exhaustive verification for the Pappus-graph odd-domination theorem.
Uses the 18-cycle plus nine explicit chords, not a graph library.
"""
from collections import Counter, deque
from itertools import combinations

N=18
CHORDS=[(0,5),(1,8),(2,13),(3,10),(4,15),(6,11),(7,14),(9,16),(12,17)]
adj=[set() for _ in range(N)]
for a,b in [(i,(i+1)%N) for i in range(N)]+CHORDS:
    assert a!=b and b not in adj[a]
    adj[a].add(b);adj[b].add(a)
assert all(len(x)==3 for x in adj)
assert len(set((min(u,v),max(u,v)) for u in range(N) for v in adj[u]))==27

D=[]
for s in range(N):
    d=[-1]*N;d[s]=0;q=deque([s])
    while q:
        x=q.popleft()
        for y in adj[x]:
            if d[y]<0:d[y]=d[x]+1;q.append(y)
    D.append(d)
assert all(Counter(row)=={0:1,1:3,2:6,3:6,4:2} for row in D)
# Check every intersection number used in the analytic minimum-code proof.
b=[3,2,2,1,0];c=[0,1,1,2,3]
for base in range(N):
    for x in range(N):
        layer=D[base][x]
        assert all(D[base][y]!=layer for y in adj[x])
        assert sum(D[base][y]==layer-1 for y in adj[x])==c[layer]
        assert sum(D[base][y]==layer+1 for y in adj[x])==b[layer]
# Girth check via a complete BFS cycle search.
girth=N+1
for root in range(N):
    d=[-1]*N;parent=[-1]*N;d[root]=0;q=deque([root])
    while q:
        x=q.popleft()
        for y in adj[x]:
            if d[y]<0:d[y]=d[x]+1;parent[y]=x;q.append(y)
            elif y!=parent[x]:girth=min(girth,d[x]+d[y]+1)
assert girth==6

neighbors=[(1<<v) | sum(1<<u for u in adj[v]) for v in range(N)]
sol=[]
for mask in range(1<<N):
    if all(((mask & row).bit_count()&1)==1 for row in neighbors):sol.append(mask)
weights=Counter(mask.bit_count() for mask in sol)
assert weights=={5:18,9:92,13:18},weights
assert len(sol)==128
by_center={}
for v in range(N):
    S=set(adj[v]) | {u for u in range(N) if D[v][u]==4}
    mask=sum(1<<u for u in S)
    assert mask in sol and mask.bit_count()==5
    by_center[v]=mask
assert set(by_center.values())=={m for m in sol if m.bit_count()==5}

def components(mask):
    unseen={v for v in range(N) if mask>>v&1};c=0
    while unseen:
        c+=1;s=unseen.pop();q=[s]
        while q:
            for u in adj[q.pop()]:
                if u in unseen:unseen.remove(u);q.append(u)
    return c
assert all(components(m)>1 for m in sol)

triple_counts=Counter()
for vs in combinations(range(N),3):
    classes=Counter(sum(((m>>v)&1)<<i for i,v in enumerate(vs)) for m in sol)
    assert len(classes)==8 and set(classes.values())=={16},(vs,classes)

profile={i:Counter() for i in range(1,5)}
for u,v in combinations(range(N),2):
    overlap=(by_center[u]&by_center[v]).bit_count()
    profile[D[u][v]][overlap]+=1
assert {k:dict(x) for k,x in profile.items()}=={1:{0:27},2:{1:54},3:{2:54},4:{1:18}}
exchange=[set() for _ in range(N)]
for u,v in combinations(range(N),2):
    if (by_center[u]^by_center[v]).bit_count()==6:
        exchange[u].add(v);exchange[v].add(u)
assert all(len(x)==6 for x in exchange)
assert all(exchange[v]=={u for u in range(N) if D[v][u]==3} for v in range(N))
assert sum(map(len,exchange))//2==54
for v in range(N):
    dist={v:0};q=deque([v])
    while q:
        x=q.popleft()
        for u in exchange[x]:
            if u not in dist:dist[u]=dist[x]+1;q.append(u)
    assert len(dist)==N and max(dist.values())==3

print('PASS direct: 262144 masks; 128 solutions; weights 18/92/18')
print('PASS geometry: 18 unique five-vertex optima; intersection profile 0,1,2,1')
print('PASS OA: all 816 triples exhibit all eight patterns 16 times')
print('PASS mobility: no one- or two-token swaps, three-token graph 6-regular, 54 edges, diameter 3')
print('PASS connectivity: none of the 128 solution-induced subgraphs is connected')

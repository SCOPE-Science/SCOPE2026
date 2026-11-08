"""Exhaustive certificate for edge metric bases of the Fano incidence graph.

Requires only Python 3. Run: python3 heawood_edge_bases_verify.py
"""
from itertools import combinations
from collections import deque, Counter

N=14
adj=[set() for _ in range(N)]
for p in range(7):
    for j in range(7):
        if (p-j)%7 in (0,1,3):
            adj[p].add(7+j)
            adj[7+j].add(p)
assert sorted(map(len,adj))==[3]*14
edges=sorted((u,v) for u in range(N) for v in adj[u] if u<v)
assert len(edges)==21
D=[]
for s in range(N):
    distances=[-1]*N;distances[s]=0
    queue=deque([s])
    while queue:
        u=queue.popleft()
        for v in adj[u]:
            if distances[v]<0:
                distances[v]=distances[u]+1
                queue.append(v)
    assert max(distances)==3
    D.append([min(distances[u],distances[v]) for u,v in edges])

# An unresolved pair of edges yields one bit per landmark.
edgepairs=list(combinations(range(len(edges)),2))
fail=[]
for s in range(N):
    failmask=sum(1<<i for i,(a,b) in enumerate(edgepairs) if D[s][a]==D[s][b])
    fail.append(failmask)
def resolving(S):
    z=(1<<len(edgepairs))-1
    for s in S: z &= fail[s]
    return z==0

for size in range(5):
    assert sum(resolving(S) for S in combinations(range(N),size))==0
bases=[frozenset(S) for S in combinations(range(N),5) if resolving(S)]
assert len(bases)==168
assert Counter(len(S&set(range(7))) for S in bases)=={2:84,3:84}
baseindex={S:i for i,S in enumerate(bases)}

def stategraph(constrained):
    graph=[set() for _ in bases]
    for i,S in enumerate(bases):
        for u in S:
            for v in range(N):
                if v in S or (constrained and v not in adj[u]): continue
                T=frozenset((S-{u})|{v})
                j=baseindex.get(T)
                if j is not None:graph[i].add(j)
    return graph

def components(graph):
    seen=set();result=[]
    for s in range(len(graph)):
        if s in seen:continue
        queue=[s];seen.add(s);component=[]
        while queue:
            u=queue.pop();component.append(u)
            for v in graph[u]:
                if v not in seen:seen.add(v);queue.append(v)
        result.append(component)
    return result

TJ=stategraph(False)
TS=stategraph(True)
assert Counter(map(len,TJ))=={5:168}
assert Counter(map(len,TS))=={2:168}
assert sum(map(len,TJ))//2==420
assert sum(map(len,TS))//2==168
assert Counter(map(len,components(TJ)))=={168:1}
assert Counter(map(len,components(TS)))=={8:21}

ecc=[]
for s in range(len(bases)):
    dist={s:0};queue=deque([s])
    while queue:
        i=queue.popleft()
        for j in TJ[i]:
            if j not in dist:
                dist[j]=dist[i]+1
                queue.append(j)
    assert len(dist)==168
    ecc.append(max(dist.values()))
assert Counter(ecc)=={5:168}

print('PASS independent shortest-path edge distances, 21 edges, 14 vertices')
print('PASS no edge-resolving sets of size <=4, 168 bases of size 5')
print('PASS jump graph 5-regular: 168 vertices, 420 edges, diameter/radius 5')
print('PASS slide graph 2-regular: 168 vertices, 168 edges, 21 components C8')

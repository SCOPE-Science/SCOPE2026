"""Independent minimum resolving partitions verification on the GP(5,2) graph.
Standard-library-only; run: python3 check_partition_gp.py
"""
from collections import Counter, deque

N=10
adj=[set() for _ in range(N)]
def connect(a,b): adj[a].add(b);adj[b].add(a)
for i in range(5):
    connect(i,(i+1)%5)
    connect(i,5+i)
    connect(5+i,5+(i+2)%5)
assert all(len(a)==3 for a in adj)

def distances():
    rows=[]
    for a in range(N):
        d=[-1]*N;d[a]=0;todo=deque([a])
        while todo:
            u=todo.popleft()
            for v in adj[u]:
                if d[v]==-1:
                    d[v]=d[u]+1;todo.append(v)
        rows.append(d)
    assert all(max(row)==2 for row in rows)
    return rows
D=distances()

def canon(xs):
    names={};new=[]
    for x in xs:
        if x not in names: names[x]=len(names)
        new.append(names[x])
    return tuple(new)

def partitions(k):
    def recurse(p,m):
        if len(p)==N:
            if m+1==k:yield tuple(p)
            return
        for c in range(min(k,m+2)):
            p.append(c)
            yield from recurse(p,max(m,c))
            p.pop()
    yield from recurse([0],0)

def resolves(p,k):
    sets=[tuple(i for i in range(N) if p[i]==z) for z in range(k)]
    sig=[tuple(min(D[u][v] for v in block) for block in sets) for u in range(N)]
    return len(set(sig))==N

for k in (2,3,4):
    valid=[p for p in partitions(k) if resolves(p,k)]
    print('GP_k',k,'valid',len(valid),flush=True)
    if valid:break
assert k==4 and len(valid)==7040
byid={p:i for i,p in enumerate(valid)}
links=[set() for _ in valid]
for i,p in enumerate(valid):
    sizes=Counter(p)
    for u in range(N):
        if sizes[p[u]]==1:continue
        for z in range(4):
            if z==p[u]:continue
            q=list(p);q[u]=z;q=canon(q)
            if q in byid:
                links[i].add(byid[q])
assert all(i in links[j] for i,neigh in enumerate(links) for j in neigh)
print('GP_graph_vertices',len(valid),'edges',sum(len(L) for L in links)//2)
print('GP_degrees',sorted(Counter(map(len,links)).items()))
sizes=Counter(tuple(sorted(Counter(p).values())) for p in valid)
print('GP_partition_shapes',sorted(sizes.items()))
seen={0};todo=[0]
for i in todo:
    for j in links[i]:
        if j not in seen:seen.add(j);todo.append(j)
assert len(seen)==7040
print('GP_connected',len(seen)==7040)
# Independent B.F.S. at a witness from each of the graph's two eccentricity types.
for i in (0,20,500,1500,3500,7039):
    dd={i:0};todo=[i]
    for j in todo:
        for u in links[j]:
            if u not in dd:dd[u]=dd[j]+1;todo.append(u)
    assert len(dd)==len(valid)
    print('GP_witness_ecc',i,max(dd.values()))
assert len(valid)==7040 and sum(map(len,links))==69000
print('INDEPENDENT_GP_CHECK_OK')

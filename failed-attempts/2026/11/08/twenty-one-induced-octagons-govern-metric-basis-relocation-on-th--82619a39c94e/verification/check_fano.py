"""Exhaustive graph-distance and octagon check for Fano incidence graph."""
from collections import Counter,deque
from itertools import combinations

V=tuple(range(14)); adj=[set() for _ in V]
for p in range(7):
    for r in (0,1,3):
        ell=7+(p-r)%7
        adj[p].add(ell); adj[ell].add(p)

def distances(u):
    ds=[-1]*14;ds[u]=0;q=deque([u])
    while q:
        a=q.popleft()
        for b in adj[a]:
            if ds[b]<0:ds[b]=ds[a]+1;q.append(b)
    return ds
D=[distances(u) for u in V]
def resolves(s):
    return len({tuple(D[u][v] for v in s) for u in V})==14
assert sum(map(resolves,combinations(V,4)))==0
bases=set(filter(resolves,combinations(V,5)))
assert len(bases)==168
assert Counter(sum(p<7 for p in b) for b in bases)=={2:84,3:84}

def is_octagon(sub):
    z=set(sub)
    if any(len(adj[v]&z)!=2 for v in z):return False
    seen={sub[0]}; q=[sub[0]]
    for v in q:
        for w in adj[v]&z:
            if w not in seen:seen.add(w);q.append(w)
    return len(seen)==8

octagons=[frozenset(t) for t in combinations(V,8) if is_octagon(t)]
assert len(octagons)==21
pattern=(1,0,1,0,1,1,0,1)
proposed=set()
for z in octagons:
    first=min(z);second=min(adj[first]&z)
    order=[first,second]
    while len(order)<8:
        nxt=next(v for v in adj[order[-1]]&z if v!=order[-2]);order.append(nxt)
    assert len(set(order))==8 and order[-1] in adj[order[0]]
    found={tuple(sorted(order[(i+j)%8] for j in range(8) if pattern[j])) for i in range(8)}
    assert len(found)==8
    assert all(resolves(s) for s in found)
    assert proposed.isdisjoint(found)
    proposed.update(found)
assert proposed==bases

B=sorted(bases);idx={x:i for i,x in enumerate(B)}
S=[set() for _ in B]; J=[set() for _ in B]
for k,x in enumerate(B):
    a=set(x)
    for y in B:
        if len(a&set(y))!=4:continue
        v=next(iter(a-set(y)));w=next(iter(set(y)-a))
        J[k].add(idx[y])
        if w in adj[v]:S[k].add(idx[y])

def stats(graph):
    components=[]; unseen=set(range(len(B)))
    while unseen:
        v=min(unseen);unseen.remove(v);seen={v};q=[v]
        for x in q:
            for y in graph[x]:
                if y not in seen:seen.add(y);unseen.discard(y);q.append(y)
        components.append(q)
    e=sum(map(len,graph))//2
    ecc=[]
    for v in range(len(B)):
        ds={v:0};q=[v]
        for x in q:
            for y in graph[x]:
                if y not in ds:ds[y]=ds[x]+1;q.append(y)
        ecc.append(max(ds.values()))
    return e,dict(Counter(map(len,graph))),dict(Counter(map(len,components))),dict(Counter(ecc)),components
se=stats(S);je=stats(J)
assert se[:4]==(168,{2:168},{8:21},{4:168})
assert je[:4]==(420,{5:168},{168:1},{5:168})
assert {frozenset(v for state in comp for v in B[state]) for comp in se[4]}==set(octagons)
print('CHECK_OK checker=python vertex_pairs=91 quadruples=1001 quintuples=2002 octagons=21 bases=168')
print('slide_edges=168 slide_components=21:C8 slide_degree=2 slide_component_diameter=4')
print('jump_edges=420 jump_components=1 jump_degree=5 jump_diameter=5')
print('point_line_splits=84:84 octagon_pattern=10101101 unique_octagon=yes')

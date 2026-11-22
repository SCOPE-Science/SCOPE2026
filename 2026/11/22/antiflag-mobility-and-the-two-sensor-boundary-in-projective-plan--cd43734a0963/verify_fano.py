"""Standalone verification of the Fano-incidence power-domination theorem.
Only the Python standard library is required. Prints a fixed audit digest.
"""
from itertools import combinations, product
from collections import Counter, deque

vectors=[v for v in product((0,1),repeat=3) if v != (0,0,0)]
vertices=range(14)
adj=[set() for _ in vertices]
for i,p in enumerate(vectors):
    for j,l in enumerate(vectors):
        if sum(a*b for a,b in zip(p,l))%2==0:
            adj[i].add(7+j);adj[7+j].add(i)
assert all(len(a)==3 for a in adj)
def observed(S):
    obs=set(S)
    for v in S:obs|=adj[v]
    while 1:
        nxt={next(iter(d)) for v in obs if len(d:=adj[v]-obs)==1}
        if not nxt:return obs
        obs|=nxt
pairs={tuple(x) for x in combinations(vertices,2) if len(observed(x))==14}
assert not any(len(observed((v,)))==14 for v in vertices)
anti={(i,7+j) for i in range(7) for j in range(7) if 7+j not in adj[i]}
assert pairs==anti and len(pairs)==28
jump={s:set() for s in pairs}
slide={s:set() for s in pairs}
for s in pairs:
    for t in pairs:
        if s==t:continue
        if len(set(s)^set(t))==2:
            jump[s].add(t)
            x=next(iter(set(s)-set(t)))
            y=next(iter(set(t)-set(s)))
            if y in adj[x]: slide[s].add(t)
assert all(len(a)==6 for a in jump.values())
assert all(len(a)==0 for a in slide.values())
profiles=Counter();paths=Counter();ecc=Counter()
for si,s in enumerate(sorted(pairs)):
    dist={s:0}; ways={s:1}; todo=deque([s])
    while todo:
        x=todo.popleft()
        for y in jump[x]:
            if y not in dist:
                dist[y]=dist[x]+1;ways[y]=0;todo.append(y)
            if dist[y]==dist[x]+1:ways[y]+=ways[x]
    assert len(dist)==28
    ecc[max(dist.values())]+=1
    for t in sorted(pairs)[si+1:]:
        profiles[dist[t]]+=1
        paths[(dist[t],ways[t])]+=1
assert profiles=={1:84,2:210,3:84}
assert paths=={(1,1):84,(2,1):168,(2,2):42,(3,4):84}
assert ecc=={3:28}
print('PASS FANO pair_count=28 jump_edges=84 slide_edges=0 diameter=3')
print('distance_profile='+str(sorted(profiles.items())))
print('path_multiplicities='+str(sorted(paths.items())))

# Independently test the universal two-sensor obstruction in PG(2,3).
def proj(q):
    def norm(x):
        a=next(c for c in x if c)
        z=pow(a,-1,q)
        return tuple(v*z%q for v in x)
    X=sorted({norm(v) for v in product(range(q),repeat=3) if any(v)})
    M=len(X); graph=[set() for _ in range(2*M)]
    for i,u in enumerate(X):
        for j,w in enumerate(X):
            if sum(a*b for a,b in zip(u,w))%q==0:
                graph[i].add(M+j);graph[M+j].add(i)
    return graph
g3=proj(3)
def powered(S,nb):
    seen=set(S)
    for s in S:seen|=nb[s]
    while 1:
        nxt=set()
        for v in seen:
            z=nb[v]-seen
            if len(z)==1:nxt|=z
        if not nxt:return len(seen)==len(nb)
        seen|=nxt
assert all(not powered(c,g3) for c in combinations(range(len(g3)),2))
print('PASS PG(2,3) all 325 two-sensor placements fail')

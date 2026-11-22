"""Finite certificate for minimum semitotal domination mobility on the icosahedron.

All graph adjacencies are generated from the two five-cycles, apex vertices, and cross-ring edges.
No external packages are required. Execute: python verify_geometry.py
"""
from itertools import combinations
from collections import Counter, deque

V = tuple(range(12))
A, B = 0, 11
def p(i): return 1+i%5
def q(i): return 6+i%5
edges=set()
def edge(u,v):
    assert u != v
    edges.add(tuple(sorted((u,v))))
for i in range(5):
    edge(A,p(i)); edge(B,q(i))
    edge(p(i),p(i+1)); edge(q(i),q(i+1))
    edge(p(i),q(i)); edge(p(i),q(i-1))
assert len(edges)==30
adj=[set() for _ in V]
for u,v in edges:adj[u].add(v);adj[v].add(u)
assert all(len(x)==5 for x in adj)

def all_dist(u):
    d={u:0}; queue=deque([u])
    while queue:
        x=queue.popleft()
        for y in adj[x]:
            if y not in d:
                d[y]=1+d[x];queue.append(y)
    assert len(d)==12
    return d
D=[all_dist(v) for v in V]
assert Counter(D[u][v] for u in V for v in V if u!=v)==Counter({1:60,2:60,3:12})
opp={u:next(v for v in V if D[u][v]==3) for u in V}
assert all(opp[opp[u]]==u for u in V)
assert all(set(adj[u])|set(adj[opp[u]])==set(V)-{u,opp[u]} for u in V)

def feasible(T):
    T=set(T)
    return (all(T&({v}|adj[v]) for v in V)
            and all(any(D[u][v]<=2 for v in T-{u}) for u in T))
assert all(not feasible(s) for k in (0,1,2) for s in combinations(V,k))
states=frozenset(frozenset(s) for s in combinations(V,3) if feasible(s))
assert len(states)==80

def pair_dist(T):
    return tuple(sorted(D[u][v] for u,v in combinations(sorted(T),2)))
assert Counter(map(pair_dist,states))==Counter({(1,2,3):60,(2,2,2):20})
for T in states:
    is_antipodal=any(opp[u]==v for u,v in combinations(sorted(T),2))
    assert is_antipodal==(pair_dist(T)==(1,2,3))
    assert (not is_antipodal)==(pair_dist(T)==(2,2,2))

J={T:set() for T in states}; S={T:set() for T in states}
for T in states:
    for removed in T:
        for inserted in V:
            if inserted in T: continue
            U=(T-{removed})|{inserted}
            if U in states:
                J[T].add(U)
                if inserted in adj[removed]:S[T].add(U)
assert all(T in J[U] for T in states for U in J[T])
assert all(T in S[U] for T in states for U in S[T])

def metric(graph):
    dist={}
    for start in graph:
        d={start:0};queue=deque([start])
        while queue:
            u=queue.popleft()
            for v in graph[u]:
                if v not in d:
                    d[v]=d[u]+1;queue.append(v)
        assert len(d)==80, 'disconnected solution graph'
        dist[start]=d
    return dist
DJ=metric(J);DS=metric(S)
assert sum(len(v) for v in J.values())//2==480
assert sum(len(v) for v in S.values())//2==300
assert Counter(len(J[T]) for T in states)==Counter({13:60,9:20})
assert Counter(len(S[T]) for T in states)==Counter({7:60,9:20})
assert Counter(max(DJ[T].values()) for T in states)==Counter({3:80})
assert Counter(max(DS[T].values()) for T in states)==Counter({4:60,3:20})
ordered=sorted(states,key=lambda x:tuple(sorted(x)))
assert Counter(DJ[T][U] for i,T in enumerate(ordered) for U in ordered[i+1:])==Counter({1:480,2:1200,3:1480})
assert Counter(DS[T][U] for i,T in enumerate(ordered) for U in ordered[i+1:])==Counter({1:300,2:1050,3:1570,4:240})
assert Counter(DS[T][U]-DJ[T][U] for i,T in enumerate(ordered) for U in ordered[i+1:])==Counter({0:2440,1:690,2:30})

def obstruction(T,U):
    if len(T&U)!=2: return False
    shared=T&U
    a,b=tuple(shared)
    if opp[a]!=b:return False
    x=next(iter(T-shared));y=next(iter(U-shared))
    return opp[x]==y
assert sum(obstruction(T,U) for i,T in enumerate(ordered) for U in ordered[i+1:])==30
assert all((DS[T][U]-DJ[T][U]==2)==obstruction(T,U)
           for i,T in enumerate(ordered) for U in ordered[i+1:])
print('PASS independent closed-neighborhood feasibility and shortest path enumeration')
print('V=80; types=60 antipodal triples+20 distance-two triangles; J=480 edges; S=300 edges')
print('J radius/diameter=3/3; S radius/diameter=3/4; detours (0,1,2)=(2440,690,30)')
print('All 30 maximum-detour pairs exchange antipodal third vertices while holding antipodal pair')

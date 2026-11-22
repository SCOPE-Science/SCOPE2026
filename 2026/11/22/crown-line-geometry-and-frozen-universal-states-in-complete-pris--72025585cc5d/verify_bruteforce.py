"""Direct finite graph and zero-forcing verification for complete prisms.

Run: python3 verify_bruteforce.py
Requires only Python's standard library.
"""
from itertools import combinations
from collections import deque, Counter


def adjacency(n):
    adj = [set() for _ in range(2*n)]
    for u in range(2*n):
        for v in range(u+1, 2*n):
            if u//n == v//n or u % n == v % n:
                adj[u].add(v)
                adj[v].add(u)
    return adj


def zero_forces(initial, adj):
    blue = set(initial)
    while True:
        forced = set()
        for v in blue:
            white_neighbors = adj[v] - blue
            if len(white_neighbors) == 1:
                forced.update(white_neighbors)
        if not forced:
            return len(blue) == len(adj)
        blue.update(forced)


def bfs_metrics(graph):
    n = len(graph)
    unseen = set(range(n))
    components = []
    distance_maps = [{} for _ in range(n)]
    path_counts = [{} for _ in range(n)]
    for s in range(n):
        distances = {s:0}
        counts = {s:1}
        q = deque([s])
        while q:
            v=q.popleft()
            for w in graph[v]:
                if w not in distances:
                    distances[w] = distances[v]+1
                    counts[w] = counts[v]
                    q.append(w)
                elif distances[w] == distances[v]+1:
                    counts[w] += counts[v]
        distance_maps[s] = distances
        path_counts[s] = counts
        if s in unseen:
            unseen.difference_update(distances)
            components.append(set(distances))
    return sorted(components, key=len, reverse=True),distance_maps,path_counts


def run(n):
    adj = adjacency(n)
    universe = set(range(2*n))
    accepted = set()
    for k in range(n+1):
        for values in combinations(range(2*n),k):
            if zero_forces(values,adj):
                assert k == n, (n,values)
                accepted.add(frozenset(values))
    a_layer=frozenset(range(n))
    b_layer=frozenset(range(n,2*n))
    predicted = {a_layer,b_layer}
    for a in range(n):
        for b in range(n):
            if a != b:
                predicted.add(frozenset((set(a_layer)-{a})|{n+b}))
                predicted.add(frozenset((set(b_layer)-{n+a})|{b}))
    assert accepted==predicted, (n,len(accepted),len(predicted))
    states=sorted(accepted,key=lambda s:tuple(sorted(s)))
    p={s:i for i,s in enumerate(states)}
    tj=[set() for _ in states]
    ts=[set() for _ in states]
    for i,s in enumerate(states):
        for u in s:
            for v in universe-s:
                t=frozenset((s-{u})|{v})
                if t in p:
                    tj[i].add(p[t])
                    if v in adj[u]:ts[i].add(p[t])
    m=n*(n-1)
    assert len(states)==2*m+2
    assert sum(map(len,tj))//2 == 2*m*(n-1)
    assert sum(map(len,ts))//2 == 2*m*(n-2)
    c1,d1,_=bfs_metrics(tj)
    c2,d2,p2=bfs_metrics(ts)
    assert [len(c) for c in c1]==[m+1,m+1]
    assert [len(c) for c in c2]==[m,m,1,1]
    assert sorted(Counter(map(len,tj)).items())==[(2*n-3,2*m),(m,2)]
    assert sorted(Counter(map(len,ts)).items())==[(0,2),(2*n-4,2*m)]
    assert all(max(d1[i].values())==(1 if states[i] in {a_layer,b_layer} else 2) for i in range(len(states)))
    for i,s in enumerate(states):
        if s in {a_layer,b_layer}:
            assert len(d2[i])==1
            continue
        largest=max(d2[i].values())
        assert largest==3
        ant=[j for j,v in d2[i].items() if v==3]
        assert len(ant)==1
        # In a mixed state, a is the omitted index in the majority layer.
        if len(s & a_layer)==n-1:
            a=next(iter(a_layer-s))
            b=next(iter(s & b_layer)) -n
            antipode=frozenset((set(a_layer)-{b})|{n+a})
        else:
            a=next(iter(b_layer-s)) -n
            b=next(iter(s & a_layer))
            antipode=frozenset((set(b_layer)-{n+b})|{a})
        assert states[ant[0]]==antipode
        assert p2[i][ant[0]]==2*(n-2)
    return n,len(states),sum(map(len,tj))//2,sum(map(len,ts))//2,len(c1),len(c2)


if __name__=='__main__':
    for n in range(4,9):
        print('BRUTE_OK',*run(n))

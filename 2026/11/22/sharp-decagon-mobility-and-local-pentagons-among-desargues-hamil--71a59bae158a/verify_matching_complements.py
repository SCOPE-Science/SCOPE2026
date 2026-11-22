"""Exact finite certificate using perfect matching complements on GP(10,3).
Run: python3 verify_matching_complements.py (Python 3 standard library only).
"""
from collections import Counter, deque
from itertools import permutations

N = 10
V = 2 * N
edges = sorted({tuple(sorted((a,b))) for i in range(N)
                for a,b in ((i,(i+1)%N),(i,N+i),(N+i,N+(i+3)%N))})
assert len(edges) == 30
neighbors = [[] for _ in range(V)]
for k,(a,b) in enumerate(edges):
    neighbors[a].append((b,k))
    neighbors[b].append((a,k))
assert all(len(row) == 3 for row in neighbors)

matchings = []
def enumerate_matchings(rem, chosen):
    if rem == 0:
        matchings.append(frozenset(chosen))
        return
    a = (rem & -rem).bit_length()-1
    for b,k in neighbors[a]:
        if rem & (1 << b):
            enumerate_matchings(rem & ~(1 << a) & ~(1 << b), chosen + [k])

enumerate_matchings((1 << V)-1, [])
assert len(matchings) == 60 and len(set(matchings)) == 60

def factor_components(M):
    nbr = [[] for _ in range(V)]
    for i,(a,b) in enumerate(edges):
        if i not in M:
            nbr[a].append(b)
            nbr[b].append(a)
    assert all(len(q)==2 for q in nbr)
    unseen = set(range(V)); sizes=[]
    while unseen:
        root = min(unseen); unseen.remove(root)
        Q = [root]
        for u in Q:
            for v in nbr[u]:
                if v in unseen:
                    unseen.remove(v);Q.append(v)
        sizes.append(len(Q))
    return tuple(sorted(sizes))

assert Counter(factor_components(m) for m in matchings) == Counter({(10,10):36, (20,):24})
cycles = [m for m in matchings if factor_components(m) == (20,)]
assert len(cycles) == 24

# A difference of perfect matchings is a vertex-disjoint union of even cycles.
def simple_flip_length(A,B):
    delta = A ^ B
    if not delta:
        return 0
    nbr=[[] for _ in range(V)]
    for k in delta:
        a,b=edges[k]; nbr[a].append(b);nbr[b].append(a)
    support={i for i in range(V) if nbr[i]}
    assert all(len(nbr[i])==2 for i in support)
    root=min(support); seen={root}; Q=[root]
    for u in Q:
        for v in nbr[u]:
            if v not in seen:
                seen.add(v); Q.append(v)
    return len(delta) if seen == support else 0

adj=[set() for _ in cycles];flip_hist=Counter();diff_hist=Counter()
for i in range(24):
    for j in range(i):
        d=len(cycles[i]^cycles[j]); k=simple_flip_length(cycles[i],cycles[j])
        diff_hist[d]+=1;flip_hist[k]+=1
        if k==10:
            adj[i].add(j);adj[j].add(i)
assert diff_hist == Counter({10:84,12:60,16:60,18:60,20:12})
assert flip_hist == Counter({10:84,18:60,0:132})
assert sum(map(len,adj))//2 == 84
assert Counter(map(len,adj)) == Counter({7:24})
assert all(not simple_flip_length(cycles[i],cycles[j]) in (6,8) for i in range(24) for j in range(i))

def shortest_distances(start):
    dist={start:0};Q=deque([start])
    while Q:
        u=Q.popleft()
        for v in adj[u]:
            if v not in dist:
                dist[v]=dist[u]+1;Q.append(v)
    return Counter(dist.values())
assert all(shortest_distances(i)==Counter({0:1,1:7,2:16}) for i in range(24))

# Local geometry: the graph on the seven neighbours of each cycle is C5 plus two isolated points.
for i in range(24):
    nset=adj[i]
    localdeg=Counter(len(adj[j] & nset) for j in nset)
    assert localdeg == Counter({2:5,0:2})
    two={j for j in nset if len(adj[j]&nset)==2}
    root=min(two);seen={root};Q=[root]
    for u in Q:
        for v in (adj[u]&two):
            if v not in seen:seen.add(v);Q.append(v)
    assert len(seen)==5
assert Counter(len(adj[i]&adj[j]) for i in range(24) for j in range(i) if j in adj[i]) == Counter({2:60,0:24})
assert Counter(len(adj[i]&adj[j]) for i in range(24) for j in range(i) if j not in adj[i]) == Counter({2:192})
print('PASS matching-complement enumeration: 60 perfect matchings, 24 Hamiltonian complements')
print('PASS flip enumeration: differences 10:84, 12:60, 16:60, 18:60, 20:12; legal ten-cycle trades 84')
print('PASS local geometry: 7-regular, each neighborhood C5 plus 2 isolates, 40 triangles')
print('PASS metric: connected, all shells (1,7,16), sharp radius and diameter 2')

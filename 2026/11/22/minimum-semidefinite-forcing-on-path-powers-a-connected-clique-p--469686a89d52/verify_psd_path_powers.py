"""Independent exhaustive checks for optimal PSD zero-forcing sets of path powers.
Run: python verify_psd_path_powers.py
Requires only the Python standard library.
"""
from itertools import combinations
from collections import deque

def graph(n, k):
    return [set(j for j in range(n) if j != i and abs(i-j) <= k) for i in range(n)]

def white_components(adj, black):
    unseen = set(range(len(adj))) - black
    while unseen:
        x = unseen.pop()
        c = {x}
        pending = [x]
        for u in pending:
            for v in adj[u] & unseen:
                unseen.remove(v)
                c.add(v)
                pending.append(v)
        yield c

def force(adj, seed, psd=True):
    black = set(seed)
    while len(black) < len(adj):
        components = list(white_components(adj, black)) if psd else [set(range(len(adj))) - black]
        forced = set()
        for c in components:
            for u in black:
                nbrs = adj[u] & c
                if len(nbrs) == 1:
                    forced |= nbrs
        if not forced:
            break
        black |= forced
    return len(black) == len(adj)

def expected_sets(n,k):
    left = [frozenset({0} | (set(range(1,k+1))-{i})) for i in range(1,k+1)]
    right = [frozenset({n-1} | (set(range(n-k-1,n-1))-{i})) for i in range(n-k-1,n-1)]
    interior = [frozenset(range(a,a+k)) for a in range(1,n-k)]
    return set(left+right+interior)

def exchange_graph(sets,k):
    sets = list(sets)
    adj = [set() for _ in sets]
    for i in range(len(sets)):
        for j in range(i+1,len(sets)):
            if len(sets[i] & sets[j]) == k-1:
                adj[i].add(j);adj[j].add(i)
    dmax=0
    for v in range(len(sets)):
        queue=deque([v]); dist={v:0}
        while queue:
            u=queue.popleft()
            for w in adj[u]:
                if w not in dist:
                    dist[w]=dist[u]+1;queue.append(w)
        assert len(dist)==len(sets), ("disconnected",sets,v)
        dmax=max(dmax,max(dist.values()))
    return sum(map(len,adj))//2,dmax

def expected_edges(n,k):
    if n==k+2: return k*k+2*k
    if n==k+3: return k*k+n+1
    return k*k+n

total=0
for n in range(4,15):
    for k in range(2,min(n-2,6)+1):
        adj=graph(n,k)
        actual={frozenset(s) for s in combinations(range(n),k) if force(adj,s,True)}
        expected=expected_sets(n,k)
        assert actual==expected,(n,k,actual^expected)
        assert len(actual)==n+k-1
        assert not any(force(adj,s,True) for s in combinations(range(n),k-1)),(n,k)
        ordinary={frozenset(s) for s in combinations(range(n),k) if force(adj,s,False)}
        assert ordinary=={s for s in expected if 0 in s or n-1 in s},(n,k,"ordinary")
        e,d=exchange_graph(actual,k)
        assert (e,d)==(expected_edges(n,k),n-k),(n,k,e,d)
        total+=1
print('EXHAUSTIVE_PSD_PATH_POWER_CLASSIFICATION_PASS instances=',total)
print('MINIMUM_SIZE_LOWER_BOUND_AND_ORDINARY_COMPARISON_PASS')
print('EXCHANGE_EDGE_COUNTS_AND_EXACT_DIAMETERS_PASS')
print('VERIFY_OK')

#!/usr/bin/env python3
"""Exact unlabelled-tree enumeration and metric-edge distance spectra (stdlib)."""
from collections import Counter, defaultdict, deque

def edges_from(g):
    return sorted((i,j) for i, ns in enumerate(g) for j in ns if i<j)

def from_edges(n,edges):
    g=[set() for _ in range(n)]
    for u,v in edges:
        g[u].add(v); g[v].add(u)
    return g

def code_root(g, v, parent):
    return '('+''.join(sorted(code_root(g, w, v) for w in g[v] if w!=parent))+')'

def canonical(g):
    deg=[len(x) for x in g]
    remaining=set(range(len(g)))
    while len(remaining)>2:
        leaves={i for i in remaining if deg[i]<=1}
        for i in leaves:
            remaining.remove(i)
            for j in g[i]:deg[j]-=1
    cen=sorted(remaining)
    if len(cen)==1:return 'V'+code_root(g,cen[0],-1)
    return 'E'+''.join(sorted((code_root(g,cen[0],cen[1]), code_root(g,cen[1],cen[0]))))

def trees(n):
    d={canonical(from_edges(2,[(0,1)])):from_edges(2,[(0,1)])}
    for k in range(3,n+1):
        e={}
        for g in d.values():
            for i in range(k-1):
                h=[set(s) for s in g]+[set()]
                h[i].add(k-1);h[k-1].add(i)
                e[canonical(h)]=h
        d=e
        yield k, d

def histogram(g):
    n=len(g); es=edges_from(g)
    ds=[]
    for u in range(n):
        d=[-1]*n;d[u]=0;dq=deque([u])
        while dq:
            v=dq.popleft()
            for w in g[v]:
                if d[w]<0:d[w]=d[v]+1;dq.append(w)
        ds.append(d)
    cnt=Counter(min(ds[u][x], ds[u][y], ds[v][x],ds[v][y]) for i,(u,v) in enumerate(es) for x,y in es[i+1:])
    return tuple(cnt.get(j,0) for j in range(n-2))

def degree(g):return tuple(sorted((len(s) for s in g),reverse=True))

if __name__ == '__main__':
    sizes = (1, 2, 3, 6, 11, 23, 47, 106, 235, 551, 1301, 3159, 7741)
    reduced_counts = {3: 0, 4: 1, 5: 1, 6: 2, 7: 2, 8: 4,
                      9: 5, 10: 10, 11: 14, 12: 26, 13: 42,
                      14: 78, 15: 132}
    actual = []
    for n, T in trees(15):
        actual.append(len(T))
        reduced = [(key, g) for key, g in T.items()
                   if all(len(incident) != 2 for incident in g)]
        assert len(reduced) == reduced_counts[n], (n, len(reduced))
        by_hist = defaultdict(list)
        for key, g in reduced:
            assert canonical(g) == key
            by_hist[histogram(g)].append((key, g))
        collisions = [(h, group) for h, group in by_hist.items()
                      if len(group) > 1]
        if n < 15:
            assert not collisions, (n, collisions)
        else:
            target = {(25, 26, 24, 16), (25, 28, 26, 12),
                      (37, 42, 12)}
            observed = set()
            assert len(collisions) == 3
            for h, group in collisions:
                assert len(group) == 2
                sig = tuple(v for v in h if v)
                assert sig in target
                observed.add(sig)
                print('HISTOGRAM', sig)
                for key, g in group:
                    print('CANONICAL', key, 'DEGREES', degree(g),
                          'EDGES', edges_from(g))
            assert observed == target
        print('ORDER', n, 'TREES', len(T), 'REDUCED', len(reduced),
              'COLLISION_CLASSES', len(collisions))
    assert tuple(actual) == sizes
    print('REDUCED_METRIC_TREE_SHARP_ORDER_15_PASS')

"""Independent exact induced-matching verifier on Möbius ladders.

Uses twisted-column coordinates and raw endpoint adjacency, no assumptions
about the extremal classification or the edge conflict graph.
Run: python3 check_twisted.py [maximum_n], default 10.
"""
import itertools,sys
from collections import Counter, deque

def raw_graph(n):
    vertices=[(i,layer) for i in range(n) for layer in range(2)]
    edges=[]
    for i in range(n):
        edges.append(frozenset(((i,0),(i,1))))
        if i<n-1:
            for layer in (0,1):
                edges.append(frozenset(((i,layer),(i+1,layer))))
        else:
            for layer in (0,1):
                edges.append(frozenset(((n-1,layer),(0,1-layer))))
    assert len(edges)==3*n and len(set(edges))==3*n
    a={v:set() for v in vertices}
    for e in edges:
        u,v=tuple(e);a[u].add(v);a[v].add(u)
    return edges,a

def check(n):
    edges,adj=raw_graph(n)
    m=n//2
    all_opt=[]
    for comb in itertools.combinations(range(len(edges)),m):
        endpoints=[v for idx in comb for v in edges[idx]]
        if len(set(endpoints))!=2*m: continue
        chosen=set(endpoints)
        if any(len(adj[v]&chosen)!=1 for v in chosen):continue
        all_opt.append(frozenset(comb))
    opt=set(all_opt)
    deg=Counter(); remaining=set(opt); components=[]; edge_total=0
    for x in opt:
        d=sum(len(x&y)==m-1 for y in opt if y!=x)
        deg[d]+=1;edge_total+=d
    while remaining:
        seed=remaining.pop();q=deque([seed]); cnt=1
        while q:
            x=q.popleft()
            for a in x:
                z=x-{a}
                for b in range(len(edges)):
                    y=z|{b}
                    if len(y)==m and y in remaining:
                        remaining.remove(y);q.append(y);cnt+=1
        components.append(cnt)
    expected=(6 if n%4==2 else 2) if n%2==0 else n*n
    assert len(opt)==expected, (n,len(opt),expected)
    if n%2==0:
        assert components==[1]*expected and deg==Counter({0:expected})
    else:
        assert components==[n*n]
        assert deg==Counter({4:n*(n-3),5:2*n,6:n})
    assert sum(v*k for k,v in deg.items())==edge_total
    return n,m,len(opt),sorted(deg.items()),sorted(components),edge_total//2

if __name__=='__main__':
    max_n=int(sys.argv[1]) if len(sys.argv)>1 else 10
    for n in range(4,max_n+1):
        print(check(n),flush=True)

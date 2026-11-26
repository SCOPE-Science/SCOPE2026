#!/usr/bin/env python3
"""Independent tree-geometry and reconfiguration checks for subdivided cliques."""
import itertools,math
from collections import deque

def tree_from_prufer(seq,n):
    deg=[1]*n
    for x in seq: deg[x]+=1
    edges=[]
    for x in seq:
        leaf=next(k for k in range(n) if deg[k]==1)
        edges.append(tuple(sorted((x,leaf))))
        deg[x]-=1;deg[leaf]-=1
    a,b=(i for i in range(n) if deg[i]==1)
    edges.append((a,b))
    return frozenset(edges)

def wiener(T,n):
    adj=[[] for _ in range(n)]
    for a,b in T:
        adj[a].append(b);adj[b].append(a)
    ans=0
    for i in range(n):
        dist={i:0};q=deque([i])
        while q:
            v=q.popleft()
            for u in adj[v]:
                if u not in dist:dist[u]=dist[v]+1;q.append(u)
        ans+=sum(dist.values())
    return ans//2

def main():
    for n in range(3,8):
        trees={tree_from_prufer(seq,n) for seq in itertools.product(range(n),repeat=n-2)}
        assert len(trees)==n**(n-2)
        degree_sum=0
        totw=0
        for T in trees:
            W=wiener(T,n)
            totw+=W
            # expected skew forcing TE degree = n-1 + edge exchange count;
            # a tree swap (delete tree edge, add cross-cut edge) is unique.
            adj=[[] for _ in range(n)]
            for a,b in T: adj[a].append(b);adj[b].append(a)
            swaps=set()
            for a,b in T:
                component={a};stack=[a]
                while stack:
                    u=stack.pop()
                    for v in adj[u]:
                        if {u,v}=={a,b}:continue
                        if v not in component:component.add(v);stack.append(v)
                for u in component:
                    for v in set(range(n))-component:
                        x=tuple(sorted((u,v)))
                        if x!=(a,b): swaps.add((tuple(sorted((a,b))),x))
            assert len(swaps)==W-(n-1),(n,len(swaps),W)
            degree_sum+=n-1+len(swaps)
        # number of edges in Cartesian product K_n □ tree-basis graph
        totaledges=n*degree_sum//2
        exact=n*sum(math.comb(n,a)*a**a*(n-a)**(n-a) for a in range(1,n))//4
        assert totaledges==exact,(n,totaledges,exact)
        print(f'K{n}: {len(trees)} spanning trees; {n*len(trees)} optimal sets; {totaledges} exchange edges; Wiener sum {totw}: PASS')
    # Exact independent brute distances for K4, K5 using tree exchange and root change.
    for n in [3,4,5]:
        trees=list({tree_from_prufer(seq,n) for seq in itertools.product(range(n),repeat=n-2)})
        neigh=[[] for _ in trees]
        for i,T in enumerate(trees):
            for j,U in enumerate(trees):
                if i!=j and len(T^U)==2:neigh[i].append(j)
        for ti,T in enumerate(trees):
            q=deque([ti]);d={ti:0}
            while q:
                i=q.popleft()
                for j in neigh[i]:
                    if j not in d:d[j]=d[i]+1;q.append(j)
            assert len(d)==len(trees)
            for tj,U in enumerate(trees):assert d[tj]==n-1-len(T&U)
        dia=1+max(n-1-len(T&U) for T in trees for U in trees)
        print(f'K{n}: all tree-basis distances and overall exchange diameter {dia}: PASS')
if __name__=='__main__':main()

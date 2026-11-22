#!/usr/bin/env python3
"""Independent exhaustive edge-metric-basis enumeration on DP(n,1), 3<=n<=12."""
from itertools import combinations

def count(n):
    V = [(layer,i) for layer in 'xuvy' for i in range(n)]
    es = set()
    def add(p,q): es.add(frozenset((p,q)))
    for i in range(n):
        j=(i+1)%n
        add(('x',i),('x',j));add(('y',i),('y',j))
        add(('x',i),('u',i));add(('v',i),('y',i))
        add(('u',i),('v',j));add(('v',i),('u',j))
    E=sorted((tuple(sorted(e)) for e in es))
    # Floyd Warshall independent of BFS / bitmask implementation.
    N=len(V); pos={v:k for k,v in enumerate(V)}
    D=[[N+1]*N for _ in V]
    for i in range(N):D[i][i]=0
    for e in E:
        a,b=map(pos.__getitem__,e);D[a][b]=D[b][a]=1
    for k in range(N):
        for i in range(N):
            q=D[i][k]
            for j in range(N):
                if q+D[k][j]<D[i][j]: D[i][j]=q+D[k][j]
    cols=[tuple(min(D[i][pos[a]],D[i][pos[b]]) for a,b in E) for i in range(N)]
    # Only a subset of the full lattice is required: min size >=3 by cubic regularity.
    counts={3:0,4:0}; witnesses={3:None,4:None}
    for k in [3,4]:
        for subset in combinations(range(N),k):
            if len(set(zip(*(cols[i] for i in subset))))==len(E):
                counts[k]+=1
                if witnesses[k] is None:witnesses[k]=subset
    return counts,witnesses

if __name__=='__main__':
    for n in range(3,13):
        counts, witnesses=count(n)
        print(f'{n}: triples={counts[3]} foursets={counts[4]} witness3={witnesses[3]} witness4={witnesses[4]}',flush=True)

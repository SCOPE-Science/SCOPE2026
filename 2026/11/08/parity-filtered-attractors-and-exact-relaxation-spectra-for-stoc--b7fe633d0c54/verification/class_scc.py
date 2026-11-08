#!/usr/bin/env python3
"""Independent exhaustive recurrent-class verification of cyclic pendant-defect graph dynamics."""
import itertools
from collections import Counter
import networkx as nx

def classes(n,S):
    S=tuple(sorted(S)); k=len(S); N=n+k
    adj=[set() for _ in range(N)]
    for i in range(n):
        j=(i+1)%n;adj[i].add(j);adj[j].add(i)
    for a,root in enumerate(S):
        j=n+a;adj[root].add(j);adj[j].add(root)
    g=nx.DiGraph();g.add_nodes_from(range(1<<N))
    for x in range(1<<N):
        for v in range(N):
            ones=sum(bool((x>>j)&1) for j in adj[v])+((x>>v)&1)
            size=len(adj[v])+1
            y=x
            if 2*ones < size and not (x>>v)&1: y=x|(1<<v)
            elif 2*ones>size and (x>>v)&1: y=x^(1<<v)
            if y!=x:g.add_edge(x,y)
    allc=list(nx.strongly_connected_components(g));cc=[c for c in allc if not any(v not in c for u in c for v in g.successors(u))]
    return cc,g

def predicted(n,S):
    k=len(S); S=sorted(S)
    ell=[(S[(i+1)%k]-S[i])%n or n for i in range(k)]
    props=[]
    for mask in range(1<<k):
        I=[i for i in range(k) if (mask>>i)&1]
        if len(I)%2!=n%2:continue
        if any((i+1)%k in I for i in I if k>1):continue
        import math
        sz=math.prod(ell[i] for i in I)
        props.extend([sz,sz])
    return sorted(props)

def main():
    combos=0;states=0
    for n in range(3,8):
        for k in range(1,n+1):
            for S in itertools.combinations(range(n),k):
                cc,g=classes(n,S)
                actual=sorted(len(c) for c in cc)
                expect=predicted(n,S)
                assert actual==expect,(n,S,actual,expect)
                combos+=1;states+=g.number_of_nodes()
        print(f'n={n}: all subsets verified; cumulative graph choices {combos}, configurations {states}',flush=True)
    print('PASS',combos,states)
if __name__=='__main__':main()

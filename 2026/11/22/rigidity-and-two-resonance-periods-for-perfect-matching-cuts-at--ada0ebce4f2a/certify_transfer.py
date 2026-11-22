#!/usr/bin/env python3
"""Exact finite-state certificate for the cyclic perfect-matching-cut automata.
Only Python's standard library is used. This file is a standalone recomputation.
"""
from collections import defaultdict

EXPECTED={4:[1],5:[1,2],6:[1],7:[1,2,5]}

def graph_for_step(k):
    width=2*k+2
    left_mask=(1<<(width-1))-1
    graph=defaultdict(set)
    windows=0
    for word in range(1<<width):
        t=lambda j:(word>>(j+k+1))&1  # j=-k-1,...,k
        # For d_j=1-t_(j-1)-t_j to be a 0/1 bit, the two t's cannot both be 1.
        if t(-k-1) and t(-k):continue
        if t(-1) and t(0):continue
        if t(k-1) and t(k):continue
        d=lambda j:1-t(j-1)-t(j)
        s=lambda j:(sum(t(h) for h in range(j,j+k))+d(j)+d(j+k))%2
        if s(-k)+s(0)!=1-d(0):continue
        windows+=1
        a=word&left_mask
        b=word>>1
        graph[a].add(b)
        graph.setdefault(b,set())
    return graph,windows

def tarjan(graph):
    indices={}; low={}; stack=[]; active=set(); out=[]; clock=0
    def visit(v):
        nonlocal clock
        indices[v]=low[v]=clock;clock+=1
        stack.append(v);active.add(v)
        for w in graph[v]:
            if w not in indices:
                visit(w);low[v]=min(low[v],low[w])
            elif w in active:
                low[v]=min(low[v],indices[w])
        if low[v]==indices[v]:
            component=set()
            while True:
                w=stack.pop();active.remove(w);component.add(w)
                if w==v:break
            out.append(component)
    for v in list(graph):
        if v not in indices:visit(v)
    return out

def certify(k):
    g,w=graph_for_step(k)
    cyclic=[]
    for C in tarjan(g):
        if len(C)==1 and next(iter(C)) not in g[next(iter(C))]:continue
        # Assert each recurrent component is a simple directed cycle; the
        # component need not contain every graph vertex.
        internal_edges=sum(len(g[v]&C) for v in C)
        assert internal_edges==len(C)
        assert all(len(g[v]&C)==1 for v in C)
        assert all(sum(v in g[u] for u in C)==1 for v in C)
        cyclic.append((len(C),min(C)))
    sizes=sorted(n for n,_ in cyclic)
    assert sizes==EXPECTED[k],(k,sizes)
    # Explicit roots provide reproducible identifiers for the cyclic SCCs.
    print(f'k={k} windows={w} nodes={len(g)} edges={sum(map(len,g.values()))} '
          f'cyclic_SCC_lengths={sizes} roots={sorted(cyclic)}')
    return sizes

if __name__=='__main__':
    for k in sorted(EXPECTED):certify(k)
    print('PASS: all recurrent components exactly the listed directed cycles.')

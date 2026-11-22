#!/usr/bin/env python3
"""Independent witness construction and validation for length-three palindrome covers.
Only standard library is required. No claims about secondary-structure avoidance.
"""
from collections import defaultdict
from itertools import product

def euler_edges(q):
    # Undirected multigraph K_q with a loop at every vertex and a
    # duplicated fixed perfect matching when q is even.
    edges = [(a, a) for a in range(q)]
    edges += [(a,b) for a in range(q) for b in range(a+1,q)]
    if q % 2 == 0:
        edges += [(a,a+1) for a in range(0,q,2)]
    adj = [[] for _ in range(q)]
    for eid,(a,b) in enumerate(edges):
        adj[a].append((b,eid))
        if a!=b: adj[b].append((a,eid))
        else: adj[b].append((a,eid)) # two half-edges for a loop
    used = [False]*len(edges)
    stack=[(0,None)]
    trail=[]
    while stack:
        v,_ = stack[-1]
        while adj[v] and used[adj[v][-1][1]]:
            adj[v].pop()
        if not adj[v]:
            vertex, incoming=stack.pop()
            if incoming is not None: trail.append(incoming)
        else:
            u,eid=adj[v].pop()
            if not used[eid]:
                used[eid]=True
                stack.append((u,(v,u,eid)))
    trail.reverse()
    assert len(trail)==len(edges) and all(used)
    assert all(trail[j][1] == trail[(j+1)%len(trail)][0] for j in range(len(trail)))
    return trail

def witness(q):
    chosen = set()
    seq = []
    for a,b,eid in euler_edges(q):
        e=(min(a,b),max(a,b))
        if a==b:
            path=[a,a,a]
        elif e not in chosen:
            chosen.add(e)
            path=[a,b,a,b]
        else:
            path=[a,b]
        if seq: assert seq[-1]==path[0]
        if not seq:seq.extend(path)
        else:seq.extend(path[1:])
    assert seq[0]==seq[-1]
    w=tuple(seq[:-1])
    target={(a,b,a) for a in range(q) for b in range(q)}
    found={(w[i%len(w)],w[(i+1)%len(w)],w[(i+2)%len(w)]) for i in range(len(w))}
    assert target<=found
    predicted=(3*q*q+q+(q if q%2==0 else 0))//2
    assert len(w)==predicted, (q,len(w),predicted)
    assert len(target)==q*q
    return w

def brute_binary():
    q=2; target={(a,b,a) for a in range(q) for b in range(q)}
    for n in range(1,9):
        hits=[]
        for w in product(range(q),repeat=n):
            factors={(w[i],w[(i+1)%n],w[(i+2)%n]) for i in range(n)}
            if target<=factors:hits.append(w)
        if n<8:assert not hits,(n,hits[:2])
        else:assert hits
    return len(hits)

if __name__=='__main__':
    for q in range(2,9):
        w=witness(q)
        print(q,len(w),''.join(str(c) for c in w) if q<=4 else '(verified)')
    print('binary exhaustive length <=8: OK, shortest-rooted-count',brute_binary())

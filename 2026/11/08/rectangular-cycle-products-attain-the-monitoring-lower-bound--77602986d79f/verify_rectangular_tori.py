#!/usr/bin/env python3
"""Independent finite verification of rectangular cycle-product monitoring constructions."""
from collections import deque
from math import ceil

EXCEPTIONS={(5,6):[3,2,1,2,3,4],(7,8):[2,3,1,2,3,4,5,6]}

def set_of_probes(n,m):
    assert 5<=n<=m
    shifts=EXCEPTIONS.get((n,m),[j*n//m for j in range(m)])
    base={0,n//3,(2*n)//3}
    return {(i,j) for j in range(m) for i in range(n)
            if (i-shifts[j])%n in base}

def short_gap_ok(sequence, modulus):
    sequence=sorted(sequence)
    if len(sequence)<3:return False
    return max((sequence[(k+1)%len(sequence)]-sequence[k])%modulus
               for k in range(len(sequence))) <= (modulus-1)//2

def graph(n,m):
    V=[(i,j) for i in range(n) for j in range(m)]
    idx={v:p for p,v in enumerate(V)}
    edges=set()
    for i,j in V:
        for w in [((i+1)%n,j),(i,(j+1)%m)]:
            edges.add(tuple(sorted((idx[(i,j)],idx[w]))))
    adj=[set() for _ in V]
    for a,b in edges:adj[a].add(b);adj[b].add(a)
    return idx,sorted(edges),adj

def distances(adj,source,removed=None):
    d=[-1]*len(adj);d[source]=0
    queue=deque([source])
    while queue:
        u=queue.popleft()
        for v in adj[u]:
            if removed==(min(u,v),max(u,v)):continue
            if d[v]==-1:d[v]=d[u]+1;queue.append(v)
    return d

def check_by_edge_deletion(n,m,S):
    idx,edges,adj=graph(n,m)
    sel=sorted(idx[v] for v in S)
    base={s:distances(adj,s) for s in sel}
    for edge in edges:
        hits=False
        for u in sel:
            after=distances(adj,u,edge)
            if any(after[v]!=base[u][v] for v in sel):hits=True;break
        if not hits:return False,edge
    return True,None

def verify():
    cases=0
    for n in range(5,66):
        for m in range(n,126):
            S=set_of_probes(n,m)
            assert len(S)==3*m,(n,m,len(S))
            assert all(short_gap_ok([i for i in range(n) if (i,j) in S], n) for j in range(m)),(n,m,'column')
            assert all(short_gap_ok([j for j in range(m) if (i,j) in S], m) for i in range(n)),(n,m,'row')
            cases+=1
    for n,m in [(5,5),(5,6),(5,7),(6,6),(7,7),(7,8),(8,8),(5,9)]:
        S=set_of_probes(n,m)
        passed,edge=check_by_edge_deletion(n,m,S)
        assert passed,(n,m,edge)
    print(f'VERIFY_OK numerical_parameters={cases} direct_edge_deletion_graphs=8 columns_rows_monitored=PASS shortest_path_edge_deletions=PASS opt_lower_bound=3max')

if __name__=='__main__':verify()

#!/usr/bin/env python3
"""Finite exact checks for the ancestry-type theorem. Python 3, standard library only.

Checks are finite sanity tests. The text proof establishes the theorem for all trees.
"""
from itertools import product, combinations


def edges_from_prufer(n, seq):
    degree = [1] * n
    for x in seq: degree[x] += 1
    edges = []
    for x in seq:
        leaf = next(i for i in range(n) if degree[i] == 1)
        edges.append((leaf, x))
        degree[leaf] -= 1
        degree[x] -= 1
    u,v = (i for i in range(n) if degree[i] == 1)
    edges.append((u,v))
    return edges


def ancestor_sets(n, edges, root):
    adj = [[] for _ in range(n)]
    for a,b in edges:
        adj[a].append(b);adj[b].append(a)
    seen={root}; todo=[root]; ancestors=[set() for _ in range(n)]
    for u in todo:
        for v in adj[u]:
            if v in seen: continue
            seen.add(v);todo.append(v)
            ancestors[v] = ancestors[u] | {u}
    assert len(seen)==n
    return ancestors


def types(anc, marks):
    n=len(anc)
    return [tuple('=' if x==a else 'D' if x in anc[a] else 'A' if a in anc[x] else 'I' for a in marks) for x in range(n)]


def build_binary_extremizer(m):
    """Exactly 4m nodes, degree at most 2, with 4m types."""
    edges=[]; mark_nodes=[]; gate_nodes=[]; nodes=0
    def new():
        nonlocal nodes
        x=nodes;nodes+=1;return x
    def build(start,end):
        if end-start==1:
            gate=new();gate_nodes.append(gate)
            a=new(); mark_nodes.append((start,a));edges.append((gate,a))
            t=new();edges.append((a,t))
            return gate
        v=new();mid=(start+end)//2
        for j,k in ((start,mid),(mid,end)):
            child=build(j,k)
            edges.append((v,child))
        return v
    root=build(0,m)
    extra=new();edges.append((gate_nodes[0],extra))
    marks=[x for _,x in sorted(mark_nodes)]
    return nodes,edges,root,marks


def verify():
    checks=0
    for n in range(2,7):
        for seq in product(range(n),repeat=n-2):
            edges=edges_from_prufer(n,seq)
            for root in range(n):
                anc=ancestor_sets(n,edges,root)
                for k in range(1,n+1):
                    for marks in combinations(range(n),k):
                        prof=types(anc,marks)
                        ext={p for p in prof if '=' not in p}
                        assert len(set(prof))<=4*k
                        assert len(ext)<=3*k
                        checks+=1
    for m in range(1,13):
        n,edges,root,marks=build_binary_extremizer(m)
        assert n==4*m
        an=ancestor_sets(n,edges,root)
        ps=types(an,marks)
        assert len(set(ps))==4*m
        assert len({p for p in ps if '=' not in p})==3*m
        outdegree=[0]*n
        for u,v in edges:
            if u in an[v]:outdegree[u]+=1
            else:outdegree[v]+=1
        assert max(outdegree)<=2
    for m in range(1,13):
        n=2*m+1
        ed=[(i,i+1) for i in range(n-1)]
        an=ancestor_sets(n,ed,0)
        marks=list(range(1,n,2))
        assert len(set(types(an,marks)))==2*m+1
    print('VERIFY_OK',checks,'all labelled rooted trees n=2..6 / all nonempty mark sets;', '12 binary and 12 path extremizers')

if __name__ == '__main__': verify()

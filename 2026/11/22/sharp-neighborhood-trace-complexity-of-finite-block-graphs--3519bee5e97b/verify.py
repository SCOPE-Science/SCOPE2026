#!/usr/bin/env python3
"""Independent finite checks for block-graph neighborhood traces. Standard library only."""
import itertools
import random


def biconnected_blocks(adj):
    n = len(adj); dfsno = [-1]*n; low = [0]*n; stack=[]; blocks=[]; timer=0
    def visit(u,parent):
        nonlocal timer
        dfsno[u]=low[u]=timer; timer+=1
        for v in adj[u]:
            if dfsno[v]<0:
                stack.append((u,v)); visit(v,u); low[u]=min(low[u],low[v])
                if low[v]>=dfsno[u]:
                    edges=[]
                    while stack:
                        e=stack.pop(); edges.append(e)
                        if e==(u,v):break
                    blocks.append(set(itertools.chain.from_iterable(edges)))
            elif v!=parent and dfsno[v]<dfsno[u]:
                stack.append((u,v));low[u]=min(low[u],dfsno[v])
    for u in range(n):
        if dfsno[u]<0:visit(u,-1)
    return blocks

def block_graph(adj):
    return all(all(v in adj[u] for u,v in itertools.combinations(b,2))
               for b in biconnected_blocks(adj))

def traces(adj,A):
    A=set(A)
    return {frozenset(adj[v]&A) for v in range(len(adj))}

def upper(m):
    if m==0:return 1
    if m==1:return 2
    if m==3:return 8
    return 3*m-2

def make_witness(m):
    adj=[set() for _ in range(m)]
    def edge(a,b):adj[a].add(b);adj[b].add(a)
    def new_vertex(ns):
        v=len(adj);adj.append(set())
        for u in ns:edge(v,u)
        return v
    if m==3:
        edge(0,1);edge(1,2);edge(0,2)
        new_vertex([0,1,2])
    else:
        for i in range(m-1):
            edge(i,i+1)
            new_vertex([i,i+1])
    for i in range(m):new_vertex([i])
    new_vertex([])
    return adj

def random_block_graph(n,rng):
    adj=[set() for _ in range(n)]
    for v in range(1,n):
        if rng.random()<.11:continue
        # Add a fresh leaf clique by attaching v to an existing singleton or entire block.
        old=[set(b) for b in biconnected_blocks(adj[:v])]
        # biconnected_blocks expects adjacency internal to prefix, correct by filtering
        old=[b for b in old if max(b)<v]
        opts=[{u} for u in range(v)] + old
        selected=rng.choice(opts)
        for u in selected:adj[v].add(u);adj[u].add(v)
    return adj

def check():
    total_graphs=total_pairs=total_block=0
    # Enumerate every simple labelled graph on 0..n-1 for n <= 6.
    for n in range(1,7):
        es=list(itertools.combinations(range(n),2))
        for mask in range(1<<len(es)):
            adj=[set() for _ in range(n)]
            for j,(u,v) in enumerate(es):
                if mask>>j&1:adj[u].add(v);adj[v].add(u)
            total_graphs+=1
            if not block_graph(adj):continue
            total_block+=1
            for amask in range(1,1<<n):
                A=[j for j in range(n) if amask>>j&1]
                nt=len(traces(adj,A));total_pairs+=1
                assert nt<=upper(len(A)),(n,mask,A,nt)
    for m in range(1,19):
        g=make_witness(m)
        assert block_graph(g)
        assert len(traces(g,range(m)))==upper(m),(m,len(traces(g,range(m))),upper(m))
    rng=random.Random(453712)
    sampled=0
    for n in range(7,71):
        for rep in range(18):
            g=random_block_graph(n,rng)
            assert block_graph(g),(n,rep)
            for j in range(16):
                m=rng.randrange(1,min(n,20)+1)
                A=rng.sample(range(n),m)
                nt=len(traces(g,A))
                assert nt<=upper(m),(n,rep,m,nt)
                sampled+=1
    print('VERIFY_OK all_simple_graphs',total_graphs,'block_graphs',total_block,
          'parameter_sets',total_pairs,'sharp_witness_orders',18,
          'random_cases',sampled)

if __name__=='__main__':check()

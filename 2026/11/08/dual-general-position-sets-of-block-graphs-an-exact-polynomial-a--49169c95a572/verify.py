#!/usr/bin/env python3
"""Exact finite checks of dual-general-position polynomial for block graphs.
Python standard library only. All graph subsets are checked against distance definitions.
"""
from collections import Counter
from itertools import combinations
from math import comb
from random import Random


def components(g, drop=None):
    unseen=set(range(len(g)))-({drop} if drop is not None else set())
    ans=[]
    while unseen:
        root=unseen.pop(); group={root}; frontier=[root]
        while frontier:
            x=frontier.pop()
            for y in g[x]:
                if y in unseen:
                    unseen.remove(y);group.add(y);frontier.append(y)
        ans.append(group)
    return ans


def get_blocks(g):
    n=len(g); disc=[-1]*n; low=[0]*n; stack=[]; blocks=[]; clock=0
    def dfs(x,parent):
        nonlocal clock
        disc[x]=low[x]=clock;clock+=1
        for y in sorted(g[x]):
            if disc[y]<0:
                stack.append((x,y));dfs(y,x);low[x]=min(low[x],low[y])
                if low[y]>=disc[x]:
                    verts=set()
                    while True:
                        e=stack.pop();verts.update(e)
                        if e==(x,y):break
                    blocks.append(frozenset(verts))
            elif y!=parent and disc[y]<disc[x]:
                stack.append((x,y));low[x]=min(low[x],disc[y])
    dfs(0,-1)
    assert all(v>=0 for v in disc)
    return blocks


def block_graph(g):
    if len(components(g))!=1:return None
    blocks=get_blocks(g) if len(g)>1 else [frozenset([0])]
    for B in blocks:
        if any(v not in g[u] for u,v in combinations(sorted(B),2)):return None
    return blocks


def theorem(g,blocks):
    n=len(g); cut={v for v in range(n) if len(components(g,v))>1}
    simp=set(range(n))-cut
    expected=Counter({k:comb(len(simp),k) for k in range(len(simp)+1)})
    special=set()
    for B in blocks:
        articulations=B&cut
        if len(articulations)==1:
            c=next(iter(articulations))
            if sum(c in Q for Q in blocks)==2:
                expected[len(B)]+=1;special.add(B)
    return expected,simp,special


def direct(g):
    n=len(g);d=[]
    for v in range(n):
        dd={v:0};todo=[v]
        for x in todo:
            for w in g[x]:
                if w not in dd:dd[w]=dd[x]+1;todo.append(w)
        assert len(dd)==n
        d.append(dd)
    values=Counter(); subsets=set()
    for mask in range(1<<n):
        selected={i for i in range(n) if mask&(1<<i)}
        outside=set(range(n))-selected
        valid=True
        for a,b in combinations(sorted(selected),2):
            if any(d[a][b]==d[a][c]+d[c][b] for c in selected-{a,b}):
                valid=False;break
        if valid:
            for a,b in combinations(sorted(outside),2):
                if any(d[a][b]==d[a][c]+d[c][b] for c in selected):
                    valid=False;break
        if valid:
            values[len(selected)]+=1;subsets.add(frozenset(selected))
    return values,subsets


def test(g):
    B=block_graph(g)
    if B is None:return None
    formula,simp,exceptional=theorem(g,B)
    obs,sets=direct(g)
    assert formula==obs,(len(g),g,formula,obs)
    assert {S for S in sets if not S.issubset(simp)}==exceptional
    # Nonheredity exactly when an exceptional pendant block exists.
    hereditary=all(frozenset(S-{v}) in sets for S in sets for v in S)
    assert hereditary==(not exceptional)
    return len(sets), len(exceptional)


def random_block_graph(rng,n):
    g=[set() for _ in range(n)]
    active=1
    while active<n:
        c=rng.randrange(active)
        k=rng.randint(1,min(n-active,4))
        nodes=[c]+list(range(active,active+k))
        for u,v in combinations(nodes,2):g[u].add(v);g[v].add(u)
        active+=k
    return g


def main():
    ngraphs=0;ns=0;nsets=0;nex=0
    for n in range(1,7):
        edgelist=list(combinations(range(n),2))
        for mask in range(1<<len(edgelist)):
            g=[set() for _ in range(n)]
            for i,(u,v) in enumerate(edgelist):
                if mask>>i&1:g[u].add(v);g[v].add(u)
            result=test(g)
            if result is not None:
                ngraphs+=1;ns+=(1<<n);nsets+=result[0];nex+=result[1]
    rng=Random(314159)
    for n in range(7,12):
        for trial in range(30):
            g=random_block_graph(rng,n);res=test(g)
            assert res is not None
            ngraphs+=1;ns+=(1<<n);nsets+=res[0];nex+=res[1]
    print('VERIFY_OK graphs={} subsets={} dual_sets={} exceptional_sets={} all_labeled_n_le_6=PASS deterministic_glued_cliques_n_7_to_11=PASS hereditary_boundary=PASS'.format(ngraphs,ns,nsets,nex))

if __name__=='__main__':main()

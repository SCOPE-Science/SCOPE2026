#!/usr/bin/env python3
"""Independent exhaustive small-graph tests of closure and Horn rule claims."""
from itertools import combinations
from math import comb, factorial
from collections import defaultdict
from random import Random


def induced_cycles(n, edges):
    result=[]
    for k in range(3,n+1):
        for verts in combinations(range(n), k):
            V=set(verts)
            C=[i for i,(a,b) in enumerate(edges) if a in V and b in V]
            if len(C)!=k:continue
            degree={v:0 for v in verts}
            for i in C:
                a,b=edges[i];degree[a]+=1;degree[b]+=1
            if any(degree[v]!=2 for v in verts):continue
            todo=[verts[0]];seen={verts[0]}
            while todo:
                u=todo.pop()
                for i in C:
                    a,b=edges[i]
                    v=b if a==u else a if b==u else None
                    if v is not None and v not in seen:seen.add(v);todo.append(v)
            if len(seen)==k:result.append(sum(1<<i for i in C))
    return result


def all_rooted_cycle_stems(n,edges):
    adjacency=[[] for _ in range(n)]
    for i,(u,v) in enumerate(edges):adjacency[u].append((v,i));adjacency[v].append((u,i))
    out=[]
    for e,(u,v) in enumerate(edges):
        def visit(a, seen, mask):
            if a==v:
                if mask.bit_count()>=2:out.append((mask,e))
                return
            for b,i in adjacency[a]:
                if i==e or (seen>>b&1):continue
                visit(b, seen|(1<<b), mask|(1<<i))
        visit(u,1<<u,0)
    assert len(out)==len(set(out))
    return out


def closure_masks(n,edges):
    out=[]
    for S in range(1<<len(edges)):
        par=list(range(n))
        def root(i):
            while par[i]!=i:
                i=par[i]
            return i
        for j,(u,v) in enumerate(edges):
            if S>>j&1:par[root(u)]=root(v)
        close=S
        for j,(u,v) in enumerate(edges):
            if root(u)==root(v):close|=1<<j
        out.append(close)
    return out


def pseudo_intents(closures, edge_count):
    ans=[]
    for sz in range(edge_count+1):
        for ii in combinations(range(edge_count),sz):
            S=sum(1<<j for j in ii)
            if closures[S]!=S and all((Q&S)!=Q or (closures[Q]&~S)==0 for Q in ans):ans.append(S)
    return ans


def test(n, edges, full_pseudo=True):
    E=len(edges); clos=closure_masks(n,edges)
    cycles=induced_cycles(n,edges)
    forced={(C^(1<<j), j) for C in cycles for j in range(E) if C>>j&1}
    direct=all_rooted_cycle_stems(n,edges)
    assert forced<=set(direct)
    seen_cycle=set()
    for S in range(1<<E):
        # Independent one-pass check for all rooted simple-cycle implications.
        one=S
        for P,e in direct:
            if (S&P)==P:one|=1<<e
        assert one==clos[S],(n,edges,S,'direct')
        # Iterated chordless-cycle rules, independent of graph union-find.
        new=S
        while True:
            nxt=new
            for P,e in forced:
                if (P&new)==P:nxt|=1<<e
            if nxt==new:break
            new=nxt
        assert new==clos[S],(n,edges,S,'canonical')
        # Each forced premise is a minimal non-closed set with one missing edge.
    for P,e in forced:
        assert clos[P]==(P|(1<<e))
        for j in range(E):
            if P>>j&1:assert clos[P^(1<<j)]==P^(1<<j)
    if full_pseudo:
        got=set(pseudo_intents(clos,E))
        assert got=={p for p,_ in forced},(n,edges,got-{p for p,_ in forced},{p for p,_ in forced}-got)
    # Direct iff all cycles chordless
    isdirect=True
    for S in range(1<<E):
        one=S
        for P,e in forced:
            if (P&S)==P:one|=1<<e
        if one!=clos[S]:isdirect=False;break
    assert isdirect==(len(forced)==len(direct))
    return len(cycles),len(forced),len(direct)

if __name__=='__main__':
    graphs=0;closures=0;pseudos=0
    for n in range(3,6):
        all_edges=list(combinations(range(n),2))
        for mask in range(1<<len(all_edges)):
            edges=[e for j,e in enumerate(all_edges) if mask>>j&1]
            test(n,edges)
            graphs+=1;closures+=(1<<len(edges));pseudos+=(1<<len(edges))
    # extra nontrivial random graphs on 6 vertices with <= 11 edges
    random=Random(19)
    for _ in range(24):
        all_edges=list(combinations(range(6),2))
        edges=[e for e in all_edges if random.random()<0.52]
        if len(edges)>11: edges=edges[:11]
        test(6,edges)
        graphs+=1;closures+=(1<<len(edges));pseudos+=(1<<len(edges))
    for n in range(3,8):
        wheel=[(i,(i+1)%n) for i in range(n)]+[(n,i) for i in range(n)]
        cycles,can,direct=test(n+1,wheel,full_pseudo=n<=6)
        assert (cycles,can)==((4 if n==3 else n+1),(12 if n==3 else 4*n))
        print('WHEEL',n,cycles,can,direct)
    for n in range(3,7):
        graph=list(combinations(range(n),2))
        ncycles,canonical,allroot=test(n,graph,full_pseudo=n<=5)
        expected_direct=(factorial(n)//2)*sum(1/factorial(j) for j in range(n-2))
        assert canonical==3*comb(n,3)
        assert allroot==int(round(expected_direct))
        print('COMPLETE',n,ncycles,canonical,allroot)
    print('VERIFY_OK small_graphs',graphs,'subsets_checked',closures,'pseudo_intent_subset_candidates',pseudos,'wheel=3..7','complete=3..6')

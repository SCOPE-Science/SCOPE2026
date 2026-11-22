#!/usr/bin/env python3
"""Exact rational cohomology and first unicyclic degree/Tutte twin census.

Uses Python standard library only. Run: python3 verify_unicyclic_six.py.
"""
from fractions import Fraction
from itertools import combinations, permutations
from collections import defaultdict, Counter
import json

GRAPHS = {
    "triangle_path_and_leaf": [(0,1),(1,2),(0,2),(0,3),(3,4),(1,5)],
    "triangle_fork": [(0,1),(1,2),(0,2),(0,3),(3,4),(3,5)],
    "square_adjacent_leaves": [(0,1),(1,2),(2,3),(0,3),(0,4),(1,5)],
    "square_opposite_leaves": [(0,1),(1,2),(2,3),(0,3),(0,4),(2,5)],
}
EXPECT = {
    "triangle_path_and_leaf": [1,6,28,76,157,238,268,238,157,76,28,6,1],
    "triangle_fork": [1,6,28,75,160,249,282,249,160,75,28,6,1],
    "square_adjacent_leaves": [1,6,29,76,157,238,266,238,157,76,29,6,1],
    "square_opposite_leaves": [1,6,29,77,161,246,276,246,161,77,29,6,1]
}

def sort_edges(edges):
    return tuple(sorted((min(a,b),max(a,b)) for a,b in edges))

def differential(mask, n, edges):
    """Exterior d with d(vertex)=0, d(edge ij)=x_i wedge x_j."""
    present=[i for i in range(n+len(edges)) if mask>>i & 1]
    terms=defaultdict(int)
    for place,g in enumerate(present):
        if g<n: continue
        a,b=edges[g-n]
        expanded=present[:place]+[a,b]+present[place+1:]
        if len(set(expanded))<len(expanded): continue
        inv=sum(v>w for j,v in enumerate(expanded) for w in expanded[j+1:])
        out=sum(1<<z for z in expanded)
        terms[out]+=(-1)**(place+inv)
    return {m:c for m,c in terms.items() if c}

def rank_sparse(columns):
    """Exact rational Gaussian elimination by sparse column pivots."""
    pivots={}
    for initial in columns:
        v={i:Fraction(a) for i,a in initial.items() if a}
        while v:
            k=min(v)
            if k not in pivots:
                s=v[k]
                pivots[k]={j:a/s for j,a in v.items()}
                break
            multiple=v[k]
            for j,c in pivots[k].items():
                t=v.get(j,0)-multiple*c
                if t:v[j]=t
                elif j in v:del v[j]
    return len(pivots)

def full_betti(n, edges):
    edges=sort_edges(edges)
    N=n+len(edges)
    supports=[1<<v for v in range(n)]+[(1<<a)|(1<<b) for a,b in edges]
    blocks=defaultdict(lambda:defaultdict(list))
    for mask in range(1<<N):
        s=0
        for i in range(N):
            if mask>>i&1:s|=supports[i]
        blocks[s][mask.bit_count()].append(mask)
    betti=[0]*(N+1)
    rank_by_degree=[0]*(N+2)
    for s,graded in blocks.items():
        ranks=[0]*(N+2)
        for k in range(N):
            dom=graded.get(k,())
            cod=graded.get(k+1,())
            if not dom or not cod:continue
            index={v:i for i,v in enumerate(cod)}
            cols=[]
            for m in dom:
                terms=differential(m,n,edges)
                assert all(t in index for t in terms), "support not preserved"
                cols.append({index[t]:c for t,c in terms.items()})
            ranks[k+1]=rank_sparse(cols)
        for k in range(N+1):
            betti[k]+=len(graded.get(k,()))-ranks[k]-ranks[k+1]
            rank_by_degree[k]+=ranks[k]
    for mask in range(1<<N):
        terms=defaultdict(int)
        for u,c in differential(mask,n,edges).items():
            for v,d in differential(u,n,edges).items():terms[v]+=c*d
        assert not any(terms.values()), "d squared nonzero"
    assert betti==betti[::-1],"Poincare duality"
    assert sum((-1)**k*b for k,b in enumerate(betti))==0,"Euler characteristic"
    assert betti[0]==betti[-1]==1 and betti[1]==n
    return betti,rank_by_degree

def connected(n, edges):
    seen={0};q=[0]
    adj=[set() for _ in range(n)]
    for a,b in edges:adj[a].add(b);adj[b].add(a)
    for v in q:
        for w in adj[v]-seen:seen.add(w);q.append(w)
    return len(seen)==n

def cycle_length(n,edges):
    adj=[set() for _ in range(n)]
    for a,b in edges:adj[a].add(b);adj[b].add(a)
    alive=set(range(n));leaves=[i for i in alive if len(adj[i])==1]
    while leaves:
        v=leaves.pop()
        if v not in alive:continue
        alive.remove(v)
        for w in adj[v]:
            if w in alive:
                adj[w].remove(v)
                if len(adj[w])==1:leaves.append(w)
    return len(alive)

def canonical(n,edges):
    positions=list(combinations(range(n),2)); enc={e:i for i,e in enumerate(positions)}
    best=None
    for p in permutations(range(n)):
        signature=0
        for a,b in edges:
            i,j=sorted((p[a],p[b]));signature|=1<<enc[i,j]
        if best is None or signature<best:best=signature
    return best

def census():
    counts={};twins=[]
    for n in range(3,7):
        seen={}
        all_edges=list(combinations(range(n),2))
        for ed in combinations(all_edges,n):
            if not connected(n,ed):continue
            c=cycle_length(n,ed)
            deg=[0]*n
            for a,b in ed:deg[a]+=1;deg[b]+=1
            key=(c,tuple(sorted(deg)))
            can=canonical(n,ed)
            seen[can]=(key,ed)
        groups=defaultdict(list)
        for can,(key,ed) in seen.items():groups[key].append((can,ed))
        counts[n]=len(seen)
        for key,arr in groups.items():
            if len(arr)>1:twins.append({'n':n,'cycle_length':key[0], 'degree_sequence':list(key[1]),'classes':len(arr)})
    assert counts=={3:1,4:2,5:5,6:13}
    assert sorted((r['n'],r['cycle_length'],r['classes']) for r in twins)==[(6,3,2),(6,4,2)]
    # Identify the representatives, not just the sizes of the two collision classes.
    named={key:canonical(6,ed) for key,ed in GRAPHS.items()}
    assert len(set(named.values()))==4, "four graphs must be nonisomorphic"
    for cycle,names in ((3,("triangle_path_and_leaf","triangle_fork")),
                        (4,("square_adjacent_leaves","square_opposite_leaves"))):
        pair={named[name] for name in names}
        assert any({canon for canon,_ in group}==pair
                   for key,group in groups.items() if key[0]==cycle),             "twin groups do not coincide with named four graphs"
    return counts,twins

def main():
    counts,twins=census()
    results={}
    for key,edges in GRAPHS.items():
        b,r=full_betti(6,edges)
        assert b==EXPECT[key],(key,b)
        results[key]={'edges':sort_edges(edges),'betti':b,'total':sum(b),'differential_ranks':r[1:13]}
    print(json.dumps({'census':counts,'twin_groups':twins,'cohomology':results,'checks':'all exact rational ranks, d^2, duality, Euler and graph census passed'},indent=2))
if __name__=='__main__':main()

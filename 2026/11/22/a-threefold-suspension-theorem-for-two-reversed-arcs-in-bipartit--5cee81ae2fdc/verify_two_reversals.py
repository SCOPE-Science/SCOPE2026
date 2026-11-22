"""Finite face and suspension-link checks for two-arc-reversed bipartite multipath complexes.
Scientific objects only; no external data or dependencies.
"""
from itertools import combinations, product
from collections import Counter
import random, json, sys

# Vertices on A: 0,...,a-1; B: a,...,a+b-1.
# Reverse edges (0,a) and (1,a+1). All other edges A -> B.

def graph_arcs(a,b,edges):
    return [(a+j,i) if (i,j) in ((0,0),(1,1)) else (i,a+j) for i,j in sorted(edges)]

def is_multipath(arcs):
    out=set(); inc=set(); follow={}
    for x,y in arcs:
        if x in out or y in inc:return False
        out.add(x);inc.add(y);follow[x]=y
    for v in follow:
        seen=set();w=v
        while w in follow:
            if w in seen:return False
            seen.add(w);w=follow[w]
    return True

def all_faces(arcs):
    n=len(arcs)
    return set(c for k in range(n+1) for c in combinations(range(n),k) if is_multipath([arcs[i] for i in c]))

def matching_faces(edges, a,b):
    e=sorted((i,j) for i,j in edges if i>=2 and j>=2)
    return {frozenset(c) for k in range(len(e)+1) for c in combinations(e,k) if len(set(i for i,j in c))==k and len(set(j for i,j in c))==k}

def gf2_rank(rows):
    pivots={}
    for x in rows:
        while x:
            p=x.bit_length()-1
            if p in pivots:x^=pivots[p]
            else:pivots[p]=x;break
    return len(pivots)

def betti(faces):
    levels={}
    for s in faces:
        if s:levels.setdefault(len(s)-1,[]).append(s)
    maxd=max(levels,default=-1)
    ranks={}
    for d in range(1,maxd+1):
        lows={s:i for i,s in enumerate(levels.get(d-1,[]))}
        cols=[]
        for s in levels.get(d,[]):
            value=0
            for v in s:
                s0=tuple(x for x in s if x!=v)
                value^=1<<lows[s0]
            cols.append(value)
        ranks[d]=gf2_rank(cols)
    return {d:len(levels.get(d,[]))-ranks.get(d,0)-ranks.get(d+1,0)-(1 if d==0 else 0) for d in range(maxd+1) if len(levels.get(d,[]))-ranks.get(d,0)-ranks.get(d+1,0)-(1 if d==0 else 0)}

def check(a,b,edges,homology=False):
    assert {(0,0),(1,1),(0,1),(1,0)}<=edges
    arcs=graph_arcs(a,b,edges)
    ids={p:i for i,p in enumerate(arcs)}
    r1=ids[(a,0)];r2=ids[(a+1,1)]
    cross1=ids[(0,a+1)];cross2=ids[(1,a)]
    core={r2,cross1,cross2}
    fs=all_faces(arcs)
    B={f for f in fs if r1 not in f}
    L={f for f in B if tuple(sorted(f+(r1,))) in fs}
    # Every face of the deletion is extendable by r2: a cone.
    assert all(tuple(sorted(f+(r2,))) in B for f in B if r2 not in f)
    # Exactly the cofaces of the directed 3-edge path are excluded from the link.
    assert all((f in L)==(not core.issubset(f)) for f in B)
    # Every link face is a matching of the residual induced bipartite graph.
    link={frozenset((arcs[i][0],arcs[i][1]-a) if arcs[i][0]<a else (arcs[i][1],arcs[i][0]-a) for i in f if i not in core) for f in B if core.issubset(f)}
    correct=matching_faces(edges,a,b)
    assert link==correct,(link^correct)
    if homology:
        v=betti(fs)
        # Compare to reduced mod-2 homology of residual matching complex, shifting by 3.
        residual_arcs=sorted((i,a+j) for i,j in edges if i>=2 and j>=2)
        M=all_faces(residual_arcs)
        w=betti(M)
        if not residual_arcs: w={-1:1} # the (-1)-sphere convention
        expected={d+3:k for d,k in w.items()}
        assert v==expected,(a,b,v,expected)
        return len(fs),v
    return len(fs),None

def check_missing_cross(a,b,edges):
    assert {(0,0),(1,1)}<=edges
    assert (0,1) not in edges or (1,0) not in edges
    arcs=graph_arcs(a,b,edges)
    ids={p:i for i,p in enumerate(arcs)}
    r1=ids[(a,0)]
    fs=all_faces(arcs)
    # A missing cross arc precludes all directed cycles.
    assert all(tuple(sorted(f+(r1,))) in fs for f in fs if r1 not in f)
    return len(fs)

if __name__=='__main__':
    cases=0; faces=0; mod_cases=0; counts=[]; missing_cross_checked=0
    for a,b in [(2,2),(2,3),(3,3),(3,4),(4,3),(4,4),(5,3),(5,4)]:
        all_edges={(i,j) for i in range(a) for j in range(b)}
        anchor={(0,0),(1,1),(0,1),(1,0)}
        opts=sorted(all_edges-anchor)
        if len(opts)<=6: masks=range(1<<len(opts))
        else:
            rng=random.Random(3500+a*51+b)
            masks=sorted(set([0,(1<<len(opts))-1]+[rng.randrange(1<<len(opts)) for _ in range(90)]))
        for mask in masks:
            e=anchor|{edge for i,edge in enumerate(opts) if mask>>i&1}
            hom=(len(e)<=13)
            n,h=check(a,b,e,homology=hom)
            cases+=1;faces+=n;mod_cases+=hom
            if e==all_edges:counts.append({'a':a,'b':b,'faces':n,'mod2_reduced':h})
    for a,b in [(2,2),(3,3),(3,4),(4,4),(5,3)]:
        E={(i,j) for i in range(a) for j in range(b)}
        for q in [(0,1),(1,0)]:
            F=E-{q}
            check_missing_cross(a,b,F)
            missing_cross_checked+=1
            # Also randomly thin the remaining forward edges.
            rr=random.Random(102030+a*17+b*7+q[0])
            for _ in range(9):
                C={(0,0),(1,1)}|{e for e in F if e in {(0,0),(1,1)} or rr.randrange(2)}
                check_missing_cross(a,b,C)
                missing_cross_checked+=1
    print(json.dumps({'missing_cross_cone_checks':missing_cross_checked,'status':'PASS','graphs_checked':cases,'aggregate_faces':faces,'homology_checked':mod_cases,'complete_graphs':counts},sort_keys=True))

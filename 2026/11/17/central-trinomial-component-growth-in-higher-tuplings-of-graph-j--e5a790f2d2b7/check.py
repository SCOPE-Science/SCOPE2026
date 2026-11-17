#!/usr/bin/env python3
"""Finite direct checks of the graph-join tupling theorem (stdlib only)."""
from itertools import product, combinations
from collections import defaultdict, deque
from math import comb

def cycle(n):
    return n, [(i,(i+1)%n) for i in range(n)]
def complete(n):
    return n, list(combinations(range(n),2))
def wheel(n):
    # rim length n-1 with hub n-1
    return n, [(i,(i+1)%(n-1)) for i in range(n-1)]+[(i,n-1) for i in range(n-1)]

def check(graphs):
    r=len(graphs); assert r>=4
    sizes=[n for n,_ in graphs]; ens=[len(ed) for _,ed in graphs]
    assert all(n>=3 for n in sizes)
    offsets=[sum(sizes[:i]) for i in range(r)]
    edges=[[tuple(sorted((u+offsets[i],v+offsets[i]))) for u,v in es] for i,(_,es) in enumerate(graphs)]
    # Each top face of the simplicial join consists of an edge of every factor.
    # Generate every 2-partition of each 2r-element facet into two r-element faces.
    adj=defaultdict(set)
    vertex_type={}
    membership={v:i for i,(o,n) in enumerate(zip(offsets,sizes)) for v in range(o,o+n)}
    for edge_tuple in product(*edges):
        face=tuple(sorted(v for e in edge_tuple for v in e))
        for aset in combinations(face,r):
            a=tuple(aset)
            b=tuple(v for v in face if v not in a)
            if a>b: continue
            adj[a].add(b);adj[b].add(a)
    assert all(adj.values()),'isolated vertices?'
    # Every r-face of the join extends to a facet (connected graphs have no isolated vertices).
    all_vertices=set()
    for local_choices in product(*[[()]+[(x,) for x in range(o,o+n)]+list(ed) for (o,n),ed in zip(zip(offsets,sizes),edges)]):
        if sum(map(len,local_choices))==r:
            all_vertices.add(tuple(sorted(v for chunk in local_choices for v in chunk)))
    assert all_vertices == set(adj), ('vertex mismatch',len(all_vertices),len(adj))
    def key(v):
        c=[0]*r
        for a in v:c[membership[a]]+=1
        return tuple(c)
    groups=defaultdict(set)
    for v in adj:
        p=key(v); complement=tuple(2-x for x in p)
        gr=min(p,complement)
        groups[gr].add(v)
    # Exhaustive BFS on direct face-partition graph.
    seen=set(); components=[]
    for src in adj:
        if src in seen: continue
        todo=[src];seen.add(src); nodes=[]; E2=0
        for v in todo:
            nodes.append(v); E2+=len(adj[v])
            for w in adj[v]:
                if w not in seen: seen.add(w);todo.append(w)
        assert E2%2==0
        types={min(key(v), tuple(2-x for x in key(v))) for v in nodes}
        assert len(types)==1,types
        g=next(iter(types)); B=[i for i,z in enumerate(g) if z==1]; F=[i for i,z in enumerate(g) if z==2];Z=[i for i,z in enumerate(g) if z==0]
        eprod=1
        for e in ens:eprod*=e
        if not F:
            pv=1
            for v in sizes:pv*=v
            pe=(2**(r-1))*eprod
        else:
            vB=1; eF=1;eZ=1
            for i in B:vB*=sizes[i]
            for i in F:eF*=ens[i]
            for i in Z:eZ*=ens[i]
            pv=vB*(eF+eZ)
            pe=(2**len(B))*eprod
        assert (len(nodes),E2//2)==(pv,pe), (g,len(nodes),E2//2,pv,pe)
        components.append((g,pv,pe,pe-pv+1))
    assert len(components)==(sum(comb(r,2*k)*comb(2*k,k) for k in range(r//2+1))+1)//2
    assert len(groups)==len(components)
    for g,pv,pe,_ in components: assert len(groups[g])==pv
    print('CASE r=%d v=%s e=%s components=%d vertices=%d edges=%d total_beta1=%d' % (r,sizes,ens,len(components),len(adj),sum(len(q) for q in adj.values())//2,sum(t[3] for t in components)))
    print('  COMPONENT_TIERS',sorted([(sum(x==2 for x in c[0]),c[1],c[2],c[3]) for c in components]))

if __name__=='__main__':
    for gs in [
      [complete(3)]*4,
      [complete(3)]*5,
      [cycle(5)]*4,
      [cycle(5),complete(3),complete(4),wheel(5)],
      [cycle(5),cycle(7),complete(3),complete(3)],
    ]: check(gs)
    print('BALANCED_PATTERN_JOIN_TUPLING_PASS')

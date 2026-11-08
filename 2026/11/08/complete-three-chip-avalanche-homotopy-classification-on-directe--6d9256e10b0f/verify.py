#!/usr/bin/env python3
"""Exact checks for cyclic three-support avalanche complexes. Stdlib only."""
from collections import Counter, defaultdict
from itertools import combinations, permutations
from math import gcd

def is_progression(n,T):
    return any((x+z-2*y)%n==0 for x,y,z in permutations(T))

def rotate_facets(n,T):
    return {frozenset((x+t)%n for x in T) for t in range(n)}

def dynamics(n,T):
    c=[int(i in T) for i in range(n)]
    configs=set(); facets=set()
    while tuple(c) not in configs:
        configs.add(tuple(c))
        firing={i for i in range(n) if c[i]>=1}
        facets.add(frozenset(firing))
        next_c=list(c)
        for v in firing:
            next_c[v]-=1
            next_c[(v+1)%n]+=1
        c=next_c
    return facets

def homology_mod2(n,facets):
    vertices=set().union(*facets)
    ed=set(); tris=set()
    for face in facets:
        for edge in combinations(sorted(face),2):ed.add(edge)
        if len(face)==3:tris.add(tuple(sorted(face)))
    elist=sorted(ed); edix={e:i for i,e in enumerate(elist)}
    basis={}
    for t in tris:
        v=0
        for e in combinations(t,2):v^=1<<edix[e]
        while v:
            pivot=v.bit_length()-1
            if pivot in basis:v^=basis[pivot]
            else:basis[pivot]=v;break
    rank2=len(basis)
    adj={v:set() for v in vertices}
    for x,y in ed:adj[x].add(y);adj[y].add(x)
    comps=[]
    while adj:
        work=[next(iter(adj))]; got=set()
        while work:
            a=work.pop()
            if a not in got:
                got.add(a);work.extend(adj[a]-got)
        comps.append(got)
        for a in got:del adj[a]
    rank1=len(vertices)-len(comps)
    return len(comps),len(ed)-rank1-rank2,len(tris)-rank2

def check(n,T,simulate=False,homology=False):
    a,b=T[1:]
    faces=rotate_facets(n,T)
    if simulate:assert faces==dynamics(n,T),(n,T,'dynamics')
    g=gcd(n,a,b); m=n//g
    ap=is_progression(n,T)
    anti=(n%2==0 and any((x-y)%n==n//2 for x,y in combinations(T,2)))
    if ap:
        beta=(g,0,0) if m==3 else (g,0,g) if m==4 else (g,g,0)
        # Determine distinct whole components independently from all facets.
        if m==3:assert len(faces)==g
        else:assert len(faces)==n
        if m>=5:
            # Find an arithmetic ordering, then perform m free-edge collapses per coset.
            step=next((z-y)%n for x,y,z in permutations(T) if (x+z-2*y)%n==0)
            edge_count=Counter(e for tri in faces for e in combinations(sorted(tri),2))
            long_edges={tuple(sorted((i,(i+2*step)%n))) for i in range(n)}
            assert len(long_edges)==n and all(edge_count[e]==1 for e in long_edges)
            kept=set(edge_count)-long_edges
            short_edges={tuple(sorted((i,(i+step)%n))) for i in range(n)}
            assert kept==short_edges and len(kept)==n
    else:
        assert len(faces)==n
        edge_count=Counter(e for tri in faces for e in combinations(sorted(tri),2))
        orbits=defaultdict(set)
        for e in edge_count:
            d=(e[1]-e[0])%n
            orbits[min(d,n-d)].add(e)
        assert len(orbits)==3,(n,T,'edge difference classes',orbits)
        free=[k for k,v in orbits.items() if all(edge_count[e]==1 for e in v)]
        assert len(free)>=2,(n,T,'no free orbits')
        # A complete, explicit sequence of n elementary collapses.
        erased=orbits[min(free)]
        assert len(erased)==n and all(sum(e[0] in f and e[1] in f for f in faces)==1 for e in erased)
        remaining=set(edge_count)-erased
        # Correct spelling of conditional counts is validated separately below.
        assert len(remaining)==(3*n//2 if anti else 2*n),(n,T,len(remaining))
        adj={i:set() for i in range(n)}
        for x,y in remaining:adj[x].add(y);adj[y].add(x)
        comp=[]
        while adj:
            work=[next(iter(adj))]; seen=set()
            while work:
                x=work.pop()
                if x not in seen:seen.add(x);work.extend(adj[x]-seen)
            comp.append(seen)
            for x in seen:del adj[x]
        assert len(comp)==g and all(len(c)==m for c in comp)
        expected_rank=m//2+1 if anti else m+1
        assert all(sum(x in c and y in c for x,y in remaining)-len(c)+1==expected_rank for c in comp)
        beta=(g,g*expected_rank,0)
    if homology:assert homology_mod2(n,faces)==beta,(n,T,'homology',homology_mod2(n,faces),beta)
    return ('AP' if ap else ('opposite' if anti else 'ordinary')),beta

if __name__=='__main__':
    counts=Counter(); tests=0; modular=0; dyn=0
    for n in range(3,40):
        for a,b in combinations(range(1,n),2):
            # Use separate dynamics on all supports of moderate size.
            simulate=n<=20
            homolog=n<=18
            label,beta=check(n,(0,a,b),simulate,homolog)
            counts[label]+=1;tests+=1;modular+=homolog;dyn+=simulate
    print('ALL_VERIFY_OK',f'cyclic_supports={tests}',f'actual_dynamics={dyn}',f'mod2_homology={modular}',dict(counts))
    for n,T in [(9,(0,2,5)),(10,(0,2,5)),(12,(0,3,6)),(9,(0,3,6)),(14,(0,2,4))]:
        print('example',n,T,check(n,T,True,True))

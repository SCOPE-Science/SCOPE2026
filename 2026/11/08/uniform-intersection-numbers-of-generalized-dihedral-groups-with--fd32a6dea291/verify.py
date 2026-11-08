#!/usr/bin/env python3
"""Exact subgroup and intersection enumeration for odd generalized dihedral groups."""
from itertools import product,combinations
from math import prod

def subgroups_A(mods):
    A=list(product(*(range(n) for n in mods)))
    zero=tuple(0 for _ in mods)
    def add(x,y): return tuple((a+b)%n for a,b,n in zip(x,y,mods))
    def closure(gens):
        S={zero}
        frontier=[zero]
        while frontier:
            x=frontier.pop()
            for y in gens:
                z=add(x,y)
                if z not in S: S.add(z);frontier.append(z)
        return frozenset(S)
    # enumerate all additive subgroups for small test cases
    seen={frozenset([zero])}
    todo=[frozenset([zero])]
    while todo:
        H=todo.pop()
        for a in A:
            if a not in H:
                K=closure(list(H)+[a])
                if K not in seen: seen.add(K);todo.append(K)
    return A,seen,add

def run(mods):
    A,AS,add=subgroups_A(mods)
    zero=tuple(0 for _ in mods)
    proper=[s for s in AS if len(s)!=len(A)]
    maximal=[s for s in proper if not any(s<t and len(t)<len(A) for t in proper)]
    assert all(len(A)//len(w) in (3,5) for w in maximal)
    gmap={(v,e):i for i,(v,e) in enumerate(product(A,range(2)))}
    whole=(1<<len(gmap))-1
    def bits(elements):return sum(1<<gmap[x] for x in elements)
    Max=[bits((a,0) for a in A)]
    for W in maximal:
        seen_cosets=set()
        for a in A:
            coset=frozenset(add(a,w) for w in W)
            if coset not in seen_cosets:
                seen_cosets.add(coset)
                Max.append(bits([(w,0) for w in W]+[(c,1) for c in coset]))
    assert len(set(Max))==len(Max)
    phi=whole
    for M in Max:phi &= M
    # Compute all family-intersection sizes by bitset DP.
    min_good=len(Max)+1;max_bad=-1
    intersections=[whole]
    # for exhaustive number of subsets, min good and max bad can be derived iteratively
    counts=[0]
    for M in Max:
        n0=len(intersections)
        intersections.extend((x & M for x in intersections[:n0]))
        counts.extend((c+1 for c in counts[:n0]))
    for mask,c in zip(intersections,counts):
        if mask==phi:
            if c<min_good:min_good=c
        elif c>max_bad:max_bad=c
    ranks={}
    for n in mods:
        p=next(p for p in (3,5,7,11) if n%p==0)
        ranks[p]=ranks.get(p,0)+1
    H=sum((p**r-1)//(p-1)*p for p,r in ranks.items())
    assert len(Max)==H+1
    assert min_good ==1+sum(ranks.values()), (mods,min_good)
    assert max_bad+1==2+H-min(p**r for p,r in ranks.items()),(mods,max_bad)
    print('verified',mods,'group_order',2*len(A),'max_subgroups',len(Max),'Frattini_order',phi.bit_count(), 'i',min_good,'ui',max_bad+1,'families',len(intersections))

for mods in [(3,3),(9,3),(3,5),(3,3,5)]:
    run(mods)
print('VERIFY_OK')

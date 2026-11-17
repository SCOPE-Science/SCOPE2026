#!/usr/bin/env python3
"""Exact finite check for geometric conjugation-fixed partition-graph clique complexes.

Requires Python 3.9+ standard library only.  No third-party datasets are needed.
Every partition, original edge, eligible orbit, clique, and elementary collapse
is generated from the definitions and checked before use.
"""
from collections import Counter
from functools import lru_cache
from itertools import combinations

@lru_cache(None)
def partitions(n, maximum):
    if n == 0:
        return ((),)
    ans = []
    for first in range(min(n, maximum), 0, -1):
        for rest in partitions(n-first, first):
            ans.append((first,) + rest)
    return tuple(ans)


def transpose(part):
    return tuple(sum(x >= k for x in part) for k in range(1,part[0]+1))


def transfer_neighbors(part):
    result=set()
    for source in range(len(part)):
        reduced=list(part)
        reduced[source]-=1
        for destination in range(len(part)+1):
            changed=reduced[:]
            if destination == len(part):
                changed.append(1)
            else:
                changed[destination]+=1
            result.add(tuple(sorted((v for v in changed if v>0),reverse=True)))
    result.discard(part)
    return result


def cliques(adjacency):
    # Every clique has a unique strictly increasing ordering, so no face is missed.
    faces=set()
    def extend(face, successors):
        if face:
            faces.add(face)
        for v in sorted(successors):
            extend(face+(v,), successors.intersection(adjacency[v]).intersection(range(v+1,len(adjacency))))
    for v in range(len(adjacency)):
        extend((v,), adjacency[v].intersection(range(v+1,len(adjacency))))
    return faces


def exact_orbit_complex(parts, adjacency):
    index={p:i for i,p in enumerate(parts)}
    involution=tuple(index[transpose(p)] for p in parts)
    assert all(involution[involution[i]]==i for i in range(len(parts)))
    assert all(involution[j] in adjacency[involution[i]]
               for i in range(len(parts)) for j in adjacency[i])
    seen=set();orbits=[]
    for i in range(len(parts)):
        if i in seen: continue
        j=involution[i];orb=tuple(sorted(set((i,j))))
        seen.update(orb)
        if len(orb)==1 or j in adjacency[i]:
            orbits.append(orb)
    quotient=[set() for _ in orbits]
    for a,b in combinations(range(len(orbits)),2):
        if all(v in adjacency[u] for u in orbits[a] for v in orbits[b]):
            quotient[a].add(b);quotient[b].add(a)
    f=cliques(quotient)
    # Independent reconstruction from *all* invariant original cliques.
    fixed_orbit_faces=set()
    original_faces=cliques(adjacency)
    eligible={orb:k for k,orb in enumerate(orbits)}
    for face in original_faces:
        if {involution[i] for i in face}!=set(face): continue
        collection=[]
        for i in face:
            orb=tuple(sorted(set((i,involution[i]))))
            if orb not in eligible: raise AssertionError('missing eligible orbit')
            collection.append(eligible[orb])
        fixed_orbit_faces.add(tuple(sorted(set(collection))))
    assert f==fixed_orbit_faces
    return orbits, quotient, f, original_faces


def collapse_all_positive_dim_two_and_above(faces):
    remaining=set(faces)
    matched=[]
    while any(len(face)>=3 for face in remaining):
        candidate=None
        for face in sorted(remaining,key=lambda x:(-len(x),x)):
            if len(face)<3:continue
            # A codimension-one face is free only if this is its *unique*
            # strict coface of any dimension, not just its unique facet.
            for i in range(len(face)):
                lower=face[:i]+face[i+1:]
                if lower not in remaining: raise AssertionError('not closed')
                strict=[f for f in remaining if len(f)>len(lower) and set(lower).issubset(f)]
                if strict==[face]:
                    candidate=(lower,face);break
            if candidate is not None:break
        if candidate is None:
            return remaining,matched,False
        lower,higher=candidate
        remaining.remove(lower);remaining.remove(higher)
        matched.append(candidate)
    return remaining,matched,True


def graph_info(vertices, remaining):
    adjacency=[set() for _ in range(vertices)]
    for face in remaining:
        if len(face)==2:
            a,b=face;adjacency[a].add(b);adjacency[b].add(a)
    seen=set();components=[]
    for v in range(vertices):
        if v in seen:continue
        pending=[v];seen.add(v);comp=set()
        while pending:
            u=pending.pop();comp.add(u)
            for w in adjacency[u]-seen:
                seen.add(w);pending.append(w)
        components.append(comp)
    edges=sum(map(len,adjacency))//2
    cycles=edges-vertices+len(components)
    return edges, components, cycles


def main():
    print('n partitions f0 f1 f2 f3 collapsed components cycles')
    for n in range(1,19):
        parts=partitions(n,n);index={p:i for i,p in enumerate(parts)}
        adjacency=[set() for _ in parts]
        for i,p in enumerate(parts):
            for q in transfer_neighbors(p):
                j=index[q]
                adjacency[i].add(j)
        assert all(i in adjacency[j] for i in range(len(parts)) for j in adjacency[i])
        orbits,quotient,faces,original_faces=exact_orbit_complex(parts,adjacency)
        counts=Counter(map(len,faces))
        remainder,steps,done=collapse_all_positive_dim_two_and_above(faces)
        assert done
        assert all(len(f)<=2 for f in remainder)
        edge_count,components,cycles=graph_info(len(orbits),remainder)
        assert (cycles==0 if n<=17 else cycles==1)
        assert (len(components)==2 if n==18 else True)
        assert len(steps)==sum(v for k,v in counts.items() if k>=3)
        print(n,len(parts),*(counts.get(k,0) for k in range(1,5)),len(steps),len(components),cycles)
        if n==18:
            assert counts=={1:15,2:18,3:4}
            assert edge_count==14
            assert sorted(len(c) for c in components)==[2,13]
            chi_original=sum((-1)**(len(face)-1) for face in original_faces)
            assert chi_original==311
            print('n18 collapse pairs:',steps)
            print('n18 final edges:',sorted(f for f in remainder if len(f)==2))
            print('n18 components:',[sorted(c) for c in components])
            print('n18 original Euler characteristic:',chi_original)
    print('PARTITION_CONJUGATION_FIRST_CIRCLE_EXACT_CHECKS_OK')

if __name__=='__main__':
    main()

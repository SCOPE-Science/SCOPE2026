#!/usr/bin/env python3
"""Exact finite checks of a directed-chain/chord homology construction.

This supplements, but does not replace, the argument for all positive m.
Uses only the Python standard library and integer arithmetic.
"""
from itertools import combinations


def arc_sets(m):
    n = 4 * m
    a = list(range(0, 2 * m, 2))
    b = list(range(2 * m + 1, 4 * m, 2))
    return n, {(i, i + 1) for i in range(n-1)}, sorted((i, j) for i in a for j in b)


def test(m, chosen):
    n, chain, chords = arc_sets(m)
    edges = chain | set(chosen)
    assert set(chosen).issubset(chords)
    assert len(edges) == n-1+len(chosen)
    # Exhaustive reachability, not an assumption about transitive closure.
    for source in range(n):
        reachable = {source}
        changed = True
        while changed:
            nxt = reachable | {v for u,v in edges if u in reachable}
            changed = nxt != reachable
            reachable = nxt
        assert reachable == set(range(source, n))
    # Projection of every 2-boundary onto the missing-edge coordinates.
    # Distinct 2-paths have different missing endpoint pairs.
    image = {}
    for i,j in edges:
        for u,k in edges:
            if u != j:
                continue
            assert i < j < k
            assert (i,k) not in edges, ('directed triangle',m,chosen,i,j,k)
            assert (i,k) not in image, ('long-square',m,chosen,i,j,k)
            image[(i,k)] = j
    # The edge incidence rank is n-1, because chain edges form a spanning tree.
    # The following k integral cycles have distinct pivot chord coefficients.
    cycles=[]
    for u,v in sorted(chosen):
        z={(u,v):1}
        for t in range(u,v):z[(t,t+1)]=z.get((t,t+1),0)-1
        boundary={}
        for (i,j),coefficient in z.items():
            boundary[i]=boundary.get(i,0)-coefficient
            boundary[j]=boundary.get(j,0)+coefficient
        assert all(value==0 for value in boundary.values())
        cycles.append(z)
    for c,z in zip(sorted(chosen),cycles):
        assert z[c] == 1
        assert all((other not in z) for other in chosen if other != c)
    # As Omega_2 = 0 integrally, H_1 has a basis of these k cycles.
    return len(image), len(chosen)


def main():
    total=0
    for m in range(1,4):
        n,base,chords = arc_sets(m)
        for subset in range(1<<len(chords)):
            chosen=[c for idx,c in enumerate(chords) if subset>>idx&1]
            test(m,chosen)
            total+=1
        print('m',m,'vertices',n,'all',1<<len(chords),'subsets verified')
    for m in range(4,9):
        n,base,chords=arc_sets(m)
        # Verify the complete interval of betti ranks using first k chords.
        for k in range(len(chords)+1):
            test(m,chords[:k])
            total+=1
        print('m',m,'vertices',n,'all ranks 0 through',len(chords),'verified')
    print('PASS:',total,'graph instances; exact reachability, unique missing 2-path endpoints, and integral 1-cycle basis')

if __name__=='__main__':main()

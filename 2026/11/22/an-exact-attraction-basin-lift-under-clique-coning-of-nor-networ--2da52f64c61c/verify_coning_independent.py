#!/usr/bin/env python3
"""Second checker: explicit frozenset state dynamics and backward basin fibers."""
import itertools
import random
from collections import defaultdict


def all_graphs(n):
    poss = list(itertools.combinations(range(n),2))
    for chosen in itertools.product((False,True),repeat=len(poss)):
        edges = {frozenset(e) for e,on in zip(poss,chosen) if on}
        if all(any(i in e for e in edges) for i in range(n)):
            yield edges


def add_hubs(edges,n,r):
    edges=set(edges)
    for u in range(n,n+r):
        for v in range(u):
            edges.add(frozenset((u,v)))
    return edges


def all_states(n):
    return tuple(frozenset(i for i in range(n) if mask & (1<<i)) for mask in range(1<<n))


def nor(states, edges, n):
    nbr={i:set() for i in range(n)}
    for e in edges:
        a,b=tuple(e)
        nbr[a].add(b);nbr[b].add(a)
    return {s:frozenset(i for i in range(n) if not (nbr[i] & s)) for s in states}


def orbit_attractors(f):
    # Compute cycle of every start via independent path tracing.
    assigned={}
    for s in f:
        seq=[]; visited={}; cur=s
        while cur not in assigned and cur not in visited:
            visited[cur]=len(seq);seq.append(cur);cur=f[cur]
        cyc=assigned[cur] if cur in assigned else frozenset(seq[visited[cur]:])
        for v in seq:
            assigned[v]=cyc
    basins=defaultdict(set)
    for s,cyc in assigned.items(): basins[cyc].add(s)
    return basins


def main():
    count=0
    for n in range(2,5):
        for e in all_graphs(n):
            b=orbit_attractors(nor(all_states(n), e, n))
            all_base=frozenset(range(n))
            special=frozenset((frozenset(),all_base))
            assert special in b
            td=sum(all(any(frozenset((i,j)) in e for j in s if j!=i) for i in range(n))
                   for s in all_states(n))
            assert len(b[special])==td+1
            for r in (1,2,3):
                full=orbit_attractors(nor(all_states(n+r),add_hubs(e,n,r),n+r))
                big=frozenset((frozenset(),frozenset(range(n+r))))
                assert len(full[big]) == 2**(n+r)-2**n+td+1-r
                # Recurrent attractor labels and basins identical for every other base orbit.
                for cyc, basin in b.items():
                    if cyc==special: continue
                    assert cyc in full and full[cyc] == basin, (n,r,e,cyc)
                for k in range(r):
                    one=frozenset((n+k,))
                    assert full[frozenset((one,))] == {one}
                assert len(full)==len(b)+r
                assert sum(map(len,full.values())) == 2**(n+r)
                count+=1
    print('PASS independent set/edge implementation, n=2..4, r=1..3; experiments:',count)

if __name__=='__main__':main()

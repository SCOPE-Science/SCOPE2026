#!/usr/bin/env python3
"""Verify the geometric 40-by-120 decomposition of period-mismatch data."""
import itertools
from verify_graph import all_periods,graph,N

PAIRS = ((0,1),(2,3),(0,4),(1,2),(3,4),
         (2,4),(1,4),(1,3),(0,3),(0,2))

def main():
    nb=graph(2)
    assert len(set(PAIRS)) == 10
    assert all((j in nb[i]) == set(PAIRS[i]).isdisjoint(PAIRS[j])
               for i in range(10) for j in range(10) if i!=j)
    _,pc,_=all_periods(nb,'CCA')
    _,ph,_=all_periods(nb,'GHM')
    mismatch={s for s in range(N) if (pc[s],ph[s]) == (8,4)}
    assert len(mismatch)==4800
    pi={p:i for i,p in enumerate(PAIRS)}
    actions=[]
    for perm in itertools.permutations(range(5)):
        action=tuple(pi[tuple(sorted((perm[a],perm[b])))] for a,b in PAIRS)
        assert all((j in nb[i]) == (action[j] in nb[action[i]])
                   for i in range(10) for j in range(10) if i!=j)
        actions.append(action)
    assert len(set(actions))==120
    remaining=set(mismatch)
    orbit_sizes=[]
    while remaining:
        x=min(remaining)
        digits=tuple((x//3**i)%3 for i in range(10))
        orbit={sum(digits[i]*3**act[i] for i in range(10)) for act in actions}
        assert orbit <= remaining
        remaining.difference_update(orbit)
        orbit_sizes.append(len(orbit))
    assert orbit_sizes==[120]*40
    print('Petersen group S5 has 120 automorphisms; mismatch configurations partition into 40 orbits of size 120; total 4800.')

if __name__=='__main__':main()

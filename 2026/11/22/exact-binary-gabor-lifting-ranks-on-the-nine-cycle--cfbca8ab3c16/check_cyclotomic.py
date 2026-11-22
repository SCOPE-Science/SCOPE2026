#!/usr/bin/env python3
"""Exact integer verification of binary cyclic nine-point Gabor rank strata."""
from collections import Counter
from itertools import product

N=9
EXPECTED={73:117,69:81,65:54,21:3,9:1}

def classify(g):
    assert len(g)==9 and set(g)<={-1,1}
    periodic=all(g[t]==g[(t+3)%9] for t in range(9))
    zeros={(0,k) for k in range(1,9)}
    events=[]
    for a in range(1,9):
        h=[g[t]*g[(t+a)%9] for t in range(9)]
        assert sum(h)!=0  # odd number of binary entries
        if len({h[r]+h[r+3]+h[r+6] for r in range(3)})==1:
            zeros.update({(a,3),(a,6)})
            events.append(a)
        if all(h[r]==h[r+3]==h[r+6] for r in range(3)):
            zeros.update((a,k) for k in (1,2,4,5,7,8))
            assert periodic
        else:
            assert not periodic
    assert len(zeros)==8+2*len(events)+48*int(periodic)
    return 81-len(zeros),periodic,tuple(events)

counts=Counter();event_counts=Counter(); period_counts=Counter()
for tail in product((-1,1),repeat=8):
    g=(1,)+tail
    rank,periodic,events=classify(g)
    counts[rank]+=1
    period_counts[periodic]+=1
    event_counts[(periodic, events)]+=1
assert dict(counts)==EXPECTED,(counts,EXPECTED)
assert period_counts=={False:252,True:4}
assert sum(counts.values())==256
assert all(len(events) in (0,2,4,8) for (_,events) in event_counts)

# Independent structural orbit check for the 27 nonconstant unit-shift events.
reps=({0,1,2},{0,1,5},{0,2,4})
orbits=[]
for s in reps:
    orbit={frozenset((t+x)%9 for t in s) for x in range(9)}
    assert len(orbit)==9
    orbits.append(orbit)
assert all(orbits[i].isdisjoint(orbits[j]) for i in range(3) for j in range(i+1,3))
all_one_each={frozenset((r+3*j[r]) for r in range(3)) for j in product(range(3),repeat=3)}
assert set.union(*orbits)==all_one_each
for s,expected_event in zip(reps,(3,4,2)):
    h=[1 if t in s else -1 for t in range(9)]
    g=[1]
    for t in range(8):g.append(g[-1]*h[t])
    assert g[8]*h[8]==1
    rank,periodic,events=classify(g)
    assert rank==65 and not periodic
    assert expected_event in events
    assert 1 in events

print('CYCLOTOMIC_INTEGER_CHECK_PASS',sorted(counts.items()))
print('PERIODIC_COUNTS',dict(period_counts))
print('EVENT_PROFILE_COUNT',len(event_counts))

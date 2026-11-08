"""Independent exhaustive chip-state update check within necessary periodic bounds."""
from itertools import product
from collections import Counter

def step(chips,neighbors,degrees):
    fired=[int(c>=d) for c,d in zip(chips,degrees)]
    return tuple(chips[i]-degrees[i]*fired[i]+sum(fired[j] for j in neighbors[i]) for i in range(len(chips)))

def test(n):
    edges=[(0,i) for i in range(1,n+1)]+[(i,i+1) for i in range(1,n)]
    neighbors=[[] for _ in range(n+1)]
    for i,j in edges:
        neighbors[i].append(j);neighbors[j].append(i)
    degrees=[len(ns) for ns in neighbors]
    counts=Counter()
    cases=1
    for d in degrees: cases*=2*d
    for state in product(*(range(2*d) for d in degrees)):
        one=step(state,neighbors,degrees)
        two=step(one,neighbors,degrees)
        three=step(two,neighbors,degrees)
        if three==state and one!=state:
            counts[sum(state)]+=1
    total=sum(counts.values())
    assert total==[12,48,168,564,1788][n-2],(n,total)
    low=list(range(2*n-1,3*n-2))
    high=list(range(4*n-2,5*n-3))
    assert set(counts)==set(low+high),(n,counts)
    complement=7*n-5
    assert all(counts[k]==counts[complement-k] for k in counts)
    print(f'n={n}, cases={cases}, primitive3={total}, support={min(counts)}..{max(counts)}, bands={low[0]}..{low[-1]} and {high[0]}..{high[-1]}')
for n in range(2,7):test(n)
print('DIRECT_STATE_ENUMERATION=PASS')

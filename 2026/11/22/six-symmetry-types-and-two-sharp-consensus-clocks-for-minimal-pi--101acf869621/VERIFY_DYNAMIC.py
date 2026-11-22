"""Independent exhaustive pinned-majority dynamics checker for the Franklin graph.
Usage: python3 VERIFY_DYNAMIC.py
Builds and simulates the full bit-vector majority map without forest routines.
"""
from collections import Counter
from itertools import combinations

N=12
U=(1<<N)-1
neighbor=[set() for _ in range(N)]
for i in range(N):
    j=(i+1)%N
    neighbor[i].add(j);neighbor[j].add(i)
for i in range(0,N,2):
    j=(i+5)%N
    neighbor[i].add(j);neighbor[j].add(i)
assert all(len(v)==3 for v in neighbor)

def move(s,seed):
    return seed | sum(1<<i for i in range(N)
                      if not seed & (1<<i)
                      and sum(bool(s & (1<<j)) for j in neighbor[i])>=2)

def time_from(s,seed):
    seen=set()
    t=0
    while s!=U and s not in seen:
        seen.add(s)
        s=move(s,seed)
        t+=1
    return t if s==U else None

per_k=Counter()
times=Counter()
placements=[]
for k in range(5):
    for tup in combinations(range(N),k):
        seed=sum(1<<i for i in tup)
        t=time_from(seed,seed)
        if t is None: continue
        per_k[k]+=1
        if k==4:
            times[t]+=1
            placements.append((seed,t))
assert per_k==Counter({4:144})
assert times==Counter({3:72,4:72})

# Independent stronger check, all configurations consistent with every one
# of the 144 minimum forcing placements. 144 * 256 = 36,864 trajectories.
checked=0
for seed,maximum_time in placements:
    free=[i for i in range(N) if not(seed>>i&1)]
    assert len(free)==8
    latest=0
    for s in range(1<<8):
        starting=seed | sum(1<<v for j,v in enumerate(free) if (s>>j)&1)
        t=time_from(starting,seed)
        assert t is not None and t<=maximum_time
        latest=max(latest,t)
        checked+=1
    assert latest==maximum_time
assert checked==36864
print('ALL DYNAMICAL CHECKS PASSED')
print('universal forcing count by seed size',sorted(per_k.items()))
print('sharp forced-consensus steps',sorted(times.items()))
print('full configuration trajectories checked',checked)

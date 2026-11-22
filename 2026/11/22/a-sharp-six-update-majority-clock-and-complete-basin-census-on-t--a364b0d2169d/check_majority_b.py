#!/usr/bin/env python3
"""Independent explicit-edge and tuple-state verifier for the Bidiakis majority census.
Pure Python 3; no third-party dependencies. Run: python3 check_majority_b.py.
"""
from collections import Counter

# A direct edge listing, independently of any LCF-construction code.
EDGES = ((0,1),(0,6),(0,11),(1,2),(1,5),(2,3),(2,10),
         (3,4),(3,9),(4,5),(4,8),(5,6),(6,7),(7,8),
         (7,11),(8,9),(9,10),(10,11))
assert len(EDGES) == len(set(EDGES)) == 18
adj = [[] for _ in range(12)]
for u,v in EDGES:
    adj[u].append(v)
    adj[v].append(u)
assert sorted(len(a) for a in adj) == [3]*12


def update(x):
    y=[]
    for j in range(12):
        # Independently evaluate the majority of three input entries.
        a,b,c = (x[i] for i in adj[j])
        y.append((a and b) or (b and c) or (c and a))
    return tuple(int(t) for t in y)

all_states = [tuple((k >> i) & 1 for i in range(12)) for k in range(4096)]
orb_sizes = Counter()
delays = Counter()
cycle_basins = Counter()
cycles_seen = set()
for x0 in all_states:
    trace = []
    when = {}
    x = x0
    while x not in when:
        when[x] = len(trace)
        trace.append(x)
        x = update(x)
        assert len(trace) <= 4096
    begin = when[x]
    circular = trace[begin:]
    canonical = min(tuple(circular[r:]+circular[:r])
                    for r in range(len(circular)))
    delays[begin] += 1
    cycle_basins[canonical] += 1
    cycles_seen.add(canonical)

assert dict(sorted(delays.items())) == {0:226, 1:1226, 2:1364,
                                         3:608,4:408,5:216,6:48}
assert all(len(c) in (1,2) for c in cycles_seen)
assert Counter(len(c) for c in cycles_seen) == {1:20,2:103}
spec = {period:dict(sorted(Counter(size for c,size in cycle_basins.items()
                                    if len(c)==period).items()))
        for period in (1,2)}
assert spec == {
    1:{1:8,3:2,6:8,392:2},
    2:{2:27,4:8,6:28,7:8,13:8,18:2,26:8,138:8,192:4,360:2}
}
# Reconstruction of six-step witness by direct tuple iteration.
x = all_states[59]
assert all_states[118] == update(x)
assert update(update(update(update(update(update(x)))))) == all_states[33]
assert update(all_states[33]) == all_states[66]
assert update(all_states[66]) == all_states[33]
print('PASS B: direct 4096-state orbit tracing verifies all populations and basin spectra')
print('Cycle spectrum:',Counter(len(c) for c in cycles_seen))
print('Earliest-entry spectrum:',dict(sorted(delays.items())))

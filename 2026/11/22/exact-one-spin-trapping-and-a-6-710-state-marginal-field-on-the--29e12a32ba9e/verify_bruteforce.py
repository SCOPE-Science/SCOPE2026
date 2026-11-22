#!/usr/bin/env python3
"""Exhaustive integer certificate for one-spin stability on GP(10,2).

All sites and all binary assignments are examined; no external packages needed.
The doubled-field convention uses t=2h/J to avoid floating arithmetic.
"""
from collections import Counter
N = 20
V = (1 << N) - 1
edges = ([(i, (i+1)%10) for i in range(10)]
         + [(i, 10+i) for i in range(10)]
         + [(10+i, 10+(i+2)%10) for i in range(10)])
assert len(set(tuple(sorted(e)) for e in edges)) == 30
adj = [0]*N
for i,j in edges:
    adj[i] |= 1 << j
    adj[j] |= 1 << i
assert all(a.bit_count() == 3 for a in adj)
# Representatives of all parameter chambers and critical points.
fields2 = (0, 1, 2, 4, 6, 8)
strict = {t:Counter() for t in fields2}
weak = {t:Counter() for t in fields2}
ground = {t:None for t in fields2}
ground_count = Counter()
for mask in range(1 << N):
    up = mask.bit_count()
    magnet = 2*up-N
    aligned = sum(int(bool(mask & (1<<i)) == bool(mask & (1<<j))) for i,j in edges)
    exchange = 2*aligned-30
    for t in fields2:
        energy2 = 2*exchange-t*magnet
        if ground[t] is None or energy2 < ground[t]:
            ground[t] = energy2
            ground_count[t] = 1
        elif energy2 == ground[t]:
            ground_count[t] += 1
    # Each vertex is checked through the exact one-spin flip energy difference.
    # ΔH/J = 2 σ_i (h/J - Σ_{j~i}σ_j); double its inner factor.
    # Range of the integer field t for which every single-spin flip costs positive energy.
    for t in fields2:
        min_delta = 10**9
        for i in range(N):
            s = 1 if mask & (1 << i) else -1
            nsum = 2*(mask & adj[i]).bit_count()-3
            v = s*(t-2*nsum)
            if v < min_delta: min_delta=v
            if min_delta < 0: break
        if min_delta >= 0:
            weak[t][(magnet, exchange)] += 1
            if min_delta > 0:
                strict[t][(magnet, exchange)] += 1

expected_strict = {
 0:{(-4,-18):5,(0,-18):240,(4,-18):5},
 1:{(-4,-18):5,(0,-18):240,(4,-18):5},
 2:{(4,-18):5},
 4:{(4,-18):5,(6,-12):280,(8,-6):10},
 6:{},
 8:{(20,30):1}}
expected_weak_totals={0:250,2:6710,6:5828}
expected_ground={0:(-36,250),1:(-40,5),2:(-44,5),4:(-52,5),6:(-60,5828),8:(-100,1)}
for t in fields2:
    assert dict(strict[t]) == expected_strict[t], ('strict',t,strict[t])
    assert (ground[t],ground_count[t]) == expected_ground[t], ('ground',t,ground[t],ground_count[t])
for t,expected in expected_weak_totals.items():
    assert sum(weak[t].values())==expected,(t,sum(weak[t].values()))
print('EXHAUSTIVE_PASS states=1048576')
for t in fields2:
    print('h_over_J=',t,'/2 strict=',sum(strict[t].values()),'weak=',sum(weak[t].values()),'ground=',ground_count[t])

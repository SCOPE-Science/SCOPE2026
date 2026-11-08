#!/usr/bin/env python3
"""Exact checks of the negative-repunit four-generator semigroup formulas."""
from heapq import heappush, heappop
from hashlib import sha256

OFFSETS = ((1, 0), (2, 1, 0), (3, 2, 0),
           (4, 0), (5, 1, 0), (6, 2, 0), (0,))
H = (0, 1, 2, 1, 2, 3, 2)

def coins(m):
    return m // 7 + H[m % 7]

def predicted_pf(a):
    return sorted((a - 1) * (a - 1 - j) +
                  a * coins(a - 1 - j) - a
                  for j in OFFSETS[a % 7])

def apery_dijkstra(a):
    generators = (2*a-1, 4*a-3, 8*a-7)
    dist = [None] * a
    dist[0] = 0
    queue = [(0, 0)]
    while queue:
        d, r = heappop(queue)
        if d != dist[r]:
            continue
        for gen in generators:
            nr, nd = (r + gen) % a, d + gen
            if dist[nr] is None or nd < dist[nr]:
                dist[nr] = nd
                heappush(queue, (nd, nr))
    return dist

def direct_gaps(a, top):
    generators = (a, 2*a-1, 4*a-3, 8*a-7)
    present = bytearray(top + 1)
    present[0] = 1
    for n in range(1, top+1):
        present[n] = any(n >= g and present[n-g] for g in generators)
    return present

# Independent coin-change dynamic program.
L = [0]
for n in range(1, 10001):
    L.append(1 + min(L[n-c] for c in (1,3,7) if c<=n))
assert all(L[n] == coins(n) for n in range(len(L)))

# Weighted shortest paths, not the greedy formula, compute Apéry residues.
for a in range(8, 1501):
    dist = apery_dijkstra(a)
    for m in range(a):
        assert dist[(-m) % a] == (a-1)*m + a*coins(m), (a,m)
    W = set(dist)
    actual_pf = sorted(u-a for u in W if
                       all(u+gen not in W for gen in (2*a-1,4*a-3,8*a-7)))
    assert actual_pf == predicted_pf(a), (a,actual_pf,predicted_pf(a))

# Completely separate unbounded coin-sum recurrence for all tested gaps.
for a in range(8, 111):
    predicted = predicted_pf(a)
    top = predicted[-1] + 8*a
    present = direct_gaps(a, top)
    actual = [n for n in range(1, predicted[-1]+1)
              if not present[n] and all(present[n+g]
              for g in (a,2*a-1,4*a-3,8*a-7))]
    assert actual == predicted, (a,actual,predicted)
    assert all(present[n] for n in range(predicted[-1]+1,top+1)),a
    gaps = sum(1 for n in range(predicted[-1]+1) if not present[n])
    dist = apery_dijkstra(a)
    assert gaps == sum(dist)//a-(a-1)//2

# Compact exact example record, independently regenerable.
for a in (8,13,14,15,16,19,20,21,22):
    print(f'a={a}, a_mod_7={a%7}, PF={predicted_pf(a)}, type={len(predicted_pf(a))}')
print('ALL_TESTS_PASS: coins<=10000, Apéry/PF a=8..1500, gap DP a=8..110')

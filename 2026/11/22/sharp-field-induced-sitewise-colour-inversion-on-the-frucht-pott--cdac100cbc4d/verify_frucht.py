"""Exact finite enumeration for a three-colour antiferromagnetic spin system.

Run with Python 3: python verify_frucht.py
The graph, colors, energy, and field convention are defined below.
No external libraries or data files are required.
"""
from itertools import combinations, product
from collections import Counter

V = tuple(range(12))
EDGES = ((0,1),(0,6),(0,7),(1,2),(1,7),(2,3),(2,8),
         (3,4),(3,9),(4,5),(4,9),(5,6),(5,10),(6,10),
         (7,11),(8,11),(8,9),(10,11))
A = frozenset((0,2,5,9,11))
B = frozenset(V) - A

def edge_internal(s):
    return sum(u in s and v in s for u,v in EDGES)

assert len(EDGES) == 18
assert all(sum(u in e for e in EDGES) == 3 for u in V)
assert edge_internal(A) == 0 and edge_internal(B) == 3
assert {tuple(sorted(e)) for e in EDGES if set(e) <= B} == {(1,7),(3,4),(6,10)}

independent = Counter()
maximal = []
for mask in range(1 << 12):
    s = frozenset(i for i in V if mask & (1 << i))
    if edge_internal(s) == 0:
        independent[len(s)] += 1
        if len(s) == 5:
            maximal.append(s)
assert [independent[k] for k in range(13)] == [1,12,48,73,34,1] + [0]*7
assert maximal == [A]
assert sum(independent[k]*(2**k) for k in range(13)) == 1377

min_cost = [100] * 13
counts = [0] * 13
support = {5:[0]*12,7:[0]*12}
for col in product((0,1,2), repeat=12):
    k = col.count(0)
    m = sum(col[u] == col[v] for u,v in EDGES)
    if m < min_cost[k]:
        min_cost[k] = m
        counts[k] = 0
        if k in support:
            support[k] = [0]*12
    if m == min_cost[k]:
        counts[k] += 1
        if k in support:
            for i in V:
                support[k][i] += int(col[i] == 0)

assert min_cost == [3,2,1,0,0,0,2,3,6,9,12,15,18]
assert counts == [2,12,24,16,112,16,544,32,544,584,192,24,1]
assert support[5] == [16 if v in A else 0 for v in V]
assert support[7] == [32 if v in B else 0 for v in V]

def ground_by_twice_field(h2):
    energies = [2*min_cost[k]-h2*k for k in range(13)]
    low = min(energies)
    return low, tuple(k for k in range(13) if energies[k] == low)

assert ground_by_twice_field(1)[1] == (5,)
assert ground_by_twice_field(3)[1] == (5,7)
assert ground_by_twice_field(4)[1] == (7,)
assert ground_by_twice_field(6)[1] == (7,8,9,10,11,12)
assert ground_by_twice_field(8)[1] == (12,)
assert counts[5] == 16 and counts[7] == 32
assert counts[5]+counts[7] == 48
assert sum(counts[k] for k in range(7,13)) == 1377
print('EXACT_FRUCHT_POTTS_CERTIFICATE_OK 531441 configurations 4096 subsets')

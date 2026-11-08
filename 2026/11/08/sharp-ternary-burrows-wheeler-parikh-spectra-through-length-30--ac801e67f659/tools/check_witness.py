"""Independent direct-rotation test for every exhibited BWT last column.
Usage: python3 tools/check_witness.py data/parikh_profiles.csv
"""
import csv
import sys
from collections import Counter

with open(sys.argv[1], encoding='utf-8', newline='') as source:
    rows = list(csv.DictReader(source))

for row in rows:
    n = int(row['n'])
    target = (int(row['parikh_min']), int(row['parikh_mid']), int(row['parikh_max']))
    L = row['witness_BWT_L']
    assert len(L) == n and set(L) <= set('012')
    count = Counter(L)
    assert tuple(sorted([count[str(c)] for c in range(3)])) == target
    assert all(L[i] != L[i+1] for i in range(n-1))
    F = ''.join(sorted(L))
    seen = Counter()
    offsets = {s: sum(count[t] for t in '012' if t < s) for s in '012'}
    pi = []
    for s in L:
        pi.append(offsets[s] + seen[s])
        seen[s] += 1
    i, backwards = 0, []
    for step in range(n):
        backwards.append(L[i])
        i = pi[i]
        assert i != 0 or step == n-1
    assert i == 0
    u = ''.join(backwards[::-1])
    rotations = sorted(u[j:] + u[:j] for j in range(n))
    assert len(set(rotations)) == n
    assert ''.join(r[-1] for r in rotations) == L
    assert sum(u[j] != u[(j+1) % n] for j in range(n)) == (n+1)//2
    assert sum(x != y for x,y in zip(L,F)) == (n+1)//2
print(f'ALL {len(rows)} DIRECT BWT WITNESSES PASSED')

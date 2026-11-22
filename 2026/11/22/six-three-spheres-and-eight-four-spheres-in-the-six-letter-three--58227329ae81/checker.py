#!/usr/bin/env python3
"""Exact, dependency-free certificate for the 3-cycle permutation complex on six letters."""
from itertools import permutations, combinations
from collections import defaultdict, deque, Counter
from functools import lru_cache
import json
from pathlib import Path

N = 6
BASE = Path(__file__).resolve().parent

def is_single_three_cycle(p):
    seen = set()
    sizes = []
    for x in range(N):
        if x in seen:
            continue
        y, size = x, 0
        while y not in seen:
            seen.add(y)
            y = p[y]
            size += 1
        sizes.append(size)
    return sorted(sizes) == [1, 1, 1, 3]

S = [p for p in permutations(range(N)) if is_single_three_cycle(p)]
assert len(S) == 40
all_by_dim = [set() for _ in range(N)]
for p in S:
    for size in range(1, N + 1):
        all_by_dim[size - 1].update(combinations(p, size))
faces = [sorted(s) for s in all_by_dim]
assert list(map(len, faces)) == [6, 30, 120, 247, 194, 40]
cells = sum(faces, [])
index = {word: i for i, word in enumerate(cells)}
assert len(cells) == 637 and len(index) == 637
D = [len(word) - 1 for word in cells]
lowfaces = [[] for _ in cells]

def incidence(high, low):
    h, l = cells[high], cells[low]
    where = [i for i in range(len(h)) if h[:i] + h[i + 1:] == l]
    assert len(where) == 1
    return (-1) ** where[0]

for high, word in enumerate(cells):
    if len(word) > 1:
        for pos in range(len(word)):
            low = index[word[:pos] + word[pos + 1:]]
            assert D[high] == D[low] + 1
            lowfaces[high].append(low)

# Direct finite boundary-square check, including signs.
for hi in range(len(cells)):
    if D[hi] < 2:
        continue
    coeff = defaultdict(int)
    for mid in lowfaces[hi]:
        for lo in lowfaces[mid]:
            coeff[lo] += incidence(hi, mid) * incidence(mid, lo)
    assert all(x == 0 for x in coeff.values())

cert = json.loads((BASE / 'morse_pairs.json').read_text(encoding='utf8'))
assert cert['alphabet_size'] == N
pairs = [tuple(pair) for pair in cert['pairs']]
assert len(pairs) == 311 and len(set(pairs)) == len(pairs)
paired = {}
for lo, hi in pairs:
    assert hi in range(len(cells)) and lo in lowfaces[hi]
    assert lo not in paired and hi not in paired
    paired[lo], paired[hi] = hi, lo
assert len(paired) == 622
critical = [i for i in range(len(cells)) if i not in paired]
assert Counter(D[i] for i in critical) == {0: 1, 3: 6, 4: 8}

# The discrete-Morse directed Hasse graph has a downward arrow for
# each unmatched incidence and an upward arrow for each matched incidence.
matched = set(pairs)
arcs = [[] for _ in cells]
indegree = [0] * len(cells)
for hi, down in enumerate(lowfaces):
    for lo in down:
        src, dst = (lo, hi) if (lo, hi) in matched else (hi, lo)
        arcs[src].append(dst)
        indegree[dst] += 1
queue = deque(i for i, d in enumerate(indegree) if d == 0)
seen = 0
while queue:
    src = queue.popleft()
    seen += 1
    for dst in arcs[src]:
        indegree[dst] -= 1
        if indegree[dst] == 0:
            queue.append(dst)
assert seen == len(cells), 'matched Hasse diagram contains a directed cycle'

# Exact degree-4-to-degree-3 Morse differential. Only alternating
# gradient paths through pairs of dimensions (3,4) can contribute.
critical3 = {i for i in critical if D[i] == 3}
critical4 = [i for i in critical if D[i] == 4]
up4 = {lo: hi for lo, hi in pairs if D[lo] == 3}

@lru_cache(None)
def flow(low):
    assert D[low] == 3
    if low in critical3:
        return {low: 1}
    if low not in up4:
        return {}
    hi = up4[low]
    denom = incidence(hi, low)
    output = defaultdict(int)
    for alternate in lowfaces[hi]:
        if alternate == low:
            continue
        coefficient = -incidence(hi, alternate) * denom
        for dst, n in flow(alternate).items():
            output[dst] += coefficient * n
    return {dst: n for dst, n in output.items() if n}

for hi in critical4:
    result = defaultdict(int)
    for low in lowfaces[hi]:
        for dst, coeff in flow(low).items():
            result[dst] += incidence(hi, low) * coeff
    assert not any(result.values()), f'nonzero integral Morse boundary at cell {hi}'

assert sum((-1) ** d * len(f) for d, f in enumerate(faces)) == 1 - 6 + 8
print('PASS: 40 three-cycles; f-vector (6,30,120,247,194,40)')
print('PASS: full signed cellular boundary squares to zero')
print('PASS: 311 distinct unit-incidence matches; 637-cell matching DAG acyclic')
print('PASS: critical cells 1 in degree 0, 6 in degree 3, 8 in degree 4')
print('PASS: all 48 signed integer Morse boundary coefficients are zero')
print('CONCLUSION: X_6 is homotopy equivalent to 6 S^3 wedge 8 S^4')

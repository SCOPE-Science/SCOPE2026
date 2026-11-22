"""Independent orbit reconstruction for optimum strong Roman functions on H(5,2).
Run: python3 verify_geometry.py. Uses only the Python standard library.
"""
from itertools import combinations, permutations
from collections import Counter
from collections import deque

P = [m for m in range(32) if m.bit_count() == 2]
L = [m for m in range(32) if m.bit_count() == 3]
index = {m: i for i, m in enumerate(P)}
index.update({m: 10 + i for i, m in enumerate(L)})
adj = [set() for _ in range(20)]
for i, p in enumerate(P):
    for j, l in enumerate(L):
        if p & l == p:
            adj[i].add(10 + j)
            adj[10 + j].add(i)

def valid(s):
    if sum(map(int,s)) != 14:
        return False
    for v, ch in enumerate(s):
        if ch != '0':
            continue
        if not any(int(s[u]) >= 1 + (sum(s[w] == '0' for w in adj[u]) + 1) // 2
                   and int(s[u]) >= 2 for u in adj[v]):
            return False
    return True

def orbit(seed):
    answer = set()
    assert len(seed)==20 and valid(seed)
    for pi in permutations(range(5)):
        trans = [0] * 20
        for idx, mask in enumerate(P + L):
            mapped = sum(1 << pi[b] for b in range(5) if mask & (1 << b))
            trans[index[mapped]] = int(seed[idx])
        answer.add(''.join(map(str, trans)))
    return answer

high = orbit('10000200222200200001')
low = orbit('10000222002200100002')
assert len(high) == 10 and len(low) == 30 and high.isdisjoint(low)
F = sorted(high | low)

# Count all pairwise label Hamming distances and check that the small-change
# reconfiguration graph is a twofold subdivision of the Petersen graph.
H = {s: set() for s in F}
hist = Counter()
for i, a in enumerate(F):
    for b in F[i + 1:]:
        d = sum(x != y for x, y in zip(a, b))
        hist[d] += 1
        if d == 6:
            H[a].add(b)
            H[b].add(a)
assert hist == {6: 60, 8: 60, 10: 180, 12: 360, 14: 120}
assert all(len(H[s]) == (6 if s in high else 2) for s in F)

def anchor(s):
    return P[next(i for i in range(10) if s[i] == '1')]
parallel = Counter()
for s in low:
    endpoints = sorted(H[s])
    assert len(endpoints) == 2 and all(x in high for x in endpoints)
    a,b = sorted([anchor(x) for x in endpoints])
    assert a & b == 0
    parallel[(a,b)] += 1
assert len(parallel) == 15 and set(parallel.values()) == {2}

radii=[]
for start in F:
    d={start:0}; q=deque([start])
    while q:
        x=q.popleft()
        for y in H[x]:
            if y not in d:
                d[y]=d[x]+1; q.append(y)
    assert len(d)==40
    radii.append(max(d.values()))
assert min(radii)==5 and max(radii)==6
print('PASS: representatives generate 10+30 valid distinct functions; 60 minimal exchanges; doubled Petersen subdivision; radius 5 diameter 6')

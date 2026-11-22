"""Independent exact checker for two-colour domination in the folded five-cube.
Run: python3 check_b.py. No third-party modules required.
"""
from itertools import combinations
from collections import Counter, deque

# Even-parity binary words of length five, adjacent when Hamming distance four.
words = [x for x in range(32) if x.bit_count() % 2 == 0]
assert len(words) == 16
neighbors = [sum(1 << j for j, y in enumerate(words)
                 if (x ^ y).bit_count() == 4) for x in words]
assert all(x.bit_count() == 5 for x in neighbors)
full = (1 << 16) - 1
cover = [0] * (1 << 16)
for s in range(1, 1 << 16):
    p = (s & -s).bit_length() - 1
    cover[s] = cover[s ^ (1 << p)] | neighbors[p]
by_size = [[] for _ in range(17)]
for m in range(1 << 16):
    by_size[m.bit_count()].append(m)

opt = []
for weight in range(7):
    count = 0
    for a in range(weight + 1):
        for A in by_size[a]:
            for B in by_size[weight - a]:
                blank = full ^ (A | B)
                if blank & ~cover[A] or blank & ~cover[B]:
                    continue
                count += 1
                if weight == 6:
                    opt.append((A, B))
    assert count == (320 if weight == 6 else 0), (weight, count)
    print(f"weight_{weight}={count}")

assert len(opt) == 320
# Exhaustive independent test of the far-neighbour involution.
seen_types = Counter()
for A, B in opt:
    assert A.bit_count() == B.bit_count() == 3 and not A & B
    assert B == full ^ (A | cover[A])
    assert A == full ^ (B | cover[B])
    e = sum(bool(neighbors[i] >> j & 1) for i, j in combinations(
        (v for v in range(16) if A >> v & 1), 2))
    seen_types[e] += 1
assert seen_types == {0: 160, 2: 160}, seen_types
print("independent_first=160 path_first=160")

n = len(opt)
adj = [[] for _ in range(n)]
counts = Counter()
for i in range(n):
    A, B = opt[i]
    for j in range(i + 1, n):
        C, D = opt[j]
        da, db = (A ^ C).bit_count() // 2, (B ^ D).bit_count() // 2
        counts[da + db] += 1
        if da + db == 2:
            assert da == db == 1
            adj[i].append(j)
            adj[j].append(i)
assert counts == {2:1440, 3:2880, 4:13920, 5:14400, 6:18400}, counts
assert all(len(row) == 9 for row in adj)
assert sum(map(len, adj)) == 2880

distance_sum = 0
for start in range(n):
    dist = [-1] * n
    dist[start] = 0
    todo = deque([start])
    while todo:
        i = todo.popleft()
        for j in adj[i]:
            if dist[j] == -1:
                dist[j] = dist[i] + 1
                todo.append(j)
    assert tuple(Counter(dist)[i] for i in range(6)) == (1, 9, 54, 159, 90, 7)
    distance_sum += sum(dist)
assert distance_sum // 2 == 158240
assert all(w not in adj[v] for u in range(n)
           for v, w in combinations(adj[u], 2))  # no triangle
print("optima=320 one_token_edges=0 two_token_edges=1440")
print("two_token_degree=9 diameter=5 shells=1,9,54,159,90,7")
print("triangles=0 wiener=158240")

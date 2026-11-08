#!/usr/bin/env python3
"""Exact exhaustive certificate for incidence of cubic-contact quartic bitangent hexads.

Coordinates: F_2^6, with q(a,b)=a.b and its 28 anisotropic vectors.
A hexad is an unordered six-set of odd theta characteristics of sum zero.
Type I has no syzygetic triads; type II has eight.
No external packages, external input, or approximations.
"""
from itertools import combinations
from collections import Counter, defaultdict, deque


def q(v):
    return (((v & 1) * ((v >> 3) & 1) +
             ((v >> 1) & 1) * ((v >> 4) & 1) +
             ((v >> 2) & 1) * ((v >> 5) & 1)) & 1)

odd = [v for v in range(64) if q(v)]
assert len(odd) == 28
index = {v: i for i, v in enumerate(odd)}

# Independent count of complementary odd pairs for every nonzero difference.
for s in range(1, 64):
    assert sum(1 for v in odd if v ^ s in index) == 12

hexads = []
types = []
mask_to_index = {}
for sub in combinations(odd, 6):
    s = 0
    for v in sub:
        s ^= v
    if s:
        continue
    syz = sum(q(a ^ b ^ c) for a, b, c in combinations(sub, 3))
    assert syz in (0, 8)
    typ = 0 if syz == 0 else 1
    mask = sum(1 << index[v] for v in sub)
    mask_to_index[mask] = len(hexads)
    hexads.append(mask)
    types.append(typ)
assert len(hexads) == 6048
assert Counter(types) == {0: 1008, 1: 5040}

# Tetrad table, calculated without using the hexad pair-incidence routines.
# All candidate complementary pairs are found directly in the 28-vector model.
tetrads = defaultdict(list)
for h_id, mask in enumerate(hexads):
    positions = [i for i in range(28) if (mask >> i) & 1]
    for t in combinations(positions, 4):
        tmask = sum(1 << i for i in t)
        tetrads[tmask].append(h_id)
assert len(tetrads) <= 20475
profile = Counter()
for sub in combinations(range(28), 4):
    tmask = sum(1 << i for i in sub)
    cnt = Counter(types[h] for h in tetrads[tmask])
    profile[(cnt[0], cnt[1])] += 1
    x = odd[sub[0]] ^ odd[sub[1]] ^ odd[sub[2]] ^ odd[sub[3]]
    if x == 0:
        assert (cnt[0], cnt[1]) == (0, 0)
    else:
        syz_triads = sum(q(odd[sub[a]] ^ odd[sub[b]] ^ odd[sub[c]])
                          for a, b, c in combinations(range(4), 3))
        if syz_triads == 0:
            assert (cnt[0], cnt[1]) == (3, 3)
        else:
            assert syz_triads == 2 and (cnt[0], cnt[1]) == (0, 4)
assert profile == {(0, 0): 315, (3, 3): 5040, (0, 4): 15120}

# Compute cross-type adjacency from shared tetrads, separately from spectra.
across = [set() for _ in hexads]
for containing in tetrads.values():
    for i in containing:
        for j in containing:
            if types[i] != types[j]:
                across[i].add(j)
assert all(len(across[i]) == (45 if types[i] == 0 else 9)
           for i in range(len(hexads)))
assert sum(len(a) for a in across) // 2 == 45360
seen = {0}
queue = deque([0])
while queue:
    for nxt in across[queue.popleft()]:
        if nxt not in seen:
            seen.add(nxt)
            queue.append(nxt)
assert len(seen) == len(hexads)

# Whole 6048-by-6048 pair-incidence test; not only orbit representatives.
expected = {
    (0, 0): (152, 540, 225, 60, 30, 0, 1),
    (0, 1): (1005, 2100, 1470, 420, 45, 0, 0),
    (1, 0): (201, 420, 294, 84, 9, 0, 0),
    (1, 1): (996, 2124, 1449, 428, 42, 0, 1),
}
by_type = [[mask for mask, t in zip(hexads, types) if t == v]
           for v in (0, 1)]
for h, typ in zip(hexads, types):
    for other_type in (0, 1):
        counts = [0] * 7
        for other in by_type[other_type]:
            counts[(h & other).bit_count()] += 1
        assert tuple(counts) == expected[typ, other_type], (
            typ, other_type, tuple(counts))

print('VERIFY_OK')
print('28 odd theta characteristics; 6048 hexads (1008 type I; 5040 type II)')
print('4-bitangent extension profiles:', sorted(profile.items()))
for item in sorted(expected):
    print('intersection distribution', item, expected[item])
print('cross-type four-overlap exchange graph: 6048 vertices, 45360 edges, connected')

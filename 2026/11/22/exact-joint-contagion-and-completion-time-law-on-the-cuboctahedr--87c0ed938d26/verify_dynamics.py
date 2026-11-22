"""Exact synchronous three-neighbor bootstrap census on the cuboctahedral graph."""
from collections import Counter

cube_edges = sorted((u, u ^ (1 << bit)) for u in range(8)
                    for bit in range(3) if u < (u ^ (1 << bit)))
assert len(cube_edges) == 12
adj = []
for i, e in enumerate(cube_edges):
    adj.append(sum(1 << j for j, f in enumerate(cube_edges)
                   if i != j and bool(set(e) & set(f))))
assert all(x.bit_count() == 4 for x in adj)

counts = Counter()
minimal = []
round_hist = Counter()
joint = Counter()
for seed in range(1 << 12):
    active = seed
    time = 0
    profile = [active.bit_count()]
    while True:
        incoming = 0
        for i in range(12):
            if not (active & (1 << i)) and (active & adj[i]).bit_count() >= 3:
                incoming |= 1 << i
        if not incoming:
            break
        active |= incoming
        time += 1
        profile.append(active.bit_count())
    if active == (1 << 12) - 1:
        counts[seed.bit_count()] += 1
        round_hist[time] += 1
        joint[(seed.bit_count(), time)] += 1
        if seed.bit_count() == 5:
            minimal.append((seed, tuple(profile)))

expected = {5:72,6:300,7:492,8:417,9:212,10:66,11:12,12:1}
assert dict(counts) == expected, (counts, expected)
assert len(minimal) == 72
assert all(p == (5,7,9,11,12) for _,p in minimal)
expected_joint = {
    (5,4):72,
    (6,2):108, (6,3):192,
    (7,1):36, (7,2):336, (7,3):120,
    (8,1):177, (8,2):240,
    (9,1):164, (9,2):48,
    (10,1):66, (11,1):12, (12,0):1
}
assert dict(joint) == expected_joint, (joint,expected_joint)
assert sum(counts.values()) == 1572
print('dynamics: PASS', sorted(counts.items()))
print('joint (seed count, completion time) law:',sorted(joint.items()))
print('5-seed wave profile:', sorted({p for _,p in minimal}))
print('P(1/2) = 393/1024')

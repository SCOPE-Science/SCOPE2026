#!/usr/bin/env python3
"""Independent direct census: all 3^10 named Petersen vertex labelings."""
from itertools import combinations, product, permutations
from collections import Counter
from hashlib import sha256
E = tuple(combinations(range(5), 2))
N = [tuple(j for j, e in enumerate(E) if set(e).isdisjoint(E[i])) for i in range(10)]
valid = []
hits = bytearray()
counts = Counter()
for f in product((0, 1, 2), repeat=10):
    ok = True
    for v, lab in enumerate(f):
        if lab in (1, 2):
            if any(f[u] == lab for u in N[v]):
                ok = False; break
        else:
            neighbors = {f[u] for u in N[v]}
            if 1 not in neighbors or 2 not in neighbors:
                ok = False; break
    hits.append(int(ok))
    if ok:
        valid.append(f)
        counts[sum(lab != 0 for lab in f)] += 1
assert len(hits) == 59049
assert counts == Counter({6: 30, 7: 80}), counts
perm_mappings = []
for p in permutations(range(5)):
    perm_mappings.append(tuple(E.index(tuple(sorted((p[a],p[b])))) for a,b in E))
def transform(f, mapping):
    g=[0]*10
    for i,j in enumerate(mapping): g[j]=f[i]
    return tuple(g)
remaining=set(valid)
orbits=[]
while remaining:
    seed=min(remaining)
    orbit={transform(seed,m) for m in perm_mappings}
    assert orbit <= remaining
    orbits.append((sum(v!=0 for v in seed), len(orbit), seed))
    remaining -= orbit
assert sorted((w,size) for w,size,_ in orbits)==[(6,30),(7,20),(7,20),(7,20),(7,20)]
print('EXACT_DIRECT_OK', sorted(counts.items()), 'orbits', sorted((w,n) for w,n,_ in orbits))
print('membership_sha256', sha256(hits).hexdigest())

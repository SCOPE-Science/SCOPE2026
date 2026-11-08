#!/usr/bin/env python3
"""Replay a nine-representative minimal obstruction certificate."""
from itertools import product

rows = list(product(range(2), repeat=4))
reps = [0x0033, 0x003c, 0x112c, 0x143a, 0x14a3,
        0x14aa, 0x1863, 0x1866, 0x5a69]
transforms = []
for swap, flip in product((0,1), product((0,1), repeat=4)):
    perm = []
    for x,y,u,v in rows:
        a = (u,v,x,y) if swap else (x,y,u,v)
        perm.append(rows.index(tuple(a[j] ^ flip[j] for j in range(4))))
    transforms.append(perm)

obstructions = set()
for r in reps:
    for p in transforms:
        obstructions.add(sum(1 << p[i] for i in range(16) if r >> i & 1))
assert len(obstructions) == 132
models = []
for f, g in product(product((0,1),repeat=2), repeat=2):
    models.append(sum(1 << i for i,(x,y,u,v) in enumerate(rows)
                      if y == f[x] or v == g[u]))
assert len(set(models)) == 16

def possible(t): return any((t & ~a) == 0 for a in models)

# All certificate rows are inclusion-minimal violations.
for t in obstructions:
    assert not possible(t)
    assert all(possible(t & ~(1 << i)) for i in range(16) if t >> i & 1)

# Every other violating team contains a certified obstruction.
for t in range(1 << 16):
    contains_obstruction = any((t & b) == b for b in obstructions)
    assert contains_obstruction == (not possible(t))
print('nine orbit representatives give all 132 minimal violations')
print('all 65536 teams checked against the obstruction certificate')
print('VERIFIED')

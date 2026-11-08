#!/usr/bin/env python3
"""Independent row-word/tuple census of two-row binary toroidal locator masks."""
from itertools import combinations
from collections import defaultdict

sites=[(r,c) for r in (0,1) for c in (0,1,2)]
masks=list(combinations(sites,4))
classes=defaultdict(list)
for s in masks:
    classes[len(set(c for r,c in s))].append(s)
assert {k:len(v) for k,v in classes.items()}=={2:3,3:12}

# Encode rows as explicit lists, never use the bitmask technique of the direct checker.
solutions={m:set() for m in masks}
for top in range(256):
    a=tuple((top>>j)%2 for j in range(8))
    for bottom in range(256):
        b=tuple((bottom>>j)%2 for j in range(8))
        grid=(a,b)
        arr=top+256*bottom
        for mask in masks:
            words=set()
            for row in range(2):
                for col in range(8):
                    word=tuple(grid[(row+dr)%2][(col+dc)%8] for dr,dc in mask)
                    words.add(word)
            if len(words)==16:
                solutions[mask].add(arr)

valid=[solutions[m] for m in classes[3]]
assert len(valid)==12 and len(set.union(*valid))==64
assert len(set.intersection(*valid))==64
assert all(not solutions[m] for m in classes[2])
assert all(len(t)==64 for t in valid)

# Independent orbit construction: use transformations of two row strings.
def translated(x,rs,cs):
    a=tuple((x>>j)&1 for j in range(8))
    b=tuple((x>>(8+j))&1 for j in range(8))
    rows=(a,b)
    return sum(rows[(i+rs)%2][(j+cs)%8]<<(8*i+j) for i in range(2) for j in range(8))

reps=(0x0b5e,0x0da7,0x0f5a,0x0fa5)
orbits=[{translated(seed,rs,cs) for rs in range(2) for cs in range(8)} for seed in reps]
assert all(len(o)==16 for o in orbits)
assert len(set.union(*orbits))==64
assert set.union(*orbits)==valid[0]
print('INDEPENDENT_OK: explicit row/tuple enumeration and 4 complete 16-element translation orbits')

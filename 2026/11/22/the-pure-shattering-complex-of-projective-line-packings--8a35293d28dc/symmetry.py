"""Independent GL(4,2)-orbit check for packing-shattering facets.

Run: python3 symmetry.py. Standard Python library only.
"""
from collections import Counter
from itertools import combinations
from verify import lines, spreads, packings
line_index = {line: i for i, line in enumerate(lines)}
spread_index = {spread: i for i, spread in enumerate(spreads)}

# Elementary binary matrix operations generating all GL(4,2).
def swap(x, a, b):
    ba = (x >> a) & 1
    bb = (x >> b) & 1
    return x ^ ((ba ^ bb) << a) ^ ((ba ^ bb) << b)
def shear(x, a, b):
    return x ^ (((x >> b) & 1) << a)
ops = [(lambda x, a=a: swap(x, a, a + 1)) for a in range(3)]
ops += [(lambda x, a=a, b=b: shear(x, a, b))
        for a in range(3) for b in (a + 1,)]

# Check that these elementary operations generate GL(4,2), of order 20160.
ident = (1, 2, 4, 8)
seen = {ident}
front = [ident]
while front:
    basis = front.pop()
    for f in ops:
        nxt = tuple(f(x) for x in basis)
        if nxt not in seen:
            seen.add(nxt)
            front.append(nxt)
assert len(seen) == 20160, len(seen)

spread_maps = []
for f in ops:
    lp = [line_index[tuple(sorted(f(p) for p in line))]
          for line in lines]
    sp = [spread_index[tuple(sorted(lp[i] for i in spread))]
          for spread in spreads]
    spread_maps.append(sp)

def orbit(s):
    work = [s]
    members = {s}
    while work:
        x = work.pop()
        for m in spread_maps:
            y = tuple(sorted(m[i] for i in x))
            if y not in members:
                members.add(y)
                work.append(y)
    return members

support_mult = Counter(s for p in packings for s in combinations(p, 4))
for mult, expected in [(1, [3360, 3360]), (2, [840])]:
    remaining = {s for s, count in support_mult.items() if count == mult}
    sizes = []
    while remaining:
        orb = orbit(next(iter(remaining)))
        assert orb <= remaining
        sizes.append(len(orb))
        remaining -= orb
    assert sorted(sizes) == expected, (mult, sizes)
    print('QUARTET_MULTIPLICITY', mult, 'ORBIT_SIZES', *sorted(sizes))
print('GL4_ACTION_PASS order=20160')

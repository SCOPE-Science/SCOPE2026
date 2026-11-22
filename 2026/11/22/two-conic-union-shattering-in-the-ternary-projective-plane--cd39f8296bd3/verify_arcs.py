#!/usr/bin/env python3
"""Exact finite incidence / projective-orbit certificate for two-oval traces."""
from collections import Counter
from itertools import combinations, product

def normal(v):
    for a in v:
        if a:
            return tuple(a*x % 3 for x in v)  # every nonzero element is its own inverse in F_3
    raise ValueError('zero vector')

P = sorted({normal(v) for v in product(range(3), repeat=3) if any(v)})
assert len(P) == 13
L = sorted({sum(1 << i for i, p in enumerate(P)
                if sum(a*b for a, b in zip(u, p)) % 3 == 0)
            for u in P})
assert len(L) == 13 and all(l.bit_count() == 4 for l in L)
assert all((a & b).bit_count() == 1 for a,b in combinations(L,2))
O = sorted({sum(1 << i for i in I) for I in combinations(range(13), 4)
            if all((sum((l >> i) & 1 for i in I) <= 2) for l in L)})
assert len(O) == 234
C = sorted({a | b for a, b in combinations(O, 2)})
assert len(C) == 4641
assert Counter(c.bit_count() for c in C) == {5:468, 6:1248, 7:1638, 8:1287}

MATRICES = (
    ((0,1,0),(1,0,0),(0,0,1)),
    ((2,0,0),(0,1,0),(0,0,1)),
    ((1,1,0),(0,1,0),(0,0,1)),
    ((0,1,0),(0,0,1),(1,0,0)),
)
permutations = []
for m in MATRICES:
    p = [P.index(normal(tuple(sum(m[i][j]*v[j] for j in range(3)) % 3
                              for i in range(3)))) for v in P]
    assert len(set(p)) == 13
    permutations.append(tuple(1 << j for j in p))

# The four projective transformations generate the full projective linear group.
plain_perms=[tuple(x.bit_length()-1 for x in p) for p in permutations]
identity=tuple(range(13))
permutation_group={identity}
queue=[identity]
for a in queue:
    for b in plain_perms:
        c=tuple(a[b[j]] for j in range(13))
        if c not in permutation_group:
            permutation_group.add(c);queue.append(c)
assert len(permutation_group)==5616

def move(s, permutation):
    return sum(permutation[i] for i in range(13) if s >> i & 1)

def orbit_partition(k):
    left = {sum(1 << i for i in I) for I in combinations(range(13),k)}
    ans=[]
    while left:
        rep=min(left)
        orbit={rep}
        queue=[rep]
        for s in queue:
            for p in permutations:
                t=move(s,p)
                if t not in orbit:
                    orbit.add(t)
                    queue.append(t)
        assert orbit <= left
        left.difference_update(orbit)
        ans.append((rep, len(orbit), orbit))
    return ans

expected = {
 6: [(63,468,64),(126,78,64),(183,936,64),(187,234,64)],
 7: [(127,78,127),(191,936,128),(254,468,128),(439,234,128)],
 8: [(255,468,254),(447,702,255),(510,117,255)]
}
all_orbits={}
for k in (6,7,8):
    part=orbit_partition(k)
    observed=[(s,sz,len({c&s for c in C})) for s,sz,_ in part]
    assert observed == expected[k], (k,observed)
    all_orbits[k]=part

# Verify exceptional seven-sets geometrically as unions of two projective lines.
double_lines={a|b for a,b in combinations(L,2)}
assert len(double_lines)==78
assert all_orbits[7][0][2]==double_lines
# Every six-set has at least one extension outside the forbidden double-line orbit.
for _,_,orb in all_orbits[6]:
    for s in orb:
        assert any((s | (1<<i)) not in double_lines
                   for i in range(13) if not (s>>i)&1)
# The 6-class checks and hereditary closure give the complete face polynomial.
face_counts=(1,13,78,286,715,1287,1716,1638)
assert sum(sz for _,sz,orbit in all_orbits[7]) == 1716
assert all(len({c&s for c in C}) < 256 for s,_,_ in all_orbits[8])
print('ARCS_ORBITS_PASS; polynomial='+str(face_counts)+'; seven_orbits=78,936,468,234; eight_orbits=468,702,117')

#!/usr/bin/env python3
from itertools import combinations

def matchings(items):
    items = tuple(items)
    if not items:
        yield ()
        return
    a = items[0]
    for j in range(1, len(items)):
        b = items[j]
        rest = items[1:j] + items[j+1:]
        for m in matchings(rest):
            yield ((a,b),) + m

parts = []
seen = set()
for m in matchings(range(6)):
    canon = tuple(sorted(tuple(sorted(p)) for p in m))
    if canon not in seen:
        seen.add(canon)
        parts.append(canon)
assert len(parts) == 15

# The projective pair-sign group is F_2^3 / <(1,1,1)>.
# Choose representatives with first bit zero.
reps = [(0,0,0),(0,0,1),(0,1,0),(0,1,1)]
assert len(reps) == 4
for P in parts:
    for bits in reps:
        signs = [1]*6
        for bit, pair in zip(bits, P):
            if bit:
                for i in pair:
                    signs[i] = -1
        # Each changed pair changes exactly two coordinates; all determinants are +1.
        det = 1
        for s in signs:
            det *= s
        assert det == 1
        # Any diagonal quadratic sum c_i x_i^2 is unchanged.
        assert all(s*s == 1 for s in signs)
        # Each product-coordinate [x_i:x_j] is unchanged when both entries of a pair
        # receive the same sign.
        for bit, pair in zip(bits, P):
            i,j = pair
            assert signs[i] == signs[j]
print('PAIR_PARTITIONS=15')
print('GROUP_ORDER=4')
print('NONTRIVIAL_DETERMINANTS=+1')
print('DIAGONAL_QUADRICS_INVARIANT=YES')
print('PRODUCT_COORDINATES_INVARIANT=YES')
print('VERIFY_OK')

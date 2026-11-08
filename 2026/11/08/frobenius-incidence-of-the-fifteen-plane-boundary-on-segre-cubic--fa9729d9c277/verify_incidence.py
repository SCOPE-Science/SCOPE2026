#!/usr/bin/env python3
"""Exact eleven-type arithmetic incidence certificate for the Segre 15-plane boundary.
Uses only the Python standard library; all arithmetic is exact over Z.
"""
from collections import Counter
from functools import lru_cache
from math import comb


def pairings(a):
    if not a:
        yield ()
    else:
        first = a[0]
        for other in a[1:]:
            for rest in pairings([v for v in a[1:] if v != other]):
                yield tuple(sorted(((first, other),) + rest))

MATCH = tuple(sorted(set(pairings(list(range(6))))))
assert len(MATCH) == 15
INDEX = {m: i for i, m in enumerate(MATCH)}

@lru_cache(None)
def bipartite_components(mask):
    if not mask:
        return 6
    adj = [0] * 6
    for i, matching in enumerate(MATCH):
        if mask & (1 << i):
            for x, y in matching:
                adj[x] |= 1 << y
                adj[y] |= 1 << x
    color = [0] * 6
    good_components = 0
    for root in range(6):
        if color[root]:
            continue
        queue = [root]
        color[root] = 1
        bipartite = True
        while queue:
            x = queue.pop()
            for y in range(6):
                if not adj[x] & (1 << y):
                    continue
                if not color[y]:
                    color[y] = -color[x]
                    queue.append(y)
                elif color[y] == color[x]:
                    bipartite = False
        good_components += int(bipartite)
    return good_components


def partitions(n, maximum=None):
    maximum = n if maximum is None else maximum
    if not n:
        yield ()
    else:
        for d in range(min(n, maximum), 0, -1):
            for rest in partitions(n - d, d):
                yield (d,) + rest


def permutation(part):
    out = list(range(6))
    offset = 0
    for length in part:
        for i in range(length):
            out[offset + i] = offset + (i + 1) % length
        offset += length
    return out


def sigma_permutation_of_planes(part):
    p = permutation(part)
    return tuple(INDEX[tuple(sorted(tuple(sorted((p[x], p[y])))
                                    for x, y in m))] for m in MATCH)


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def scale(c, a):
    return tuple(c * x for x in a)

ZERO = (0, 0, 0)
EXPECTED = {
    (6,): {1: (0, 1, 1), 6: (1, 0, 0)},
    (5, 1): {},
    (4, 2): {1: (0, 1, 1), 2: (-2, 1, 0), 3: (1, 0, 0), 6: (2, 0, 0)},
    (4, 1, 1): {1: (0, 1, 1), 2: (0, 1, 0), 3: (1, 0, 0)},
    (3, 3): {1: (0, 3, 3), 6: (1, 0, 0)},
    (3, 2, 1): {3: (1, 0, 0), 6: (1, 0, 0)},
    (3, 1, 1, 1): {3: (3, 0, 0), 6: (1, 0, 0)},
    (2, 2, 2): {1: (6, -11, 7), 2: (-12, 9, 0), 3: (3, 0, 0), 6: (4, 0, 0)},
    (2, 2, 1, 1): {1: (-2, -3, 3), 2: (-2, 5, 0), 3: (3, 0, 0), 6: (2, 0, 0)},
    (2, 1, 1, 1, 1): {1: (-6, -3, 3), 2: (-12, 9, 0), 3: (7, 0, 0), 6: (4, 0, 0)},
    (1, 1, 1, 1, 1, 1): {1: (90, -75, 15), 2: (-90, 45, 0), 3: (15, 0, 0), 6: (10, 0, 0)},
}

def strata(part):
    image = sigma_permutation_of_planes(part)

    @lru_cache(None)
    def map_mask(mask):
        return sum(1 << image[i] for i in range(15) if mask & (1 << i))

    @lru_cache(None)
    def saturation(mask):
        while True:
            new_mask = mask | map_mask(mask)
            if new_mask == mask:
                return mask
            mask = new_mask

    S = [ZERO] * 16
    for mask in range(1, 1 << 15):
        b = bipartite_components(saturation(mask))
        v = tuple(int(j < b) for j in range(3))
        S[mask.bit_count()] = add(S[mask.bit_count()], v)
    N = [ZERO] * 16
    for k in range(15, 0, -1):
        cur = S[k]
        for m in range(k + 1, 16):
            cur = add(cur, scale(-comb(m, k), N[m]))
        N[k] = cur
    return {i: N[i] for i in range(1, 16) if N[i] != ZERO}


def run():
    assert len(EXPECTED) == 11
    for part in partitions(6):
        calculated = strata(part)
        assert calculated == EXPECTED[part], (part, calculated, EXPECTED[part])
        polynomial = [sum(v[i] for v in calculated.values()) for i in range(3)]
        print(f'{part}: N_m={calculated} B=[constant,q,q²]={polynomial}')
    assert sum(v[0] + 5*v[1] + 25*v[2]
               for v in EXPECTED[(1,1,1,1,1,1)].values()) == 250
    print('VERIFY_SEGRE_BOUNDARY_OK 11 FROBENIUS TYPES')

if __name__ == '__main__':
    run()

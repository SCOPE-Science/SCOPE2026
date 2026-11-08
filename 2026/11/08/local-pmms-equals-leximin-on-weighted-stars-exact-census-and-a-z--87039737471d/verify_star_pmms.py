"""Independent finite checks for the local-PMMS/leximin star theorem.

Run: python3 verify_star_pmms.py
Requires only the Python standard library. All enumerations are exact integers.
"""
from collections import Counter
from itertools import product, combinations
from math import comb
import random


def independent_pair_share(center_value, leaves, inside, outside):
    """Enumerate connected two-way partitions of the two-agent induced star.

    A connected partition has exactly one singleton leaf on one side.
    Do not assume the proposed sorting characterization.
    """
    union = tuple(inside) + (outside,)
    total = center_value + sum(leaves[i] for i in union)
    return max(min(leaves[i], total - leaves[i]) for i in union)


def direct_fair(center_value, leaves, inside):
    k = len(leaves)
    inside = tuple(inside)
    outsiders = tuple(i for i in range(k) if i not in inside)
    hub_value = center_value + sum(leaves[i] for i in inside)
    for j in outsiders:
        mu = independent_pair_share(center_value, leaves, inside, j)
        if hub_value < mu or leaves[j] < mu:
            return False
    return True


def structural_fair(center_value, leaves, inside):
    outside = [leaves[i] for i in range(len(leaves)) if i not in inside]
    hub_leaves = [leaves[i] for i in inside]
    if not outside or not hub_leaves:
        return True
    if max(hub_leaves) <= min(outside):
        return True
    return center_value == 0 and sum(x > 0 for x in hub_leaves) <= 1


def binom(n, r):
    return comb(n, r) if 0 <= r <= n else 0


def proposed_count(center_value, leaves, r):
    k = len(leaves)
    if r == 0:
        return 1
    z = sum(x == 0 for x in leaves)
    p = k-z
    if center_value == 0 and r <= z+1:
        return binom(z, r) + p * binom(z, r-1)
    threshold = sorted(leaves)[r-1]
    below = sum(x < threshold for x in leaves)
    same = sum(x == threshold for x in leaves)
    return comb(same, r-below)


def leximin_keys(center_value, leaves, inside):
    inside = set(inside)
    v = center_value + sum(w for i,w in enumerate(leaves) if i in inside)
    return tuple(sorted((v,) + tuple(w for i,w in enumerate(leaves) if i not in inside)))


def full_check(center_value, leaves):
    k = len(leaves)
    cases = 0
    for r in range(k+1):
        sets = tuple(combinations(range(k),r))
        actual = {subset for subset in sets if direct_fair(center_value,leaves,subset)}
        structural = {subset for subset in sets if structural_fair(center_value,leaves,subset)}
        assert actual == structural, ("structural", center_value,leaves,r, actual^structural)
        assert len(actual) == proposed_count(center_value,leaves,r), ("count", center_value,leaves,r,len(actual),proposed_count(center_value,leaves,r))
        # Independent global leximin optimization over all connected allocations.
        vectors = {subset:leximin_keys(center_value,leaves,subset) for subset in sets}
        optimum = max(vectors.values())
        leximin = {subset for subset,v in vectors.items() if v == optimum}
        assert actual == leximin, ("leximin",center_value,leaves,r,actual^leximin)
        cases += len(sets)
    return cases


def main():
    settings = assignments = 0
    for k in range(1, 8):
        for leaves in product(range(3), repeat=k):
            for h in (0,1,2):
                assignments += full_check(h, leaves)
                settings += k+1
    rng = random.Random(61329)
    for k in (8, 9):
        for _ in range(500):
            leaves = tuple(rng.randrange(6) for _ in range(k))
            h = rng.randrange(5)
            assignments += full_check(h, leaves)
            settings += k+1
    print('CHECK_OK', 'settings',settings,'connected_partition_choices',assignments)
    for k in (5,6,7):
        leaves = tuple(3*i+1 for i in range(k))
        r = 1
        assert proposed_count(0, leaves, r) == k
        assert proposed_count(1, leaves, r) == 1
        assert proposed_count(0, leaves, 2) == 1
        assert proposed_count(1, leaves, 2) == 1
    print('ZERO_HUB_CLIFF_OK')

if __name__ == '__main__':
    main()

"""Direct enumeration of globally minimal defensive alliances in clique windmills.

This verifier uses the original neighborhood condition and checks every
nonempty proper subset; it does not rely on the proof's classification.
"""
from collections import Counter
from itertools import product
from math import comb


def formula(profile):
    profile = tuple(profile)
    n = sum(profile)
    out = Counter()
    for size in profile:
        threshold = size // 2 + 1
        out[threshold] += comb(size, threshold)
    if sum(size % 2 for size in profile) <= 1:
        ways = 1
        for size in profile:
            ways *= comb(size, size // 2)
        out[n // 2 + 1] += ways
    return +out


def graph(profile):
    n = sum(profile) + 1
    neighbor_masks = [0] * n
    next_vertex = 1
    for size in profile:
        members = tuple(range(next_vertex, next_vertex + size))
        for vertex in members:
            neighbor_masks[0] |= 1 << vertex
            neighbor_masks[vertex] |= 1
            for other in members:
                if other != vertex:
                    neighbor_masks[vertex] |= 1 << other
        next_vertex += size
    return neighbor_masks


def brute(profile):
    neighbors = graph(profile)
    vertex_count = len(neighbors)
    total = 1 << vertex_count
    is_alliance = bytearray(total)
    for subset in range(1, total):
        valid = True
        for v, neighbor in enumerate(neighbors):
            if subset & (1 << v):
                inside = (subset & neighbor).bit_count()
                degree = neighbor.bit_count()
                if 2 * inside + 1 < degree:
                    valid = False
                    break
        if valid:
            is_alliance[subset] = 1
    minimal_count = Counter()
    local_only = 0
    for subset in range(1, total):
        if not is_alliance[subset]:
            continue
        proper = (subset - 1) & subset
        globally_minimal = True
        while proper:
            if is_alliance[proper]:
                globally_minimal = False
                break
            proper = (proper - 1) & subset
        if globally_minimal:
            minimal_count[subset.bit_count()] += 1
        elif all(not is_alliance[subset ^ (1 << v)]
                 for v in range(vertex_count) if subset & (1 << v)):
            local_only += 1
    return +minimal_count, sum(is_alliance), local_only, total - 1


def main():
    instances = 0
    checked_subsets = 0
    alliances = 0
    minimal = 0
    local_not_global = 0
    for petals in (2, 3, 4):
        for profile in product(range(1, 6), repeat=petals):
            if sum(profile) > 12:
                continue
            actual, all_count, loc, subsets = brute(profile)
            predicted = formula(profile)
            assert actual == predicted, (profile, actual, predicted)
            instances += 1
            checked_subsets += subsets
            alliances += all_count
            minimal += sum(actual.values())
            local_not_global += loc
    # The local/global distinction already appears for one leaf and one K3 petal.
    p = (1, 3)
    _, _, loc, _ = brute(p)
    assert loc == 3, loc
    # Every friendship graph with at least two triangle petals has two sizes.
    for petals in range(2, 30):
        assert formula((2,) * petals) == Counter({2: petals, petals + 1: 2 ** petals})
    print('VERIFY_OK',
          'profiles=' + str(instances),
          'examined_subsets=' + str(checked_subsets),
          'alliances=' + str(alliances),
          'globally_minimal=' + str(minimal),
          'local_not_global=' + str(local_not_global),
          'all_polynomials=PASS',
          'friendship_gaps=PASS')


if __name__ == '__main__':
    main()

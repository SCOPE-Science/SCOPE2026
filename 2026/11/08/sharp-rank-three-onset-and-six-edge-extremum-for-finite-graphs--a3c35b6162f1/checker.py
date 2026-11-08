#!/usr/bin/env python3
"""Independent finite checks for the graph-rank-three extremal theorem.

Standard library only. Run: python checker.py
"""
from functools import lru_cache
from itertools import combinations, permutations


def pairs(n):
    return list(combinations(range(n), 2))


def mask_from_edges(n, edges):
    index = {e: i for i, e in enumerate(pairs(n))}
    return sum(1 << index[tuple(sorted(e))] for e in edges)


def adjacency(n, mask):
    ns = [0] * n
    for i, (a, b) in enumerate(pairs(n)):
        if (mask >> i) & 1:
            ns[a] |= 1 << b
            ns[b] |= 1 << a
    return ns


def rank_at_least_three(n, mask):
    ns = adjacency(n, mask)
    for v in range(n):
        adjacent_good = nonadjacent_good = False
        for w in range(n):
            if w == v:
                continue
            profiles = 0
            for x in range(n):
                if x != v and x != w:
                    profile = 2 * ((ns[v] >> x) & 1) + ((ns[w] >> x) & 1)
                    profiles |= 1 << profile
            if profiles == 15:
                if (ns[v] >> w) & 1:
                    adjacent_good = True
                else:
                    nonadjacent_good = True
            if adjacent_good and nonadjacent_good:
                return True
    return False


def direct_finite_rank(n, mask):
    ns = adjacency(n, mask)
    @lru_cache(None)
    def rank(vertices):
        f = [i for i in range(n) if (vertices >> i) & 1]
        rem = [i for i in range(n) if not (vertices >> i) & 1]
        types = [[] for _ in range(1 << len(f))]
        for x in rem:
            ty = sum(((ns[x] >> z) & 1) << k for k, z in enumerate(f))
            types[ty].append(x)
        if any(not xs for xs in types):
            return 0
        return 1 + min(max(rank(vertices | (1 << x)) for x in xs) for xs in types)
    return rank(0)


def main():
    tested = 0
    for n in range(1, 7):
        for mask in range(1 << len(pairs(n))):
            assert not rank_at_least_three(n, mask), (n, mask)
            tested += 1
    print('no_rank_three_through_six', tested)

    witness_edges = [(0, 2), (0, 3), (0, 5), (1, 2), (1, 4), (2, 3)]
    witness_mask = mask_from_edges(7, witness_edges)
    assert rank_at_least_three(7, witness_mask)
    assert direct_finite_rank(7, witness_mask) == 3
    print('witness_rank', 3)

    orbital_masks = set()
    for p in permutations(range(7)):
        orbital_masks.add(mask_from_edges(7, [(p[u], p[v]) for u, v in witness_edges]))
    assert len(orbital_masks) == 5040  # witness has no nontrivial automorphism

    edge_list = pairs(7)
    count = {k: 0 for k in range(7)}
    extremal_masks = set()
    for k in range(7):
        for selection in combinations(range(len(edge_list)), k):
            mask = sum(1 << e for e in selection)
            if rank_at_least_three(7, mask):
                count[k] += 1
                if k == 6:
                    extremal_masks.add(mask)
    assert [count[k] for k in range(7)] == [0, 0, 0, 0, 0, 0, 5040]
    assert extremal_masks == orbital_masks
    print('seven_vertex_edge_counts', count)
    print('unique_extremal_orbit_size', len(orbital_masks))

    # Any union of five-vertex components has exactly the same outside
    # two-vertex adjacency profiles as one such component plus one isolate.
    for mask in range(1 << len(pairs(5))):
        extended = 0
        for bit, (u, v) in enumerate(pairs(5)):
            if (mask >> bit) & 1:
                extended |= 1 << pairs(6).index((u, v))
        assert not rank_at_least_three(6, extended)
    print('five_vertex_disjoint_union_criterion_OK', 1024)
    print('ALL_RANK_THREE_CHECKS_OK')

if __name__ == '__main__':
    main()

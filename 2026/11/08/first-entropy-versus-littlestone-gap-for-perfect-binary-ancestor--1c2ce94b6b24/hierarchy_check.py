"""Independent finite verification of the hierarchy ideal Littlestone dimensions.

Requires Python 3.9+, standard library only. The two methods share only the
mathematical definition of an ancestor-closed subset, not their recurrences.
"""
from functools import lru_cache


def check_height(h):
    n = (1 << (h + 1)) - 1
    ancestor = []
    for v in range(n):
        a, w = 0, v
        while True:
            a |= 1 << w
            if w == 0:
                break
            w = (w - 1) // 2
        ancestor.append(a)
    descendant = [sum(1 << w for w in range(n)
                      if ancestor[w] & (1 << v)) for v in range(n)]

    # Algorithm A: delete the forced-positive ancestors or forced-negative
    # descendants from the remaining induced poset.
    @lru_cache(None)
    def poset_rank(remaining):
        if not remaining:
            return 0
        return max(1 + min(poset_rank(remaining & ~ancestor[v]),
                           poset_rank(remaining & ~descendant[v]))
                   for v in range(n) if remaining & (1 << v))

    # Algorithm B: independently enumerate all actual membership vectors
    # and recursively split the corresponding set of hypotheses.
    ideals = [mask for mask in range(1 << n)
              if all(not (mask & (1 << v)) or
                     (mask & ancestor[v]) == ancestor[v]
                     for v in range(n))]
    columns = [sum(1 << i for i, mask in enumerate(ideals)
                   if mask & (1 << v)) for v in range(n)]

    @lru_cache(None)
    def version_rank(space):
        if space.bit_count() <= 1:
            return 0
        best = 0
        for col in columns:
            yes = space & col
            no = space ^ yes
            if yes and no:
                best = max(best, 1 + min(version_rank(yes),
                                         version_rank(no)))
        return best

    rank_a = poset_rank((1 << n) - 1)
    rank_b = version_rank((1 << len(ideals)) - 1)
    expected_counts = [2, 5, 26, 677]
    expected_ranks = [1, 2, 4, 8]
    assert len(ideals) == expected_counts[h]
    assert rank_a == rank_b == expected_ranks[h]
    print('height={} vertices={} ideals={} poset_ldim={} hypothesis_ldim={} poset_states={} hypothesis_states={}'.format(
        h, n, len(ideals), rank_a, rank_b,
        poset_rank.cache_info().currsize,
        version_rank.cache_info().currsize))


if __name__ == '__main__':
    for height in range(4):
        check_height(height)
    print('ALL_HIERARCHY_IDEAL_CHECKS_PASS')

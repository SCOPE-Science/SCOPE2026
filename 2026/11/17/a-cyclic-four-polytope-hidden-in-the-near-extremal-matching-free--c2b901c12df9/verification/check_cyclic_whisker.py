"""Standalone finite checks for the whiskered-cycle matching-free dual theorem.

Uses only the Python standard library. The proof for arbitrary n is separate.
"""
from functools import lru_cache
from itertools import combinations


def graph_edges(n):
    return ([(i, (i + 1) % n) for i in range(n)] +
            [(i, n + i) for i in range(n)])


def dual_faces(n):
    edges = graph_edges(n)
    N = 2 * n
    @lru_cache(None)
    def matching_number(remaining):
        if not remaining:
            return 0
        low = remaining & -remaining
        v = low.bit_length() - 1
        r = matching_number(remaining ^ low)
        for a, b in edges:
            if a == v and remaining & (1 << b):
                r = max(r, 1 + matching_number(remaining ^ low ^ (1 << b)))
            elif b == v and remaining & (1 << a):
                r = max(r, 1 + matching_number(remaining ^ low ^ (1 << a)))
        return r
    faces = {frozenset()}
    full = (1 << N) - 1
    for j in range(1, 5):
        for tup in combinations(range(N), j):
            rem = full
            for v in tup:
                rem ^= 1 << v
            if matching_number(rem) >= n - 2:
                faces.add(frozenset(tup))
    return faces


def cyclic_facets(n):
    eds = [frozenset((i, (i + 1) % n)) for i in range(n)]
    return {frozenset(e | f) for e, f in combinations(eds, 2)
            if not e & f}


def all_subfaces(facets):
    faces = {frozenset()}
    for f in facets:
        for j in range(1, len(f) + 1):
            faces.update(frozenset(t) for t in combinations(sorted(f), j))
    return faces


def test(n):
    dual = dual_faces(n)
    # Check the elementary dominated-vertex condition in the entire dual,
    # then remove centers in order. This tests each pair before deletion.
    current = set(dual)
    pairs = 0
    for center in range(n):
        leaf = center + n
        for f in current:
            if center in f and leaf not in f:
                assert f | {leaf} in current, (n, center, f)
        # An elementary collapse removes pairs (F, F + leaf) by descending size.
        candidates = sorted((f for f in current if center in f and leaf not in f),
                            key=lambda f: -len(f))
        for f in candidates:
            g = f | {leaf}
            if f not in current:
                continue
            assert g in current
            # F must be a free face in the current complex.
            assert not any(f < h and h != g for h in current), (n, center, f)
            current.remove(f)
            current.remove(g)
            pairs += 1
        assert all(center not in f for f in current)
    leaf_core = {frozenset(x - n for x in f) for f in current}
    expected = all_subfaces(cyclic_facets(n))
    assert leaf_core == expected, (n, leaf_core ^ expected)
    assert len(dual) - 2 * pairs == len(expected)
    assert len(cyclic_facets(n)) == n * (n - 3) // 2
    counts = tuple(sum(len(f) == j for f in current) for j in range(5))
    return len(dual), pairs, counts, len(cyclic_facets(n))


if __name__ == '__main__':
    for n in range(5, 12):
        print('n=%d dual_faces=%d elementary_pairs=%d core_f=%s facets=%d' %
              (n, *test(n)))
    print('CYCLIC_WHISKER_DUAL_CHECKS_PASS')

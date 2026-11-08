#!/usr/bin/env python3
"""Independent finite minimax and explicit-tree checks for shift-graph neighborhoods.

Use: python3 check_shift_online.py
Finite checks are evidence, not substitutes for the uniform proof.
"""
from functools import lru_cache
from itertools import combinations


def vertices(n):
    return list(combinations(range(1, n + 1), 2))


def adjacent(a, b):
    return a[1] == b[0] or b[1] == a[0]


def exact_online_dimension(n):
    v = vertices(n)
    neighborhoods = [sum(1 << j for j, h in enumerate(v) if adjacent(x, h)) for x in v]

    @lru_cache(maxsize=None)
    def rank(s):
        if s.bit_count() <= 1:
            return 0
        best = 0
        for q in neighborhoods:
            yes = s & q
            no = s & ~q
            if yes and no:
                best = max(best, 1 + min(rank(yes), rank(no)))
        return best

    return rank((1 << len(v)) - 1), rank.cache_info().currsize


# Query at each node is keyed by the previous label answers.
TREE = {
    '': (3, 4),
    '1': (1, 4),
    '11': (5, 6),
    '10': (1, 2),
    '0': (1, 2),
    '01': (4, 5),
    '00': (1, 3),
}
WITNESS = {
    '111': (4, 5),
    '110': (4, 6),
    '101': (2, 3),
    '100': (1, 3),
    '011': (2, 4),
    '010': (2, 5),
    '001': (3, 4),
    '000': (1, 2),
}


def check_tree():
    v = set(vertices(6))
    assert len(TREE) == 7 and len(WITNESS) == 8
    assert len(set(WITNESS.values())) == 8
    for pattern, h in WITNESS.items():
        assert h in v
        assert len(pattern) == 3
        for k, bit in enumerate(pattern):
            query = TREE[pattern[:k]]
            assert query in v
            assert adjacent(h, query) == (bit == '1'), (pattern, h, query)


def check_upper_arms(n):
    # Finite structural audit of the essential upper-bound lemma.
    v = vertices(n)
    for a, b in v:
        left = {(i, a) for i in range(1, a)}
        right = {(b, j) for j in range(b + 1, n + 1)}
        assert left.isdisjoint(right)
        assert left | right == {h for h in v if adjacent(h, (a, b))}
        for x in v:
            positives = {h for h in left | right if adjacent(h, x)}
            assert positives in (left, right, left | right, set()) or len(positives) <= 1, (n, a, b, x, positives)
            if positives not in (left, right, left | right, set()):
                assert len(positives) == 1


def check_small_lower():
    # A depth-two tree in Sh_4; witnesses may overlap across branches only if
    # the labels agree, and these explicit paths are pairwise inconsistent.
    q = {'': (2, 3), '1': (1, 3), '0': (1, 2)}
    w = {'11': (3, 4), '10': (1, 2), '01': (2, 3), '00': (1, 3)}
    for pattern, h in w.items():
        for k, bit in enumerate(pattern):
            assert adjacent(h, q[pattern[:k]]) == (bit == '1'), (pattern, h, q[pattern[:k]])


def main():
    expected = {2: 0, 3: 1, 4: 2, 5: 2, 6: 3, 7: 3, 8: 3, 9: 3}
    count = 0
    for n, answer in expected.items():
        got, states = exact_online_dimension(n)
        assert got == answer, (n, got, answer)
        print(f'n={n} hypotheses={len(vertices(n))} Ldim={got} checked_states={states}')
        count += states
    check_small_lower()
    check_tree()
    for n in range(2, 13):
        check_upper_arms(n)
    print(f'SHIFT_NEIGHBORHOOD_VERIFIED exact_cases={len(expected)} total_states={count} checked_arm_orders=11 depth3_leaves=8')


if __name__ == '__main__':
    main()

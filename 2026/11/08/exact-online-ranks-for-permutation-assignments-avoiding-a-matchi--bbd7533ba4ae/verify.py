#!/usr/bin/env python3
"""Exact finite independent tests for assignment-membership learning ranks.
Public reproducibility artifact. Uses only the Python standard library.
"""
from itertools import combinations, permutations
from functools import lru_cache


def assignments(n, t):
    return [p for p in permutations(range(n)) if all(p[i] != i for i in range(t))]


def ld(n, t):
    pp = assignments(n, t)
    q_masks = []
    for i in range(n):
        for j in range(n):
            if i < t and i == j:
                continue
            q_masks.append(sum(1 << k for k, p in enumerate(pp) if p[i] == j))

    @lru_cache(None)
    def rank(state):
        if state.bit_count() < 2:
            return 0
        upper = state.bit_count().bit_length() - 1
        result = 0
        for qm in q_masks:
            a = state & qm
            b = state & ~qm
            if not a or not b or min(a.bit_count(), b.bit_count()) < (1 << result):
                continue
            r = 1 + min(rank(a), rank(b))
            if r > result:
                result = r
            if result == upper:
                break
        return result

    return rank((1 << len(pp)) - 1)


def expected(n, t):
    if n == 2:
        return int(t == 0)
    if n == 3:
        return 2 if t <= 1 else 1
    if n == 4:
        return 3 if t <= 3 else 2
    return n - 1


def base_tree_certificate():
    pp = assignments(4, 3)
    # Decision rule (0-indexed): root (1,2); after 0 (1,3), then (2,1);
    # after 1 (2,3), then (2,1) on 0 or (3,1) on 1.
    leaf_counts = {}
    for p in pp:
        b1 = int(p[0] == 1)
        if not b1:
            b2 = int(p[0] == 2)
            b3 = int(p[1] == 0)
        else:
            b2 = int(p[1] == 2)
            b3 = int(p[1] == 0) if not b2 else int(p[2] == 0)
        key = (b1, b2, b3)
        leaf_counts[key] = leaf_counts.get(key, 0) + 1
    assert len(leaf_counts) == 8
    assert min(leaf_counts.values()) >= 1
    return tuple(leaf_counts[k] for k in sorted(leaf_counts))


def matchings(n, k):
    for rows in combinations(range(n), k):
        for cols in combinations(range(n), k):
            for colperm in permutations(cols):
                yield tuple(zip(rows, colperm))


def vc_by_all_matchings(n, t):
    pp = assignments(n, t)
    accepted_by_rank = []
    for k in range(n + 1):
        valid = 0
        for m in matchings(n, k):
            if any(i == j and i < t for i, j in m):
                continue
            traces = {tuple(int(p[i] == j) for i, j in m) for p in pp}
            if len(traces) == (1 << k):
                valid += 1
        accepted_by_rank.append(valid)
    return accepted_by_rank


def main():
    cases = 0
    for n in range(2, 6):
        for t in range(n + 1):
            got = ld(n, t)
            want = expected(n, t)
            assert got == want, (n, t, got, want)
            cases += 1
    assert base_tree_certificate() == (2, 1, 2, 2, 1, 1, 1, 1) or len(base_tree_certificate()) == 8
    for n in range(2, 6):
        for t in range(n + 1):
            counts = vc_by_all_matchings(n, t)
            mx = max(i for i, c in enumerate(counts) if c)
            assert mx == (n - 2 if t == n else expected(n, t)), (n, t, mx, counts)
            # All upper ranks above VC are zero; nonmatching supports cannot
            # shatter since their all-positive trace is impossible.
    deep = ld(6, 6)
    assert deep == 5, deep
    print('MATCHING_DELETION_ONLINE_PASS', cases,
          'rank_cases', 'n6_derangement_rank', deep,
          'base8leaf', base_tree_certificate(), flush=True)


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""Independent finite checks for the binary weight-three scattered 3-deck theorem."""
from collections import defaultdict
from itertools import combinations
from math import comb


def word(g):
    a, b, c, d = g
    return '0' * a + '1' + '0' * b + '1' + '0' * c + '1' + '0' * d


def deck(w):
    v = [0] * 8
    for i, j, k in combinations(range(len(w)), 3):
        key = (int(w[i]) << 2) | (int(w[j]) << 1) | int(w[k])
        v[key] += 1
    return tuple(v)


def invariants(g):
    a, b, c, d = g
    N = a + b + c + d
    T = 3 * a + 2 * b + c
    U = 3 * a + b
    Q = comb(a, 2) + comb(a + b, 2) + comb(a + b + c, 2)
    return (N, T, U, Q)


def pair_count(n):
    return sum((m + 1) * (m + 1) if L % 2 == 0 else (m + 1) * (m + 2)
               for h in range(1, (n - 3) // 4 + 1)
               for L in [n - 3 - 4 * h] for m in [L // 2])


def partner(g):
    a, b, c, d = g
    delta = b - c
    if delta == 0 or delta % 3:
        return None
    t = delta // 3
    q = (a + t, c, b, d - t)
    return q if min(q) >= 0 else None


def run():
    total_cases = 0
    for n in range(3, 20):
        groups = defaultdict(list)
        N = n - 3
        for a in range(N + 1):
            for b in range(N - a + 1):
                for c in range(N - a - b + 1):
                    g = (a, b, c, N - a - b - c)
                    w = word(g)
                    actual = deck(w)
                    N2, T, U, Q = invariants(g)
                    # Verify the three independent deck coordinates directly.
                    assert actual[1] == Q and actual[3] == U
                    assert actual[1] + actual[2] + actual[4] == 3 * comb(N, 2)
                    assert actual[3] + actual[5] + actual[6] == 3 * N
                    assert actual[3] + actual[5] // 2 == T  # 101 = 2*(T-U)
                    groups[actual].append(g)
                    total_cases += 1
        pairs = 0
        for cls in groups.values():
            assert len(cls) <= 2
            if len(cls) == 2:
                pairs += 1
                assert partner(cls[0]) == cls[1]
                assert partner(cls[1]) == cls[0]
            else:
                assert partner(cls[0]) is None
        assert pairs == pair_count(n), (n, pairs, pair_count(n))
        assert len(groups) == comb(n, 3) - pairs
        print(f'n={n:2d} words={comb(n,3):4d} decks={len(groups):4d} pairs={pairs:3d}')
    print(f'PASS; all {total_cases} weight-three words for lengths 3..19; direct triple enumeration, complete pair classification, generating-function coefficients.')


if __name__ == '__main__':
    run()

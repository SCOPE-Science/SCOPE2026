"""Exact combinatorial verification of shortest eight-agent gossip consensus.

Run with Python 3.9+; no third-party packages. Pair selections are unordered
pairs of labelled agents, independently and uniformly selected.
"""
from collections import defaultdict
from functools import lru_cache
from fractions import Fraction
from itertools import product


def successors(state):
    n = len(state)
    for i in range(n):
        ai = state[i]
        for j in range(i + 1, n):
            bj = state[j]
            if ai.bit_count() == bj.bit_count() and (ai & bj) == 0:
                new = list(state)
                new[i] = new[j] = ai | bj
                yield tuple(new)


def forward_counts(n):
    assert n > 1 and n & (n - 1) == 0
    current = {tuple(1 << i for i in range(n)): 1}
    sizes = []
    length = n * (n.bit_length() - 1) // 2
    for depth in range(1, length + 1):
        nxt = defaultdict(int)
        for state, multiplicity in current.items():
            for state2 in successors(state):
                nxt[state2] += multiplicity
        current = nxt
        sizes.append((depth, len(current), sum(current.values())))
    final = (2**n - 1,) * n
    assert set(current) == {final}
    return current[final], sizes


def suffix_count(n):
    """Independent *suffix* count by top-down recursion with memoization."""
    full = (1 << n) - 1
    end = (full,) * n

    @lru_cache(maxsize=None)
    def rec(state):
        if state == end:
            return 1
        return sum(rec(s) for s in successors(state))

    ans = rec(tuple(1 << i for i in range(n)))
    return ans, rec.cache_info()


def direct_four_agent_count():
    """Brute force all 6**4 unconstrained pair selections using integer rows."""
    n = 4
    pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    count = 0
    for choice in product(pairs, repeat=4):
        rows = [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]
        for i, j in choice:
            row = [(a + b) / 2 for a, b in zip(rows[i], rows[j])]
            rows[i] = rows[j] = row
        if all(all(x == Fraction(1, n) for x in row) for row in rows):
            count += 1
    return count


def main():
    assert direct_four_agent_count() == 24
    x4, _ = forward_counts(4)
    assert x4 == 24
    x8, profile = forward_counts(8)
    assert x8 == 2528870400
    y8, info = suffix_count(8)
    assert y8 == x8
    assert profile == [
        (1, 28, 28), (2, 210, 420), (3, 1260, 4200),
        (4, 5215, 44520), (5, 13020, 312480),
        (6, 18690, 1683360), (7, 44520, 9636480),
        (8, 94115, 51408000), (9, 45920, 190955520),
        (10, 44100, 776724480), (11, 560, 2528870400),
        (12, 1, 2528870400),
    ]
    p = Fraction(x8, 28 ** 12)
    assert p == Fraction(225, 20661046784)
    print('N4 unrestricted 4-step consensus schedules: 24 of 1296 = 1/54')
    print('N8 12-step consensus schedules:', x8)
    print('N8 probability:', p, 'decimal:', float(p))
    print('Independent suffix dynamic-programming result:', y8)
    print('Suffix cache:', info)
    print('Forward profile depth/states/ordered paths:')
    for row in profile:
        print(*row)

if __name__ == '__main__':
    main()

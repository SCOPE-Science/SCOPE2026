#!/usr/bin/env python3
"""Independent finite-state checks of an exact reset-threshold theorem.

Running python verify.py prints VERIFY_OK or raises AssertionError.
"""
from collections import deque
from functools import lru_cache


@lru_cache(None)
def transitions(n):
    assert n >= 2
    return [tuple((i + 1) % n for i in range(n)),
            tuple(0 if i == n - 1 else i for i in range(n)),
            tuple(n - 1 if i == n - 2 else i for i in range(n))]


def image(n, subset, letter):
    if letter == 'a':
        return ((subset << 1) & ((1 << n) - 1)) | (subset >> (n - 1))
    if letter == 'b':
        return ((subset & ~(1 << (n - 1))) | (1 if (subset >> (n - 1)) & 1 else 0))
    if letter == 'c':
        return ((subset & ~(1 << (n - 2))) | ((1 << (n - 1)) if (subset >> (n - 2)) & 1 else 0))
    raise ValueError(letter)


def word_image(n, word):
    subset = (1 << n) - 1
    for letter in word:
        subset = image(n, subset, letter)
    return subset


def predicted(n):
    k = n // 2
    if n % 2:
        words = ["cb" + ("a" * (n - 2) + "cb") * (k - 1)]
    else:
        words = ["b" + ("a" * (n - 2) + "cb") * (k - 1),
                 "c" + ("b" + "a" * (n - 2) + "c") * (k - 1)]
    length = (n - 2) * (n // 2) + 1
    assert all(len(w) == length for w in words)
    return length, set(words)


def bfs(n):
    full = (1 << n) - 1
    q = deque([full])
    d = {full: 0}
    ways = {full: 1}
    prev = {full: []}
    end_depth = None
    while q:
        s = q.popleft()
        depth = d[s]
        if end_depth is not None and depth > end_depth:
            break
        if s.bit_count() == 1:
            end_depth = depth
            continue
        if end_depth is not None:
            continue
        for letter in 'abc':
            z = image(n, s, letter)
            if z not in d:
                d[z] = depth + 1
                ways[z] = ways[s]
                prev[z] = [(s, letter)]
                q.append(z)
            elif d[z] == depth + 1:
                ways[z] += ways[s]
                prev[z].append((s, letter))
    targets = [s for s in d if s.bit_count() == 1 and d[s] == end_depth]
    total = sum(ways[s] for s in targets)
    return end_depth, total, targets, prev, full


def enumerate_optimal(targets, prev, full):
    from functools import lru_cache
    @lru_cache(None)
    def traverse(s):
        if s == full:
            return ('',)
        return tuple(p + letter for x, letter in prev[s] for p in traverse(x))
    return set(w for t in targets for w in traverse(t))


def eligible_distance(n, r):
    # Event-only optimization independent of the subset power automaton.
    # The initial residue is free; each move decreases it by one.
    best = 10 ** 20
    starts = []
    for q in range(n):
        count = 0
        for length in range(1, 1 + n * r):
            residue = (q - (length - 1)) % n
            if residue in (0, n - 1):
                count += 1
                if count == r:
                    if length < best:
                        best, starts = length, [q]
                    elif length == best:
                        starts.append(q)
                    break
    return best, starts


def main():
    comparisons = 0
    for n in range(2, 16):
        expected_length, expected_words = predicted(n)
        for w in expected_words:
            assert word_image(n, w).bit_count() == 1, (n, w)
        got_length, count, targets, prev, full = bfs(n)
        assert got_length == expected_length, (n, got_length, expected_length)
        assert count == len(expected_words), (n, count, expected_words)
        if n <= 12:
            assert enumerate_optimal(targets, prev, full) == expected_words
        comparisons += len(prev)
    for n in range(2, 51):
        d, sites = eligible_distance(n, n-1)
        assert d == predicted(n)[0]
        assert len(sites) == len(predicted(n)[1])
    print('VERIFY_OK n=2..15 BFS, n=2..12 all shortest words, n=2..50 independent event DP; subset states:', comparisons)

if __name__ == '__main__':
    main()

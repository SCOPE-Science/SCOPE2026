#!/usr/bin/env python3
"""Exhaustive finite checks for the cyclic-rotation permutation-word complex.

Uses only the Python standard library. This is a finite check of the written
all-n acyclic matching argument, not a substitute for that argument.
"""
from collections import defaultdict, deque
from itertools import combinations
from math import comb


def complex_cells(n):
    words = set()
    for start in range(n):
        rotation = tuple((start + j) % n for j in range(n))
        for length in range(1, n + 1):
            words.update(tuple(rotation[i] for i in positions)
                         for positions in combinations(range(n), length))
    return words


def matched_pairs(words):
    first = {}
    second = {}
    for word in words:
        if 0 in word:
            continue
        desc = [j for j in range(1, len(word)) if word[j-1] > word[j]]
        assert len(desc) <= 1
        j = desc[0] if desc else 0
        upper = word[:j] + (0,) + word[j:]
        assert upper in words
        first[word] = upper
    occupied = set(first) | set(first.values())
    for word in words:
        if word in occupied or word[-1] != 0 or len(word) < 2 or 1 in word:
            continue
        assert tuple(sorted(word[:-1])) == word[:-1]
        upper = (1,) + word
        assert upper in words and upper not in occupied
        second[word] = upper
    assert len(set(first.values())) == len(first)
    assert len(set(second.values())) == len(second)
    pairs = dict(first)
    pairs.update(second)
    assert len(pairs) == len(first) + len(second)
    assert set(pairs).isdisjoint(set(pairs.values()))
    return pairs, len(first), len(second)


def check_directed_hasse_acyclic(words, pairs):
    out = defaultdict(list)
    indegree = {w: 0 for w in words}
    edge_count = 0
    for upper in words:
        if len(upper) == 1:
            continue
        for i in range(len(upper)):
            lower = upper[:i] + upper[i+1:]
            assert lower in words
            if pairs.get(lower) == upper:
                tail, head = lower, upper
            else:
                tail, head = upper, lower
            out[tail].append(head)
            indegree[head] += 1
            edge_count += 1
    q = deque(w for w, deg in indegree.items() if deg == 0)
    visited = 0
    while q:
        w = q.popleft()
        visited += 1
        for v in out[w]:
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)
    assert visited == len(words), 'Closed matching gradient path detected'
    return edge_count


def wrap(i, j):
    return int(i > j)


def run(n):
    words = complex_cells(n)
    fv = tuple(sum(len(w) == k for w in words) for k in range(1, n + 1))
    assert fv == tuple(k * comb(n, k) for k in range(1, n + 1))
    pairs, first, second = matched_pairs(words)
    critical = words - set(pairs) - set(pairs.values())
    assert critical == {(0,), (1, 0)}, (n, critical)
    covers = check_directed_hasse_acyclic(words, pairs)
    for a, b, c in (w for w in words if len(w) == 3):
        assert wrap(a, b) + wrap(b, c) - wrap(a, c) == 0
    cycle = sum(wrap(i, (i + 1) % n) for i in range(n))
    assert cycle == 1
    assert sum((-1)**(k-1)*v for k,v in enumerate(fv, 1)) == 0
    print(f'n={n:2d}: cells={len(words):6d} Hasse_covers={covers:7d} '
          f'matched_I={first:6d} matched_II={second:6d} '
          f'critical=(0,1) cocycle=PASS winding=1 PASS')


if __name__ == '__main__':
    for n in range(2, 12):
        run(n)
    print('CYCLIC_ROTATION_WORD_COMPLEX_VERIFICATION_PASS')

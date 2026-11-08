#!/usr/bin/env python3
"""Exhaustive small-domain checks for exact-block partition membership.
Only Python standard library is required. Finite checks supplement the proof.
"""
from collections import Counter
from functools import lru_cache
from itertools import combinations
from math import comb


def partitions(n):
    # Restricted-growth words, independent of the shattering criterion.
    def rec(i, blocks):
        if i == n:
            yield frozenset(blocks)
            return
        for j in range(len(blocks)):
            old = blocks[j]
            blocks[j] = old | (1 << i)
            yield from rec(i + 1, blocks)
            blocks[j] = old
        blocks.append(1 << i)
        yield from rec(i + 1, blocks)
        blocks.pop()
    yield from rec(0, [])


@lru_cache(None)
def stirling(n, k):
    if n == 0:
        return int(k == 0)
    if k == 0 or k > n:
        return 0
    return stirling(n - 1, k - 1) + k * stirling(n - 1, k)


@lru_cache(None)
def no_singletons(n, k):
    if n == 0:
        return int(k == 0)
    if k == 0:
        return 0
    return sum(comb(n - 1, j - 1) * no_singletons(n - j, k - 1)
               for j in range(2, n + 1))


def expected_faces(n):
    return tuple(sum(comb(n, m) * stirling(m, k) for m in range(k, n))
                 + no_singletons(n, k) for k in range(n + 1))


def expected_facets(n):
    return tuple(n * stirling(n - 1, k) + no_singletons(n, k)
                 for k in range(n + 1))


def structural(sh):
    used = 0
    for q in sh:
        if q & used:
            return False
        used |= q
    full = (1 << N) - 1
    return used != full or all(q.bit_count() >= 2 for q in sh)


def brute(sh, concepts):
    traces = set()
    for blocks in concepts:
        bit = 0
        for j, q in enumerate(sh):
            if q in blocks:
                bit |= 1 << j
        traces.add(bit)
        if len(traces) == (1 << len(sh)):
            return True
    return len(traces) == (1 << len(sh))


def online_dim(n, concepts):
    # Independent exact decision-tree recurrence over version spaces.
    queries = list(range(1, 1 << n))
    yes = [sum(1 << i for i, c in enumerate(concepts) if q in c)
           for q in queries]
    @lru_cache(None)
    def calc(mask):
        best = 0
        for positive_mask in yes:
            yes_branch = mask & positive_mask
            no_branch = mask & ~positive_mask
            if yes_branch and no_branch:
                best = max(best, 1 + min(calc(yes_branch), calc(no_branch)))
        return best
    return calc((1 << len(concepts)) - 1)


all_support_cases = 0
for N in range(1, 6):
    concepts = list(partitions(N))
    queries = list(range(1, 1 << N))
    max_size = (1 << N) - 1 if N <= 4 else 4
    # N<=4: all 2^(2^N-1) supports. N=5: all supports through size four.
    shattered = set()
    faces = Counter()
    for k in range(min(max_size, len(queries)) + 1):
        for sh in combinations(queries, k):
            all_support_cases += 1
            expected = structural(sh)
            observed = brute(sh, concepts)
            assert observed == expected, (N, sh, observed, expected)
            if observed:
                faces[k] += 1
                if N <= 4:
                    shattered.add(frozenset(sh))
    for k in range(0, N):
        assert faces[k] == expected_faces(N)[k], (N, k, faces[k], expected_faces(N))
    if N <= 4:
        facets = Counter()
        for sh in shattered:
            if not any(sh | {q} in shattered for q in queries if q not in sh):
                facets[len(sh)] += 1
                used = 0
                for q in sh:
                    used |= q
                assert (used.bit_count() == N-1 or
                        (used.bit_count() == N and all(q.bit_count() >= 2 for q in sh)))
        assert tuple(facets[k] for k in range(N+1)) == expected_facets(N), (N, facets)
        assert online_dim(N, concepts) == N - 1
    print('n=', N, 'Bell=', len(concepts), 'tested_size_le=', max_size,
          'faces=', [faces[k] for k in range(N)], flush=True)

print('PARTITION_EXACT_BLOCK_PASS supports=', all_support_cases,
      'all_supports_n_le_4=1', 'sizes_le_4_n_5=1', 'online_n_le_4=1')

#!/usr/bin/env python3
from functools import lru_cache
from itertools import combinations


def stirling2(n, k):
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            dp[i][j] = dp[i - 1][j - 1] + j * dp[i - 1][j]
    return dp[n][k]


def rgs_partitions(n):
    if n == 0:
        return [()]
    out = []
    def rec(prefix, next_max):
        if len(prefix) == n:
            out.append(tuple(prefix))
            return
        for x in range(next_max + 1):
            prefix.append(x)
            rec(prefix, max(next_max, x + 1))
            prefix.pop()
    # Canonical RGS starts with 0; next available label is 1.
    rec([0], 1)
    return out


def refines(p, q):
    # p <= q in the partition lattice: every p-block lies inside a q-block.
    n = len(p)
    for i in range(n):
        for j in range(i + 1, n):
            if p[i] == p[j] and q[i] != q[j]:
                return False
    return True


def chain_count(n):
    parts = rgs_partitions(n)
    bottom = tuple(range(n)) if n else ()
    top = (0,) * n
    # Sort by number of blocks decreasing, so strict coarsenings are later.
    parts.sort(key=lambda p: (-len(set(p)), p))
    ways = {top: 1}
    for p in reversed(parts[:-1]):
        # This branch is not relied on; retained for clarity.
        pass
    @lru_cache(None)
    def count_from(p):
        if p == top:
            return 1
        return sum(count_from(q) for q in parts if q != p and refines(p, q))
    return count_from(bottom)


@lru_cache(None)
def lengyel(n):
    if n == 1:
        return 1
    return sum(stirling2(n, k) * lengyel(k) for k in range(1, n))


def all_chains(n):
    parts = rgs_partitions(n)
    bottom = tuple(range(n))
    top = (0,) * n
    @lru_cache(None)
    def tails(p):
        if p == top:
            return ((top,),)
        result = []
        for q in parts:
            if q != p and refines(p, q):
                for tail in tails(q):
                    result.append((p,) + tail)
        return tuple(result)
    return tails(bottom)


def first_merge_rank(chain, i, j):
    if i == j:
        return 0
    for level, p in enumerate(chain[1:], start=1):
        if p[i] == p[j]:
            return level
    raise AssertionError('top partition must merge every pair')


def check_ultrametric_chain(chain):
    n = len(chain[0])
    for i in range(n):
        for j in range(n):
            for k in range(n):
                dij = first_merge_rank(chain, i, j)
                dik = first_merge_rank(chain, i, k)
                djk = first_merge_rank(chain, j, k)
                assert dij <= max(dik, djk)

expected = [1, 1, 4, 32, 436, 9012, 262760]
chain_counts = []
for n, want in enumerate(expected, start=1):
    got = chain_count(n)
    chain_counts.append(got)
    assert got == want, (n, got, want)
    assert got == lengyel(n), (n, got, lengyel(n))

# Independently enumerate every chain through n=5 and verify that its
# first-merge ranks satisfy the ultrametric inequality.
for n in range(1, 6):
    chains = all_chains(n)
    assert len(chains) == expected[n - 1]
    for chain in chains:
        check_ultrametric_chain(chain)

full_counts = []
for n in range(1, 8):
    b = sum(stirling2(n, k) * lengyel(k) for k in range(1, n + 1))
    full_counts.append(b)
    if n == 1:
        assert b == 1
    else:
        assert b == 2 * lengyel(n)

assert full_counts == [1, 2, 8, 64, 872, 18024, 525520]
print('injective:', chain_counts)
print('all tuples:', full_counts)
print('VERIFY_OK')

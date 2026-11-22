"""Deterministic finite sanity checks for small cactus enriched-nerve maps.

No finite tests are used as substitutes for the proofs in RESULT.md.
Run: python check_cactus_nerve.py
"""
from collections import deque


def distance_matrix(graph):
    n = len(graph)
    ds = []
    for start in range(n):
        d = [None] * n
        d[start] = 0
        q = deque([start])
        while q:
            v = q.popleft()
            for w in graph[v]:
                if d[w] is None:
                    d[w] = d[v] + 1
                    q.append(w)
        assert all(x is not None for x in d)
        ds.append(d)
    return ds


def cactus_from_block_lengths(lengths):
    # Attach every new leaf block to the existing vertex numbered zero.
    g = [set()]
    blocks = []
    for length in lengths:
        vertices = [0] + list(range(len(g), len(g) + length - 1))
        g.extend(set() for _ in range(length - 1))
        for i in range(length):
            # Length 2 denotes a bridge, not two parallel edges.
            j = (i + 1) % length
            g[vertices[i]].add(vertices[j])
            g[vertices[j]].add(vertices[i])
        blocks.append(vertices)
    return g, blocks


def check_folds(lengths, limit):
    g, blocks = cactus_from_block_lengths(lengths)
    d = distance_matrix(g)
    n = len(g)
    maps = [tuple(range(n))]
    for block in blocks:
        anchor = block[0]
        current = list(maps[-1])
        if len(block) == 4 and limit == 1:
            # Preserve the first adjacent vertex, fold the opposite vertex to it.
            f = list(range(n))
            f[block[2]] = block[1]
            f[block[3]] = anchor
            maps.append(tuple(f[x] for x in current))
            current = list(maps[-1])
        h = list(range(n))
        for x in block:
            h[x] = anchor
        maps.append(tuple(h[x] for x in current))
    assert all(maps[-1][x] == 0 for x in range(n))
    for prev, cur in zip(maps, maps[1:]):
        assert max(d[prev[x]][cur[x]] for x in range(n)) <= limit
        for u in range(n):
            for v in range(n):
                assert d[cur[u]][cur[v]] <= d[u][v], (lengths, cur, u, v)
    return len(maps), n


def cycle_cocycle(n):
    # For every nondegenerate 1-simplex of N(C_n)(2), use the unique signed
    # minimal displacement, which is unique for n>=5 at distance <=2.
    def omega(i, j):
        steps = [s for s in (-2, -1, 0, 1, 2) if (i + s) % n == j]
        assert len(steps) == 1
        return steps[0]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                ij = abs(omega(i, j)) if (j - i) % n in (0, 1, 2, n-2, n-1) else 99
                jk = abs(omega(j, k)) if (k - j) % n in (0, 1, 2, n-2, n-1) else 99
                if ij + jk <= 2:
                    assert omega(i, j) + omega(j, k) == omega(i, k)
    assert sum(omega(i, (i + 1) % n) for i in range(n)) == n


if __name__ == '__main__':
    ntests = 0
    for lengths in ([2], [3], [4], [2, 3, 4], [4, 4, 3, 2]):
        check_folds(lengths, 1)
        ntests += 1
    for lengths in ([5], [5, 3, 4], [2, 5, 5, 4], [5, 5, 5]):
        check_folds(lengths, 2)
        ntests += 1
    for n in range(5, 19):
        cycle_cocycle(n)
        ntests += 1
    print('PASS', ntests, 'finite fold and integral-cocycle checks')

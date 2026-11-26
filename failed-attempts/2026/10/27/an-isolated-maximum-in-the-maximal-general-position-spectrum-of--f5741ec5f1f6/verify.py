"""Standalone finite checks for maximal general-position sets in sunlet graphs.

The infinite result is established by the accompanying mathematical proof;
these tests independently use the original three-on-one-geodesic definition.
"""
from collections import Counter


def sunlet_distances(n):
    size = 2 * n
    nbrs = [[] for _ in range(size)]
    for i in range(n):
        for j in ((i + 1) % n, i + n):
            nbrs[i].append(j)
            nbrs[j].append(i)
    dist = [[size + 1] * size for _ in range(size)]
    for root in range(size):
        dist[root][root] = 0
        queue = [root]
        for u in queue:
            for v in nbrs[u]:
                if dist[root][v] > dist[root][u] + 1:
                    dist[root][v] = dist[root][u] + 1
                    queue.append(v)
    return dist


def geodesic_triples(n, distances):
    size = 2 * n
    triples = []
    for a in range(size):
        for b in range(a + 1, size):
            for c in range(b + 1, size):
                d = distances
                if (d[a][b] + d[b][c] == d[a][c]
                        or d[a][c] + d[c][b] == d[a][b]
                        or d[b][a] + d[a][c] == d[b][c]):
                    triples.append((1 << a) | (1 << b) | (1 << c))
    return triples


def brute(n):
    dist = sunlet_distances(n)
    triples = geodesic_triples(n, dist)
    size = 2 * n
    pair_masks = [[] for _ in range(size)]
    for t in triples:
        for v in range(size):
            if t & (1 << v):
                pair_masks[v].append(t ^ (1 << v))
    valid = bytearray(1 << size)
    valid[0] = 1
    for mask in range(1, 1 << size):
        v = mask.bit_length() - 1
        rem = mask ^ (1 << v)
        if valid[rem] and not any((rem & pair) == pair for pair in pair_masks[v]):
            valid[mask] = 1
    m_dist = Counter()
    maximum_nonleaf = 0
    num_top = 0
    leaves = sum(1 << (n + v) for v in range(n))
    for mask in range(1 << size):
        if not valid[mask]:
            continue
        is_maximal = all(valid[mask | (1 << v)] == 0
                         for v in range(size) if not (mask & (1 << v)))
        if is_maximal:
            m_dist[mask.bit_count()] += 1
            if mask == leaves:
                num_top += 1
            else:
                assert mask & ((1 << n) - 1), (n, mask)
                maximum_nonleaf = max(maximum_nonleaf, mask.bit_count())
    assert valid[leaves]
    assert num_top == 1
    assert maximum_nonleaf == (n + 1) // 2 + 1, (n, maximum_nonleaf)
    assert all(size <= (n + 1) // 2 + 1 or size == n for size in m_dist)
    if n >= 4:
        assert m_dist[n] == 1
    print(f"DEFINITION_OK n={n} maximal_distribution={dict(sorted(m_dist.items()))} ")


def theoretical(n):
    m = n // 2
    if n % 2:
        picked = set(range(1, m + 1)) | {n - m}
        matching = [(n - a, m - a) for a in range(1, m)]
    else:
        picked = set(range(1, m + 1))
        matching = [(n - a, m - a) for a in range(1, m)]
    # Each paired endpoint lies on opposite sides of 0 and their
    # path through 0 has length at most half the cycle.
    used = set()
    for a, b in matching:
        assert a != b and a not in used and b not in used
        used.update((a, b))
        assert min(a, n-a) + min(b, n-b) == min((a-b)%n, (b-a)%n)
    assert len(matching) == m-1
    assert len(picked) == (n + 1) // 2
    assert all(not (min(a,n-a)+min(b,n-b)==min((a-b)%n,(b-a)%n))
               for a in picked for b in picked if a < b)
    dist=sunlet_distances(n)
    witness=[0]+[n+i for i in sorted(picked)]
    assert len(witness)==(n+1)//2+1
    for a in range(len(witness)):
        for b in range(a+1,len(witness)):
            for c in range(b+1,len(witness)):
                u,v,w=(witness[a],witness[b],witness[c])
                assert not (dist[u][v]+dist[v][w]==dist[u][w] or
                            dist[u][w]+dist[w][v]==dist[u][v] or
                            dist[v][u]+dist[u][w]==dist[v][w])
    print(f"MATCHING_WITNESS_OK n={n} matching_size={len(matching)} witness_size={len(witness)}")


if __name__ == '__main__':
    for n in range(3, 10):
        brute(n)
    for n in range(4, 41):
        theoretical(n)
    print('VERIFICATION_OK')

#!/usr/bin/env python3
"""Independent finite checks for optimal independent domination on helm graphs.

Pure Python, standard library only. Run: python3 check.py
"""
from collections import Counter, deque
from math import isqrt


def independent_masks(n):
    return [s for s in range(1, 1 << n)
            if not (s & (s << 1)) and not ((s & 1) and (s & (1 << (n - 1))))]


def predicted_distance(a, b, n):
    d = (a ^ b).bit_count()
    if a & b:
        return d
    aa = [i for i in range(n) if a >> i & 1]
    bb = [j for j in range(n) if b >> j & 1]
    if all((i - j) % n in (1, n - 1) for i in aa for j in bb):
        return d + 2
    return d


def predicted_ecc(a, n):
    sites = [i for i in range(n) if a >> i & 1]
    gaps = [(sites[(j + 1) % len(sites)] - sites[j]) % n
            for j in range(len(sites))]
    if len(sites) == 1:
        gaps = [n]
    baseline = len(sites) + sum(g // 2 for g in gaps)
    special = len(sites) == 1 or (len(sites) == 2 and (sites[1] - sites[0]) % n in (2, n - 2))
    return max(baseline, 5) if special else baseline


def helm_adj(n):
    # Vertex 0 = hub, 1..n = rim, n+1..2n = pendants.
    v = 2*n + 1
    adj = [0] * v
    def edge(a, b):
        adj[a] |= 1 << b
        adj[b] |= 1 << a
    for i in range(n):
        r = 1 + i
        edge(0, r)
        edge(r, 1 + ((i + 1) % n))
        edge(r, n + 1 + i)
    return adj


def direct_optima(n):
    adj = helm_adj(n)
    full = (1 << len(adj)) - 1
    sol = []
    for m in range(1 << len(adj)):
        if m.bit_count() > n:
            continue
        domination = 0
        left = m
        good = True
        while left:
            bit = left & -left
            v = bit.bit_length() - 1
            if adj[v] & m:
                good = False
                break
            domination |= bit | adj[v]
            left ^= bit
        if good and domination == full:
            assert m.bit_count() == n, ('unexpected smaller optimum', n, m)
            sol.append(m)
    return sol, adj


def encode_helm(a, n):
    # Rim selected if a_i=1, otherwise its pendant.
    m = 0
    for i in range(n):
        m |= 1 << (1 + i if a >> i & 1 else n + 1 + i)
    return m


def bfs_distances(start, neighbors):
    dist = {start: 0}
    queue = deque([start])
    while queue:
        a = queue.popleft()
        for b in neighbors[a]:
            if b not in dist:
                dist[b] = dist[a] + 1
                queue.append(b)
    return dist


def check(n):
    states = independent_masks(n)
    ss = set(states)
    nbr = {s: [s ^ (1 << i) for i in range(n) if s ^ (1 << i) in ss]
           for s in states}
    # Independent algorithm builds original helm, enumerates its optima,
    # and constructs edges using genuine graph-adjacent token replacements.
    if n <= 8:
        optima, adj = direct_optima(n)
        enc = {a: encode_helm(a, n) for a in states}
        assert set(optima) == set(enc.values()), ('incorrect optimum classification', n)
        reverse = {v: a for a, v in enc.items()}
        direct_nbr = {a: set() for a in states}
        for u in optima:
            for v in optima:
                if u >= v:
                    continue
                removed = u & ~v
                added = v & ~u
                if removed.bit_count() == added.bit_count() == 1:
                    x = removed.bit_length() - 1
                    y = added.bit_length() - 1
                    if adj[x] & (1 << y):
                        a, b = reverse[u], reverse[v]
                        direct_nbr[a].add(b)
                        direct_nbr[b].add(a)
        assert all(set(nbr[a]) == direct_nbr[a] for a in states), ('bad slides', n)
    # Statewise BFS; evaluates every reachable ordered pair.
    counts = Counter()
    antipodes = 0
    components = []
    seen = set()
    ecc = Counter()
    for a in states:
        dist = bfs_distances(a, nbr)
        if a not in seen:
            seen.update(dist)
            components.append(len(dist))
        e = max(dist.values())
        ecc[e] += 1
        if n >= 5:
            assert len(dist) == len(states), ('unexpected disconnection', n)
            assert predicted_ecc(a, n) == e, ('ecc mismatch', n, a, predicted_ecc(a,n), e)
            for b in states:
                assert predicted_distance(a, b, n) == dist[b], ('metric mismatch', n,a,b)
        for b, d in dist.items():
            if a < b:
                counts[d] += 1
    F = [0,1]
    for i in range(n+1):
        F.append(F[-1]+F[-2])
    if n >= 5:
        expected_diam = 5 if n == 5 else (n if n%2 == 0 else n-1)
        assert max(ecc) == expected_diam, (n, ecc, expected_diam)
        expected_rad = (5 if n in (5,7) else 4 if n == 6 else n//2+1)
        assert min(ecc) == expected_rad, (n,ecc,expected_rad)
        expected_pairs = n if n%2 else 1
        assert counts[expected_diam] == expected_pairs, (n,counts[expected_diam],expected_pairs)
    assert len(states) == F[n-1] + F[n+1] - 1
    assert sum(len(nbr[a]) for a in states) // 2 == n * (F[n-1]-1)
    return len(states), sum(len(nbr[a]) for a in states)//2, sorted(components), sorted(ecc.items())


if __name__ == '__main__':
    for n in range(3, 14):
        v, e, c, ecc = check(n)
        print(f'n={n}: optima={v} slides={e} components={c} eccentricities={ecc}')
    print('PASS: direct helm classification through n=8, and all-pair metric / radius / diameter / antipodes through n=13')

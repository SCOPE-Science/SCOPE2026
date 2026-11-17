"""Standalone finite tests of the edge-orbit Lefschetz identity."""
from itertools import combinations, permutations
from functools import lru_cache


def orbits(g):
    remaining = set(range(len(g)))
    output = []
    while remaining:
        a = min(remaining)
        cyc = []
        x = a
        while x in remaining:
            remaining.remove(x)
            cyc.append(x)
            x = g[x]
        assert x == a
        output.append(tuple(cyc))
    return output


def invariant_independence_sum(n, edges, g):
    edge_set = set(tuple(sorted(e)) for e in edges)
    cycles = orbits(g)
    good = [frozenset(c) for c in cycles if all(tuple(sorted((u, v))) not in edge_set for u, v in combinations(c, 2))]
    k = len(good)
    adj = [0] * k
    for i in range(k):
        for j in range(i+1, k):
            if any(tuple(sorted((u, v))) in edge_set for u in good[i] for v in good[j]):
                adj[i] |= 1 << j
                adj[j] |= 1 << i
    @lru_cache(None)
    def f(mask):
        if mask == 0:
            return 1
        b = mask & -mask
        i = b.bit_length() - 1
        return f(mask ^ b) - f(mask & ~ (b | adj[i]))
    return f((1 << k) - 1)


def subdivide(n, edges, g):
    edges = sorted(tuple(sorted(e)) for e in edges)
    lookup = {e: i for i, e in enumerate(edges)}
    long_edges = []
    h = list(g) + [-1] * (3*len(edges))
    for i, (u, v) in enumerate(edges):
        a, b, c = n+3*i, n+3*i+1, n+3*i+2
        long_edges += [(u, a), (a, b), (b, c), (c, v)]
        gu, gv = g[u], g[v]
        j = lookup[tuple(sorted((gu, gv)))]
        tgt = [n+3*j, n+3*j+1, n+3*j+2]
        if gu > gv:
            tgt.reverse()
        h[a], h[b], h[c] = tgt
    assert sorted(h) == list(range(len(h)))
    assert {tuple(sorted((h[u], h[v]))) for (u,v) in long_edges} == {tuple(sorted(x)) for x in long_edges}
    return len(h), long_edges, h


def edge_cycles(edges, g):
    ed = sorted(tuple(sorted(e)) for e in edges)
    pos = {e: i for i, e in enumerate(ed)}
    return len(orbits([pos[tuple(sorted((g[u],g[v])))] for u,v in ed]))


def check(n, edges, g):
    z = invariant_independence_sum(n, edges, g)
    m, subedges, h = subdivide(n, edges, g)
    zs = invariant_independence_sum(m, subedges, h)
    c = edge_cycles(edges, g)
    assert zs == (-1)**c * z, (n, edges, g, z, zs, c)
    return c, z, zs


if __name__ == '__main__':
    cases = 0; invert_cases = 0; nonzero = 0
    for n in range(1, 5):
        pairs = list(combinations(range(n), 2))
        for mask in range(1 << len(pairs)):
            edges = [pairs[i] for i in range(len(pairs)) if (mask >> i)&1]
            if len(edges) > 4:
                continue
            edge_set = set(edges)
            for g in permutations(range(n)):
                if {tuple(sorted((g[u],g[v]))) for u,v in edges} != edge_set:
                    continue
                c,z,zs = check(n, edges, g)
                cases += 1
                nonzero += (z != 0)
                if any(g[u] == v and g[v] == u for (u,v) in edges):
                    invert_cases += 1
    # Automorphism samples with larger edge sets and explicit inversions.
    extras = [
        (5, [(i, (i+1)%5) for i in range(5)], (1,2,3,4,0)),
        (5, [(i, (i+1)%5) for i in range(5)], (0,4,3,2,1)),
        (5, list(combinations(range(5), 2)), (1,0,2,3,4)),
        (5, list(combinations(range(5), 2)), (1,2,3,4,0)),
        (6, [(0,1),(1,2),(2,3),(3,4),(4,5)], (5,4,3,2,1,0)),
        (6, [(0,1),(1,2),(2,0),(3,4),(4,5),(5,3)], (3,4,5,0,1,2))
    ]
    for n,edges,g in extras:
        check(n,edges,g)
        cases += 1
    print(f'EDGE_ORBIT_LEFSCHETZ_IDENTITY_PASS cases={cases} edge_flip_cases={invert_cases} nonzero_base_cases={nonzero}')
    print('Includes all automorphisms of every graph on up to four vertices with at most four edges, plus six larger symmetry cases.')

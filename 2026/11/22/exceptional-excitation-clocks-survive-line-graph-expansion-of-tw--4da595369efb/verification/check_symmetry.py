#!/usr/bin/env python3
"""Exact symmetry audit of recurrent cycles of length at least four.

Input representative lists are generated with `./classify 1 --reps` and
`./classify 2 --reps`; no external graph packages are needed.
"""
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent


def graph(k):
    edges = [tuple(sorted((i, (i + 1) % 5))) for i in range(5)]
    edges += [(i, 5 + i) for i in range(5)]
    edges += [tuple(sorted((5 + i, 5 + (i + k) % 5))) for i in range(5)]
    assert len(edges) == len(set(edges)) == 15
    adj = [[False] * 10 for _ in range(10)]
    for a, b in edges:
        adj[a][b] = adj[b][a] = True
    return edges, adj


def automorphisms(adj):
    # Exact backtracking with adjacency and nonadjacency preservation.
    assigned = {}
    unused = set(range(10))
    out = []

    def rec():
        if len(assigned) == 10:
            out.append(tuple(assigned[i] for i in range(10)))
            return
        u = max((i for i in range(10) if i not in assigned),
                key=lambda i: (sum(adj[i][j] for j in assigned), -i))
        for v in sorted(unused):
            if any(adj[u][w] != adj[v][t] for w, t in assigned.items()):
                continue
            assigned[u] = v
            unused.remove(v)
            rec()
            unused.add(v)
            del assigned[u]

    rec()
    return out


def check(k):
    edges, adj = graph(k)
    lookup = {e: i for i, e in enumerate(edges)}
    aut = automorphisms(adj)
    expect_group = 20 if k == 1 else 120
    assert len(aut) == expect_group
    edge_perms = []
    for g in aut:
        edge_perms.append([lookup[tuple(sorted((g[u], g[v])))] for u, v in edges])
    nbr = [[j for j, (c, d) in enumerate(edges)
            if i != j and (a == c or a == d or b == c or b == d)]
           for i, (a, b) in enumerate(edges)]
    assert all(len(row) == 4 for row in nbr)
    weights = [3 ** j for j in range(15)]

    def next_state(x):
        digits = [(x // weights[i]) % 3 for i in range(15)]
        return sum(weights[i] *
                   (int(any(digits[j] == 1 for j in nbr[i])) if digits[i] == 0
                    else (digits[i] + 1) % 3)
                   for i in range(15))

    def orbit_min(x, period):
        y = x
        best = x
        for _ in range(period - 1):
            y = next_state(y)
            best = min(best, y)
        assert next_state(y) == x
        z = x
        for j in range(1, period):
            z = next_state(z)
            assert z != x, (period, j, x)
        return best

    def permute(x, perm):
        return sum(((x // weights[i]) % 3) * weights[perm[i]] for i in range(15))

    by_period = defaultdict(set)
    rep_lines = (HERE / f'reps_{k}.txt').read_text().splitlines()
    for line in rep_lines:
        p, x = map(int, line.split())
        assert p >= 4 and 0 <= x < 3 ** 15
        z = orbit_min(x, p)
        assert z not in by_period[p]
        by_period[p].add(z)
    expected = ({4: Counter({10: 4, 20: 2}), 5: Counter({2: 1, 4: 1}),
                 7: Counter({20: 5})} if k == 1 else
                {4: Counter({60: 1}), 5: Counter({30: 1}),
                 8: Counter({60: 1})})
    assert set(by_period) == set(expected)
    for p, rep_set in sorted(by_period.items()):
        remaining = set(rep_set)
        partition = Counter()
        while remaining:
            x = min(remaining)
            orbit = {orbit_min(permute(x, g), p) for g in edge_perms}
            assert orbit <= remaining, (k, p, len(orbit - remaining))
            remaining -= orbit
            partition[len(orbit)] += 1
        assert partition == expected[p], (k, p, partition, expected[p])
        print(f'k={k} period={p} temporal_orbits={len(rep_set)} '
              f'geometric_orbits={sum(partition.values())} sizes={dict(sorted(partition.items()))}')
    print(f'k={k} automorphism_group={len(aut)} verified')

if __name__ == '__main__':
    for parameter in (1, 2):
        check(parameter)

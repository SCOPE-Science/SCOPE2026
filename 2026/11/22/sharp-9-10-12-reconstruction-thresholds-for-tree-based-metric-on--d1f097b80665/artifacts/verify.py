"""Reproduce sharp metric type-profile collision thresholds for trees of order <=12.

Only Python 3 standard library. No external files or packages.
"""
from collections import Counter, defaultdict
from itertools import product

A000055 = (1, 1, 1, 2, 3, 6, 11, 23, 47, 106, 235, 551)


def adjacency(n, edges):
    g = [[] for _ in range(n)]
    for a, b in edges:
        assert 0 <= a < n and 0 <= b < n and a != b
        g[a].append(b)
        g[b].append(a)
    return g


def rooted_code(g, u, parent):
    return '(' + ''.join(sorted(rooted_code(g, v, u)
                                for v in g[u] if v != parent)) + ')'


def canon(n, edges):
    """Standard centre-rooted AHU complete invariant for unlabelled trees."""
    g = adjacency(n, edges)
    deg = [len(x) for x in g]
    leaves = [i for i, d in enumerate(deg) if d <= 1]
    alive = n
    while alive > 2:
        alive -= len(leaves)
        future = []
        for x in leaves:
            for y in g[x]:
                deg[y] -= 1
                if deg[y] == 1:
                    future.append(y)
        leaves = future
    return min(rooted_code(g, c, -1) for c in leaves)


def tree_families(limit=12):
    families = {1: {'()': ()}}
    for n in range(2, limit + 1):
        out = {}
        for prev in families[n - 1].values():
            for x in range(n - 1):
                edges = prev + ((x, n - 1),)
                key = canon(n, edges)
                out.setdefault(key, edges)
        families[n] = out
    return families


def add(*polys):
    out = Counter()
    for p in polys:
        out.update(p)
    return out


def mul(a, b):
    out = Counter()
    for (i, j), va in a.items():
        for (k, l), vb in b.items():
            out[(i + k, j + l)] += va * vb
    return out


def species_poly(n, edges):
    """Distance-1 and distance-3 counts; vacancy count is n-i-j."""
    g = adjacency(n, edges)
    par = [-1] * n
    order = [0]
    par[0] = 0
    for u in order:
        for v in g[u]:
            if par[v] == -1:
                par[v] = u
                order.append(v)
    assert len(order) == n
    f = {}
    for u in reversed(order):
        a, b, c = Counter({(1, 0): 1}), Counter({(0, 0): 1}), Counter({(0, 1): 1})
        for v in g[u]:
            if par[v] == u and v != u:
                aa, bb, cc = f[v]
                a = mul(a, add(aa, bb))
                b = mul(b, add(aa, bb, cc))
                c = mul(c, add(bb, cc))
        f[u] = (a, b, c)
    return add(*f[0])


def occupancy_coefficients(n, poly):
    out = [0] * (n + 1)
    for (i, j), value in poly.items():
        out[i + j] += value
    return tuple(out)


def brute_species(n, edges):
    """Independent full 3^n assignment check of all triangle constraints."""
    out = Counter()
    for assignment in product(range(3), repeat=n):
        if all(abs(assignment[u] - assignment[v]) != 2 for u, v in edges):
            out[(assignment.count(0), assignment.count(2))] += 1
    return out


def stats(family, mode):
    groups = defaultdict(list)
    for key, edges in family.items():
        n = len(edges) + 1
        p = species_poly(n, edges)
        inv = (sum(p.values()) if mode == 'scalar'
               else occupancy_coefficients(n, p) if mode == 'occupancy'
               else tuple(sorted(p.items())))
        groups[inv].append((key, edges))
    hits = [v for v in groups.values() if len(v) > 1]
    return groups, hits


def audit():
    fam = tree_families(12)
    print('classes by order:', [len(fam[n]) for n in range(1, 13)])
    assert tuple(len(fam[n]) for n in range(1, 13)) == A000055
    threshold = {'scalar': 9, 'occupancy': 10, 'species': 12}
    all_results = {}
    for mode in ('scalar', 'occupancy', 'species'):
        for n in range(1, threshold[mode] + 1):
            groups, collided = stats(fam[n], mode)
            if n < threshold[mode]:
                assert not collided, (mode, n)
            else:
                assert len(collided) == 1 and len(collided[0]) == 2, (mode, n, collided)
                a, b = collided[0]
                p = species_poly(n, a[1])
                q = species_poly(n, b[1])
                assert brute_species(n, a[1]) == p
                assert brute_species(n, b[1]) == q
                assert canon(n, a[1]) != canon(n, b[1])
                same = {
                    'scalar': sum(p.values()) == sum(q.values()),
                    'occupancy': occupancy_coefficients(n, p) == occupancy_coefficients(n, q),
                    'species': p == q
                }
                assert same[mode]
                print('FIRST', mode, 'n=', n, 'types=', len(fam[n]), 'collision_fibres=', len(collided))
                for code, edges in (a, b):
                    deg = sorted(len(x) for x in adjacency(n, edges))
                    print(' canonical=', code, 'degree_sequence=', deg, 'edges=', edges)
                print(' scalar=', sum(p.values()), sum(q.values()))
                print(' occupancy=', occupancy_coefficients(n, p))
                if mode == 'scalar':
                    print(' occupancy other=', occupancy_coefficients(n, q))
                if mode == 'occupancy':
                    sep = [(k, p.get(k, 0), q.get(k, 0)) for k in sorted(set(p) | set(q)) if p.get(k, 0) != q.get(k, 0)]
                    print(' species coefficient difference sample=', sep[:8])
                all_results[mode] = (a, b)
        print('OK', mode, 'all smaller orders separated')
    # Directly classify all one-point vectors over a 3-distance tree metric
    # at the 9-vertex scalar witness. These constraints coincide exactly.
    a, b = all_results['scalar']
    for _, edges in (a, b):
        n = len(edges) + 1
        valid = 0
        for f in product((1, 2, 3), repeat=n):
            if all(abs(f[u] - f[v]) <= (1 if tuple(sorted((u, v))) in set(edges) else 2)
                   for u in range(n) for v in range(u+1, n)):
                valid += 1
        assert valid == 3753
    print('VERIFY_OK')

if __name__ == '__main__':
    audit()

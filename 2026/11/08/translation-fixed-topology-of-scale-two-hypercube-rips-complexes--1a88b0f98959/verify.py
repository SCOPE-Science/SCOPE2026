"""Brute-force finite enumeration of translation-fixed scale-two Rips orbit complexes.

Run: python verify.py. Requires networkx 3.x.
"""
from itertools import combinations
import networkx as nx


def all_subspaces(n):
    universe = range(1 << n)
    trivial = frozenset([0])
    seen = {trivial}
    pending = [trivial]
    for h in pending:
        for x in universe:
            if x not in h:
                k = frozenset(h | {y ^ x for y in h})
                if k not in seen:
                    seen.add(k)
                    pending.append(k)
    return pending


def orbit_complex(n, h):
    remaining = set(range(1 << n))
    orbits = []
    while remaining:
        x = min(remaining)
        orbit = tuple(sorted(x ^ y for y in h))
        assert set(orbit) <= remaining
        remaining.difference_update(orbit)
        if all((u ^ v).bit_count() <= 2 for u, v in combinations(orbit, 2)):
            orbits.append(orbit)
    g = nx.Graph()
    g.add_nodes_from(range(len(orbits)))
    for a, b in combinations(range(len(orbits)), 2):
        if all((x ^ y).bit_count() <= 2 for x in orbits[a] for y in orbits[b]):
            g.add_edge(a, b)
    # A three-vertex orbit simplex exists exactly when its pairwise unions fit.
    triangles = sum(all(g.has_edge(i, j) for i, j in combinations(t, 2))
                    for t in combinations(g.nodes, 3))
    return g, triangles


def check(n, h):
    r = len(h).bit_length() - 1
    g, triangles = orbit_complex(n, h)
    diam = max(x.bit_count() for x in h)
    if diam > 2:
        assert len(g) == 0
        return 'empty'
    if r == 1:
        assert diam in (1, 2)
        cube = nx.hypercube_graph(n - 1)
        assert triangles == 0
        assert nx.is_isomorphic(g, cube)
        assert len(g) == 2 ** (n - 1)
        assert g.number_of_edges() == 2 ** (n - 2) * (n - 1)
        assert nx.number_connected_components(g) == 1
        assert g.number_of_edges() - g.number_of_nodes() + 1 == 1 + (n - 3) * 2 ** (n - 2)
        return 'cube'
    if r == 2:
        assert triangles == 0
        assert len(g) == 2 ** (n - 2)
        assert g.number_of_edges() == 0
        return 'discrete'
    raise AssertionError(('unexpected subgroup',n,h,r,diam))


if __name__ == '__main__':
    totals = {'cube': 0, 'discrete': 0, 'empty': 0}
    for n in range(2, 7):
        case_counts = {'cube': 0, 'discrete': 0, 'empty': 0}
        subspaces = all_subspaces(n)
        for h in subspaces:
            if len(h) == 1:
                continue
            result = check(n, h)
            case_counts[result] += 1
            totals[result] += 1
        print('n=',n,'subgroups=',len(subspaces)-1,'types=',case_counts)
    # Extra large-rank-one cases independent of above subgroup enumeration.
    for n in (7,8):
        for v in range(1, 1 << n):
            if v.bit_count() in (1,2):
                assert check(n, frozenset((0,v))) == 'cube'
                totals['cube'] += 1
        print('n=',n,'all admissible cyclic subgroups checked')
    print('TOTALS',totals)
    print('ALL_VERIFY_OK')

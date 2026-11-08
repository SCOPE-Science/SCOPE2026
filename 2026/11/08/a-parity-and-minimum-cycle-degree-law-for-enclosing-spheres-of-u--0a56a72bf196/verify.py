"""Exact integer checks for the radial/contact theorem of homogeneous in-in zonotopes.
Run: python inin_unicyclic_verify.py .  No third-party dependencies.
"""
from itertools import product
from collections import defaultdict


def graphs(max_n=8):
    # Every isomorphism class of connected simple unicyclic graphs has a labeling
    # with cycle vertices 0,...,L-1 and remaining tree parents smaller than child.
    for n in range(3, max_n + 1):
        for L in range(3, n + 1):
            cycle = tuple((i, i + 1) for i in range(L - 1)) + ((0, L - 1),)
            for parents in product(*(range(i) for i in range(L, n))):
                edges = cycle + tuple((p, i) for i, p in enumerate(parents, start=L))
                yield n, L, edges


def expected(n, L, edges, t):
    deg = [0] * n
    for u, v in edges:
        deg[u] += 1
        deg[v] += 1
    if L % 2 == 0:
        return sum((d + t) ** 2 for d in deg), 2
    delta = min(deg[:L]);k = sum(d == delta for d in deg[:L])
    return sum((d + t) ** 2 for d in deg) - 4 * (delta + t - 1), 4 * k


def endpoints(n, edges, t, all_cube_signs=False):
    best = -1
    contacts = set()
    for edge_signs in product((-1, 1), repeat=len(edges)):
        b = [0] * n
        for (u, v), s in zip(edges, edge_signs):
            b[u] += s
            b[v] -= s
        if all_cube_signs:
            cubes = product((-1, 1), repeat=n)
            pts = (tuple(b[i] + t * s[i] for i in range(n)) for s in cubes)
        else:
            zero = [i for i in range(n) if b[i] == 0]
            pts = (tuple(b[i] + t * (1 if b[i] > 0 else -1 if b[i] < 0 else f[zero.index(i)]) for i in range(n)) for f in product((-1, 1), repeat=len(zero)))
        for v in pts:
            d = sum(x * x for x in v)
            if d > best:
                best = d
                contacts = {v}
            elif d == best:
                contacts.add(v)
    return best, len(contacts)


def run():
    tests = 0
    instances = 0
    max_n = 8
    by_n = defaultdict(int)
    for n, L, edges in graphs(max_n):
        by_n[n] += 1
        for t in (1, 2):
            got = endpoints(n, edges, t)
            want = expected(n, L, edges, t)
            assert got == want, (n, L, edges, t, got, want)
            tests += 1
        instances += 1
    print('Canonical exhaustive unicyclic graph configurations through n=8:', instances)
    print('Configurations by n:', dict(sorted(by_n.items())))
    print('Exact extremum/contact comparisons:', tests)
    # Independent full hypercube x edge endpoint enumeration on a representative
    # selection, including both parities, cycles, and branched attachments.
    independent = 0
    for n, L, edges in graphs(6):
        for t in (1, 2):
            full = endpoints(n, edges, t, all_cube_signs=True)
            want = expected(n, L, edges, t)
            assert full == want, (n, L, edges, t, full, want)
            independent += 1
    print('Full 2^(number_of_vertices+number_of_edges) endpoint checks:', independent)
    print('PASS')

if __name__ == '__main__':
    run()

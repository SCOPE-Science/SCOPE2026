"""Exact finite test of path-count commutation formulas for graph inverse semigroups.

Usage: python3 verify.py
No third-party modules are needed. Tests are finite checks, not a proof of the universal theorem.
"""
from itertools import product


def path_counts(n, edges):
    """Directed acyclic multigraph; vertices are topologically ordered 0,...,n-1."""
    m = [[int(u == v) for v in range(n)] for u in range(n)]
    for u in range(n - 1, -1, -1):
        for a, b in edges:
            if a == u:
                for v in range(n):
                    m[u][v] += m[b][v]
    p = [sum(m[u][v] for u in range(n)) for v in range(n)]
    return m, p


def formula(n, edges):
    m, p = path_counts(n, edges)
    q = sum(z * z for z in p)
    a = lambda u, v: p[u] * p[v] - p[v] * m[v][u] - p[u] * m[u][v] + (p[u] if u == v else 0)
    return (1 + 2 * q - sum(p)
            + sum(a(u, v)**2 for u in range(n) for v in range(n))
            + 2 * sum(p[u] * m[u][v]**2 for u in range(n) for v in range(n)))


def paths_and_elements(n, edges):
    outs = [[] for _ in range(n)]
    for j, (u, v) in enumerate(edges):
        outs[u].append((j, v))
    paths = [(v, (), v) for v in range(n)]
    for _ in range(n):
        for u, seq, w in list(paths):
            for eid, v in outs[w]:
                x = (u, seq + (eid,), v)
                if x not in paths:
                    paths.append(x)
    by_end = [[t for t in paths if t[2] == v] for v in range(n)]
    elements = [(a, b) for bucket in by_end for a in bucket for b in bucket]
    return paths, by_end, elements


def prefix(a, b):
    return a[0] == b[0] and len(a[1]) <= len(b[1]) and a[1] == b[1][:len(a[1])]


def prod(x, y):
    if x is None or y is None:
        return None
    a, b = x
    c, d = y
    if prefix(b, c):
        suffix = c[1][len(b[1]):]
        return ((a[0], a[1] + suffix, c[2]), d)
    if prefix(c, b):
        suffix = b[1][len(c[1]):]
        return (a, (d[0], d[1] + suffix, b[2]))
    return None


def centralizer_formula(a, paths, by_end):
    alpha, beta = a
    c = lambda w, x: sum(prefix(x, gamma) or prefix(gamma, x) for gamma in by_end[w])
    p = [len(bucket) for bucket in by_end]
    if alpha == beta:
        return 1 + sum(c(w, alpha)**2 + (p[w] - c(w, alpha))**2 for w in range(len(p)))
    shared = sum(prefix(lam, alpha) and prefix(lam, beta) for lam in paths)
    return 1 + sum((p[w] - c(w, alpha)) * (p[w] - c(w, beta)) for w in range(len(p))) + shared


def check(n, edges):
    paths, by_end, elements = paths_and_elements(n, edges)
    nonzero = len(elements)
    total = 2 * nonzero + 1  # pairs with at least one coordinate zero
    for a in elements:
        brute_c = 1
        for b in elements:
            if prod(a, b) == prod(b, a):
                brute_c += 1
        assert brute_c == centralizer_formula(a, paths, by_end), (n, edges, a, brute_c)
        total += brute_c - 1
    # The first term contains all zero-coordinate pairs; loop counts nonzero pairs.
    assert total == formula(n, edges), (n, edges, total, formula(n, edges))
    return len(elements) + 1, total


def main():
    simple = 0
    for n in range(1, 6):
        possibilities = [(u, v) for u in range(n) for v in range(u + 1, n)]
        for mask in range(1 << len(possibilities)):
            edges = [e for i, e in enumerate(possibilities) if mask >> i & 1]
            check(n, edges)
            simple += 1
    multi = 0
    for n in range(2, 5):
        possibilities = [(u, v) for u in range(n) for v in range(u + 1, n)]
        for multiplicities in product(range(3), repeat=len(possibilities)):
            edges = [e for e, count in zip(possibilities, multiplicities) for _ in range(count)]
            if len(edges) > 8:
                continue
            check(n, edges)
            multi += 1
    for n, edges, expected_order, expected_pairs in [
        (2, [(0, 1)], 6, 22),
        (3, [(0, 1), (1, 2)], 15, 125),
        (4, [(0, 1), (0, 2), (1, 3), (2, 3)], 35, 817),
        (2, [(0, 1), (0, 1)], 11, 71),
    ]:
        order, pairs = check(n, edges)
        assert (order, pairs) == (expected_order, expected_pairs)
    print('PASS: simple DAGs', simple, 'acyclic multigraphs', multi,
          '; per-element centralizers and all ordered commuting pairs')
    print('PASS: example (semigroup order, ordered commuting pairs): (6,22), (15,125), (35,817), (11,71)')


if __name__ == '__main__':
    main()

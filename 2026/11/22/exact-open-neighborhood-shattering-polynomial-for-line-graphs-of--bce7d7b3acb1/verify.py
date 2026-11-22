"""Independent finite checks of the open-neighborhood shattering formulas for tree line graphs.
Uses only the Python standard library.  The theorem itself is proved separately.
"""
from itertools import combinations, product
from math import comb
from random import Random


def edges_from_prufer(code):
    n = len(code) + 2
    deg = [1] * n
    for v in code:
        deg[v] += 1
    edges = []
    for v in code:
        u = next(i for i in range(n) if deg[i] == 1)
        edges.append(tuple(sorted((u, v))))
        deg[u] -= 1
        deg[v] -= 1
    u, v = [i for i in range(n) if deg[i] == 1]
    edges.append((u, v))
    return tuple(edges)


def theorem(n, edges):
    adj = [set() for _ in range(n)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    deg = list(map(len, adj))
    s1 = len(edges) if len(edges) > 1 else 0
    s2 = s3 = 0
    for u in range(n):
        d = deg[u]
        if d < 3:
            continue
        a = sum(deg[v] >= 2 for v in adj[u])
        b = sum(any(deg[w] >= 2 for w in adj[v] if w != u) for v in adj[u])
        missing = (comb(d, 2) if a == 0 else
                   d - 1 if a == 1 and b == 0 else
                   1 if a == 2 and b == 0 else 0)
        s2 += comb(d, 2) - missing
        if d >= 4:
            s3 += comb(a, 3) - int(a == 3 and b == 0)
    for u, v in edges:
        for x in adj[u] - {v}:
            for y in adj[v] - {u}:
                if deg[x] + deg[u] >= 4 and deg[v] + deg[y] >= 4:
                    s2 += 1
    return (1, s1, s2, s3)


def brute(n, edges, check_four=True):
    m = len(edges)
    neighborhoods = [
        sum(1 << j for j, (a, b) in enumerate(edges)
            if i != j and (u in (a, b) or v in (a, b)))
        for i, (u, v) in enumerate(edges)
    ]
    out = [1, 0, 0, 0]
    for k in range(1, min(m, 4 if check_four else 3) + 1):
        for indices in combinations(range(m), k):
            traces = {tuple(bool(mask & (1 << i)) for i in indices)
                      for mask in neighborhoods}
            if len(traces) == (1 << k):
                assert k <= 3, ('four-shattering', n, edges, indices)
                out[k] += 1
    return tuple(out)


def run():
    count = 0
    for n in range(2, 8):
        for code in product(range(n), repeat=n-2):
            e = edges_from_prufer(code)
            p = theorem(n, e)
            q = brute(n, e)
            assert p == q, (n, e, p, q)
            count += 1
    rng = Random(20261115)
    for n in range(8, 22):
        for _ in range(50):
            e = edges_from_prufer(tuple(rng.randrange(n) for _ in range(n-2)))
            assert theorem(n, e) == brute(n, e), (n, e)
            count += 1
    n = 9
    extremal_edges = ((0, 1), (1, 5), (0, 2), (2, 6),
                      (0, 3), (3, 7), (0, 4), (4, 8))
    assert theorem(n, extremal_edges)[3] == 4
    assert brute(n, extremal_edges)[3] == 4
    print('VERIFY_OK', count, 'trees; four-support checks and nine-vertex extremizer')


if __name__ == '__main__':
    run()

"""Exact integer checks for non-backtracking spectra of tripartite edge subdivisions.

Run with python3 verify.py. No third-party packages are needed.
"""
from collections import Counter


def multiply(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                if y:
                    out[i + j] += x * y
    return out


def power(f, n):
    p = [1]
    while n:
        if n & 1:
            p = multiply(p, f)
        f = multiply(f, f)
        n //= 2
    return p


def graph(a):
    n = 3 * a
    edge_pairs = [(u, v) for u in range(n) for v in range(u + 1, n)
                  if u // a != v // a]
    assert len(edge_pairs) == 3 * a * a
    return n, edge_pairs


def charpoly_nonbacktracking(a):
    n, edges = graph(a)
    # Graph with one new vertex for every original edge.
    adj = [set() for _ in range(n + len(edges))]
    for j, (u, v) in enumerate(edges):
        w = n + j
        adj[u].add(w); adj[v].add(w)
        adj[w].add(u); adj[w].add(v)
    arcs = [(u, v) for u in range(len(adj)) for v in sorted(adj[u])]
    arc_index = {e: i for i, e in enumerate(arcs)}
    succ = [[arc_index[(v, w)] for w in adj[v] if w != u] for u, v in arcs]
    m = len(arcs)
    traces = [0] * (m + 1)
    # Exact traces: number of closed directed walks of each length.
    for origin in range(m):
        v = [0] * m; v[origin] = 1
        for k in range(1, m + 1):
            nxt = [0] * m
            for i, val in enumerate(v):
                if val:
                    for j in succ[i]:
                        nxt[j] += val
            v = nxt
            traces[k] += v[origin]
    # Newton identities for det(t I - B), descending coefficients.
    coefs = [1]
    for k in range(1, m + 1):
        total = sum(coefs[k - j] * traces[j] for j in range(1, k + 1))
        assert total % k == 0
        coefs.append(-total // k)
    return list(reversed(coefs))


def expected(a):
    h = 3 * a * (a - 1)
    d = 2 * a - 1
    f = power([-1, 0, 0, 0, 1], h)  # (t^4 - 1)^h
    for g, exponent in [([d, 0, -(d + 1), 0, 1], 1),
                        ([d, 0, 0, 0, 1], 3 * a - 3),
                        ([d, 0, a, 0, 1], 2)]:
        f = multiply(f, power(g, exponent))
    return f


def check_incidence_spectrum(a):
    n, edges = graph(a)
    CTC = [[0] * n for _ in range(n)]
    for u, v in edges:
        CTC[u][u] += 1; CTC[v][v] += 1
        CTC[u][v] += 1; CTC[v][u] += 1
    assert all(CTC[i][i] == 2 * a for i in range(n))
    assert all(CTC[i][j] == (1 if i // a != j // a else 0)
               for i in range(n) for j in range(n) if i != j)
    # Exact coefficient comparison using traces of C^T C (small matrices).
    mat = [[int(i == j) for j in range(n)] for i in range(n)]
    coeffs = [1]
    for k in range(1, n + 1):
        mat = [[sum(mat[i][h] * CTC[h][j] for h in range(n))
                for j in range(n)] for i in range(n)]
        trace = sum(mat[i][i] for i in range(n))
        # Power sums can instead be computed directly from the predicted spectrum.
        reference = (4 * a) ** k + (3 * a - 3) * (2 * a) ** k + 2 * a ** k
        assert trace == reference
    return True


def ramanujan_at_lower_edge(a):
    # sqrt(a) < sqrt(2a-1) - 1 iff a > 4 + 2 sqrt(3).
    # Integer-only check: a > 2 and (a-2)^2 > 4a.
    return a > 2 and (a - 2) ** 2 > 4 * a


def run():
    for a in range(1, 4):
        got, want = charpoly_nonbacktracking(a), expected(a)
        assert got == want, (a, len(got), len(want))
        print('EXACT_NONBACKTRACKING_CHARPOLY_OK', a, 'degree', len(got) - 1)
    for a in range(1, 12):
        check_incidence_spectrum(a)
    print('INCIDENCE_SINGULAR_SPECTRUM_OK', 'a=1..11')
    for a in range(2, 80):
        lower = (2 * a - 1) ** .5 - 1
        upper = (2 * a - 1) ** .5 + 1
        assert ((a ** .5) < lower) == ramanujan_at_lower_edge(a)
        assert (2 * a) ** .5 < upper
        assert ramanujan_at_lower_edge(a) == (a >= 8)
        N = 3 * a * a + 3 * a
        M = 6 * a * a
        h = 3 * a * (a - 1)
        assert 2 * (M - N) + 4 == 2 * h + 4
    print('SHARP_LOWER_EDGE_AND_REAL_COUNT_OK', 'a=2..79')
    print('VERIFY_OK')

if __name__ == '__main__':
    run()

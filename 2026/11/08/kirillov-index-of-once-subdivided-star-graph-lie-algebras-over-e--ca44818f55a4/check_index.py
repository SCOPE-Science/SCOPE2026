"""Exact finite-field checks for Kirillov indices of subdivided-star graph Lie algebras.

This file constructs the graph and its brackets from vertices, edges and
unoriented two-paths, rather than using the reduced block formula in the proof.
No third-party libraries are required.
"""
from itertools import combinations, product


def rank_mod(matrix, p):
    a = [[int(x) % p for x in row] for row in matrix]
    rows = len(a)
    cols = len(a[0]) if rows else 0
    r = 0
    for j in range(cols):
        pivot = next((i for i in range(r, rows) if a[i][j]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        inv = pow(a[r][j], -1, p)
        a[r] = [(v * inv) % p for v in a[r]]
        for i in range(rows):
            if i == r:
                continue
            coeff = a[i][j]
            if coeff:
                a[i] = [(a[i][k] - coeff * a[r][k]) % p for k in range(cols)]
        r += 1
        if r == rows:
            break
    return r


def graph_data(m):
    # c=0, intermediate vertices 1,...,m, leaves m+1,...,2m.
    n = 2 * m + 1
    edges = sorted([(0, 1+i) for i in range(m)] +
                   [(1+i, m+1+i) for i in range(m)])
    adj = [set() for _ in range(n)]
    for a, b in edges:
        adj[a].add(b); adj[b].add(a)
    # Basis of the center: path (middle vertex, unordered endpoints).
    paths = sorted((middle, a, b) for middle in range(n)
                   for a, b in combinations(sorted(adj[middle]), 2))
    return n, edges, adj, paths


def kirillov_matrix(m, p, edge_coeff, path_coeff):
    n, edges, adj, paths = graph_data(m)
    e_index = {e: i for i, e in enumerate(edges)}
    path_index = {key: i for i, key in enumerate(paths)}
    size = n + len(edges)
    b = [[0] * size for _ in range(size)]
    def assign(i, j, x):
        assert i != j
        b[i][j] = x % p
        b[j][i] = -x % p
    # Bracket of two vertices is an edge basis vector.
    for i, (a, c) in enumerate(edges):
        assign(a, c, edge_coeff[i])
    # For a third vertex t and edge e=(a,c), [t,e] has sign + if
    # t-a-c is a 2-path, sign - if a-c-t is a 2-path.
    for i, (a, c) in enumerate(edges):
        for t in range(n):
            if t == a or t == c:
                continue
            if t in adj[a]:
                key = (a, *sorted((t, c)))
                assign(t, n+i, path_coeff[path_index[key]])
            elif t in adj[c]:
                key = (c, *sorted((t, a)))
                assign(t, n+i, -path_coeff[path_index[key]])
    return b


def witness(m):
    n, edges, adj, paths = graph_data(m)
    a = [0] * len(edges)
    for i in range(1, m, 2):
        a[edges.index((1+i, m+1+i))] = 1
    z = [0] * len(paths)
    for k, (mid, low, high) in enumerate(paths):
        if mid == 0:
            if low >= 1 and high == low + 1 and (low - 1) % 2 == 0:
                z[k] = 1
        else:
            # c--u_i--v_i, one for each arm.
            if low == 0:
                z[k] = 1
    assert sum(z) == m + m // 2
    return a, z


def predicted(m):
    central_dim = m*(m+1)//2
    maximum_rank = 2*(m+1)+2*(m//2)
    index = (4*m + 1 + central_dim) - maximum_rank
    return central_dim, maximum_rank, index


def check():
    cases = 0
    for p in (2, 3, 5, 7):
        for m in range(1, 11):
            a, z = witness(m)
            b = kirillov_matrix(m, p, a, z)
            c, r, index = predicted(m)
            assert len(b) == 4*m+1
            assert rank_mod(b, p) == r, (p, m)
            assert index == c + 2*((m+1)//2)-1
            assert r % 2 == 0
            cases += 1
    # Exhaustively enumerate all coefficient functionals for the first
    # nontrivial field, where this is computationally feasible.
    total = 0
    for m in (1, 2, 3):
        n, edges, adj, paths = graph_data(m)
        top = predicted(m)[1]
        observed = 0
        for coefficients in product((0, 1), repeat=len(edges)+len(paths)):
            a = coefficients[:len(edges)]; z = coefficients[len(edges):]
            observed = max(observed, rank_mod(kirillov_matrix(m, 2, a, z), 2))
            total += 1
        assert observed == top, (m, observed, top)
    print('VERIFY_OK witness_cases=%s exhaustive_binary_functionals=%s'
          ' m_range=1..10 prime_fields=2,3,5,7' % (cases, total))


if __name__ == '__main__':
    check()

"""Independent exact checks for sharp tree-Poisson Lipschitz bounds.
Run with: python check_tree_poisson.py
Only Python's standard library is required.
"""
from fractions import Fraction
from itertools import product
from collections import deque
import random


def tree_from_prufer(seq, n):
    deg = [1] * n
    for v in seq:
        deg[v] += 1
    edges = []
    for v in seq:
        u = next(i for i in range(n) if deg[i] == 1)
        edges.append((u, v))
        deg[u] -= 1
        deg[v] -= 1
    u, v = [i for i in range(n) if deg[i] == 1]
    return edges + [(u, v)]


def graph_data(n, edges):
    adj = [[] for _ in range(n)]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    parent = [-1] * n
    order = [0]
    parent[0] = 0
    for v in order:
        for w in adj[v]:
            if w != parent[v]:
                assert parent[w] < 0
                parent[w] = v
                order.append(w)
    assert len(order) == n
    sizes = [1] * n
    for v in reversed(order[1:]):
        sizes[parent[v]] += sizes[v]
    return adj, parent, order, sizes


def inverse_exact(matrix):
    n = len(matrix)
    a = [[Fraction(x) for x in row] + [Fraction(int(i == j)) for j in range(n)] for i, row in enumerate(matrix)]
    for col in range(n):
        pivot = next(i for i in range(col, n) if a[i][col])
        a[col], a[pivot] = a[pivot], a[col]
        k = a[col][col]
        a[col] = [v/k for v in a[col]]
        for i in range(n):
            if i != col and a[i][col]:
                k = a[i][col]
                a[i] = [v-k*w for v, w in zip(a[i], a[col])]
    return [row[n:] for row in a]


def independently_solve_poisson_norm(n, edges):
    adj, parent, order, sizes = graph_data(n, edges)
    # Invert L+J/n, then subtract J/n to get L^+ on zero-mean vectors.
    M = [[Fraction((len(adj[i]) if i == j else (-1 if j in adj[i] else 0))) + Fraction(1, n)
          for j in range(n)] for i in range(n)]
    Minv = inverse_exact(M)
    Lplus = [[Minv[i][j]-Fraction(1, n) for j in range(n)] for i in range(n)]
    descendant = {}
    for v in order[1:]:
        seen = {v}
        queue = [v]
        for u in queue:
            for w in adj[u]:
                if w != parent[u] and w not in seen:
                    seen.add(w)
                    queue.append(w)
        descendant[v] = seen
    # The edge increments of each subtree indicator form the canonical cube basis.
    rows = []
    for v in order[1:]:
        row = []
        for w in order[1:]:
            S = descendant[w]
            val = sum(Lplus[v][j]-Lplus[parent[v]][j] for j in S)
            row.append(val)
        rows.append(row)
    return max(sum(abs(x) for x in row) for row in rows), rows, descendant, parent, order


def independent_cross_distance(n, edges):
    adj, parent, order, sizes = graph_data(n, edges)
    dist = [[0] * n for _ in range(n)]
    for i in range(n):
        distance = [-1] * n
        distance[i] = 0
        queue = [i]
        for u in queue:
            for v in adj[u]:
                if distance[v] < 0:
                    distance[v] = distance[u]+1
                    queue.append(v)
        dist[i] = distance
    candidates = []
    for u, v in edges:
        S = {u}
        queue = [u]
        for x in queue:
            for y in adj[x]:
                if (x == u and y == v) or (x == v and y == u):
                    continue
                if y not in S:
                    S.add(y)
                    queue.append(y)
        rest = set(range(n)) - S
        score = Fraction(sum(dist[x][y] for x in S for y in rest), n)
        candidates.append(score)
    return max(candidates), candidates


def test_tree(n, edges, check_vertex_extremes=False):
    K1, rows, cuts, parent, order = independently_solve_poisson_norm(n, edges)
    K2, by_edge = independent_cross_distance(n, edges)
    assert K1 == K2, (n, edges, K1, K2)
    lower = Fraction(2*n-3, n)
    upper = Fraction((n*n)//4, 2)
    assert lower <= K1 <= upper, (n, edges, K1, lower, upper)
    # Realize each output row's entire absolute sum by choosing the cube signs.
    for row in rows:
        signs = [1 if v > 0 else -1 for v in row]
        result = abs(sum(c*s for c, s in zip(row, signs)))
        assert result == sum(abs(c) for c in row)
    if check_vertex_extremes:
        values = []
        for signs in product((-1, 1), repeat=n-1):
            vals = [sum(row[j]*signs[j] for j in range(n-1)) for row in rows]
            values.append(max(map(abs, vals)))
        assert max(values) == K1
    return K1


def test_exact_cases():
    cases = 0
    for n in range(2, 7):
        for seq in product(range(n), repeat=n-2):
            e = tree_from_prufer(seq, n)
            got = test_tree(n, e, check_vertex_extremes=(n <= 5))
            if n >= 4:
                degrees = [0]*n
                for u, v in e:
                    degrees[u] += 1
                    degrees[v] += 1
                if got == Fraction(2*n-3, n):
                    assert max(degrees) == n-1
                if got == Fraction((n*n)//4, 2):
                    assert max(degrees) <= 2
            cases += 1
    print('EXACT_PSEUDOINVERSE_VS_CROSS_CUT_DISTANCE_PASSED', cases)
    rng = random.Random(9037)
    more = 0
    for n in (7, 8, 10):
        for _ in range(40):
            seq = [rng.randrange(n) for _ in range(n-2)]
            test_tree(n, tree_from_prufer(seq, n))
            more += 1
    print('ADDITIONAL_EXACT_RANDOM_TREES_PASSED', more)
    for n in range(2, 16):
        star = [(0, i) for i in range(1, n)]
        path = [(i, i+1) for i in range(n-1)]
        ks = independent_cross_distance(n, star)[0]
        kp = independent_cross_distance(n, path)[0]
        assert ks == Fraction(2*n-3, n)
        assert kp == Fraction((n*n)//4, 2)
    print('SHARP_STAR_AND_PATH_ENDPOINTS_PASSED', 14)
    print('ALL_TREE_POISSON_CHECKS_PASSED')


if __name__ == '__main__':
    test_exact_cases()

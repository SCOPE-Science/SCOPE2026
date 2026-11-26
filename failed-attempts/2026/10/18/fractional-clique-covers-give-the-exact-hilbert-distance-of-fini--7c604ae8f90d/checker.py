"""Exact finite illustrative checks for clique-family Hilbert distortion.

Standard-library-only code. This enumerates LP vertices over rational arithmetic;
finite instances illustrate rather than prove the general theorem.
"""
from fractions import Fraction as Q
from itertools import combinations


def gaussian(rows, rhs):
    n = len(rhs)
    a = [[Q(x) for x in row] + [Q(y)] for row, y in zip(rows, rhs)]
    for c in range(n):
        k = next((r for r in range(c, n) if a[r][c]), None)
        if k is None:
            return None
        a[k], a[c] = a[c], a[k]
        d = a[c][c]
        a[c] = [z / d for z in a[c]]
        for r in range(n):
            if r != c:
                t = a[r][c]
                if t:
                    a[r] = [u - t * v for u, v in zip(a[r], a[c])]
    return [a[r][-1] for r in range(n)]


def maximal_cliques(n, edges):
    e = {frozenset(x) for x in edges}
    cliques = []
    for k in range(1, n + 1):
        for c in combinations(range(n), k):
            if all(frozenset(ab) in e for ab in combinations(c, 2)):
                cliques.append(frozenset(c))
    return [c for c in cliques if not any(c < d for d in cliques)]


def vertex_extremum(A, b, direction):
    """Extremize sum(x_i) subject to Ax<=b over the nonnegative orthant.

    Input includes nonnegativity constraints explicitly. Finite polytopes only.
    """
    n = len(A[0]); best = None; best_x = None
    for chosen in combinations(range(len(A)), n):
        x = gaussian([A[j] for j in chosen], [b[j] for j in chosen])
        if x is None or any(sum(Q(a) * z for a, z in zip(row, x)) > limit for row, limit in zip(A, b)):
            continue
        score = sum(x)
        if best is None or (score > best if direction == 'max' else score < best):
            best, best_x = score, x
    assert best is not None
    return best, best_x


def optimize_primal_dual(n, edges):
    cliques = maximal_cliques(n, edges)
    inc = [[int(i in C) for i in range(n)] for C in cliques]
    nonneg = [[-int(i == j) for i in range(n)] for j in range(n)]
    p, xp = vertex_extremum(inc + nonneg, [1] * len(inc) + [0] * n, 'max')
    m = len(cliques)
    cover = [[-int(i in C) for C in cliques] for i in range(n)]
    nonneg_dual = [[-int(i == j) for i in range(m)] for j in range(m)]
    d, xd = vertex_extremum(cover + nonneg_dual, [-1] * n + [0] * m, 'min')
    assert p == d, (n, edges, p, d)
    return p, cliques, xp, xd


def check_certificate(n, edges, y, lam):
    cs = maximal_cliques(n, edges)
    assert len(y) == n and len(lam) == len(cs)
    assert all(v >= 0 for v in y) and all(v >= 0 for v in lam)
    assert all(sum(y[i] for i in c) <= 1 for c in cs)
    assert all(sum(lam[j] for j, c in enumerate(cs) if i in c) >= 1 for i in range(n))
    assert sum(y) == sum(lam)
    return sum(y)


def cycle(n):
    return [tuple(sorted((i, (i + 1) % n))) for i in range(n)]


def complement(n, edges):
    s = {frozenset(e) for e in edges}
    return [e for e in combinations(range(n), 2) if frozenset(e) not in s]


def run():
    graph_count = 0
    for mask in range(1 << 6):
        edges = [e for i, e in enumerate(combinations(range(4), 2)) if mask & (1 << i)]
        optimize_primal_dual(4, edges)
        graph_count += 1
    examples = [
        ('C5', 5, cycle(5), Q(5, 2)),
        ('C6', 6, cycle(6), Q(3)),
        ('C7', 7, cycle(7), Q(7, 2)),
        ('complement-C7', 7, complement(7, cycle(7)), Q(7, 3)),
        ('K4', 4, list(combinations(range(4), 2)), Q(1)),
        ('E4', 4, [], Q(4)),
        ('P4', 4, [(0, 1), (1, 2), (2, 3)], Q(2)),
    ]
    for name, n, edges, expected in examples:
        cliques = maximal_cliques(n, edges)
        if name in ('C5', 'C7'):
            y = [Q(1, 2)] * n
            lam = [Q(1, 2)] * len(cliques)
        elif name == 'complement-C7':
            assert len(cliques) == 7 and all(len(C) == 3 for C in cliques)
            y = [Q(1, 3)] * n
            lam = [Q(1, 3)] * len(cliques)
        elif name == 'C6':
            y = [Q(i % 2 == 0) for i in range(n)]
            lam = [Q(1) if c in (frozenset({0, 1}), frozenset({2, 3}), frozenset({4, 5})) else Q(0) for c in cliques]
        elif name == 'K4':
            y = [Q(1, 4)] * n
            lam = [Q(1)]
        elif name == 'E4':
            y = [Q(1)] * n
            lam = [Q(1)] * n
        else:
            y = [Q(1), Q(0), Q(1), Q(0)]
            lam = [Q(1) if c in (frozenset({0, 1}), frozenset({2, 3})) else Q(0) for c in cliques]
        value = check_certificate(n, edges, y, lam)
        assert value == expected
        if n <= 5:
            computed = optimize_primal_dual(n, edges)[0]
            assert computed == value
        print(name, 'squared_hilbert_distance=', value)
    print('all_4_vertex_graphs_exact_primal_dual=', graph_count)
    print('exact_named_certificates=', len(examples))


if __name__ == '__main__':
    run()

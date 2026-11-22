"""Standalone direct normalized quandle 2-cohomology verification for graph quandles.

Run: python3 verify_graph_quandle_h2.py
Uses Python standard library only, independently constructs and row-reduces the
complete binary cocycle and coboundary matrices; does not use theorem equations.
"""
from itertools import combinations


def bitrank(rows):
    pivots = {}
    for row in rows:
        while row:
            high = row.bit_length() - 1
            if high in pivots:
                row ^= pivots[high]
            else:
                pivots[high] = row
                break
    return len(pivots)


def adjacency(n, edges):
    a = [[0] * n for _ in range(n)]
    for i, j in edges:
        assert 0 <= i < j < n
        a[i][j] = a[j][i] = 1
    return a


def connected(a):
    seen = {0}
    stack = [0]
    while stack:
        i = stack.pop()
        for j, e in enumerate(a[i]):
            if e and j not in seen:
                seen.add(j)
                stack.append(j)
    return len(seen) == len(a)


def predicted_h2(a):
    n = len(a)
    return n * (n - 1) + n * (bitrank([sum(a[i][j] << j for j in range(n)) for i in range(n)]) == 2)


def direct_h2(a):
    n = len(a)
    size = 2 * n
    def act(x, y):
        return 2 * (x // 2) + ((x & 1) ^ a[x // 2][y // 2])
    admissible = [(x, y) for x in range(size) for y in range(size) if x != y]
    idx = {p: k for k, p in enumerate(admissible)}
    def equation(*pairs):
        bits = 0
        for pair in pairs:
            if pair in idx:
                bits ^= 1 << idx[pair]
        return bits
    equations = (equation((x, y), (act(x, y), z), (x, z),
                          (act(x, z), act(y, z)))
                 for x in range(size) for y in range(size) for z in range(size))
    rank_cocycle_equations = bitrank(equations)
    coboundaries = []
    for w in range(size):
        row = 0
        for pair, k in idx.items():
            x, y = pair
            if (x == w) != (act(x, y) == w):
                row ^= 1 << k
        coboundaries.append(row)
    return len(admissible) - rank_cocycle_equations - bitrank(coboundaries)


def graph_classes(n, parts):
    assert sum(parts) == n
    colors = [i for i, s in enumerate(parts) for _ in range(s)]
    return [(i, j) for i in range(n) for j in range(i + 1, n)
            if colors[i] != colors[j]]


def verify():
    examined = 0
    by_rank = {}
    for n in range(2, 5):
        all_edges = list(combinations(range(n), 2))
        for mask in range(1 << len(all_edges)):
            edges = [e for k, e in enumerate(all_edges) if mask >> k & 1]
            a = adjacency(n, edges)
            if not connected(a):
                continue
            got = direct_h2(a)
            want = predicted_h2(a)
            assert got == want, (n, edges, got, want)
            rank = bitrank([sum(a[i][j] << j for j in range(n)) for i in range(n)])
            by_rank[(n, rank)] = by_rank.get((n, rank), 0) + 1
            examined += 1
    for n in range(5, 8):
        cases = [list(combinations(range(n), 2)),
                 [(i, i + 1) for i in range(n - 1)],
                 graph_classes(n, [1, n - 1]),
                 graph_classes(n, [2, n - 2]),
                 graph_classes(n, [1, 1, n - 2])]
        if n >= 6:
            cases.append([(i, (i + 1) % n) if i < (i + 1) % n else ((i + 1) % n, i) for i in range(n)])
        for edges in cases:
            a = adjacency(n, edges)
            got = direct_h2(a)
            want = predicted_h2(a)
            assert got == want, (n, edges, got, want)
            examined += 1
    assert by_rank[(4, 2)] == 13 and by_rank[(4, 4)] == 25
    print('CONNECTED_LABELLED_COUNTS_N4', by_rank)
    print('DIRECT_COCHAIN_SYSTEMS_VERIFIED', examined)
    print('GRAPH_QUANDLE_BINARY_H2_VERIFIED')

if __name__ == '__main__':
    verify()

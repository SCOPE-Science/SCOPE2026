"""Finite exact checks for the four-symbol three-survivor multiset-code profile.

Run with Python 3.9 or later: python check.py
This script uses only the standard library.
"""
from itertools import combinations


def compositions(n, q=4):
    if q == 1:
        yield (n,)
        return
    for x in range(n + 1):
        for tail in compositions(n - x, q - 1):
            yield (x,) + tail


def overlap(x, y):
    return sum(min(a, b) for a, b in zip(x, y))


def witnesses(n):
    pure = [tuple(n if j == i else 0 for j in range(4)) for i in range(4)]
    extras = {
        5: [(2, 2, 1, 0), (0, 1, 2, 2)],
        6: [(2, 2, 1, 1)],
        7: [(2, 2, 2, 1)],
        8: [(2, 2, 2, 2)],
        9: [],
    }
    return pure + extras[n]


def adjacency(n):
    words = list(compositions(n))
    adj = [0] * len(words)
    for i in range(len(words)):
        for j in range(i):
            if overlap(words[i], words[j]) <= 2:
                adj[i] |= 1 << j
                adj[j] |= 1 << i
    return words, adj


def has_clique_of_size(adj, goal):
    """Exact branch-and-bound, no external solver, floating point, or sampling.

    The graph uses compatibility edges, so its cliques are deletion codes.
    Greedy coloring gives a valid upper bound on each remaining induced subgraph.
    """
    calls = 0

    def sorted_coloring(vertices):
        order, colors, color = [], [], 0
        while vertices:
            color += 1
            pool = vertices
            while pool:
                i = (pool & -pool).bit_length() - 1
                bit = 1 << i
                pool &= ~bit
                vertices &= ~bit
                order.append(i)
                colors.append(color)
                pool &= ~adj[i]
        return order, colors

    def visit(available, depth):
        nonlocal calls
        calls += 1
        if depth >= goal:
            return True
        if not available:
            return False
        order, colors = sorted_coloring(available)
        for k in range(len(order) - 1, -1, -1):
            if depth + colors[k] < goal:
                return False
            v = order[k]
            if visit(available & adj[v], depth + 1):
                return True
            available &= ~(1 << v)
        return False

    result = visit((1 << len(adj)) - 1, 0)
    return result, calls


def verify():
    target = {5: 6, 6: 5, 7: 5, 8: 5, 9: 4}
    for n in range(5, 10):
        ws = witnesses(n)
        assert len(ws) == target[n]
        assert all(len(w) == 4 and sum(w) == n and min(w) >= 0 for w in ws)
        assert len(set(ws)) == len(ws)
        for u, v in combinations(ws, 2):
            assert overlap(u, v) <= 2
        words, adj = adjacency(n)
        assert len(words) == (n + 3) * (n + 2) * (n + 1) // 6
        found, nodes = has_clique_of_size(adj, target[n] + 1)
        assert not found
        print(f"n={n} compositions={len(words)} optimum={target[n]} "
              f"witnesses={len(ws)} upper_search_nodes={nodes} verified=True")
    print("PASS: all claimed finite cases; independent infinite-range proof is in RESULT.md")


if __name__ == '__main__':
    verify()

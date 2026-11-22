"""Exact finite checks for the cut-first spanning-tree edge-exchange law.

Uses only the Python standard library. Run: python verify.py
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations


def host_edges(a, b):
    return tuple((i, a + j) for i in range(a) for j in range(b))


def enumerate_trees(a, b):
    n = a + b
    edges = host_edges(a, b)
    for chosen in combinations(edges, n - 1):
        adj = [[] for _ in range(n)]
        for u, v in chosen:
            adj[u].append(v)
            adj[v].append(u)
        found = {0}
        stack = [0]
        while stack:
            x = stack.pop()
            for y in adj[x]:
                if y not in found:
                    found.add(y)
                    stack.append(y)
        if len(found) == n:
            yield frozenset(chosen)


def cuts(a, b, tree):
    n = a + b
    host = host_edges(a, b)
    adj = [[] for _ in range(n)]
    for u, v in tree:
        adj[u].append(v)
        adj[v].append(u)
    for u, v in tree:
        seen = {u}
        stack = [u]
        while stack:
            x = stack.pop()
            for y in adj[x]:
                if (x == u and y == v) or (x == v and y == u):
                    continue
                if y not in seen:
                    seen.add(y)
                    stack.append(y)
        cross = tuple(e for e in host if (e[0] in seen) != (e[1] in seen))
        assert (u, v) in cross
        yield (u, v), cross


def holding(a, b, tree):
    return sum((Fraction(1, len(cross)) for _, cross in cuts(a, b, tree)), Fraction(0)) / (a + b - 1)


def q_two(b):
    return Fraction(b * b - b + 4, 2 * b * (b + 1))


def double_star(a, b):
    # A0 joins all B; B0 joins every other A.
    return frozenset([(0, a + j) for j in range(b)] + [(i, a) for i in range(1, a)])


def zigzag(a, b):
    # A0-B0-A1-B1, other B leaves at A0 and other A leaves at B1.
    return frozenset([(0, a), (1, a), (1, a + 1)]
                     + [(0, a + j) for j in range(2, b)]
                     + [(i, a + 1) for i in range(2, a)])


def run():
    tests = 0
    for b in range(1, 7):
        for tree in enumerate_trees(2, b):
            assert holding(2, b, tree) == q_two(b)
            tests += 1
            label_counts = Counter(("leaf" if len(cross) == 2 else "bridge", len(cross))
                                   for _, cross in cuts(2, b, tree))
            # At b=2 leaf and bridge cross sizes coincide; use degree labels instead.
            if b > 2:
                assert label_counts[("leaf", 2)] == b - 1
                assert label_counts[("bridge", b)] == 2
                tests += 2
    for a, b in [(3, 3), (3, 4), (4, 4)]:
        d = (a - 2) * (b - 2)
        star = holding(a, b, double_star(a, b))
        zig = holding(a, b, zigzag(a, b))
        assert star - zig == (Fraction(1, a) + Fraction(1, b)
                               - Fraction(1, a + d) - Fraction(1, b + d)) / (a + b - 1)
        assert star > zig
        tests += 2
    for b in range(1, 80):
        assert q_two(b + 1) - q_two(b) == Fraction(b - 4, b * (b + 1) * (b + 2))
        tests += 1
    assert q_two(4) == q_two(5) == Fraction(2, 5)
    tests += 1
    all_three = list(enumerate_trees(3, 3))
    assert len(all_three) == 81
    counts = Counter(holding(3, 3, t) for t in all_three)
    assert counts == {Fraction(41, 150): 36, Fraction(3, 10): 36, Fraction(23, 75): 9}
    mean = sum((h * v for h, v in counts.items()), Fraction(0)) / 81
    var = sum(((h - mean) ** 2 * v for h, v in counts.items()), Fraction(0)) / 81
    assert mean == Fraction(13, 45)
    assert var == Fraction(2, 10125)
    tests += 4
    # Reversibility: every ordered tree pair has symmetric transition probability.
    for a, b in [(2, 3), (3, 3)]:
        kernels = {}
        for tree in enumerate_trees(a, b):
            row = Counter()
            for old, cross in cuts(a, b, tree):
                for new in cross:
                    nxt = frozenset((tree - {old}) | {new})
                    row[nxt] += Fraction(1, (a + b - 1) * len(cross))
            assert sum(row.values()) == 1
            kernels[tree] = row
            tests += 1
        for tree, row in kernels.items():
            for nxt, p in row.items():
                assert kernels[nxt][tree] == p
                tests += 1
    print("PASS", tests, "exact assertions; K(3,3) holding variance", var)


if __name__ == "__main__":
    run()

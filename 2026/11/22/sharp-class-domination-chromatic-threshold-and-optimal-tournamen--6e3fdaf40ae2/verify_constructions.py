"""Standalone edge-level CD-colouring verification for two-subset Kneser graphs.

Run: python3 verify_constructions.py
No third-party modules required.
"""
from itertools import combinations
from math import comb


def orient_balanced(c):
    """A tournament on c vertices with maximum outdegree ceil((c-1)/2)."""
    arcs = []
    for a, b in combinations(range(c), 2):
        delta = b - a
        if delta < c / 2 or (delta == c / 2 and a < b):
            arcs.append((a, b))
        else:
            arcs.append((b, a))
    return arcs


def construct(n):
    if n == 5:
        return [
            [(0, 1), (0, 2), (1, 2)],
            [(0, 3), (0, 4), (3, 4)],
            [(1, 3), (2, 3)],
            [(1, 4), (2, 4)],
        ]
    if n == 6:
        return [
            [(0, 1), (0, 2), (0, 3)],
            [(0, 4), (0, 5), (4, 5)],
            [(1, 4), (2, 4), (3, 4)],
            [(1, 2), (1, 3), (2, 3)],
            [(1, 5), (2, 5), (3, 5)],
        ]
    if n == 7:
        c, outside = 5, [5, 6]
    elif n >= 8:
        c, outside = n - 3, [n - 3, n - 2, n - 1]
    else:
        raise ValueError("Requires n >= 5")
    classes = [[(v, x) for x in outside] for v in range(c)]
    for v, w in orient_balanced(c):
        classes[v].append((v, w))
    classes.append(list(combinations(outside, 2)))
    return classes


def check(n, classes):
    V = {frozenset(e) for e in combinations(range(n), 2)}
    used = set()
    assert len(classes) == (n - 1 if n <= 7 else n - 2)
    for C in classes:
        # Every colour class must be independent in KG(n,2).
        assert C
        edges = [frozenset(e) for e in C]
        assert all(e & f for e, f in combinations(edges, 2))
        assert all(e not in used for e in edges)
        used.update(edges)
        # Direct witness test: a KG vertex adjacent to each class member.
        assert any(all(not (w & e) for e in edges) for w in V)
    assert used == V
    return tuple(len(C) for C in classes)


def main():
    for n in range(5, 101):
        lengths = check(n, construct(n))
        if n <= 11:
            print(n, len(lengths), lengths)
    print("CONSTRUCTIONS_OK")


if __name__ == "__main__":
    main()

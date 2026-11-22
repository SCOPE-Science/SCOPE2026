#!/usr/bin/env python3
"""Independent finite recursion checks for extension ranks of partial matchings.

All rank calls enumerate the permitted one-point graph extensions over the
actual marked vertices and compare all possible realizations in the host.
The conjectured closed formula is used only for subsequent assertions.
"""
from collections import Counter
from functools import lru_cache
from math import factorial


def game_rank(mate):
    n = len(mate)

    @lru_cache(None)
    def rank(mask):
        marked = [u for u in range(n) if mask & (1 << u)]
        unused = [v for v in range(n) if not mask & (1 << v)]
        patterns = [None]  # a newly introduced vertex has no marked neighbour
        patterns += [u for u in marked if mate[u] is None or
                     not mask & (1 << mate[u])]
        best = []
        for pattern in patterns:
            successors = []
            for v in unused:
                adjacent_mark = next((u for u in marked if mate[v] == u), None)
                if adjacent_mark == pattern:
                    successors.append(rank(mask | (1 << v)))
            if not successors:
                return 0
            best.append(max(successors))
        return 1 + min(best)

    return rank


def formula(mate, mask):
    n = len(mate)
    if any((mask & (1 << u)) and mate[u] is None for u in range(n)):
        return 0
    c = sum(u < mate[u] and not (mask & (1 << u)) and
            not (mask & (1 << mate[u]))
            for u in range(n) if mate[u] is not None)
    d = sum(mate[v] is None and not (mask & (1 << v)) for v in range(n))
    return c + int(d > 0)


def canonical(n, edges):
    mate = [None] * n
    for i in range(edges):
        a, b = 2 * i, 2 * i + 1
        mate[a] = b
        mate[b] = a
    return tuple(mate)


def all_matchings(vertices):
    """All labelled partial matchings, each exactly once."""
    if not vertices:
        yield ()
        return
    first = vertices[0]
    tail = vertices[1:]
    for edges in all_matchings(tail):
        yield edges
    for j, other in enumerate(tail):
        remain = tail[:j] + tail[j + 1:]
        for edges in all_matchings(remain):
            yield ((first, other),) + edges


def main():
    tested = 0
    for n in range(13):
        for edges in range(n // 2 + 1):
            mate = canonical(n, edges)
            rank = game_rank(mate)
            for mask in range(1 << n):
                assert rank(mask) == formula(mate, mask), (n, edges, mask)
                tested += 1

    classified = 0
    for n in range(10):
        observed = Counter()
        for edges in all_matchings(tuple(range(n))):
            mate = [None] * n
            for a, b in edges:
                mate[a] = b
                mate[b] = a
            observed[game_rank(tuple(mate))(0)] += 1
        expected = Counter()
        for p in range(n // 2 + 1):
            d = n - 2 * p
            expected[p + int(d > 0)] += factorial(n) // (2 ** p * factorial(p) * factorial(d))
        assert observed == expected, (n, observed, expected)
        classified += sum(observed.values())

    # The smallest positive-rank hosts have one isolated vertex and r-1 edges.
    for r in range(1, 15):
        assert formula(canonical(2 * r - 1, r - 1), 0) == r
        assert formula(canonical(2 * r - 2, r - 1), 0) == r - 1
    print(f"ALL_CHECKS_OK positions={tested} labelled_hosts={classified} max_n=12")


if __name__ == '__main__':
    main()

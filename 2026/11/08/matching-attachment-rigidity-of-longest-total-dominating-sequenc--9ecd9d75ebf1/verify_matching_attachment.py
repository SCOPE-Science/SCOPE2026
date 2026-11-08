#!/usr/bin/env python3
"""Independent explicit enumeration of matching-attachment sequences for odd orders."""
from itertools import combinations, permutations
from math import factorial


def matchings(vertices):
    vertices = tuple(vertices)
    if not vertices:
        yield ()
        return
    first = vertices[0]
    for i in range(1, len(vertices)):
        other = vertices[i]
        rest = vertices[1:i] + vertices[i + 1:]
        for tail in matchings(rest):
            yield ((first, other),) + tail


def constructed_sequences(n):
    assert n % 2 == 1 and n >= 3
    for root in range(n):
        others = [x for x in range(n) if x != root]
        for matched in matchings(others):
            for first_half in permutations(matched):
                for attachment_order in permutations(matched):
                    def finish(prefix, active, j):
                        if j == len(attachment_order):
                            yield prefix
                            return
                        pair = attachment_order[j]
                        for u in active:
                            for v in pair:
                                yield from finish(prefix + ((u, v),), active + pair, j + 1)
                    yield from finish(first_half, (root,), 0)


def check(n):
    edges = list(combinations(range(n), 2))
    E = {frozenset(e): i for i, e in enumerate(edges)}
    neighbors = {}
    for e in edges:
        neighbors[frozenset(e)] = frozenset(
            f for f in E if f != frozenset(e) and f.intersection(e)
        )
    seen = set()
    for seq in constructed_sequences(n):
        key = tuple(E[frozenset(e)] for e in seq)
        assert key not in seen, 'duplicate constructed sequence'
        seen.add(key)
        covered = set()
        for e in seq:
            N = neighbors[frozenset(e)]
            assert N - covered, (n, seq, e)
            covered.update(N)
        assert len(covered) == len(E), (n, seq, len(covered))
        assert len(seq) == n-1
    expected = factorial(n) * factorial(n - 1) // (2 ** ((n - 1) // 2))
    assert len(seen) == expected, (n, len(seen), expected)
    print(f'n={n}; matching-attachment sequences={len(seen)}; distinct/legal/total-dominating=PASS')


def main():
    for n in (3, 5, 7):
        check(n)
    print('PASS: independent matching-attachment generator')


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""Independent finite checks for exact three-spike incidence-cycle rank.

Uses union-find directly on the original bipartite incidence graph, with no
use of the cycle-rank proof's matching contraction or modular permutation.
Not an infinite proof.
"""
from math import gcd
from random import Random


def incidence_rank(support):
    """Return (first Betti number, components including isolated core vertices)."""
    n = max(support)
    size = 2 * (n + 1)
    parent = list(range(size))
    rank = [0] * size
    components = size
    edges = 0

    def find(v):
        while parent[v] != v:
            parent[v] = parent[parent[v]]
            v = parent[v]
        return v

    for value in sorted(support):
        for left in range(value + 1):
            right = size // 2 + value - left
            edges += 1
            x, y = find(left), find(right)
            if x != y:
                if rank[x] < rank[y]:
                    x, y = y, x
                parent[y] = x
                if rank[x] == rank[y]:
                    rank[x] += 1
                components -= 1
    return edges - size + components, components


def main():
    count = 0
    forests = 0
    for a in range(22):
        for u in range(1, 26):
            for v in range(1, 26):
                b, c = a + u, a + u + v
                actual, _ = incidence_rank((a, b, c))
                expected = max(0, a - v + gcd(u, v) + 1)
                assert actual == expected, (a, b, c, actual, expected)
                if expected == 0:
                    forests += 1
                    # One newly introduced sum greater than twice the current
                    # maximum only attaches leaves or isolated edges.
                    future, _ = incidence_rank((a, b, c, 2*c+1))
                    assert future == 0, (a,b,c,'extension')
                count += 1
    rng = Random(739105)
    more = 0
    for _ in range(1000):
        a = rng.randrange(0, 150)
        u = rng.randrange(1, 200)
        v = rng.randrange(1, 200)
        actual, _ = incidence_rank((a, a+u, a+u+v))
        expected = max(0, a-v+gcd(u,v)+1)
        assert actual == expected
        more += 1
    print(f'CHECKS_OK triples={count}; forests_extended={forests}; larger_random={more}')


if __name__ == '__main__':
    main()

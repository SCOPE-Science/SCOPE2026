#!/usr/bin/env python3
"""Exact graph-parameter and four-clique checks for the two graph models."""
from collections import Counter
from itertools import combinations, product


def neighbors(kind):
    out = []
    for a, b in product(range(4), repeat=2):
        if kind == 'rook':
            hood = {(u, v) for u, v in product(range(4), repeat=2)
                    if (u, v) != (a, b) and (u == a or v == b)}
        else:
            hood = {((a + u) % 4, (b + v) % 4)
                    for u, v in ((1, 0), (0, 1), (1, 1), (-1, 0), (0, -1), (-1, -1))}
        out.append({4 * u + v for u, v in hood})
    return out


def check(kind):
    hood = neighbors(kind)
    assert all(len(n) == 6 for n in hood)
    assert all((j in hood[i]) == (i in hood[j]) for i in range(16) for j in range(16))
    # This is A**2 = 4 I + 2 J, hence spectrum 6, 2^6, (-2)^9.
    for i in range(16):
        for j in range(16):
            assert len(hood[i] & hood[j]) == (6 if i == j else 2)
    fourcliques = [vertices for vertices in combinations(range(16), 4)
                   if all(j in hood[i] for i, j in combinations(vertices, 2))]
    # One occupied clique must see 3 occupied neighbors at every + site,
    # and every vacant site must see at most 3 occupied neighbors.
    stable4 = []
    for vertices in combinations(range(16), 4):
        ones = set(vertices)
        if all(len(hood[i] & ones) >= 3 for i in ones) and all(
                len(hood[i] & ones) <= 3 for i in set(range(16)) - ones):
            stable4.append(vertices)
    assert len(stable4) == (8 if kind == 'rook' else 0)
    assert stable4 == fourcliques
    print(kind, 'degrees=6', 'A2=4I+2J', '4-cliques', len(fourcliques),
          'fixed configurations with four + sites', len(stable4))


if __name__ == '__main__':
    check('rook')
    check('shrikhande')
    print('STRUCTURE_OK')

#!/usr/bin/env python3
"""Direct adjacency-based check for zero forcing in bicliques with a deleted matching."""
from math import comb


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def predicted(a, b, t):
    n = a + b
    a2 = choose(a, 2) - choose(a - t, 2)
    b2 = choose(b, 2) - choose(b - t, 2)
    c = a2 * b2 - t * (a - t) * (b - t) - choose(t, 2)
    result = {n: 1, n - 1: n, n - 2: a * b + a2 + b2,
              n - 3: a * b2 + b * a2, n - 4: c}
    return {k: v for k, v in result.items() if v}


def adjacency(a, b, t):
    n = a + b
    neighbors = []
    for x in range(n):
        if x < a:
            neighbors.append(sum(1 << (a + j) for j in range(b)
                                 if x >= t or x != j))
        else:
            j = x - a
            neighbors.append(sum(1 << i for i in range(a)
                                 if j >= t or j != i))
    return neighbors


def forcing(black, neighbors):
    n = len(neighbors)
    colored = black
    target = (1 << n) - 1
    while True:
        moves = 0
        for x in range(n):
            if (colored >> x) & 1:
                whites = neighbors[x] & ~colored
                if whites and not (whites & (whites - 1)):
                    moves |= whites
        if not moves:
            return colored == target
        colored |= moves


def dominating(black, neighbors):
    return all((black >> x) & 1 or (neighbors[x] & black)
               for x in range(len(neighbors)))


def exhaustive(a, b, t):
    n = a + b
    neighbors = adjacency(a, b, t)
    actual = {}
    non_dom = 0
    for black in range(1 << n):
        if forcing(black, neighbors):
            size = black.bit_count()
            actual[size] = actual.get(size, 0) + 1
            if not dominating(black, neighbors):
                non_dom += 1
    expected = predicted(a, b, t)
    assert actual == expected, ((a, b, t), actual, expected)
    assert non_dom == 0, ((a, b, t), non_dom)
    return actual


def main():
    profiles = 0
    for a in range(4, 7):
        for b in range(4, 7):
            for t in range(min(a, b) + 1):
                exhaustive(a, b, t)
                profiles += 1
    assert profiles == 50
    print('MATCHING_DELETED_BICLIQUES_EXHAUSTIVE_OK', profiles)

    # Below the theorem's size bound, a zero-forcing initial set need not dominate.
    a, b, t = 3, 4, 2
    nbr = adjacency(a, b, t)
    white = (1 << 1) | (1 << 2) | (1 << (a + 0)) | (1 << (a + 2))
    black = ((1 << (a + b)) - 1) ^ white
    assert forcing(black, nbr)
    assert not dominating(black, nbr)
    print('SMALL_PART_BOUNDARY_WITNESS_OK')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()

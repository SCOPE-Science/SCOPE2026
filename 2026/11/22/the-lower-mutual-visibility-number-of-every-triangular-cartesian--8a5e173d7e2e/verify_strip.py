#!/usr/bin/env python3
"""Independent shortest-path enumeration on finite triangular cylinders."""
from itertools import combinations


def geodesics(a, b):
    i, x = a
    j, y = b
    if x == y:
        return [tuple((k, x) for k in range(min(i, j), max(i, j) + 1))]
    step = 1 if j > i else -1
    if i == j:
        return [((i, x), (i, y))]
    result = []
    for t in range(min(i, j), max(i, j) + 1):
        first = [(k, x) for k in range(i, t + step, step)]
        second = [(k, y) for k in range(t, j + step, step)]
        result.append(tuple(first + second))
    return result


def visible(S):
    Q = set(S)
    return all(any(not (set(path[1:-1]) & Q) for path in geodesics(a, b))
               for a, b in combinations(S, 2))


def main():
    for n in range(2, 13):
        vertices = [(i, r) for i in range(n) for r in range(3)]
        valid = 0
        unextendible = 0
        for triple in combinations(vertices, 3):
            if not visible(triple):
                continue
            valid += 1
            if not any(visible(triple + (v,)) for v in vertices if v not in triple):
                unextendible += 1
                raise AssertionError(('unextendible triple', n, triple))
        witness = [(0, 0), (0, 1), (0, 2), (1, 0)]
        assert visible(witness)
        assert not any(visible(witness + [v]) for v in vertices if v not in witness)
        print('n=', n, 'valid_triples=', valid, 'maximal_triples=', unextendible,
              'maximal_four_witness=YES')
    print('PASS')


if __name__ == '__main__':
    main()

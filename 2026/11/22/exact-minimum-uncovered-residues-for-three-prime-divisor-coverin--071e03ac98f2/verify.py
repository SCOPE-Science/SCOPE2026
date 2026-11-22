#!/usr/bin/env python3
"""Independent exact small-case checks of the stated CRT construction."""
import itertools
import random


def covered(triple, selections):
    p, q, r = triple
    return sum(any(
        all(x[i] == v for i, v in zip(coordinates, values))
        for coordinates, values in selections
    ) for x in itertools.product(range(p), range(q), range(r)))


def construct():
    return [((0,), (0,)), ((1,), (0,)), ((2,), (0,)),
            ((0, 1), (1, 1)), ((0, 2), (2, 1)),
            ((1, 2), (2, 2)), ((0, 1, 2), (1, 2, 1))]


def check():
    triples = [(3, 5, 7), (3, 5, 11), (3, 7, 11),
               (5, 7, 11), (3, 11, 13), (7, 11, 13)]
    for p, q, r in triples:
        maximum = p*q + p*r + q*r - 1
        actual = covered((p, q, r), construct())
        assert actual == maximum, (p, q, r, actual, maximum)
        print(f"CRT witness: ({p},{q},{r}), uncovered={p*q*r-actual}")
    rng = random.Random(20260818)
    for triple in [(3, 5, 7), (3, 5, 11), (5, 7, 11)]:
        p, q, r = triple
        bound = p*q + p*r + q*r - 1
        groups = [(0,), (1,), (2,), (0, 1), (0, 2), (1, 2), (0, 1, 2)]
        for _ in range(200):
            sel = [(g, tuple(rng.randrange(triple[i]) for i in g)) for g in groups]
            assert covered(triple, sel) <= bound
    print('VERIFY_OK: 6 exact witness counts; 600 additional deterministic tests')


if __name__ == '__main__':
    check()

#!/usr/bin/env python3
"""Independent finite checks of the two zigzag Bruhat-polytope diameter formulas.
No external dependencies. The infinite proofs are in RESULT.md.
"""
from itertools import product
from random import Random


def word(n, first):
    """Adjacent-transposition indices, in two noninteracting batches."""
    return [i for i in range(1, n) if i % 2 == first] + [i for i in range(1, n) if i % 2 != first]


def permutation(n, operations):
    z = list(range(1, n + 1))
    for i in operations:
        z[i - 1], z[i] = z[i], z[i - 1]
    return tuple(z)


def vertices(n, first):
    w = word(n, first)
    k = len(w)
    return [permutation(n, (w[j] for j in range(k) if mask & (1 << j))) for mask in range(1 << k)]


def predicted(n, first):
    if n % 2:
        return 9 * n - 19
    return 9 * n - (18 if first == 1 else 20)


def expected_pairs(n, first):
    first_count = sum(i % 2 == first for i in range(1, n))
    second_count = n - 1 - first_count
    firstmask = (1 << first_count) - 1
    pairs = set()
    for secondmask in range(1 << second_count):
        a = firstmask | (secondmask << first_count)
        b = firstmask | (((1 << second_count) - 1 - secondmask) << first_count)
        pairs.add(tuple(sorted((a, b))))
    return pairs


def squared_dist(a, b):
    return sum((x - y) ** 2 for x, y in zip(a, b))


def verify_local():
    # For two adjacent entries, first-layer predecessor/successor indicators
    # on both permutations are a,c and A,C, while b,B determine the later swap.
    totals = {}
    for a, c, b, A, C, B in product(range(2), repeat=6):
        u = (2 - a, 3 + c)
        v = (2 - A, 3 + C)
        x = u if b == 0 else u[::-1]
        y = v if B == 0 else v[::-1]
        d = squared_dist(x, y)
        assert d <= 18
        assert d == 18 if (a == c == A == C == 1 and b != B) else d < 18
        if a != A or c != C:
            assert d <= 13
        totals[(a != A, c != C)] = max(totals.get((a != A, c != C), 0), d)
    assert totals == {(False,False):18, (True,False):13,
                      (False,True):13, (True,True):10}

    # Boundary edge with only one first-layer neighboring swap.
    for a, b, A, B in product(range(2), repeat=4):
        u = (2 - a, 3)
        v = (2 - A, 3)
        x = u if b == 0 else u[::-1]
        y = v if B == 0 else v[::-1]
        d = squared_dist(x, y)
        assert d <= 8
        assert d == 8 if (a == A == 1 and b != B) else d < 8
        if a != A:
            assert d <= 5


def verify_exhaustive(n, first):
    v = vertices(n, first)
    max_d, actual = 0, set()
    for i in range(len(v)):
        for j in range(i + 1, len(v)):
            d = squared_dist(v[i], v[j])
            if d > max_d:
                max_d, actual = d, {(i, j)}
            elif d == max_d:
                actual.add((i, j))
    expect = expected_pairs(n, first)
    assert max_d == predicted(n, first), (n, first, max_d)
    assert actual == expect, (n, first, len(actual), len(expect), actual ^ expect)
    assert len(v) == len(set(v))
    return len(v) * (len(v) - 1) // 2


def verify_random(n, first, rng):
    w = word(n, first)
    for _ in range(300):
        operations1 = [i for i in w if rng.randrange(2)]
        operations2 = [i for i in w if rng.randrange(2)]
        a = permutation(n, operations1)
        b = permutation(n, operations2)
        assert squared_dist(a, b) <= predicted(n, first)
    # Demonstrate exact sharpness using all first-batch moves and
    # complementary arbitrary subsets of the second batch.
    a = [i for i in w if i % 2 == first]
    q = [i for i in w if i % 2 != first]
    x = permutation(n, a + q[::2])
    y = permutation(n, a + q[1::2])
    assert squared_dist(x, y) == predicted(n, first)


def main():
    verify_local()
    pairs = 0
    for n in range(3, 11):
        for first in (0, 1):
            pairs += verify_exhaustive(n, first)
    rng = Random(20261112)
    for n in (11, 12, 15, 20, 31, 64, 100, 201):
        for first in (0, 1):
            verify_random(n, first, rng)
    print(f'ZIGZAG_BRUHAT_DIAMETER_PASS local_cases=80 exhaustive_n=3..10 orientations=2 vertex_pairs={pairs} random_pairs={8*2*300}')

if __name__ == '__main__':
    main()

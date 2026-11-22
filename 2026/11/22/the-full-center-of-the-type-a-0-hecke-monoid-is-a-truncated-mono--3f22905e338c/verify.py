"""Finite independent verification of central elements of type-A 0-Hecke monoids.

Run with Python 3.9 or later. Tests are finite checks, not a proof for all ranks.
"""
from itertools import permutations


def right_step(w, i):
    p = list(w)
    if p[i] < p[i + 1]:
        p[i], p[i + 1] = p[i + 1], p[i]
    return tuple(p)


def left_step(w, i):
    p = list(w)
    j, k = p.index(i), p.index(i + 1)
    if j < k:
        p[j], p[k] = p[k], p[j]
    return tuple(p)


def reduced_word(v):
    """Obtain a reduced simple-reflection word by sorting v and reversing swaps."""
    p = list(v)
    result = []
    for pass_id in range(len(p)):
        for i in range(len(p) - 1):
            if p[i] > p[i + 1]:
                p[i], p[i + 1] = p[i + 1], p[i]
                result.append(i)
    assert p == list(range(len(v)))
    return list(reversed(result))


def demazure(w, v):
    for i in reduced_word(v):
        w = right_step(w, i)
    return w


def nested_reversal(n, k):
    p = list(range(n))
    for i in range(k):
        p[i], p[n - 1 - i] = p[n - 1 - i], p[i]
    return tuple(p)


def main():
    for n in range(1, 9):
        expected = [nested_reversal(n, k) for k in range(n // 2 + 1)]
        expected_set = set(expected)
        actual = set()
        for w in permutations(range(n)):
            if all(right_step(w, i) == left_step(w, i)
                   for i in range(n - 1)):
                actual.add(w)
        assert actual == expected_set, (n, actual.symmetric_difference(expected_set))
        for i, wi in enumerate(expected):
            for j, wj in enumerate(expected):
                observed = demazure(wi, wj)
                wanted = expected[min(i + j, n // 2)]
                assert observed == wanted, (n, i, j, observed, wanted)
        print(f'n={n}: {len(actual)} central elements; multiplication verified')
    print('TYPE_A_HECKE_CENTER_VERIFIED')


if __name__ == '__main__':
    main()

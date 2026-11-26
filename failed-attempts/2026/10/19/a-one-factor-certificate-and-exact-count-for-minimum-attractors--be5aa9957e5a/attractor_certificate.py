#!/usr/bin/env python3
"""Independent finite checks for periodic-permutation prefix attractors.

Zero-based positions. Run: python3 attractor_certificate.py
"""
from itertools import product


def edges_for_factors(word):
    """Brute-force every distinct nonempty substring and union its occurrence spans."""
    n = len(word)
    masks = {}
    for a in range(n):
        for b in range(a + 1, n + 1):
            factor = word[a:b]
            masks[factor] = masks.get(factor, 0) | (((1 << (b-a)) - 1) << a)
    return tuple(masks.values())


def predicted(q, k, r, selected):
    if k == 1 or r == q - 1:
        return True
    forbidden = (selected[q - 1] == k - 1 and
                 selected[r] == 0 and
                 all(selected[i] in (0, k) for i in range(r)))
    return not forbidden


def count_formula(q, k, r):
    total = (k+1)**r * k**(q-r)
    if k == 1 or r == q-1:
        return total
    return total - 2**r * k**(q-r-2)


def check_all(q, k, r):
    word = tuple(i % q for i in range(q*k+r))
    edges = edges_for_factors(word)
    count = 0
    for selected in product(*(range(k + (i < r)) for i in range(q))):
        mask = sum(1 << (q*selected[i]+i) for i in range(q))
        directly = all(mask & hitset for hitset in edges)
        expected = predicted(q, k, r, selected)
        assert directly == expected, (q, k, r, selected, directly, expected)
        count += directly
    assert count == count_formula(q, k, r), (q,k,r,count)
    return count


def main():
    examined = 0
    states = 0
    for q in range(2, 7):
        for k in range(1, 5):
            for r in range(q):
                count = check_all(q,k,r)
                states += (k+1)**r * k**(q-r)
                examined += 1
    # Check large symbolic parameter cases by direct independent
    # count, with 3- and 4-symbol alphabets up to eight full periods.
    for q in (3, 4):
        for k in range(5, 9):
            for r in range(q):
                check_all(q, k, r)
                examined += 1
                states += (k+1)**r * k**(q-r)
    print('ALL_PERIODIC_ATTRACTOR_CHECKS_PASSED', 'instances', examined, 'candidate_sets', states)


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""Independent exhaustive word test for ternary span-three negative avoidance."""
from collections import Counter
from itertools import product

LENGTH = 13


def rotate_min(w):
    return min(w[i:] + w[:i] for i in range(len(w)))


def negative(w):
    return tuple((-a) % 3 for a in w)


def qualifies(w):
    encountered = set()
    for i in range(LENGTH):
        e = (w[i], w[(i + 1) % LENGTH], w[(i + 2) % LENGTH])
        e_negative = negative(e)
        if e == e_negative:
            return False
        key = min(e, e_negative)
        if key in encountered:
            return False
        encountered.add(key)
    return len(encountered) == LENGTH


def main():
    good = set()
    indexed_count = 0
    for w in product(range(3), repeat=LENGTH):
        if qualifies(w):
            indexed_count += 1
            good.add(rotate_min(w))
    fixed = Counter()
    orbit_reps = set()
    orbit_sizes = Counter()
    for w in good:
        transformations = {
            rotate_min(w), rotate_min(negative(w)),
            rotate_min(w[::-1]), rotate_min(negative(w[::-1])),
        }
        orbit_reps.add(min(transformations))
        orbit_sizes[len(transformations)] += 1
        if rotate_min(negative(w)) == w:
            fixed['negative'] += 1
        if rotate_min(w[::-1]) == w:
            fixed['reversal'] += 1
        if rotate_min(negative(w[::-1])) == w:
            fixed['negative-reversal'] += 1
    print('total_input_words', 3 ** LENGTH)
    print('valid_indexed_words', indexed_count)
    print('maximal_rotation_classes', len(good))
    print('symmetry_orbits', len(orbit_reps))
    print('orbit_sizes_counting_rotation_classes', dict(sorted(orbit_sizes.items())))
    print('fixed_rotation_classes', dict(sorted(fixed.items())))
    print('lexicographically_first_witness', ''.join(map(str, min(good))))
    assert indexed_count == 3744
    assert len(good) == 288
    assert len(orbit_reps) == 72
    assert orbit_sizes == Counter({4: 288})
    assert not fixed


if __name__ == '__main__':
    main()

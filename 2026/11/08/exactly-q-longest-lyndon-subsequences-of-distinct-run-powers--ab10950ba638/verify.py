#!/usr/bin/env python3
"""Exhaustively cross-check Lyndon single-deletion positions on run-cycle powers.

Only Python standard library is required. This is finite corroboration; the
unbounded-parameter theorem is proved separately.
"""
from itertools import permutations, product
from random import Random


def is_lyndon(word):
    return all(word < word[start:] for start in range(1, len(word)))


def expected_positions(order, lengths, copies):
    p = sum(lengths)
    starts = [sum(lengths[:i]) for i in range(len(lengths))]
    answer = []
    for i, length in enumerate(lengths):
        first = i == len(lengths)-1 or order[i+1] < order[i]
        offset = 0 if first else (copies-1)*p
        answer.extend(range(offset+starts[i], offset+starts[i]+length))
    return sorted(answer)


def run_case(order, lengths, copies):
    period = ''.join(c * a for c, a in zip(order, lengths))
    word = period * copies
    expected = expected_positions(order, lengths, copies)
    actual = []
    distinct = set()
    for j in range(len(word)):
        candidate = word[:j] + word[j+1:]
        if is_lyndon(candidate):
            actual.append(j)
            distinct.add(candidate)
    assert actual == expected, (order, lengths, copies, expected, actual)
    assert len(actual) == len(period)
    assert len(distinct) == len(order)
    assert not is_lyndon(word)
    return len(word), len(actual)


def main():
    configurations = 0
    deletion_checks = 0
    max_length = 0
    for q in (2, 3, 4):
        for order in permutations('abcd'[:q]):
            if order[0] != 'a':
                continue
            for lengths in product((1, 2, 3), repeat=q):
                for copies in (2, 3, 4):
                    length, checked = run_case(order, lengths, copies)
                    configurations += 1
                    deletion_checks += length
                    max_length = max(max_length, length)
    rng = Random(12022022)
    randomized = 800
    for _ in range(randomized):
        q = rng.randint(2, 6)
        order = list('abcdef'[:q])
        suffix = order[1:]
        rng.shuffle(suffix)
        order = tuple(['a'] + suffix)
        lengths = tuple(rng.randint(1, 6) for _ in range(q))
        copies = rng.randint(2, 5)
        length, checked = run_case(order, lengths, copies)
        configurations += 1
        deletion_checks += length
        max_length = max(max_length, length)
    print('PASS')
    print('exhaustive_configurations=1647')
    print('seeded_random_configurations=' + str(randomized))
    print('total_configurations=' + str(configurations))
    print('single_deletion_candidates_checked=' + str(deletion_checks))
    print('maximum_word_length=' + str(max_length))

if __name__ == '__main__':
    main()

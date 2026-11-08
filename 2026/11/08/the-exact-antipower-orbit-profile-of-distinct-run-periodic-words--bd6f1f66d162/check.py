#!/usr/bin/env python3
"""Finite corroboration of periodic antipower phase and threshold formulae.

Requires Python 3.8+ standard library. An infinite theorem still needs the proof.
"""
from itertools import product
from math import gcd
from random import Random


def check_case(lengths, block_length):
    period = ''.join(chr(65 + i) * a for i, a in enumerate(lengths))
    length = len(period)
    longest = max(lengths)
    g = gcd(length, block_length)
    t = length // g

    def block(start):
        return ''.join(period[(start + h) % length] for h in range(block_length))

    first_repeat = []
    for start in range(length):
        seen = set()
        repeat = t
        for j in range(t):
            substring = block(start + j * block_length)
            if substring in seen:
                repeat = j
                break
            seen.add(substring)
        first_repeat.append(repeat)

    threshold = next((j for j in range(1, t)
                      if block_length < longest and
                      min(j * block_length % length,
                          -j * block_length % length) <= longest - block_length), t)
    assert min(first_repeat) == threshold, (lengths, block_length, 'K')
    assert (threshold == t) == (block_length >= longest or
            longest - block_length < g), (lengths, block_length, 'full orbit')

    bad_residues = set()
    run_start = 0
    for a in lengths:
        counts = [0] * g
        for start in range(run_start, run_start + max(0, a - block_length + 1)):
            counts[start % g] += 1
        bad_residues.update(r for r, cnt in enumerate(counts) if cnt > 1)
        run_start += a
    predicted_full = t * (g - len(bad_residues))
    actual_full = sum(repeat == t for repeat in first_repeat)
    assert actual_full == predicted_full, (lengths, block_length, 'phase count')

    if t > 1:
        actual_all_two = all(repeat >= 2 for repeat in first_repeat)
        assert actual_all_two == (2 * block_length > longest), (
            lengths, block_length, 'two-block threshold')
    else:
        assert block_length % length == 0
    return 1


def run():
    exhaustive = 0
    for q in range(2, 6):
        for lengths in product(range(1, 5), repeat=q):
            for m in range(1, 2 * sum(lengths) + 1):
                exhaustive += check_case(lengths, m)
    rng = Random(147125)
    randomized = 0
    for _ in range(1600):
        q = rng.randrange(2, 8)
        lengths = tuple(rng.randrange(1, 13) for _ in range(q))
        m = rng.randrange(1, 3 * sum(lengths) + 1)
        randomized += check_case(lengths, m)
    assert check_case((7, 3, 2), 3) == 1
    print(f'CHECK_OK exhaustive={exhaustive} seeded={randomized} boundary=1')


if __name__ == '__main__':
    run()

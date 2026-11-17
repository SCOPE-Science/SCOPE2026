#!/usr/bin/env python3
"""Direct finite verification of optimal string attractors in permutation powers.

Run: python3 verify.py
Requires only Python 3 standard library. 0-based positions throughout.
"""
from itertools import product


def factor_masks(word):
    """For each distinct factor, OR all positions in all its occurrences."""
    n = len(word)
    masks = {}
    for start in range(n):
        mask = 0
        for stop in range(start + 1, n + 1):
            mask |= 1 << (stop - 1)
            v = word[start:stop]
            masks[v] = masks.get(v, 0) | mask
    return tuple(masks.values())


def direct_attractor(masks, positions):
    bits = sum(1 << position for position in positions)
    return all(bits & mask for mask in masks)


def prediction(q, k, choices):
    return not (choices[0] == 0 and choices[-1] == k - 1)


def run():
    cases = 0
    examined = 0
    max_len = 0
    for q in range(2, 9):
        for k in range(2, 7):
            # Independent direct testing, with bounded finite census size.
            if q * k > 35 or k**q > 100000:
                continue
            word = tuple(range(q)) * k
            masks = factor_masks(word)
            good = 0
            for choice in product(range(k), repeat=q):
                selected = tuple(q * t + i for i, t in enumerate(choice))
                actual = direct_attractor(masks, selected)
                claimed = prediction(q, k, choice)
                if actual != claimed:
                    raise AssertionError((q, k, choice, actual, claimed))
                good += actual
                examined += 1
            expected = k**q - k**(q-2)
            assert good == expected, (q, k, good, expected)
            cases += 1
            max_len = max(max_len, len(word))
    print(f'PASS: {cases} complete (q,k) parameter cases, {examined} candidate sets, maximum word length {max_len}.')
    print('For each candidate, tested every distinct factor against all its occurrences.')


if __name__ == '__main__':
    run()

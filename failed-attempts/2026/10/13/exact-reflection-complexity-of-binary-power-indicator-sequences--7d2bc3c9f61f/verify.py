#!/usr/bin/env python3
"""Independent finite checks of reflection classes for geometric-power words."""

def literal_count(base, length, word):
    if length == 0:
        return 1
    seen = set()
    for start in range(len(word) - length + 1):
        factor = bytes(word[start:start + length])
        seen.add(min(factor, factor[::-1]))
    return len(seen)


def exact_finite_formula(base, length):
    if length == 0:
        return 1
    total = length + 1 - length // 2
    k = 0
    while (base - 1) * base ** k < length:
        gap = (base - 1) * base ** k
        start_count = 2 if k == 0 else (base - 1) * base ** (k - 1)
        total += min(start_count, length - gap)
        previous_zeros = start_count - 1
        t = length - gap - 1
        both_orientations = max(
            0, min(previous_zeros, t) - max(0, t - previous_zeros) + 1
        )
        total -= both_orientations // 2
        k += 1
    return total


def geometric_formula(base, length):
    m = 2
    while (base - 1) * base ** (m + 1) <= length:
        m += 1
    gap = (base - 1) * base ** m
    assert length >= gap
    h = (base - 1) * base ** (m - 1)
    s = length - gap
    return (length + 1) // 2 + base ** (m - 1) + 2 + min(h, (s + 1) // 2)


def check(base, maximum_length):
    # A prefix larger than (base^2+4)*N contains all first pairs
    # with gaps below N, and a later isolated-one neighborhood.
    size = (base * base + 4) * maximum_length + 100
    word = bytearray(size)
    position = 1
    while position < size:
        word[position] = 1
        position *= base
    assert literal_count(base, 0, word) == 1
    for length in range(1, maximum_length + 1):
        count = literal_count(base, length, word)
        assert count == exact_finite_formula(base, length), (base, length, count)
        if length >= (base - 1) * base * base:
            assert count == geometric_formula(base, length), (base, length, count)
    print(f"PASS b={base} all n=1..{maximum_length}")


if __name__ == "__main__":
    for b in range(2, 8):
        check(b, 140)
    print("VERIFY_OK bases=2..7 lengths=0..140 independent reversal-class census")

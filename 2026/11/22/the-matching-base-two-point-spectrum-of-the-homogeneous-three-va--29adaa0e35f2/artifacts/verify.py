#!/usr/bin/env python3
"""Independent finite checks of two-point extension types in 3-valued metrics."""
from itertools import product
from fractions import Fraction

DISTANCES = (1, 2, 3)
EXPECTED_WEIGHTS = {
    1: (16, 5, 5, 9),
    2: (16, 12, 12, 9),
    3: (16, 12, 12, 2),
}


def local_weights(s):
    # Each matched old pair has distance one.
    states = [(a, b) for a, b in product(DISTANCES, repeat=2)
              if abs(a - b) <= s <= a + b]
    bins = [0] * 4
    for left, right in product(states, repeat=2):
        if abs(left[0] - right[0]) > 1 or abs(left[1] - right[1]) > 1:
            continue
        support = int(1 in (left[0], right[0])) + 2 * int(1 in (left[1], right[1]))
        bins[support] += 1
    return tuple(bins)


def predicted(m, s):
    no, one_x, one_y, both = local_weights(s)
    answer = no ** m
    if m >= 1:
        answer += m * (one_x + one_y + both) * no ** (m - 1)
    if m >= 2:
        answer += m * (m - 1) * one_x * one_y * no ** (m - 2)
    return answer


def unary_profiles(m):
    size = 2 * m
    def old_distance(i, j):
        return 1 if i // 2 == j // 2 else 3
    return [a for a in product(DISTANCES, repeat=size)
            if all(abs(a[i] - a[j]) <= old_distance(i, j) <= a[i] + a[j]
                   for i in range(size) for j in range(i + 1, size))]


def brute(m):
    profiles = unary_profiles(m)
    channels = [0, 0, 0]
    for a, b in product(profiles, repeat=2):
        for s in DISTANCES:
            if all(abs(u - v) <= s <= u + v for u, v in zip(a, b)):
                channels[s - 1] += 1
    return len(profiles), tuple(channels)


def main():
    for s, expected in EXPECTED_WEIGHTS.items():
        result = local_weights(s)
        assert result == expected, (s, result, expected)
        print(f"local s={s}: {result}")
    for m in range(4):
        unary, observed = brute(m)
        one_count = 4 ** m + (3 * m * (4 ** (m-1)) if m else 0)
        expected = tuple(predicted(m, s) for s in DISTANCES)
        assert unary == one_count and observed == expected, (m, unary, observed, expected)
        print(f"m={m}: unary={unary}, pair_channels={observed}")
    for m in range(1, 17):
        t1, t2, t3 = (predicted(m, s) for s in DISTANCES)
        assert t1 < t3 < t2, (m, t1, t3, t2)
    probability = (Fraction(25, 313), Fraction(144, 313), Fraction(144, 313))
    assert sum(probability) == 1
    assert sum([25,144,144]) == 313
    assert Fraction(313,144) < Fraction(9,4)
    print("limiting mutual-distance fractions:", ', '.join(map(str, probability)))
    print("mean feasible distances:", Fraction(313, 144))
    print("ALL_CHECKS_PASS")


if __name__ == '__main__':
    main()

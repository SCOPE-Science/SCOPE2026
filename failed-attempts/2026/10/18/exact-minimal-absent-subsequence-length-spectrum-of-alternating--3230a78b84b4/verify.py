#!/usr/bin/env python3
"""Independent finite-word subsequence census for the accompanying theorem."""
from collections import Counter
from math import comb


def embeds(candidate, text):
    """Return whether the letters occur in the given order, not necessarily contiguously."""
    next_position = 0
    for bit in candidate:
        position = text.find(bit, next_position)
        if position < 0:
            return False
        next_position = position + 1
    return True


def enumerate_minimal_absent(k):
    text = '01' * k
    occurring = ['']
    histogram = Counter()
    # Every proper prefix of a minimal absent word must occur in the text.
    for length in range(1, len(text) + 2):
        following = []
        for prefix in occurring:
            for bit in '01':
                candidate = prefix + bit
                if embeds(candidate, text):
                    following.append(candidate)
                elif all(embeds(candidate[:i] + candidate[i+1:], text)
                         for i in range(length)):
                    histogram[length] += 1
        occurring = following
        if not occurring:
            break
    return histogram


def expected_histogram(k):
    return Counter({k+j: comb(k+3-j, 2*j-1)
                    for j in range(1, (k+4)//3+1)})


def expected_total(k):
    return sum(expected_histogram(k).values())


def main():
    totals = []
    for k in range(1, 13):
        direct = enumerate_minimal_absent(k)
        expected = expected_histogram(k)
        assert direct == expected, (k, direct, expected)
        totals.append(sum(direct.values()))
        print('PASS k={} total={} histogram={}'.format(k, totals[-1],
              sorted(direct.items())))
    assert totals == [3, 5, 9, 16, 28, 49, 86, 151, 265,
                      465, 816, 1432]
    all_totals = [0] + [expected_total(k) for k in range(1, 51)]
    for k in range(4, 51):
        assert all_totals[k] == 2*all_totals[k-1] - all_totals[k-2] + all_totals[k-3]
    print('VERIFY_OK binary_repeated_permutation k=1..12 recurrence=1..50')


if __name__ == '__main__':
    main()

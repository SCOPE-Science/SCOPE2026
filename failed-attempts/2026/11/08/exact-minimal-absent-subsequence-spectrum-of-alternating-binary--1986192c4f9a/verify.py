#!/usr/bin/env python3
"""Independent finite checks of an exact binary scattered-subsequence theorem."""
from collections import defaultdict
from itertools import product


def is_subseq(candidate, source):
    i = 0
    for letter in source:
        if i < len(candidate) and candidate[i] == letter:
            i += 1
    return i == len(candidate)


def brute_minimal_absent(candidate, source):
    if is_subseq(candidate, source):
        return False
    return all(is_subseq(candidate[:j] + candidate[j+1:], source)
               for j in range(len(candidate)))


def descents(candidate):
    return sum(candidate[i - 1] >= candidate[i]
               for i in range(1, len(candidate)))


def predicted(candidate, k):
    return (len(candidate) >= 2 and descents(candidate) == k
            and candidate[0] >= candidate[1]
            and candidate[-2] >= candidate[-1]
            and not any(candidate[i-2:i+1] in ((0,1,0), (1,0,1))
                        for i in range(2, len(candidate))))


def matrix_counts(max_k):
    # A direct state-counting dynamic program, without a symbolic matrix inverse.
    counts = defaultdict(int)
    states = {(a, b, 1): 1 for a, b in ((0, 0), (1, 0), (1, 1))}
    length = 2
    while states and length <= 2*max_k:
        for (a, b, d), count in states.items():
            if (a, b) != (0, 1) and d <= max_k:
                counts[(d, length)] += count
        nxt = defaultdict(int)
        for (a, b, d), count in states.items():
            for c in (0, 1):
                if (a, b, c) in ((0, 1, 0), (1, 0, 1)):
                    continue
                dnew = d + int(b >= c)
                if dnew <= max_k:
                    nxt[(b, c, dnew)] += count
        states = nxt
        length += 1
    return counts


def check():
    max_k = 7
    spectra = defaultdict(int)
    tested = 0
    for k in range(1, max_k + 1):
        source = tuple([0, 1] * k)
        for length in range(1, 2*k + 3):
            for candidate in product((0, 1), repeat=length):
                expected = brute_minimal_absent(candidate, source)
                actual = predicted(candidate, k)
                assert actual == expected, (k, candidate, expected, actual)
                tested += 1
                if actual:
                    spectra[(k, length)] += 1
    matrix = matrix_counts(max_k)
    for k in range(1, max_k + 1):
        for length in range(2, 2*k + 3):
            assert spectra[(k, length)] == matrix[(k, length)], (k, length)
    totals = [sum(v for (k, _), v in spectra.items() if k == i)
              for i in range(1, max_k+1)]
    assert totals == [3, 5, 9, 16, 28, 49, 86], totals
    for j in range(3, len(totals)):
        assert totals[j] == 2*totals[j-1] - totals[j-2] + totals[j-3]
    for k in range(1, max_k + 1):
        assert spectra[(k, k+1)] == k + 2
    print('PASS: independent subsequence/deletion comparisons', tested)
    print('PASS: exact length spectra through k =', max_k)
    print('PASS: recurrence, shortest layer, totals', totals)


if __name__ == '__main__':
    check()

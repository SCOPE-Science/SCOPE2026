#!/usr/bin/env python3
"""Independent exhaustive checks for the three-marker Parikh-set classification.

Run with Python 3 standard library: python VERIFY.py
The unlimited theorem is proved in RESULT.md; this is finite corroboration.
"""
from collections import defaultdict
from itertools import combinations
from math import comb


def spectrum(bits):
    """Direct enumeration of Parikh vectors of all nonempty linear substrings."""
    result = set()
    for start in range(len(bits)):
        ones = 0
        for end in range(start, len(bits)):
            ones += bits[end]
            result.add((end - start + 1 - ones, ones))
    return frozenset(result)


def gaps(bits):
    ones = [i for i, x in enumerate(bits) if x == 1]
    assert len(ones) == 3
    return ones[0], ones[1] - ones[0] - 1, ones[2] - ones[1] - 1, len(bits) - 1 - ones[2]


def ambiguity_prediction(gap):
    a, b, c, d = gap
    A, D = max(a, d), min(a, d)
    B, C = max(b, c), min(b, c)
    return A > D and B > C and C >= A


def restricted_partition_count(k):
    if k < 0:
        return 0
    count = 0
    for t4 in range(k // 4 + 1):
        for t3 in range((k - 4*t4) // 3 + 1):
            for t2 in range((k - 4*t4 - 3*t3) // 2 + 1):
                count += 1
    return count


def predicted_class_count(n):
    return (comb(n, 3) + ((n - 1)//2 if n % 2 else 0))//2 - restricted_partition_count(n-7)


word_checks = 0
for n in range(3, 22):
    classes = defaultdict(list)
    for positions in combinations(range(n), 3):
        pos = set(positions)
        word = tuple(int(i in pos) for i in range(n))
        classes[spectrum(word)].append(word)
        word_checks += 1
    sizes = {len(v) for v in classes.values()}
    assert sizes <= {1, 2, 4}, (n, sizes)
    assert len(classes) == predicted_class_count(n)
    actual_ambiguous = sum(len(v) == 4 for v in classes.values())
    assert actual_ambiguous == restricted_partition_count(n-7)
    for words in classes.values():
        assert set(words) == set(words), 'Distinctness invariant'
        for word in words:
            assert ambiguity_prediction(gaps(word)) == (len(words) == 4), (n, word)
            assert spectrum(word) == spectrum(tuple(reversed(word)))

# Independently check the transformation count for all parameter sums up to 100.
for n in range(3, 101):
    by_parameters = 0
    for d in range(max(0, (n-7)//4)+1):
        for u in range(max(0, (n-7-4*d)//3)+1):
            for v in range(max(0, (n-7-4*d-3*u)//2)+1):
                w = n-7-4*d-3*u-2*v
                if w >= 0:
                    A, D, C, B = d+1+u, d, d+1+u+v, d+2+u+v+w
                    assert A>D and B>C and C>=A
                    by_parameters += 1
    assert by_parameters == restricted_partition_count(n-7)
print('VERIFY_OK words={} lengths=3..21 transform=3..100'.format(word_checks))

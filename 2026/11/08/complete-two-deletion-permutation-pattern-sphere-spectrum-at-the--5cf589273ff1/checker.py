#!/usr/bin/env python3
"""Exhaustive, independent enumeration of standardized two-deletion patterns of S_7."""
from collections import Counter
from itertools import combinations, permutations
from math import factorial

EXPECTED = {
    1: 2, 2: 8, 3: 40, 4: 52, 5: 158, 6: 204, 7: 388,
    8: 386, 9: 496, 10: 674, 11: 482, 12: 392, 13: 724,
    14: 288, 15: 148, 16: 232, 17: 252, 18: 88, 19: 24, 21: 2,
}

def patterns_by_retention(word):
    n = len(word)
    out = set()
    for retained in combinations(range(n), n-2):
        vals = tuple(word[i] for i in retained)
        ordering = sorted(vals)
        out.add(tuple(ordering.index(v)+1 for v in vals))
    return out

def patterns_by_deletion(word):
    n = len(word)
    out = set()
    for deleted in combinations(range(n), 2):
        vals = [word[i] for i in range(n) if i not in deleted]
        out.add(tuple(1+sum(w < v for w in vals) for v in vals))
    return out

def main():
    hist = Counter()
    max_words = []
    n = 7
    count = 0
    for w in permutations(range(1,n+1)):
        a = patterns_by_retention(w)
        b = patterns_by_deletion(w)
        assert a == b, ('independent implementations disagree', w)
        hist[len(a)] += 1
        count += 1
        if len(a) == 21:
            max_words.append(''.join(map(str,w)))
    assert count == factorial(n)
    assert dict(hist) == EXPECTED, (dict(sorted(hist.items())), EXPECTED)
    assert sum(k*v for k,v in hist.items()) == 55116
    assert sum(k*v for k,v in hist.items()) == sum(len(patterns_by_retention(w)) for w in permutations(range(1,8)))
    assert hist[20] == 0
    assert sorted(max_words) == ['3614725', '5274163'], max_words
    print('VERIFIED S7 size histogram:', dict(sorted(hist.items())))
    print('Total permutations:', count, 'sum of frequency:', sum(hist.values()))
    print('Number of two-prolific words:', len(max_words), 'maximum patterns:', 21)
    print('Missing value:', 20, 'and max words:', sorted(max_words))

if __name__ == '__main__':
    main()

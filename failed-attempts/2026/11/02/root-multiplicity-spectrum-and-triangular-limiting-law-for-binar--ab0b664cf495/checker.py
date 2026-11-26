#!/usr/bin/env python3
"""Independent finite tests for binary weight-two shuffle-root spectra.

No external packages or precomputed certificates are required.
"""
from collections import Counter
from itertools import combinations
from math import comb


def is_interleaving(w, root):
    """2D dynamic program on consumption positions of two rooted copies."""
    n = len(root)
    consumed_first = {0}
    for time, letter in enumerate(w):
        next_states = set()
        for first in consumed_first:
            second = time - first
            if first < n and root[first] == letter:
                next_states.add(first + 1)
            if second < n and root[second] == letter:
                next_states.add(first)
        consumed_first = next_states
        if not consumed_first:
            return False
    return n in consumed_first


def choose3_nonnegative(n):
    return comb(n, 3) if n >= 3 else 0


def predicted_count(m, t):
    return (choose3_nonnegative(m - 3*t + 5)
            - 2*choose3_nonnegative(m - 3*t + 2)
            + choose3_nonnegative(m - 3*t - 1))


def predicted_root_indices(m, a, c):
    d = m - 1
    low = max((a+1)//2, d-c)
    high = min(a, d-(c+1)//2)
    return tuple(range(low, high+1))


def run():
    num_words = num_root_tests = num_positive = 0
    for m in range(1, 25):
        d = m - 1
        counts = Counter()
        for i, j in combinations(range(2*m), 2):
            w = ('0'*i + '1' + '0'*(j-i-1) + '1' + '0'*(2*m-j-1))
            a, c = i, 2*m-j-1
            actual = tuple(x for x in range(m) if is_interleaving(w, '0'*x+'1'+'0'*(d-x)))
            predicted = predicted_root_indices(m, a, c)
            assert actual == predicted, (m, w, actual, predicted)
            counts[len(actual)] += 1
            num_words += 1
            num_root_tests += m
        expected = {t:predicted_count(m,t) for t in range(1,(m+2)//3+1)}
        assert all(counts[t] == expected[t] for t in expected), (m,counts,expected)
        assert not any(k > (m+2)//3 for k in counts)
        assert counts[0] == m*(m+1)//2 - 1
        assert sum(counts.values()) == comb(2*m,2)
        assert sum(v for k,v in counts.items() if k >= 1) == 3*m*(m-1)//2+1
        num_positive += sum(v for k,v in counts.items() if k>=1)
        if m in (1,2,3,4,5,6,12,18,24):
            print('m=',m,'root_histogram=',sorted(counts.items()),sep='')

    # Algebraic generating series coefficient check at additional lengths.
    for m in range(1, 101):
        h = [predicted_count(m,t) for t in range(1,(m+2)//3+1)]
        assert all(v>0 for v in h)
        assert sum(h)==3*m*(m-1)//2+1
        assert sum(t*v for t,v in enumerate([0]+h))==comb(m+2,3)
        for t,v in enumerate(h,1):
            j = m-3*t+2
            phase = (1,4,10)[j] if j < 3 else 9*(j-1)
            assert v == phase, (m,t,j,v,phase)
    print(f'PASS: {num_words} distinct binary weight-two words, {num_root_tests} independent root/interleaving DP tests, {num_positive} positive-class observations, m=1..24; generating-coefficient checks m=1..100.')

if __name__ == '__main__':
    run()

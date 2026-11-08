#!/usr/bin/env python3
"""Direct finite checks for two-run periodic closed-factor complexity.

Usage: python3 verify_closed_complexity.py [maximum_run]
The computation is finite; it does not establish the infinite theorem.
"""
import sys


def predicted_closed(a, b, n):
    p = a + b
    if n <= p:
        return (int(n <= a) + int(n <= b)
                + int(n > b and (n-b) % 2 == 0
                      and 1 <= (n-b)//2 <= a//2)
                + int(n > a and (n-a) % 2 == 0
                      and 1 <= (n-a)//2 <= b//2))
    h = n - p
    return (min(a, h-1) + min(b, h-1)
            + int(1 <= h <= a and (a-h) % 2 == 0)
            + int(1 <= h <= b and (b-h) % 2 == 0))


def directly_closed(word):
    n = len(word)
    if n == 1:
        return True
    for length in range(1, n):
        prefix = word[:length]
        if prefix != word[-length:]:
            continue
        occurrence_count = sum(
            word.startswith(prefix, shift) for shift in range(n-length+1)
        )
        if occurrence_count == 2:
            return True
    return False


def run(limit):
    cases = 0
    for a in range(1, limit + 1):
        for b in range(1, limit + 1):
            p = a + b
            max_length = 2*p + max(a, b) + 2
            period = '0'*a + '1'*b
            source = period*((max_length+p)//p+2)
            for n in range(1, max_length+1):
                observed_factors = {source[i:i+n] for i in range(p)}
                observed_closed = sum(directly_closed(w) for w in observed_factors)
                expected_closed = predicted_closed(a, b, n)
                expected_total = min(n, a) + min(n, b)
                assert len(observed_factors) == expected_total, (a, b, n, 'all', len(observed_factors), expected_total)
                assert observed_closed == expected_closed, (a, b, n, 'closed', observed_closed, expected_closed)
                cases += 1
            saturation = p + max(a, b)
            assert predicted_closed(a, b, saturation) == p
            assert predicted_closed(a, b, saturation-1) < p
    print('PASS: %d factor-length cases over %d run pairs' % (cases, limit*limit))


if __name__ == '__main__':
    maximum_run = int(sys.argv[1]) if len(sys.argv) > 1 else 12
    assert 1 <= maximum_run <= 40
    run(maximum_run)

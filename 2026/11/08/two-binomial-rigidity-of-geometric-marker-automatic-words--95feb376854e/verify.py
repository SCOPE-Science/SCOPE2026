#!/usr/bin/env python3
"""Independent finite checks for the 2-binomial rigidity theorem.

Uses a direct word scan and separately counts the interval formula. No external files.
"""
from collections import defaultdict


def exact_count(base, length):
    """Count distinct length-length factors using marker windows."""
    count = length + 1  # zero word and all singleton-marker placements
    r = 2
    while base ** (r - 1) <= length:
        a = 0
        while base**a * (base**(r - 1) - 1) < length:
            low = max(0, base ** (a+r-1) - length + 1,
                      base ** (a-1) + 1 if a > 0 else 0)
            high = min(base**a, base**(a+r) - length)
            count += max(0, high-low+1)
            a += 1
        r += 1
    return count


def scan(base, length, max_start):
    """Return class/factor counts; assert different factors never collide."""
    ends = max_start + length
    marks = set()
    p = 1
    while p < ends:
        marks.add(p)
        p *= base
    word = bytearray(int(i in marks) for i in range(ends))
    factors = set()
    signatures = {}
    r = sum(word[:length])
    t = sum(j * word[j] for j in range(length))
    for i in range(max_start + 1):
        if i:
            r -= word[i-1]
            t -= r
            if word[i+length-1]:
                r += 1
                t += length-1
        factor = bytes(word[i:i+length])
        key = (r, t)
        previous = signatures.setdefault(key, factor)
        assert previous == factor, (base,length,i,key,previous,factor)
        factors.add(factor)
    assert len(signatures) == len(factors)
    return len(factors)


def run():
    comparisons = 0
    for base in range(2, 9):
        for length in range(1, 161):
            observed = scan(base, length, 5000)
            expected = exact_count(base, length)
            assert observed == expected, (base, length, observed, expected)
            comparisons += 5001
    # Both zero and one markers occur at every length, but singleton positions
    # are never distinguished by first-order Parikh data alone.
    for base in range(2,9):
        assert scan(base,2,5000) >= 3
    print(f"VERIFY_OK bases=2..8 lengths=1..160 windows={comparisons} exact_count_matches=1120")

if __name__ == '__main__':
    run()

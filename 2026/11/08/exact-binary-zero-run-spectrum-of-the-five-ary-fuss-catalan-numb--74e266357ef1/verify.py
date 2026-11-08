#!/usr/bin/env python3
"""Exact independent finite checks for the five-ary Fuss-Catalan zero-run theorem."""
import math


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def admissible(n):
    return (n & (n << 2)) == 0


def expected_gap(j, s):
    return ((1 if s == 0 else 3) * (1 << j)) // 5


def max_lower(j, s):
    # Greedy high-to-low independent-set enumeration: choose allowed bits.
    hi = {j + 1: s, j: 0, j + 2: 0}
    bits = dict(hi)
    for i in range(j - 1, -1, -1):
        bits[i] = int(not bits.get(i + 2, 0))
    return sum((1 << i) for i in range(j) if bits[i])


for n in range(1200):
    # Direct factorial-ratio integer evaluation, independently of binary carry tests.
    c = math.comb(5 * n, n) // (4 * n + 1)
    assert c % 2 == admissible(n), (n, c)
print('INTEGER_PARITY_OK 0..1199')

for j in range(33):
    for s in (0, 1):
        assert (1 << j) - max_lower(j, s) - 1 == expected_gap(j, s), (j, s)
print('LOCAL_PREDECESSOR_GAPS_OK j=0..32')

for m in range(1, 19):
    support = [n for n in range(1 << m) if admissible(n)]
    count = fib((m + 1) // 2 + 2) * fib(m // 2 + 2)
    assert len(support) == count, (m, len(support), count)
    actual = {b - a - 1 for a, b in zip(support, support[1:]) if b > a + 1}
    predicted = {expected_gap(j, 0) for j in range(m)} | {
        expected_gap(j, 1) for j in range(max(0, m - 1))
    }
    predicted.discard(0)
    assert actual == predicted, (m, actual, predicted)
    if m in (6, 12, 18):
        print('FINITE_SPECTRUM_OK m=', m, 'odd_count=', count,
              'distinct_positive_gaps=', len(actual), 'largest_gap=', max(actual))

support = [n for n in range(1 << 18) if admissible(n)]
record = 0
seen_record_values = []
for a, b in zip(support, support[1:]):
    gap = b - a - 1
    if gap > record:
        record = gap
        seen_record_values.append(gap)
expected_values = sorted({expected_gap(j, s) for j in range(19) for s in (0, 1)} - {0})
# Large values whose first realizing endpoints exceed 2**18 are excluded.
expected_values = [v for v in expected_values if v <= record]
assert seen_record_values == expected_values, (seen_record_values, expected_values)
print('RECORD_VALUES_OK', seen_record_values)
print('VERIFY_OK exact_finite_checks=yes infinite_proof_is_structural=yes')

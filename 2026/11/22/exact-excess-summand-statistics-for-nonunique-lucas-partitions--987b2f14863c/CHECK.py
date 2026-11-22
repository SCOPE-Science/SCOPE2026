#!/usr/bin/env python3
"""Independent exhaustive finite tests for the Lucas partition summand-excess law.

Uses Python's standard library. Finite enumeration is not a proof for arbitrary m.
"""
from collections import Counter, defaultdict


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def lucas_to(m):
    a = [2, 1]
    while len(a) <= m:
        a.append(a[-1] + a[-2])
    return a


def subset_values(weights):
    m = len(weights) - 1
    def visit(i, previous, value, mask, count):
        if i > m:
            yield value, mask, count
            return
        yield from visit(i + 1, False, value, mask, count)
        if not previous:
            yield from visit(i + 1, True, value + weights[i],
                             mask | (1 << i), count + 1)
    yield from visit(0, False, 0, 0, 0)


def verify(m):
    by_sum = defaultdict(list)
    for n, mask, count in subset_values(lucas_to(m)):
        by_sum[n].append((mask, count))
    histogram = Counter()
    for n, representations in by_sum.items():
        if len(representations) > 2:
            raise AssertionError((m, n, representations))
        if len(representations) < 2:
            continue
        exceptional = [p for p in representations if (p[0] & 0b101) == 0b101]
        assert len(exceptional) == 1, (m, n, representations)
        ordinary = next(p for p in representations if p != exceptional[0])
        delta = exceptional[0][1] - ordinary[1]
        assert delta >= 0, (m, n, delta)
        histogram[delta] += 1
    predicted = {j: fibonacci(m - 2*j - 2)
                 for j in range((m - 3)//2 + 1)}
    assert dict(histogram) == predicted, (m, histogram, predicted)
    total = fibonacci(m - 1) - (m % 2 == 0)
    assert sum(histogram.values()) == total
    return total, len(by_sum)


def main():
    results = [verify(m) for m in range(3, 25)]
    print('PASS: all 22 index cutoffs m=3,...,24')
    print('PASS: exact multiplicity <=2 and unique exceptional pair in each collision')
    print('PASS: complete Fibonacci histogram for each cutoff, both total formulas')
    print('m=24: double-represented = %d, distinct represented = %d' % results[-1])
    print('Infinite claims require the separate mathematical proof.')


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""Independent full-state temporal classification, using pair-of-tuples transitions."""
from collections import Counter
from math import gcd


def transition(state):
    u, v = state
    n = len(u)
    w = tuple(u[(i-1) % n] ^ u[(i+1) % n] ^ v[i] for i in range(n))
    return (w, u)


def bits(a, n):
    return tuple((a >> i) & 1 for i in range(n))


def classify(n):
    period_count = Counter()
    for x in range(1 << n):
        row_x = bits(x, n)
        for y in range(1 << n):
            start = (row_x, bits(y, n))
            state = transition(start)
            period = 1
            while state != start:
                state = transition(state)
                period += 1
                if period > 2 * n:
                    raise AssertionError((n, start, period))
            period_count[period] += 1
    return period_count


def run():
    total_states = 0
    fixed_tests = 0
    for n in range(3, 9):
        census = classify(n)
        total_states += 4 ** n
        predicted_period = n if n % 2 == 0 else 2 * n
        assert sum(census.values()) == 4**n
        assert max(census) == predicted_period
        for t in range(1, 2*n + 1):
            direct_fixed = sum(k for d,k in census.items() if t % d == 0)
            exponent = 2 * gcd(n, t) - int(n % 2 == 1 and t % 2 == 1)
            assert direct_fixed == 2 ** exponent, (n,t,direct_fixed,exponent)
            fixed_tests += 1
        assert all(predicted_period % period == 0 for period in census)
        print('n=%d states=%d primitive_periods=%s' % (n, 4**n, sorted(census.items())))
    print('enumerated states:', total_states)
    print('fixed-point comparisons:', fixed_tests)
    print('all temporal classifications agree: PASS')


if __name__ == '__main__':
    run()

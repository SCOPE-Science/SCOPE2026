"""Independent microscopic verification of sequential parity on square bouquets.

Usage: python3 verify_states.py
No dependencies beyond Python standard library.
"""

from collections import Counter
from math import gcd


def graph_neighborhoods(k):
    n = 3 * k + 1
    masks = [0] * n
    for i in range(k):
        a, b, c = 3 * i + 1, 3 * i + 2, 3 * i + 3
        for u, v in ((0, a), (a, b), (b, c), (c, 0)):
            masks[u] |= 1 << v
            masks[v] |= 1 << u
    return masks


def advance(state, masks):
    for v, adj in enumerate(masks):
        if (state & adj).bit_count() % 2:
            state ^= 1 << v
    return state


def expected_fixed_dimension(k, t):
    dyadic = t & -t
    if k & 1:
        return 2 + 2 * (t % 3 == 0) + (k - 1) * min(3, dyadic)
    return 2 + min(5, dyadic) + (k - 2) * min(3, dyadic)


def all_divisors(x):
    return [d for d in range(1, x + 1) if x % d == 0]


def expected_period_counts(k):
    order = 3 if k == 1 else (12 if k % 2 else 8)
    fixed = {t: 2 ** expected_fixed_dimension(k, t) for t in all_divisors(order)}
    exact = {}
    for t in sorted(fixed):
        exact[t] = fixed[t] - sum(exact[d] for d in exact if t % d == 0)
    assert sum(exact.values()) == 2 ** (3 * k + 1)
    return exact


def main():
    for k in range(1, 6):
        masks = graph_neighborhoods(k)
        order = 3 if k == 1 else (12 if k % 2 else 8)
        counted = Counter()
        for start in range(1 << len(masks)):
            x = start
            for t in range(1, order + 1):
                x = advance(x, masks)
                if x == start:
                    counted[t] += 1
                    break
            else:
                raise AssertionError((k, start, 'did not return'))
        expected = expected_period_counts(k)
        assert dict(counted) == {t: val for t, val in expected.items() if val}, (k, counted, expected)
        print('k={} vertices={} states={} periods={}'.format(
            k, 3 * k + 1, 2 ** (3 * k + 1), dict(sorted(counted.items()))))
    print('PASS: all states for k=1 through 5')


if __name__ == '__main__':
    main()

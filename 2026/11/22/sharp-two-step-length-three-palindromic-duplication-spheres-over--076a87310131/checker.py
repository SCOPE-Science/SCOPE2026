#!/usr/bin/env python3
"""Exact finite checks for two sequential length-three palindromic duplications.

The argument for all lengths is in RESULT.md; these tests are independent
reconstructions of the operation, not an extrapolation from data.
"""
from itertools import product
from math import comb


def dup(word, i, k=3):
    """Insert the reversal of the length-k source beginning at i."""
    assert 0 <= i <= len(word) - k
    a = word[i:i + k]
    return word[:i + k] + a[::-1] + word[i + k:]


def max_bound(n):
    return (n - 2) * (n + 1) - comb(max(n - 4, 0), 2)


def descendants(x):
    n = len(x)
    return {dup(dup(x, i), j) for i in range(n - 2) for j in range(n + 1)}


def signature(x, i, j):
    z = dup(dup(x, i), j)
    steps = [(z[r + 1] - z[r]) % 3 for r in range(len(z) - 1)]
    bad = [r for r, d in enumerate(steps) if d != 1]
    assert bad
    trans = {0: '0', 1: '+', 2: '-'}
    return bad[0], ''.join(trans[d] for d in steps[bad[0]:bad[-1]+1])


def predicted_signature(i, j):
    d = j - i
    if d < 0:
        return i + d + 2, '0--0' + '+' * (-d-1) + '0--0'
    cases = {0: '0-----0', 1: '000-0-0', 2: '0-0+0+0',
             3: '0--0', 4: '0--000+0', 5: '0--0+0-0-'}
    if d in cases:
        return i + 2, cases[d]
    return i + 2, '0--0' + '+' * (d-4) + '0--0'


def test_history_classification(n):
    source = tuple(i % 3 for i in range(n))
    fibers = {}
    for i in range(n - 2):
        first = dup(source, i)
        for j in range(n + 1):
            y = dup(first, j)
            fibers.setdefault(y, []).append((i, j))
    expected_pairs = {(tuple(sorted(((a, b + 3), (b, a)))))
                      for a in range(n - 2)
                      for b in range(a + 3, n - 2)}
    doubletons = set()
    for histories in fibers.values():
        assert len(histories) <= 2, (n, histories)
        if len(histories) == 2:
            doubletons.add(tuple(sorted(histories)))
    assert doubletons == expected_pairs, (n, len(doubletons), len(expected_pairs))
    assert len(fibers) == max_bound(n)
    return len(fibers), len(doubletons)


def main():
    # Each finite ternary source is checked directly against the universal count.
    binary_counts = []
    for n in range(3, 10):
        vals = [len(descendants(x)) for x in product(range(2), repeat=n)]
        binary_counts.append((n, max(vals)))
        assert max(vals) <= max_bound(n)
    assert dict(binary_counts)[4] == 9
    print('Binary maxima through n=9:', binary_counts)

    exhaustive = 0
    for n in range(3, 10):
        highest = 0
        for x in product(range(3), repeat=n):
            highest = max(highest, len(descendants(x)))
            exhaustive += 1
        assert highest == max_bound(n), (n, highest, max_bound(n))
    print('Exhaustive ternary source words:', exhaustive, '(lengths 3..9)')

    records = []
    for n in list(range(3, 47)) + [60, 90, 128]:
        size, dbl = test_history_classification(n)
        records.append((n, size, dbl))
    print('Periodic-source history classifications:', len(records),
          '; n=128:', records[-1])

    # Check every position/relative displacement in a broad finite window.
    # Append original periodic tail to avoid any artificial end effect.
    checks = 0
    infinite_prefix = tuple(t % 3 for t in range(300))
    for i in range(0, 86):
        first = dup(infinite_prefix, i)
        for j in range(0, 165):
            got = signature(infinite_prefix, i, j)
            want = predicted_signature(i, j)
            assert got == want, (i, j, got, want)
            checks += 1
    print('Independent signed-difference table comparisons:', checks)
    print('All exact checks passed.')


if __name__ == '__main__':
    main()

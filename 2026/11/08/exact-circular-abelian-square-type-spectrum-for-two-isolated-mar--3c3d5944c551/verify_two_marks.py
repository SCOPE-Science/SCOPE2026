#!/usr/bin/env python3
"""Exact small-parameter verification of a circular Abelian-square type formula.

The enumerator is independent of the symbolic proof. It never assumes
that a finite census establishes the result at unbounded lengths.
"""

def observed(p: int, q: int):
    assert p >= 0 and q >= 0
    word = 'a' * p + 'b' + 'a' * q + 'b'
    n = len(word)
    doubled = word + word
    counts = []
    for m in range(1, n // 2 + 1):
        types = set()
        for start in range(n):
            factor = doubled[start:start + 2 * m]
            left_b = factor[:m].count('b')
            right_b = factor[m:].count('b')
            if left_b == right_b:
                types.add((m, left_b))
        counts.append(types)
    return counts


def predicted(p: int, q: int):
    n = p + q + 2
    short = min(p, q)
    long = max(p, q)
    h = n // 2
    threshold = (short + 3) // 2  # ceil((short + 2)/2)
    counts = []
    for m in range(1, h + 1):
        types = set()
        if 2 * m <= long:
            types.add((m, 0))
        if m >= threshold:
            types.add((m, 1))
        counts.append(types)
    return counts


def check(p: int, q: int):
    actual = observed(p, q)
    formula = predicted(p, q)
    assert actual == formula, (p, q, actual, formula)
    n = p + q + 2
    num = sum(map(len, actual))
    r = min(p, q)
    assert num == n - 2 - r + int(n % 2 == 0 and r % 2 == 0)
    if n % 2:
        assert all(len(t) >= 1 for t in actual)
        assert all(sum(len(t) for t in actual[:k]) >= k
                   for k in range(1, len(actual) + 1))


def main():
    total = 0
    for p in range(60):
        for q in range(60):
            check(p, q)
            total += 1
    print(f'EXACT_TWO_MARKS_OK {total} parameter pairs; all half-length type sets')


if __name__ == '__main__':
    main()

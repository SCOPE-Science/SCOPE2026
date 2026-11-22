#!/usr/bin/env python3
"""Direct finite checks for a ternary Delannoy-polynomial congruence.

Usage: python3 verify.py. Uses the standard library only.
Finite checks are diagnostics; all-depth conclusions use the proof in RESULT.md.
"""
from math import comb
from fractions import Fraction


def digit_data(n):
    digits = []
    while n:
        d = n % 3
        if d == 1:
            return None
        digits.append(d // 2)
        n //= 3
    return digits


def defect(digits):
    if not digits:
        return 0
    return (digits[0] + 2 * sum(digits[1:]) +
            sum(a * b for a, b in zip(digits, digits[1:]))) % 3


def direct_delannoy(n, x):
    return sum(comb(n, j) * comb(n + j, j) * x ** j for j in range(n + 1))


def full_recurrence(max_n, x):
    """Exact integer Legendre recurrence, not the digit theorem."""
    s = 1 + 2 * x
    a, b = 1, s
    for n in range(max_n):
        yield a % 9
        numerator = (2 * n + 3) * s * b - (n + 1) * a
        assert numerator % (n + 2) == 0
        a, b = b, numerator // (n + 2)


def expected_count(r):
    offsets = (2, 1, -1, -2, -1, 1)
    return (2 ** r + offsets[r % 6]) // 3


def main():
    checks = 0
    for n in range(33):
        for x in range(6):
            assert direct_delannoy(n, x) % 9 == list(full_recurrence(n + 1, x))[-1]
            checks += 1

    top = 3 ** 8
    predicted_universal = set()
    predicted_counts = []
    for r in range(9):
        count = sum(digit_data(n) is not None and defect(digit_data(n)) == 0
                    for n in range(3 ** r))
        assert count == expected_count(r)
        predicted_counts.append(count)
        checks += 1
    for n in range(top):
        digs = digit_data(n)
        if digs is not None and defect(digs) == 0:
            predicted_universal.add(n)

    observed_universal = set(range(top))
    for x in range(9):
        for n, val in enumerate(full_recurrence(top, x)):
            observed_universal.discard(n) if val != 1 else None
            digs = digit_data(n)
            if digs is not None:
                target = (1 + 3 * defect(digs) * (x % 3 == 1)) % 9
                assert val == target, (n, x, val, target)
                checks += 1
    assert observed_universal == predicted_universal
    checks += top

    # Independent binomial coefficient scaling and digit recursion.
    for m in range(1000):
        digs = []
        q = m
        while q:
            digs.append(q % 3)
            q //= 3
        if any(u == 2 for u in digs):
            continue
        am = ((-1) ** m * comb(2*m, m) * pow(4, -m, 9)) % 9
        assert am == (1 + 3 * defect(digs)) % 9
        checks += 1
        assert comb(6*m, 3*m) % 9 == comb(2*m, m) % 9
        checks += 1

    print('PASS', checks, 'finite exact tests')
    print('universal counts for r=0..8:', predicted_counts)
    print('tested indices 0 <= n <', top, 'and all 9 argument residues')


if __name__ == '__main__':
    main()

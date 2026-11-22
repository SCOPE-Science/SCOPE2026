#!/usr/bin/env python3
"""Exact finite certificate for the cyclic gap law of Bell numbers modulo 7.

Run: python3 check_bell7.py
Requires only Python 3 standard library and gap_histogram.csv alongside this file.
"""
from collections import Counter
from pathlib import Path
import csv

P = 137257
SEED = (1, 1, 2, 5, 1, 3, 0)


def polynomial_multiply(a, b):
    """Product in F_7[X]/(X^7-X-1), reducing X^7 = X+1."""
    c = [0] * 13
    for i in range(7):
        for j in range(7):
            c[i + j] = (c[i + j] + a[i] * b[j]) % 7
    for i in range(12, 6, -1):
        t = c[i]
        c[i - 7] = (c[i - 7] + t) % 7
        c[i - 6] = (c[i - 6] + t) % 7
    return tuple(c[:7])


def polynomial_x_power(e):
    result = (1, 0, 0, 0, 0, 0, 0)
    base = (0, 1, 0, 0, 0, 0, 0)
    while e:
        if e & 1:
            result = polynomial_multiply(result, base)
        base = polynomial_multiply(base, base)
        e //= 2
    return result


def sequence_recurrence():
    # Invariant: seq[n] is Bell(n) mod 7, by Touchard's congruence.
    seq = list(SEED)
    for n in range(P + 7):
        seq.append((seq[n] + seq[n + 1]) % 7)
    return seq


def second_cycle_scan():
    # Independent rolling-state scan; no indexing into the first generated list.
    state = list(SEED)
    zeros = []
    for n in range(P):
        if state[0] == 0:
            zeros.append(n)
        state = state[1:] + [(state[0] + state[1]) % 7]
    assert tuple(state) == SEED
    return zeros


def gap_histogram(zeros):
    assert zeros and all(0 <= x < P for x in zeros)
    result = Counter()
    witnesses = {}
    for j, x in enumerate(zeros):
        next_x = zeros[(j + 1) % len(zeros)]
        if j + 1 == len(zeros):
            next_x += P
        d = next_x - x
        assert 1 <= d <= P
        result[d] += 1
        witnesses.setdefault(d, []).append(x)
    assert sum(result.values()) == len(zeros)
    assert sum(d * m for d, m in result.items()) == P
    return dict(result), witnesses


def main():
    assert P == 29 * 4733
    assert all(4733 % q for q in range(2, int(4733 ** 0.5) + 1))
    assert polynomial_x_power(P) == (1, 0, 0, 0, 0, 0, 0)
    assert polynomial_x_power(P // 29) == (5, 2, 4, 5, 2, 5, 1)
    assert polynomial_x_power(P // 4733) == (0, 1, 4, 6, 4, 1, 0)

    seq = sequence_recurrence()
    assert tuple(seq[P:P + 7]) == SEED
    assert tuple(seq[29:36]) == (4, 5, 1, 3, 6, 4, 0)
    assert tuple(seq[4733:4740]) == (1, 0, 3, 2, 5, 2, 2)
    zeros = [n for n in range(P) if seq[n] == 0]
    assert zeros == second_cycle_scan()
    hist, witnesses = gap_histogram(zeros)
    with Path(__file__).with_name('gap_histogram.csv').open(newline='', encoding='utf-8') as fp:
        csv_hist = {int(d): int(c) for d, c in csv.reader(fp) if d != 'gap'}
    assert hist == csv_hist
    assert len(zeros) == 19608
    assert len(hist) == 50
    assert max(hist) == 65
    assert hist[65] == 1 and witnesses[65] == [85736]
    assert hist.get(7, 0) == 0
    assert hist[1] == 2801 and hist[2] == 2401
    print('CHECK_OK', 'period=', P, 'zeros=', len(zeros),
          'gap_types=', len(hist), 'max_gap=', max(hist),
          'unique_max_start=', witnesses[65][0],
          'gap_total=', sum(hist.values()),
          'weighted_gap_total=', sum(k * v for k, v in hist.items()))


if __name__ == '__main__':
    main()

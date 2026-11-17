#!/usr/bin/env python3
"""Finite diagnostics for constant-letter runs in binary all-one-pattern parity words.

No finite test is used as proof of an infinite statement.
"""
from collections import Counter
from fractions import Fraction


def valuation_two(n):
    assert n > 0
    return (n & -n).bit_length() - 1


def expected_run_start_densities(d):
    assert d >= 2
    m = 1 << d
    p = Fraction(2, m)
    densities = Counter()
    densities[1] += Fraction(7, 6 * m) - Fraction(2, 3 * m * m)
    for j in range(1, d - 1):
        densities[1 << j] += Fraction(1, m * (1 << (j + 1)))
    for j in range(1, d):
        densities[m - (1 << j)] += Fraction(1, m * (1 << (j + 1)))
    densities[m - 1] += (1 + p) / (6 * m)
    densities[m // 2 + 1] += Fraction(1, m * m)
    densities[m] += (2 - p) / (6 * m)
    assert sum(densities.values()) == Fraction(8 * (m - 1), 3 * m * m)
    assert sum(length * density for length, density in densities.items()) == 1
    return dict(densities)


def predicted_change_boundaries(d, stop):
    m = 1 << d
    boundary = []
    for k in range(stop // m + 2):
        if k:
            odd = k >> valuation_two(k)
            change = (valuation_two(k) % 2 == 0) ^ (valuation_two(odd + 1) >= d)
            if change and k * m < stop:
                boundary.append(k * m)
        qmax = min(d - 1, valuation_two(k + 1))
        for q in range(qmax + 1):
            x = (k + 1) * m - (1 << q)
            if 0 < x < stop:
                boundary.append(x)
    return sorted(boundary)


def direct_change_boundaries(d, stop):
    f = bytearray(stop)
    mask = (1 << (d - 1)) - 1
    for n in range(1, stop):
        t = n >> 1
        f[n] = f[t] ^ int((n & 1) != 0 and (t & mask) == mask)
    return [x for x in range(1, stop) if f[x] != f[x - 1]]


def main():
    stop = 1 << 18
    transitions = 0
    cases = 0
    for d in range(2, 9):
        actual = direct_change_boundaries(d, stop)
        predicted = predicted_change_boundaries(d, stop)
        assert actual == predicted, f"transition mismatch at d={d}"
        transitions += len(actual)
        run_lengths = [actual[0]] + [b - a for a, b in zip(actual, actual[1:])]
        counts = Counter(run_lengths)
        theory = expected_run_start_densities(d)
        assert set(counts) == set(theory), (d, set(counts) ^ set(theory))
        assert max(counts) == 1 << d
        for length, density in theory.items():
            # Exact discrepancy is small at this finite dyadic cutoff.
            discrepancy = abs(Fraction(counts[length]) - stop * density)
            assert discrepancy <= 2, (d, length, discrepancy)
        cases += 1
    print(f"VERIFY_OK orders=2..8 cutoff={stop} order_cases={cases} checked_transitions={transitions}")


if __name__ == "__main__":
    main()

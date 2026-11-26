#!/usr/bin/env python3
"""Independent finite checks of the modal Kleene chain census.

Uses only Python's standard library. The general theorem has a symbolic proof;
this exhaustive checker verifies its small finite instances and normal form.
"""
from itertools import combinations_with_replacement, product
from math import comb


def modal_axioms(values, outputs):
    """Evaluate the three original universal axioms directly, not the normal form."""
    image = dict(zip(values, outputs))
    for a in values:
        for b in values:
            if image[min(a, b)] != min(image[a], image[b]):  # MK
                return False
    for z in values:
        b = image[max(z, -z)]
        if -b > b:  # Pos
            return False
    for x in values:
        for z in values:
            u = image[max(x, min(z, -z))]
            if u > max(image[x], -u):  # Con
                return False
    return True


def plateau_normal_form(values, outputs, m):
    """Evaluate the proposed structural dichotomy independently of MK/Pos/Con."""
    if any(a > b for a, b in zip(outputs, outputs[1:])):
        return False
    c = outputs[m]
    if c < 0:
        return False
    if c > 0 and any(outputs[i] != c for i in range(m)):
        return False
    return True


def tally(m, iterator):
    values = list(range(-m, m + 1))
    result = [0, 0, 0, 0]  # all, normal, center-preserving, both
    tested = 0
    for outputs in iterator:
        tested += 1
        a = modal_axioms(values, outputs)
        b = plateau_normal_form(values, outputs, m)
        assert a == b, (m, outputs, a, b)
        if a:
            normal = outputs[-1] == m
            center = outputs[m] == 0
            result[0] += 1
            result[1] += int(normal)
            result[2] += int(center)
            result[3] += int(normal and center)
    C = comb(2 * m, m)
    expected = [C * C + comb(2 * m, m + 1),
                (C * C + C) // 2,
                C * C,
                C * C // 2]
    assert result == expected, (m, tested, result, expected)
    return tested, result


def main():
    full_tests = 0
    monotone_tests = 0
    for m in range(1, 5):
        values = list(range(-m, m + 1))
        monotone, result = tally(
            m, combinations_with_replacement(values, 2 * m + 1))
        monotone_tests += monotone
        if m <= 2:
            full, result2 = tally(m, product(values, repeat=2 * m + 1))
            assert result2 == result
            full_tests += full
        print('half_width=%d accepted=%d normal=%d centered=%d both=%d'
              % ((m,) + tuple(result)))
    for m in range(1, 61):
        C = comb(2 * m, m)
        assert sum(comb(2 * m - c, m) for c in range(1, m + 1)) == comb(2 * m, m + 1)
        assert sum(comb(2 * m - c - 1, m - 1) for c in range(1, m + 1)) == C // 2
    print('ALL_CHECKS_OK full_functions=%d monotone_maps=%d binomial_ranks=60'
          % (full_tests, monotone_tests))


if __name__ == '__main__':
    main()

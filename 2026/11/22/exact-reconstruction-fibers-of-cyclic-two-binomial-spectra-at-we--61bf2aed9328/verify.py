#!/usr/bin/env python3
"""Reproduce the cyclic scattered-01 spectrum and the weight-three fiber law."""
from collections import defaultdict, Counter
from itertools import combinations
from math import comb


def rotate_canonical(word):
    return min(word[j:] + word[:j] for j in range(len(word)))


def scattered_01(word):
    zeros = 0
    answer = 0
    for symbol in word:
        if symbol == '0':
            zeros += 1
        else:
            answer += zeros
    return answer


def literal_spectrum(word):
    return tuple(sorted(scattered_01(word[j:] + word[:j])
                        for j in range(len(word))))


def canonical_gaps(gaps):
    return min(gaps, gaps[1:] + gaps[:1], gaps[2:] + gaps[:2])


def word_from_gaps(gaps):
    return ''.join('1' + '0' * gap for gap in gaps)


def root_01_values(gaps):
    a, b, c = gaps
    return (2*a+b, 2*b+c, 2*c+a)


def derived_spectrum(gaps):
    n = 3 + sum(gaps)
    m = n - 3
    roots = root_01_values(gaps)
    values = list(roots)
    for root, gap in zip(roots, gaps):
        values.extend(root + m - 3*j for j in range(gap))
    return tuple(sorted(values))


def all_gap_necklaces(n):
    m = n - 3
    return {canonical_gaps((a, b, m-a-b))
            for a in range(m + 1) for b in range(m-a+1)}


def predicted_number_of_fibers(n):
    if n % 3:
        return (n-1)*(n-2)//6
    return (n//3)**2


def predicted_number_of_doubletons(n):
    h = n//3-1
    return h*(h-1)//2 if n % 3 == 0 else 0


def predicted_partner(gaps):
    m = sum(gaps)
    if m % 3:
        return None
    h = m//3
    a, b, c = gaps
    partner = (2*h-c, 2*h-b, 2*h-a)
    if min(partner) < 0:
        return None
    return canonical_gaps(partner)


def check():
    literal_words = 0
    for n in range(3, 19):
        observed = {}
        for sites in combinations(range(n), 3):
            word = ''.join('1' if j in sites else '0' for j in range(n))
            observed[rotate_canonical(word)] = True
        derived = all_gap_necklaces(n)
        assert len(observed) == len(derived), (n, len(observed), len(derived))
        for gaps in derived:
            word = word_from_gaps(gaps)
            assert literal_spectrum(word) == derived_spectrum(gaps), (n, gaps)
            # Independent direct evaluation of the root observations.
            one_roots = tuple(scattered_01(word[j:] + word[:j])
                              for j, symbol in enumerate(word) if symbol == '1')
            assert one_roots == root_01_values(gaps), (n, gaps)
            # Coefficients of (X^3-1) F = (X^n-1) T agree exactly.
            spectrum = Counter(literal_spectrum(word))
            lhs = Counter()
            rhs = Counter()
            for value, count in spectrum.items():
                lhs[value+3] += count
                lhs[value] -= count
            for value in one_roots:
                rhs[value+n] += 1
                rhs[value] -= 1
            assert lhs == rhs, (n, gaps, lhs, rhs)
            literal_words += 1
    class_checks = 0
    for n in range(3, 85):
        classes = all_gap_necklaces(n)
        fibers = defaultdict(list)
        for gaps in classes:
            fibers[tuple(sorted(root_01_values(gaps)))].append(gaps)
        assert len(fibers) == predicted_number_of_fibers(n), n
        doubletons = [v for v in fibers.values() if len(v) == 2]
        assert len(doubletons) == predicted_number_of_doubletons(n), n
        assert all(len(v) <= 2 for v in fibers.values()), n
        for groups in fibers.values():
            if len(groups) == 2:
                a, b = groups
                assert predicted_partner(a) == b and predicted_partner(b) == a, (n,a,b)
            else:
                a = groups[0]
                other = predicted_partner(a)
                assert other is None or other == a, (n,a,other)
        class_checks += len(classes)
    a = '110001000'
    b = '101010000'
    assert rotate_canonical(a) != rotate_canonical(b)
    assert literal_spectrum(a) == literal_spectrum(b)
    print('VERIFY_OK: independently evaluated %d binary necklace spectra at n<=18; '
          'checked %d gap necklaces at n<=84; exact fiber law, direct trace '
          'identity, rational partner, and the n=9 example all passed.' %
          (literal_words, class_checks))


if __name__ == '__main__':
    check()

#!/usr/bin/env python3
"""Independent finite checks for the shuffle-square witness-distribution theorem.

Uses only Python's standard library.  The finite checks support, but do not
replace, the all-size combinatorial proof in RESULT.md.
"""
from collections import Counter
from math import comb, factorial


def words_with_each_letter_twice(q):
    w = [-1] * (2 * q)
    counts = [0] * q

    def build(i):
        if i == 2 * q:
            yield tuple(w)
            return
        for letter in range(q):
            if counts[letter] < 2:
                counts[letter] += 1
                w[i] = letter
                yield from build(i + 1)
                counts[letter] -= 1
    yield from build(0)


def direct_witness_count(w):
    """Enumerate all unordered 2-colorings with one copy per letter."""
    q = len(w) // 2
    locations = [[i for i, letter in enumerate(w) if letter == a]
                 for a in range(q)]
    ans = 0
    for mask in range(1 << (q - 1)):
        first = {locations[0][0]}
        second = {locations[0][1]}
        for letter in range(1, q):
            choice = (mask >> (letter - 1)) & 1
            first.add(locations[letter][choice])
            second.add(locations[letter][1 - choice])
        ans += (tuple(w[i] for i in sorted(first)) ==
                tuple(w[i] for i in sorted(second)))
    return ans


def dyck_returns_or_none(w):
    """Return number of primitive excursions if the two occurrence orders agree."""
    first, second, seen = [], [], set()
    height = 0
    returns = 0
    for letter in w:
        if letter not in seen:
            seen.add(letter)
            first.append(letter)
            height += 1
        else:
            second.append(letter)
            height -= 1
        if height == 0:
            returns += 1
    return returns if first == second else None


def catalan(n):
    return comb(2 * n, n) // (n + 1)


def predicted_count(q, r):
    # Number of nonempty concatenations of r primitive Dyck excursions.
    return factorial(q) * r * comb(2 * q - r, q) // (2 * q - r)


def reciprocal_coefficients(qmax, power):
    """Coefficients of 1/(1-2**power*z*C(z)) modulo z**(qmax+1)."""
    a = [1] + [0] * qmax
    for n in range(1, qmax + 1):
        a[n] = (2**power) * sum(catalan(j - 1) * a[n - j]
                                     for j in range(1, n + 1))
    return a


def main():
    num_words = 0
    num_shuffles = 0
    for q in range(1, 6):
        hist = Counter()
        for w in words_with_each_letter_twice(q):
            num_words += 1
            direct = direct_witness_count(w)
            r = dyck_returns_or_none(w)
            predicted = 0 if r is None else 2**(r - 1)
            assert direct == predicted, (q, w, direct, predicted)
            if r is not None:
                hist[r] += 1
                num_shuffles += 1
        assert sum(hist.values()) == factorial(q) * catalan(q)
        for r in range(1, q + 1):
            assert hist[r] == predicted_count(q, r), (q, r)
        assert sum(hist[r] * 2**(r-1) for r in hist) == (factorial(q) *
                  comb(2*q, q) // 2)
        assert hist[1] == factorial(q) * catalan(q - 1)
        print('q={} shuffle_squares={} witness_classes={}'.format(
            q, sum(hist.values()), {2**(r-1): hist[r] for r in sorted(hist)}))

    qmax = 32
    coeff_first = reciprocal_coefficients(qmax, 1)
    coeff_second = reciprocal_coefficients(qmax, 2)
    for q in range(1, qmax + 1):
        assert coeff_first[q] == comb(2*q, q)
        assert coeff_second[q] == sum(4**r * predicted_count(q, r)
            // factorial(q) for r in range(1, q + 1))
        # Since the numerator counts 4**r, E[M^2] = this / (4*C_q).
    print('COMPLETE:', num_words, 'candidate words,', num_shuffles,
          'shuffle-square words, and 64 exact generating-function checks')

if __name__ == '__main__':
    main()

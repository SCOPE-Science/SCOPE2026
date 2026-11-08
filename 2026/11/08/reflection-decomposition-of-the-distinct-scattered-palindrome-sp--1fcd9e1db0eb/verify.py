#!/usr/bin/env python3
"""Reproduce the finite language and graded-coefficient checks for mirror hosts.

This is a finite check of examples, not a proof of the general theorem.
"""
from itertools import product
from collections import Counter


def subseq(s):
    result = {()}
    for letter in s:
        previous = tuple(result)
        result.update(v + (letter,) for v in previous)
    return result


def expected_languages(a, center, s):
    even = {v + v[::-1] for v in s if v}
    off_center = {v[:-1] + (v[-1],) + v[:-1][::-1] for v in s if v}
    even_host = even | off_center
    odd_host = even | {v + (center,) + v[::-1] for v in s}
    odd_host |= {v[:-1] + (v[-1],) + v[:-1][::-1]
                 for v in s if v and v[-1] != center}
    return even_host, odd_host


def poly_counts(words):
    return Counter(map(len, words))


def check_case(a, alphabet_size):
    s = subseq(a)
    even_direct = {v for v in subseq(a + a[::-1]) if v and v == v[::-1]}
    c_by_length = Counter(len(v) for v in s if v)
    for center in range(alphabet_size):
        even_expected, odd_expected = expected_languages(a, center, s)
        assert even_direct == even_expected, ("even", a, center)
        odd_direct = {v for v in subseq(a + (center,) + a[::-1])
                      if v and v == v[::-1]}
        assert odd_direct == odd_expected, ("odd", a, center)
        even_by_length = poly_counts(even_direct)
        odd_by_length = poly_counts(odd_direct)
        e_by_length = Counter(len(v) for v in s if v and v[-1] == center)
        for m in range(1, len(a) + 1):
            assert even_by_length[2*m] == c_by_length[m]
            assert even_by_length[2*m-1] == c_by_length[m]
            assert odd_by_length[2*m] == c_by_length[m]
        assert odd_by_length[1] == 1 + c_by_length[1] - e_by_length[1]
        for m in range(1, len(a) + 1):
            assert odd_by_length[2*m+1] == (
                c_by_length[m] + c_by_length[m+1] - e_by_length[m+1]
            )
        assert sum(even_by_length.values()) == 2 * sum(c_by_length.values())
        assert sum(odd_by_length.values()) == (
            3 * sum(c_by_length.values()) + 1 - sum(e_by_length.values())
        )
    return alphabet_size


def main():
    configs = ((2, 7), (3, 6), (4, 5))
    half_words = 0
    hosts = 0
    for alphabet_size, max_half_length in configs:
        for n in range(max_half_length + 1):
            for a in product(range(alphabet_size), repeat=n):
                check_case(a, alphabet_size)
                half_words += 1
                hosts += 1 + alphabet_size
    print(f"VERIFY_OK half_words={half_words} hosts={hosts} language_equalities_and_graded_counts")


if __name__ == "__main__":
    main()

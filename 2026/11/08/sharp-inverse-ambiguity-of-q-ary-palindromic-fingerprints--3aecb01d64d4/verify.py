"""Exhaustive finite checks of maximal palindromic-fingerprint fiber sizes.

No external modules are needed. This is evidence only for the stated finite ranges;
the all-length statement follows from the separate mathematical proof.
"""
from collections import Counter
from itertools import product


def radius_signature(word):
    n = len(word)
    radii = []
    for center in range(2 * n - 1):
        if center % 2 == 0:
            lo = hi = center // 2
        else:
            lo, hi = center // 2, center // 2 + 1
        radius = 0
        while lo >= 0 and hi < n and word[lo] == word[hi]:
            radius += 1
            lo -= 1
            hi += 1
        radii.append(radius)
    return tuple(radii)


def palindrome_interval_signature(word):
    """Independent signature by explicitly testing all substrings."""
    n = len(word)
    maxima = [0] * (2 * n - 1)
    for left in range(n):
        for right in range(left, n):
            sub = word[left:right + 1]
            if sub == sub[::-1]:
                k = left + right
                r = (right - left + 2) // 2
                maxima[k] = max(maxima[k], r)
    return tuple(maxima)


def verify(q, n):
    profile_counts = Counter()
    palindrome_free = 0
    initial = None
    for w in product(range(q), repeat=n):
        sig = radius_signature(w)
        profile_counts[sig] += 1
        if initial is None:
            initial = sig
        if all(w[i] != w[i - 1] for i in range(1, n)) and all(w[i] != w[i - 2] for i in range(2, n)):
            palindrome_free += 1
            if sig != tuple(1 if j % 2 == 0 else 0 for j in range(2 * n - 1)):
                raise AssertionError(('free-word signature mismatch', q, n, w, sig))
    target = q * (q - 1) * (q - 2) ** (n - 2)
    maxval = max(profile_counts.values())
    maximizers = [k for k, count in profile_counts.items() if count == maxval]
    expected_sig = tuple(1 if j % 2 == 0 else 0 for j in range(2 * n - 1))
    assert maxval == target, (q, n, maxval, target)
    assert maximizers == [expected_sig], (q, n, len(maximizers), maximizers[:2])
    assert palindrome_free == target, (q, n, palindrome_free, target)
    # Separate interval definition of the signature, on distinct exhaustive subrange.
    if q ** n <= 262144:
        for w in product(range(q), repeat=n):
            assert radius_signature(w) == palindrome_interval_signature(w), (q, n, w)
    print(f'PASS q={q} n={n} words={q**n} profiles={len(profile_counts)} maxfiber={maxval} unique=1')


def main():
    for q, max_n in [(4, 9), (5, 8), (6, 7)]:
        for n in range(2, max_n + 1):
            verify(q, n)
    print('FINITE_ENUMERATION_PASS')


if __name__ == '__main__':
    main()

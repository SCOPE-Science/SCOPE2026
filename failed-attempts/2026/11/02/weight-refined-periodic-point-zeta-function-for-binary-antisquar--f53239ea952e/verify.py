#!/usr/bin/env python3
"""Exact finite checks for the binary periodic antisquare-avoiding enumeration."""
from collections import Counter
from itertools import product

FORBIDDEN = ('0011', '0110', '1001', '1100', '010101', '101010', '001011', '110100')


def cyclic_avoids_forbidden(word):
    n = len(word)
    extension = word * (1 + (n + 5) // n)
    return not any(extension[i:i + len(p)] == p
                   for i in range(n) for p in FORBIDDEN)


def no_nontrivial_antisquare(word):
    n = len(word)
    extension = word * (3 + (2 * n + 2) // n)
    for order in range(2, n + 2):
        for i in range(n):
            left = extension[i:i + order]
            right = extension[i + order:i + 2 * order]
            if all(a != b for a, b in zip(left, right)):
                return False
    return True


def compatible_run_structure(word):
    n = len(word)
    if len(set(word)) == 1:
        return True
    start = next(i for i in range(n) if word[i] != word[(i - 1) % n])
    seq = ''.join(word[(start + j) % n] for j in range(n))
    runs = []
    for c in seq:
        if not runs or runs[-1][0] != c:
            runs.append([c, 1])
        else:
            runs[-1][1] += 1
    long = [i for i, (_, length) in enumerate(runs) if length >= 3]
    if not long or len({runs[i][0] for i in long}) != 1:
        return False
    if any(length != 1 and length < 3 for _, length in runs):
        return False
    return all(((long[(j + 1) % len(long)] - long[j]) % len(runs) or len(runs)) in (2, 4)
               for j in range(len(long)))


def predicted_profiles(max_n):
    # Coefficients of (1 - z - u z^4 - u^2 z^6)^(-1).
    a = [Counter() for _ in range(max_n + 1)]
    # Coefficients of (1 - u z - u^3 z^4 - u^4 z^6)^(-1).
    b = [Counter() for _ in range(max_n + 1)]
    a[0][0] = b[0][0] = 1
    for n in range(1, max_n + 1):
        for j, w in ((1, 0), (4, 1), (6, 2)):
            if n >= j:
                for k, v in a[n - j].items():
                    a[n][k + w] += v
        for j, w in ((1, 1), (4, 3), (6, 4)):
            if n >= j:
                for k, v in b[n - j].items():
                    b[n][k + w] += v
    result = [Counter() for _ in range(max_n + 1)]
    for n in range(1, max_n + 1):
        for j, w, multiplier in ((1, 0, 1), (4, 1, 4), (6, 2, 6)):
            if n >= j:
                for k, v in a[n - j].items():
                    result[n][k + w] += multiplier * v
        for j, w, multiplier in ((1, 1, 1), (4, 3, 4), (6, 4, 6)):
            if n >= j:
                for k, v in b[n - j].items():
                    result[n][k + w] += multiplier * v
    return result


def mobius(n):
    prime_factors = 0
    p = 2
    while p * p <= n:
        if n % p == 0:
            n //= p
            if n % p == 0:
                return 0
            prime_factors += 1
        p += 1
    return (-1) ** (prime_factors + (n > 1))


def primitive_orbit_profile(n):
    seen = set()
    profile = Counter()
    for bits in product('01', repeat=n):
        w = ''.join(bits)
        if not cyclic_avoids_forbidden(w):
            continue
        rotations = [w[i:] + w[:i] for i in range(n)]
        rep = min(rotations)
        if rep in seen or len(set(rotations)) != n:
            continue
        seen.add(rep)
        profile[w.count('1')] += 1
    return profile


def verify():
    predictions = predicted_profiles(80)
    checked = 0
    for n in range(1, 15):
        tally = Counter()
        for bits in product('01', repeat=n):
            word = ''.join(bits)
            direct = no_nontrivial_antisquare(word)
            finite = cyclic_avoids_forbidden(word)
            structural = compatible_run_structure(word)
            assert direct == finite == structural, (n, word, direct, finite, structural)
            if direct:
                tally[word.count('1')] += 1
            checked += 1
        assert tally == predictions[n], (n, tally, predictions[n])
    # The univariate period-n counts satisfy the characteristic recurrence.
    counts = [0] + [sum(predictions[n].values()) for n in range(1, 81)]
    assert counts[1:17] == [2, 2, 2, 10, 12, 26, 30, 42, 56, 92, 134, 202, 288, 422, 612, 906]
    for n in range(7, 81):
        assert counts[n] == counts[n - 1] + counts[n - 4] + counts[n - 6]
    # Primitive necklace polynomials follow from weighted Möbius inversion.
    for n in range(1, 13):
        orbit = Counter()
        for d in range(1, n + 1):
            if n % d:
                continue
            mu = mobius(d)
            for weight, v in predictions[n // d].items():
                orbit[d * weight] += mu * v
        assert all(v % n == 0 for v in orbit.values())
        orbit = Counter({k: v // n for k, v in orbit.items() if v})
        assert orbit == primitive_orbit_profile(n), (n, orbit, primitive_orbit_profile(n))
    # The support omits all balanced nonconstant profiles.
    for n in range(1, 81):
        assert all(k == 0 or k == n or 3 * k <= n or 3 * (n - k) <= n
                   for k, a in predictions[n].items() if a)
        assert predictions[n][0] == predictions[n][n] == 1
    print('VERIFY_OK: exhaustive direct antisquares/forbidden factors/grammar/weights through n=14')
    print('SOURCE_WORDS_CHECKED', checked)
    print('PRIMITIVE_NECKLACE_WEIGHTS_CHECKED_THROUGH_N', 12)
    print('RECURRENCE_AND_DENSITY_CHECKED', 80)
    print('COUNTS', counts[1:17])


if __name__ == '__main__':
    verify()

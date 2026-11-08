#!/usr/bin/env python3
"""Independent finite checks of the exact Rule 150 necklace inverse-degree law.
Only standard-library Python is required. The universal proof is in RESULT.md.
"""
from collections import Counter, defaultdict
from math import gcd


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def mobius(n):
    c, q, p = 0, n, 2
    while p * p <= q:
        if q % p == 0:
            q //= p
            c += 1
            if q % p == 0:
                return 0
            while q % p == 0:
                q //= p
        p += 1
    if q > 1:
        c += 1
    return (-1) ** c


def totient(n):
    return sum(gcd(j, n) == 1 for j in range(1, n + 1))


def rotation(x, n, k):
    k %= n
    return ((x << k) | (x >> (n-k))) & ((1 << n) - 1) if k else x


def necklace(x, n):
    return min(rotation(x, n, k) for k in range(n))


def rule150(x, n):
    return x ^ rotation(x, n, 1) ^ rotation(x, n, -1)


def smallest_period(x, n):
    for p in divisors(n):
        if rotation(x, n, p) == x:
            return p
    raise AssertionError("no period")


def parity_triplet(x, n):
    out = [0, 0, 0]
    for i in range(n):
        out[i % 3] ^= (x >> i) & 1
    return out


def is_in_image(x, n):
    if n % 3:
        return True
    a, b, c = parity_triplet(x, n)
    return a == b == c


def predicted_degree(y, n):
    if n % 3:
        return 1
    if not is_in_image(y, n):
        return 0
    p = smallest_period(y, n)
    if p % 3:
        return 2
    block = y & ((1 << p) - 1)
    return 4 if is_in_image(block, p) else 2


def fixed_image_count(n, d):
    assert n % 3 == 0 and n % d == 0
    if d % 3 or (n // d) % 2 == 0:
        return 2 ** d
    return 2 ** (d - 2)


def primitive_image_count(n, p):
    return sum(mobius(p // d) * fixed_image_count(n, d) for d in divisors(p))


def predicted_histogram(n):
    total_necklaces = sum(totient(n // d) * (2 ** d) for d in divisors(n)) // n
    if n % 3:
        return Counter({1: total_necklaces})
    number_image_necklaces = sum(primitive_image_count(n, p) // p for p in divisors(n))
    number_degree4 = sum(primitive_image_count(p, p) // p for p in divisors(n) if p % 3 == 0)
    hist = Counter({0: total_necklaces-number_image_necklaces,
                    2: number_image_necklaces-number_degree4,
                    4: number_degree4})
    return +hist


def exhaustive_test(n):
    incoming = defaultdict(set)
    for x in range(2**n):
        y = necklace(rule150(x, n), n)
        incoming[y].add(necklace(x, n))
    necklaces = {necklace(y, n) for y in range(2**n)}
    hist = Counter()
    for y in necklaces:
        actual = len(incoming[y])
        expected = predicted_degree(y, n)
        assert actual == expected, ("fiber", n, y, actual, expected)
        hist[actual] += 1
    hist = +hist
    expected_hist = predicted_histogram(n)
    assert hist == expected_hist, ("census", n, hist, expected_hist)
    return len(necklaces), hist


def main():
    results = []
    for n in range(1, 19):
        classes, hist = exhaustive_test(n)
        results.append((n, classes, dict(sorted(hist.items()))))
        print(f"n={n:2d} necklaces={classes:6d} inverse_degree_counts={dict(sorted(hist.items()))}")
    for n in range(3, 61, 3):
        hist = predicted_histogram(n)
        assert all(k in (0,2,4) for k in hist)
        assert sum(hist.values()) == sum(totient(n//d)*2**d for d in divisors(n))//n
    assert all(predicted_histogram(3**j).get(2, 0) == 2 for j in range(1, 4))
    print("VERIFY_OK exhaustive_lengths=1..18 formula_censuses=3,6,..,60")

if __name__ == '__main__':
    main()

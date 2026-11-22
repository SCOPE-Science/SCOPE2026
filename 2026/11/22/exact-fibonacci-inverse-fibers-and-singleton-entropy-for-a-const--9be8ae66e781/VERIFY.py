"""Finite checks for a cyclic binary local-AND channel, using Python standard library.

Run with: python3 VERIFY.py
The mathematical argument in RESULT.md applies to all n; enumeration only checks small n.
"""
from collections import Counter
from math import comb


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def expected_fiber(y):
    n = len(y)
    ones = [i for i, v in enumerate(y) if v]
    if not ones:
        return fib(n - 1) + fib(n + 1)
    gaps = ([n] if len(ones) == 1 else
            [(ones[(i + 1) % len(ones)] - ones[i]) % n
             for i in range(len(ones))])
    if min(gaps) < 3:
        return 0
    product = 1
    for gap in gaps:
        product *= fib(gap - 2)
    return product


def image_count_formula(n):
    return 1 + sum(n * comb(n - 2 * k - 1, k - 1) // k
                   for k in range(1, n // 3 + 1))


def singleton_count_formula(n):
    return sum(n * comb(k, n - 3 * k) // k
               for k in range((n + 3) // 4, n // 3 + 1))


def brute_fibers(n):
    counts = Counter()
    for word in range(1 << n):
        x = tuple((word >> i) & 1 for i in range(n))
        if any(x[i] and x[(i + 1) % n] and x[(i + 2) % n]
               for i in range(n)):
            continue
        output = sum((x[i] & x[(i + 1) % n]) << i for i in range(n))
        counts[output] += 1
    return counts


def main():
    tested = 0
    for n in range(5, 18):
        counts = brute_fibers(n)
        for raw in range(1 << n):
            y = tuple((raw >> i) & 1 for i in range(n))
            assert expected_fiber(y) == counts.get(raw, 0), (n, raw)
        assert len(counts) == image_count_formula(n)
        assert sum(c == 1 for c in counts.values()) == singleton_count_formula(n)
        assert counts[0] == fib(n - 1) + fib(n + 1)
        assert all(counts[0] > c for raw, c in counts.items() if raw)
        assert all(c <= fib(n - 2) for raw, c in counts.items() if raw)
        assert sum(c == fib(n - 2) for raw, c in counts.items() if raw) == n
        tested += 1 << n
    # Independent recurrence evaluations of the two rational trace series.
    image = [0] * 123
    single = [0] * 123
    # T(z) = (z+3z^3)/(1-z-z^3)
    # U(z) = (3z^3+4z^4)/(1-z^3-z^4)
    for n in range(1, 123):
        image[n] = ((image[n - 1] if n >= 2 else 0) +
                    (image[n - 3] if n >= 4 else 0) +
                    (1 if n == 1 else 3 if n == 3 else 0))
        single[n] = ((single[n - 3] if n >= 4 else 0) +
                     (single[n - 4] if n >= 5 else 0) +
                     (3 if n == 3 else 4 if n == 4 else 0))
    for n in range(5, 123):
        assert image[n] == image_count_formula(n), n
        assert single[n] == singleton_count_formula(n), n
    print('PASS: all cyclic inputs and all possible outputs at lengths 5..17; '
          'image and singleton rational identities at lengths 5..122; '
          'unique largest and exact runner-up fibers. '
          f'Tested {tested:,} output possibilities.')


if __name__ == '__main__':
    main()

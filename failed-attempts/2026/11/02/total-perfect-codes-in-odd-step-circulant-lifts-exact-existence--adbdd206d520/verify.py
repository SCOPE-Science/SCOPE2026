"""Finite independent checks of the stated odd-step circulant total-code theorem.

This program is supporting evidence only; the all-parameter result has a proof.
Usage: python3 verify.py
"""
from itertools import product


def offsets(r):
    m = 2 * r
    return tuple(range(1 - m, m, 2))


def is_total_perfect(bits, r):
    n = len(bits)
    jumps = offsets(r)
    return all(sum(bits[(i + s) % n] for s in jumps) == 1 for i in range(n))


def literal_count(n, r):
    count = 0
    for mask in range(1 << n):
        a = [(mask >> j) & 1 for j in range(n)]
        if is_total_perfect(a, r):
            count += 1
    return count


def seed_recurrence_count(n, r):
    """Enumerate all length-n candidate binaries without assuming periodicity."""
    m = 2 * r
    jumps = offsets(r)
    count = 0
    for seed in product((0, 1), repeat=2 * m - 2):
        bits = list(seed)
        for i in range(m - 1, n - m + 1):
            value = 1 - sum(bits[i + s] for s in jumps[:-1])
            if value not in (0, 1):
                break
            bits.append(value)
        if len(bits) == n and is_total_perfect(bits, r):
            count += 1
    return count


def predicted_count(n, r):
    return (2 * r) ** 2 if n % (4 * r) == 0 else 0


def canonical_codes(n, r):
    modulus = 4 * r
    evens = range(0, modulus, 2)
    odds = range(1, modulus, 2)
    for a, b in product(evens, odds):
        yield tuple(int(i % modulus in (a, b)) for i in range(n))


def main():
    literal_cases = [(8, 2), (9, 2), (10, 2), (12, 2), (12, 3), (16, 4)]
    for n, r in literal_cases:
        actual = literal_count(n, r)
        expected = predicted_count(n, r)
        assert actual == expected, (n, r, actual, expected)
    print('LITERAL_SUBSET_ENUMERATION_OK', len(literal_cases))

    num_seed_cases = 0
    for r in (1, 2, 3, 4):
        m = 2 * r
        cases = range(2 * m, 5 * m + 1) if r <= 3 else (16, 17, 18, 20, 24, 32)
        for n in cases:
            actual = seed_recurrence_count(n, r)
            expected = predicted_count(n, r)
            assert actual == expected, (r, n, actual, expected)
            num_seed_cases += 1
    print('SEED_RECURRENCE_ENUMERATION_OK', num_seed_cases)

    num_constructions = 0
    for r in range(1, 13):
        for multiple in (1, 2, 3):
            n = 4 * r * multiple
            codes = tuple(canonical_codes(n, r))
            assert len(codes) == (2 * r) ** 2
            assert len(set(codes)) == len(codes)
            for c in codes:
                assert sum(c) == n // (2 * r)
                assert is_total_perfect(c, r), (r, n)
                num_constructions += 1
    print('CANONICAL_CONSTRUCTIONS_OK', num_constructions)
    print('VERIFY_OK')


if __name__ == '__main__':
    main()

"""Independent checks for fixed-frequency scattered 001 enumeration.
Python 3 standard library. All assertions are exact integer checks.
"""
from collections import Counter, defaultdict
from itertools import product
from math import comb


def triangular_profiles(k):
    """Yield (largest zero-gap index, number of marked ones) for each partition."""
    assert k >= 1
    jmax = 2
    while (jmax + 1) * jmax // 2 <= k:
        jmax += 1

    def visit(j, remain, counts):
        if j > jmax:
            if remain == 0:
                top = max(i for i, r in counts if r)
                yield top, sum(r for _, r in counts)
            return
        weight = j * (j - 1) // 2
        for r in range(remain // weight + 1):
            yield from visit(j + 1, remain - weight * r, counts + [(j, r)])

    yield from visit(2, k, [])


def polynomial(k, n):
    # Evaluation of the actual eventual quadratic polynomial at every integer n,
    # including n where binomial coefficients have negative arguments.
    return sum((n - top - parts + 2) * (n - top - parts + 1) // 2
               for top, parts in triangular_profiles(k))


def exact_coefficient(k, n):
    return sum((n - top - parts + 2) * (n - top - parts + 1) // 2
               for top, parts in triangular_profiles(k)
               if n >= top + parts)


def scattered001(word):
    zeros = pairs00 = count = 0
    for letter in word:
        if letter == 0:
            pairs00 += zeros
            zeros += 1
        else:
            count += pairs00
    return count


def independent_dp(nmax, kmax):
    # Direct streaming automaton, no gap/partition structure used.
    # State is (#zeros, #00 subsequences capped, #001 subsequences capped).
    cap = kmax + 1
    current = {(0, 0, 0): 1}
    for n in range(nmax + 1):
        counts = Counter()
        for (_, _, k), ways in current.items():
            counts[k] += ways
        yield n, counts
        next_dp = defaultdict(int)
        for (z, pairs, k), ways in current.items():
            next_dp[(z + 1, min(cap, pairs + z), k)] += ways
            next_dp[(z, pairs, min(cap, k + pairs))] += ways
        current = next_dp


def test():
    direct_cases = 0
    for n in range(14):
        freq = Counter(scattered001(w) for w in product((0, 1), repeat=n))
        for k in range(1, 21):
            assert freq[k] == exact_coefficient(k, n), (n, k, freq[k])
            direct_cases += 1

    dp_cases = 0
    for n, counts in independent_dp(48, 15):
        for k in range(1, 16):
            assert counts[k] == exact_coefficient(k, n), (n, k, counts[k])
            dp_cases += 1

    sharp_cases = 0
    for k in range(1, 41):
        assert polynomial(k, k - 1) - exact_coefficient(k, k - 1) == 1, k
        for n in range(k, k + 6):
            assert polynomial(k, n) == exact_coefficient(k, n), (n, k)
            sharp_cases += 1
        assert sum(1 for _ in triangular_profiles(k)) > 0

    print(f'PASS direct={direct_cases}; independent_dp={dp_cases}; '
          f'eventual_quadratic={sharp_cases}; sharp_preboundary=40')


if __name__ == '__main__':
    test()

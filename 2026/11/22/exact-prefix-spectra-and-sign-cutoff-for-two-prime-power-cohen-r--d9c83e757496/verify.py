"""Independent finite checks for the prefix spectrum of Cohen--Ramanujan sums.

Run with Python 3.9 or later: python verify.py
This is finite corroboration; the published proof covers arbitrary parameters.
"""
from collections import Counter
from itertools import combinations, product
from math import prod


def mobius(m):
    sign = 1
    d = 2
    while d * d <= m:
        if m % d == 0:
            m //= d
            if m % d == 0:
                return 0
            sign = -sign
        d += 1
    if m > 1:
        sign = -sign
    return sign


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def direct_c(n, k, s, divs):
    # Cohen's independent divisor formula, not the two-prime factorization.
    return sum(d ** s * mobius(k // d) for d in divs if n % (d ** s) == 0)


def predicted(p, a, q, b, s):
    P, Q = p ** s, q ** s
    H = p ** ((a - 1) * s) * q ** ((b - 1) * s)
    k = p ** a * q ** b
    nmax = k ** s
    assert nmax == H * P * Q
    # Exact value -> multiplicity dictionary over n=0,...,k**s-1.
    counts = {}
    for j in range(P):
        for r in range(P):
            count_t = ((j + 1) * Q - 1 - r) // P - (j * Q - 1 - r) // P
            assert count_t >= 1
            value = H * (r - j * Q)
            assert value not in counts
            counts[value] = H * count_t
    assert len(counts) == P ** 2
    assert sum(counts.values()) == nmax
    return counts


def check_one(p, a, q, b, s):
    k = p ** a * q ** b
    L = k ** s
    P, Q = p ** s, q ** s
    H = p ** ((a - 1) * s) * q ** ((b - 1) * s)
    expected = predicted(p, a, q, b, s)
    divs = divisors(k)
    frequencies = Counter()
    cumulative = 0
    frequencies[0] += 1  # at n=0
    for n in range(1, L):
        cumulative += direct_c(n, k, s, divs)
        frequencies[cumulative] += 1
        # The closed formula is separately checked at every index.
        t = n // H
        assert cumulative == H * ((t % P) - Q * (t // Q)), (p,a,q,b,s,n,cumulative)
    assert dict(frequencies) == expected, (p,a,q,b,s)
    assert min(frequencies) == -H * Q * (P - 1)
    assert max(frequencies) == H * (P - 1)
    assert len(frequencies) == P * P
    assert cumulative + direct_c(L, k, s, divs) == 0
    return L


def main():
    primes = [2, 3, 5, 7]
    cases = 0
    indices = 0
    for p, q in combinations(primes, 2):
        for a, b, s in product(range(1, 4), range(1, 4), range(1, 4)):
            if (p ** a * q ** b) ** s > 150000:
                continue
            indices += check_one(p, a, q, b, s)
            cases += 1
    print(f"PASS: {cases} parameter tuples, {indices} prefix indices, divisor-formula cross-check")
    print("PASS: complete value bands, multiplicities, extrema, and zero-period sum")


if __name__ == '__main__':
    main()

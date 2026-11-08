"""Independent finite checks of cyclic dinucleotide reconstruction ambiguity.
Only standard-library Python 3 is required. These are finite corroborations, not an infinite proof.
"""
from collections import defaultdict
from itertools import product
from math import gcd, comb, pi


def phi(m):
    return sum(gcd(j, m) == 1 for j in range(1, m + 1))


def necklaces_by_pair_profile(n):
    classes = defaultdict(set)
    for symbols in product('01', repeat=n):
        w = ''.join(symbols)
        necklace = min(w[j:] + w[:j] for j in range(n))
        freq = tuple(sum(w[i] == str(s) and w[(i + 1) % n] == str(t)
                         for i in range(n))
                     for s, t in [(0,0),(0,1),(1,0),(1,1)])
        classes[freq].add(necklace)
    return classes


def exact_ambiguity(a, b, d):
    if b == 0:
        return int((a == 0) != (d == 0))
    total = 0
    for ell in range(1, b + 1):
        if a % ell == b % ell == d % ell == 0:
            q = b // ell
            total += phi(ell) * comb(a // ell + q - 1, q - 1) * comb(d // ell + q - 1, q - 1)
    assert total % b == 0
    return total // b


def arithmetic_max(n):
    result = 1
    for b in range(1, n // 2 + 1):
        for a in range(n - 2 * b + 1):
            d = n - 2 * b - a
            result = max(result, exact_ambiguity(a, b, d))
    return result


def main():
    for n in range(1, 16):
        classes = necklaces_by_pair_profile(n)
        for (a, b, b2, d), necklaces in classes.items():
            assert b == b2
            assert len(necklaces) == exact_ambiguity(a, b, d), (n, a, b, d)
        assert max(map(len, classes.values())) == arithmetic_max(n)
    for n in range(16, 65):
        assert arithmetic_max(n) >= 1
    for n in (40, 80, 120, 160):
        ratio = arithmetic_max(n) * n * n / (2 ** n)
        assert 1.1 < ratio < 4 / pi
    print('VERIFY_OK: exact necklace fibers n=1..15; arithmetic maxima n=1..160 at selected lengths')

if __name__ == '__main__':
    main()

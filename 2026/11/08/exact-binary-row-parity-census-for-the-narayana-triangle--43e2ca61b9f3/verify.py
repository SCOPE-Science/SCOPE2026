"""Finite reproducibility checks for parity statistics of Narayana triangle."""
from math import comb
from collections import Counter


def a_direct(n):
    return sum(((comb(n, k) * comb(n, k - 1) // n) & 1)
               for k in range(1, n + 1))


def a_formula(n):
    if n % 2 == 0:
        return 1 << n.bit_count()
    t = ((n + 1) & -(n + 1)).bit_length() - 1
    return (1 << (n.bit_count() - t)) * ((1 << t) - 1)


def spectrum(L):
    d = Counter()
    for s in range(1, L):
        d[1 << s] += comb(L - 1, s)
    for t in range(1, L):
        for h in range(L - t):
            d[(1 << t) - 1 << h] += comb(L - t - 1, h)
    d[(1 << L) - 1] += 1
    return d


def main():
    for n in range(1, 129):
        assert a_direct(n) == a_formula(n), n
    for L in range(1, 8):
        actual = Counter(a_direct(n) for n in range(1, 1 << L))
        assert actual == spectrum(L), L
        assert sum(v * m for v, m in actual.items()) == (5 * 3**(L - 1) - 3) // 2
    print('VERIFY_OK rows=128 dyadic_levels=7')


if __name__ == '__main__':
    main()

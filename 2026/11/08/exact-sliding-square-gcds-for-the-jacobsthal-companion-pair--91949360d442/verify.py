"""Exact, dependency-free finite cross-check for the Jacobsthal sliding-GCD formula."""
from math import gcd


def v2(n):
    e = 0
    while n % 2 == 0:
        n //= 2
        e += 1
    return e


def pair(kmax=700, nmax=12):
    cap = kmax + nmax + 2
    j = [0, 1]
    l = [2, 1]
    for i in range(2, cap + 1):
        j.append(j[-1] + 2*j[-2])
        l.append(l[-1] + 2*l[-2])
    comparisons = 0
    for k in range(1, kmax + 1):
        core = gcd(k, 2**k - (-1)**k)
        two = 1 << min(v2(k), 3)
        expected_j = two * core // (3 if k % 3 == 0 else 1)
        expected_l = two * core
        for seq, exp in ((j, expected_j), (l, expected_l)):
            pref = [0]
            for x in seq:
                pref.append(pref[-1] + x*x)
            g = 0
            for n in range(1, nmax + 1):
                g = gcd(g, pref[n+k] - pref[n])
            assert g == exp, (k, exp, g)
            comparisons += 1
    return comparisons


if __name__ == '__main__':
    result = pair()
    print(f'PASS: {result} direct exact-integer gcd comparisons; 700 lengths, two companion sequences, 12 shifts.')
    print('FINITE checks only; all-length proof is in RESULT.md.')

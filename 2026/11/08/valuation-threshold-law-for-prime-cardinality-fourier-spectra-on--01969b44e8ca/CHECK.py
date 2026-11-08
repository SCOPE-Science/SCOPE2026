"""Exact-integer finite checks for prime-cardinality cyclic Fourier spectra.

Run: python CHECK.py
No third-party dependencies.  General claims are proved analytically.
"""
from itertools import combinations, product
from math import gcd
from functools import lru_cache


def trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def divmonic(a, b):
    """Integer polynomial division (low-degree-first), monic divisor."""
    a = trim(a)
    b = trim(b)
    assert b[-1] == 1
    quotient = [0] * max(1, len(a) - len(b) + 1)
    while len(a) >= len(b) and a != [0]:
        shift = len(a) - len(b)
        factor = a[-1]
        quotient[shift] += factor
        for j, v in enumerate(b):
            a[j + shift] -= factor * v
        a = trim(a)
    return trim(quotient), trim(a)


@lru_cache(maxsize=None)
def cyclotomic(n):
    a = [-1] + [0] * (n - 1) + [1]
    for d in range(1, n):
        if n % d == 0:
            a, r = divmonic(a, cyclotomic(d))
            assert r == [0]
    return a


def exact_zero(A, h, N):
    c = [0] * N
    for a in A:
        c[(a * h) % N] += 1
    _, r = divmonic(c, cyclotomic(N))
    return r == [0]


def valuation(f, q, k):
    Q = q ** k
    d = Q
    for u in f:
        d = gcd(d, (u - f[0]) % Q)
    t = 0
    while t < k and d % q == 0:
        d //= q
        t += 1
    return t


def crt(a, p, b, Q):
    # Chinese remainder theorem: x ≡ a (mod p), x ≡ b (mod Q).
    return (a + p * (((b - a) * pow(p, -1, Q)) % Q)) % (p * Q)


def test(p, q, k, full_unrestricted=False):
    Q = q ** k
    N = p * Q
    maps = list(product(range(Q), repeat=p))
    graph = lambda f: tuple(crt(i, p, f[i], Q) for i in range(p))
    strata = {j: 0 for j in range(k + 1)}
    v = {f: valuation(f, q, k) for f in maps}
    for t in v.values():
        strata[t] += 1
    for t in range(k):
        assert strata[t] == Q * (q ** ((k-t) * (p-1)) - q ** ((k-t-1) * (p-1)))
    assert strata[k] == Q
    if full_unrestricted:
        subsets = list(combinations(range(N), p))
        count_spectral = 0
        pair_count = 0
        for A in subsets:
            zeros = {h for h in range(1, N) if exact_zero(A, h, N)}
            count = 0
            for B in subsets:
                if all(((b - a) % N) in zeros for a, b in combinations(B, 2)):
                    count += 1
            is_graph = len({a % p for a in A}) == p
            assert (count > 0) == is_graph
            if is_graph:
                count_spectral += 1
                f = tuple(next(a % Q for a in A if a % p == i) for i in range(p))
                assert count == q ** (k + (p-1) * v[f]), (p,q,k,A,count)
                pair_count += count
        assert count_spectral == Q ** p
    else:
        pair_count = 0
        for f in maps:
            A = graph(f)
            Z = {h for h in range(1, N) if exact_zero(A, h, N)}
            c = 0
            for g in maps:
                B = graph(g)
                passed = all(((b - a) % N) in Z for a, b in combinations(B, 2))
                assert passed == (v[f] + v[g] >= k)
                c += passed
            assert c == q ** (k + (p-1)*v[f])
            pair_count += c
    asserted = (k+1) * q ** (k * (p+1)) - k * q ** (k * (p+1) - (p-1))
    assert pair_count == asserted, (pair_count, asserted)
    print('PASS', (p,q,k), 'strata', strata, 'spectral_pairs', pair_count,
          'full_unrestricted', full_unrestricted)


if __name__ == '__main__':
    test(2, 3, 1, True)
    test(3, 2, 1, True)
    test(3, 2, 2, True)
    test(2, 3, 2, True)
    test(2, 5, 1, False)
    test(3, 2, 3, False)
    test(5, 2, 2, False)
    print('ALL_EXACT_CHECKS_PASSED')

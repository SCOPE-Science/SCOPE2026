"""Independent finite checks of inverse Lyndon prefix and border laws.

Run: python3 check.py
No external dependencies.
"""
from collections import Counter
from itertools import product
from math import isclose


def inverse_lyndon(w):
    return bool(w) and all(w > w[j:] for j in range(1, len(w)))


def anti_lyndon(w):
    return bool(w) and all(w > w[j:] + w[:j] for j in range(1, len(w)))


def longest_border(w):
    return max((j for j in range(1, len(w)) if w[:j] == w[-j:]), default=0)


def lyndon_counts(q, n):
    # Independent direct rotation test, not a formula lookup.
    return [0] + [sum(anti_lyndon(w) for w in product(range(q), repeat=k))
                  for k in range(1, n + 1)]


def prefix_by_root(w, roots):
    n = len(w)
    matches = []
    for root in roots:
        p = len(root)
        if all(w[j] == root[j % p] for j in range(n)):
            matches.append(root)
    return matches


def test(q, nmax):
    counts = lyndon_counts(q, nmax)
    total_words_examined = 0
    compared_array_words = 0
    for n in range(1, nmax + 1):
        roots = [w for k in range(1, n + 1)
                 for w in product(range(q), repeat=k) if anti_lyndon(w)]
        direct_count = 0
        border_hist = Counter()
        for w in product(range(q), repeat=n):
            total_words_examined += 1
            direct = inverse_lyndon(w)
            matches = prefix_by_root(w, roots)
            assert (len(matches) == 1) == direct, ('prefix classification', q, w, matches)
            if direct:
                direct_count += 1
                root = matches[0]
                b = longest_border(w)
                assert b == n - len(root), ('longest border', q, w, root, b)
                border_hist[b] += 1
        assert direct_count == sum(counts[1:n + 1]), ('total', q, n)
        assert all(border_hist[b] == counts[n-b] for b in range(n)), ('histogram', q, n)
        # Direct expectation over all q-ary strings, independently of the word-count formula.
        if n <= (8 if q == 2 else 6):
            brute_total = 0
            for w in product(range(q), repeat=n):
                compared_array_words += 1
                for i in range(n):
                    brute_total += max(k for k in range(1, n-i+1)
                                       if inverse_lyndon(w[i:i+k]))
            counts_prefix = [0] + [sum(counts[1:k+1]) for k in range(1,n+1)]
            formula_num = sum((n-k+1)*counts_prefix[k]*(q**(n-k))
                              for k in range(1,n+1))
            assert brute_total == formula_num, ('array mean', q, n, brute_total, formula_num)
    print(f'q={q}, all q-ary words of lengths 1..{nmax}: {total_words_examined} tested; '+
          f'direct array checks on {compared_array_words} words; OK')
    print(f'anti-Lyndon counts length 1..{nmax}: {counts[1:]}')
    print(f'inverse-Lyndon counts length 1..{nmax}: '+
          f'{[sum(counts[1:k+1]) for k in range(1,nmax+1)]}')

if __name__ == '__main__':
    test(2, 12)
    test(3, 8)


def mobius(x):
    n = x
    parity = 0
    p = 2
    while p*p <= n:
        if n % p == 0:
            n //= p
            if n % p == 0:
                return 0
            parity ^= 1
        p += 1
    if n > 1:
        parity ^= 1
    return (-1)**parity


def analyze(q, n):
    r = 0.0
    mean = 0.0
    mass = 0.0
    for k in range(1, n+1):
        # Aperiodic-necklace count divided by q**k.
        ratio = sum(mobius(d) * q**(-k*(1.0 - 1.0/d))
                    for d in range(1, k+1) if k % d == 0)/k
        r = r/q + ratio
        mean += r
        mass += (n-k+1)*r
    print(f'q={q} n={n} E[first inverse prefix length]={mean:.10f} '
          f'E[array length sum]={mass:.10f} '
          f'array normalized by n log n: {mass/(n*__import__("math").log(n)):.10f}')

if __name__ == '__main__':
    for q in (2,3):
        for n in (100, 1000):
            analyze(q,n)

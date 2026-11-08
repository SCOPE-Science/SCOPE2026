"""Independent finite tests for cyclic 2-binomial types and hypergeometric moments.
Run: python3 VERIFY.py. Finite tests are not a substitute for proofs.
"""
from itertools import combinations
from math import comb, gcd
from fractions import Fraction

def signature(v):
    ones = zeros = pairs = 0
    for x in v:
        if x == 0:
            zeros += 1
        else:
            ones += 1
            pairs += zeros
    return (ones, pairs)

def direct_types(w):
    return len({signature(w[s:] + w[:s]) for s in range(len(w))})

def balanced_halves(w):
    m = len(w) // 2
    h = sum(w) // 2
    return sum(sum((w + w)[s:s+m]) == h for s in range(m))

def exact_moments(m, h):
    den = comb(2*m, 2*h)
    p0 = comb(m,h)**2
    weighted_pairs = 0
    for d in range(1, m):
        paired = sum(comb(d,a)**2 * comb(m-d,h-a)**2
                     for a in range(max(0,h-(m-d)), min(d,h)+1))
        weighted_pairs += (m-d)*paired
    return Fraction(m*p0,den), Fraction(m*p0+2*weighted_pairs,den)

all_checked = 0
for m in range(2, 9):
    for h in range(1, m):
        if gcd(m,h) != 1:
            continue
        n = 2*m
        cc = []
        for indices in combinations(range(n), 2*h):
            w = tuple(1 if i in indices else 0 for i in range(n))
            T = direct_types(w)
            C = balanced_halves(w)
            assert T == n-C
            assert m <= T <= n-1
            assert (T == m) == (w[:m] == w[m:])
            cc.append(C)
            all_checked += 1
        mean,second = exact_moments(m,h)
        assert sum(cc) == mean * len(cc), (m,h,'mean')
        assert sum(c*c for c in cc) == second * len(cc), (m,h,'second')
        # One circular block of ones has precisely one equal-signature pair.
        cluster = tuple([1]*(2*h)+[0]*(2*m-2*h))
        assert direct_types(cluster) == n-1
print('DIRECT_TYPES_AND_BOTH_MOMENTS_OK', all_checked)

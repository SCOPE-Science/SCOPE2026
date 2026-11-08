"""Independent exact checks for binary 2-binomial-square counts.

No external packages. Run: python3 verify.py
"""
from collections import Counter
from math import comb, pi, sqrt


def gauss_coeffs(n):
    """All Gaussian-binomial polynomials [n choose k]_t as integer lists."""
    row = [[1]]
    for m in range(1, n + 1):
        next_row = []
        for k in range(m + 1):
            left = row[k] if k < len(row) else []
            right = row[k - 1] if k else []
            shift = m - k
            coeff = [0] * max(len(left), len(right) + shift)
            for i, v in enumerate(left):
                coeff[i] += v
            for i, v in enumerate(right):
                coeff[i + shift] += v
            next_row.append(coeff)
        row = next_row
        yield m, row


def direct_deck(w, n):
    ones = w.bit_count()
    zero_before = 0
    patterns_01 = 0
    for i in range(n):
        if w & (1 << i):
            patterns_01 += zero_before
        else:
            zero_before += 1
    return ones, patterns_01


CHECKS = {1: 2, 2: 4, 3: 8, 4: 18, 8: 1064,
          12: 122570, 20: 2944055592,
          30: 1385110798854440,
          40: 820922833348909830014}
values = {}
for n, polys in gauss_coeffs(100):
    count = sum(sum(c*c for c in p) for p in polys)
    if n in CHECKS:
        assert count == CHECKS[n], (n, count, CHECKS[n])
    if n <= 12:
        spectrum = Counter(direct_deck(w, n) for w in range(1 << n))
        direct = sum(v*v for v in spectrum.values())
        assert count == direct, (n, count, direct)
    if n in (20, 40, 60, 80, 100):
        ratio = (n*n*count)/(4**n)
        values[n] = ratio
        assert 1.0 < ratio < 2*sqrt(3)/pi
assert values[100] > values[20]
print('VERIFY_OK Gaussian-polynomial DP n=1..100; independent direct decks n=1..12; selected exact large integers')
for n in (20,40,60,80,100):
    print('scaled',n,'%.12f'%values[n])
print('limit','%.12f'%(2*sqrt(3)/pi))

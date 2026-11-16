"""Exact pentaphase STFT support census, standard Python 3 only.

Run: python3 verify_pentaphase.py
No floating point arithmetic or external data are used.
"""
from collections import Counter
from itertools import product

P = 5
NORMALIZED = [(0, *z) for z in product(range(P), repeat=4)]
EXPECTED = {5: 125, 17: 12500, 20: 12500, 21: 52500, 25: 313000}
PROFILES = {
    (0, 0, 0, 0, 0): 313000,
    (0, 0, 0, 0, 4): 2500,
    (0, 1, 1, 1, 1): 50000,
    (1, 1, 1, 1, 1): 12500,
    (1, 1, 1, 1, 4): 12500,
    (4, 4, 4, 4, 4): 125,
}

# The minimal polynomial Phi_5(X)=1+X+X^2+X^3+X^4 means
# a sum of five fifth roots of unity is zero iff all exponents occur once.
# Precompute zero-frequency counts for each normalized exponent word.
zero_frequency_count = {}
for v in NORMALIZED:
    n = sum(
        sorted((v[t] - k*t) % P for t in range(P)) == list(range(P))
        for k in range(P)
    )
    zero_frequency_count[v[1:]] = n
assert Counter(zero_frequency_count.values()) == {0: 520, 1: 100, 4: 5}

hist = Counter()
profiles = Counter()
single_row_counts = Counter()
for f in NORMALIZED:
    for g in NORMALIZED:
        row_zeros = []
        for shift in range(P):
            base = (f[0] - g[(-shift) % P]) % P
            v = tuple((f[t] - g[(t-shift) % P] - base) % P for t in range(1, P))
            row_zeros.append(zero_frequency_count[v])
        hist[25 - sum(row_zeros)] += 1
        profiles[tuple(sorted(row_zeros))] += 1
        single_row_counts[sum(z == 4 for z in row_zeros)] += 1
assert hist == EXPECTED, (hist, EXPECTED)
assert profiles == PROFILES, (profiles, PROFILES)
assert single_row_counts == {0: 375500, 1: 15000, 5: 125}
assert sum(hist.values()) == P**8
print('PENTAPHASE_CROSS_STFT_PASS', sum(hist.values()), sorted(hist.items()))
print('ROW_PROFILES', sorted(profiles.items()))
print('FOUR_ZERO_ROW_COUNTS', sorted(single_row_counts.items()))

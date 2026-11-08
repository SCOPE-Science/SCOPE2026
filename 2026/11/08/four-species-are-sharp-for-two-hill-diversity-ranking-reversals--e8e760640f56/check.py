"""Exact arithmetic checks for the sharp four-species diversity-profile result.

Run: python3 check.py  (Python standard library only).
The infinite zero-count and majorization arguments are supplied in RESULT.md.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations_with_replacement

P = (1, 9, 12, 18)
R = (3, 5, 16, 16)
assert len(P) == len(R) == 4 and sum(P) == sum(R) == 40


def moment_difference(a, b, q):
    return sum(x ** q for x in a) - sum(x ** q for x in b)


moments = [moment_difference(P, R, q) for q in (2, 3, 4)]
assert moments == [4, -54, 496], moments
assert moment_difference(P, R, 0) == 0
assert moment_difference(P, R, 1) == 0

# Combine equal bases before counting generalized-polynomial sign changes.
coef = defaultdict(int)
for x in P:
    coef[x] += 1
for x in R:
    coef[x] -= 1
ordered = sorted(((x, c) for x, c in coef.items() if c), reverse=True)
assert ordered == [(18, 1), (16, -2), (12, 1), (9, 1),
                   (5, -1), (3, -1), (1, 1)]
signs = [(c > 0) - (c < 0) for _, c in ordered]
variations = sum(a != b for a, b in zip(signs, signs[1:]))
assert variations == 4

# Check exact qth power-sum scaling under adding common positive species.
for S in (5, 6, 8, 12):
    t = Fraction(2, 3)
    extra = (Fraction(1, 3 * (S - 4)),) * (S - 4)
    a = tuple(t * Fraction(x, 40) for x in P) + extra
    b = tuple(t * Fraction(x, 40) for x in R) + extra
    assert len(a) == len(b) == S and sum(a) == sum(b) == 1
    assert all(x > 0 for x in a + b)
    for order in (2, 3, 4, 6):
        delta = sum(x ** order for x in a) - sum(x ** order for x in b)
        old = Fraction(moment_difference(P, R, order), 40 ** order)
        assert delta == t ** order * old

# A bounded, non-proving stress test of the ternary impossibility lemma.
# Every sorted positive integer triple with total 40 is examined.
triples = [t for t in combinations_with_replacement(range(1, 39), 3)
           if sum(t) == 40]

def majorizes(a, b):
    a = sorted(a, reverse=True)
    b = sorted(b, reverse=True)
    return a[0] >= b[0] and a[2] <= b[2]

pairs = 0
incomparable = 0
for i, a in enumerate(triples):
    for b in triples[i + 1:]:
        pairs += 1
        if majorizes(a, b) or majorizes(b, a):
            continue
        incomparable += 1
        co = defaultdict(int)
        for x in a:
            co[x] += 1
        for x in b:
            co[x] -= 1
        sg = [(c > 0) - (c < 0) for x, c in sorted(co.items()) if c]
        assert sum(x != y for x, y in zip(sg, sg[1:])) <= 3
        # For q>1, the Hill ordering reverses the moment-difference sign.
        nz = [s for q in range(2, 9)
              if (s := ((v := moment_difference(a, b, q)) > 0) - (v < 0))]
        assert sum(x != y for x, y in zip(nz, nz[1:])) <= 1

print("Exact moment differences at orders 2,3,4:", moments)
print("Sorted combined coefficients:", ordered)
print("Sign variations:", variations)
print("Ternary integer-profile pairs checked:", pairs)
print("Non-majorization ternary pairs checked:", incomparable)
print("Common-species extensions checked: 5, 6, 8, 12")
print("All exact checks passed; infinite claims use the analytic proof.")

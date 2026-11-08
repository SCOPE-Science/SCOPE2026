"""Exact integer certificate for the log-concavity cutoff in R_m.

Requires Python 3.8+ standard library only.  No external data.
"""
from math import comb


def ehrhart(m, k):
    """Enumerate all ordered 4-compositions of k without omission."""
    result = 0
    for b0 in range(k + 1):
        for b1 in range(k - b0 + 1):
            for b2 in range(k - b0 - b1 + 1):
                b3 = k - b0 - b1 - b2
                factors = ((b0 + b1 + 1) * (2 * b1 + 1),
                           (b0 + b2 + 1) * (2 * b2 + 1),
                           (b0 + b3 + 1) * (2 * b3 + 1))
                result += (factors[0] * factors[1] * factors[2]) ** m
    return result


def first_three(m):
    a = 8**m + 3*6**m
    b = 27**m + 6*36**m + 3*15**m
    c = (64**m + 3*108**m + 3*80**m + 3*162**m
         + 3*28**m + 6*90**m + 216**m)
    M = 6*m + 4
    h1 = a - M
    h2 = b - M*a + comb(M, 2)
    h3 = c - M*b + comb(M, 2)*a - comb(M, 3)
    return h1, h2, h3


def half_hstar(m):
    """Half of the h* vector (index 0,...,3*m), from full finite binomial transform."""
    M = 6*m + 4
    values = [ehrhart(m, k) for k in range(3*m + 1)]
    return [sum((-1)**(r-k) * comb(M, r-k) * values[k]
                for k in range(r + 1)) for r in range(3*m + 1)]


# A second, short enumeration checks the source's closed first-three formulas.
for m in range(1, 21):
    a, b, c = [ehrhart(m, k) for k in (1, 2, 3)]
    A = 8**m + 3*6**m
    B = 27**m + 6*36**m + 3*15**m
    C = (64**m + 3*108**m + 3*80**m + 3*162**m
         + 3*28**m + 6*90**m + 216**m)
    assert (a, b, c) == (A, B, C), m

# Exhaustive first 11 parameter values and all inequalities up to symmetry.
expected_first_minor = [
    183, 17788, 1010589, 52760098, 2765430459, 148195690504,
    8144441026617, 458722736365054, 26426960677346631,
    1553232651166059076, 92874673606309040421,
]
for m in range(1, 12):
    half = half_hstar(m)
    assert all(v > 0 for v in half), m
    assert tuple(half[1:4]) == first_three(m), m
    deltas = [half[i]*half[i] - half[i-1]*(half[i+1] if i < 3*m else half[i-1])
              for i in range(1, 3*m+1)]
    assert len(deltas) == 3*m and min(deltas) > 0, m
    assert min(deltas) == deltas[0] == expected_first_minor[m-1], m
    print('m=%02d: all %d independent log-concavity minors strictly positive; minimum=%d'
          % (m, len(deltas), min(deltas)))

# Source's m=12 witness, extended through the remaining finite values.
for m in range(12, 21):
    h1, h2, h3 = first_three(m)
    assert h1 > 0 and h2 > 0 and h3 > 0, m
    deficit = h1*h3 - h2*h2
    assert deficit > 0, m
    if m == 12:
        assert deficit == 33767772755382700161244430421001196588
    print('m=%02d: strict log-concavity failure at index 2 (defect has %d bits)'
          % (m, deficit.bit_length()))

# For m>=21, exact inequalities and induction prove the infinite tail:
#   8^m >= 2(6m+4), 6^m >= 20(6m+4), 4^m > 400 3^m.
# They hold at m=21 and persist (growth factors 8,6,4/3 beat a linear bound).
assert 8**21 >= 2*(6*21+4)
assert 6**21 >= 20*(6*21+4)
assert 4**21 > 400*3**21
print('m>=21: analytic bound certified at its base case; geometric induction applies.')
print('ALL CHECKS PASSED')

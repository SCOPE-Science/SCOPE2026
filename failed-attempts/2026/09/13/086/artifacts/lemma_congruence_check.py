"""Verify Lemma A: 12*s(h,k) - (h+hbar)/k is always an integer (h,hbar inverse mod k).
Also spot-checks Dedekind reciprocity used in the proof."""
from fractions import Fraction
import math, random

def saw(n, k):
    r = n % k
    if r == 0:
        return Fraction(0)
    return Fraction(r, k) - Fraction(1, 2)

def s(h, k):
    return sum(saw(r, k) * saw(h * r, k) for r in range(1, k + 1))

bad = 0
n = 0
for k in range(2, 61):
    for h in range(1, k):
        if math.gcd(h, k) != 1:
            continue
        n += 1
        H = pow(h, -1, k)
        if (12 * s(h, k) - Fraction(h + H, k)).denominator != 1:
            bad += 1
            print('FAIL', h, k)
random.seed(12345)
for k in [100, 500, 1000, 2000]:
    for _ in range(5):
        h = random.randint(1, k - 1)
        if math.gcd(h, k) != 1:
            continue
        n += 1
        H = pow(h, -1, k)
        if (12 * s(h, k) - Fraction(h + H, k)).denominator != 1:
            bad += 1
            print('FAIL', h, k)
print(f'congruence: {n} coprime pairs tested, failures = {bad}')

# Reciprocity spot checks: s(h,k)+s(k,h) == (h^2+k^2+1)/(12hk) - 1/4
for h, k in [(3, 7), (5, 11), (4, 9), (7, 29), (13, 40)]:
    lhs = s(h, k) + s(k, h)
    rhs = Fraction(h * h + k * k + 1, 12 * h * k) - Fraction(1, 4)
    assert lhs == rhs, (h, k, lhs, rhs)
print('reciprocity: 5 spot checks passed')

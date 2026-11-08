"""Exact checks for two-level specialist-network survivor convex ordering.

Run: python verify.py
Uses only Python standard library. Finite checks support (do not replace) the proof.
"""
from fractions import Fraction
from itertools import combinations
from math import comb


def partitions(total, length, floor=0):
    if length == 0:
        if total == 0:
            yield ()
        return
    for k in range(floor, total + 1):
        for rest in partitions(total - k, length - 1, k):
            yield (k,) + rest


def majorizes(high, low):
    high = sorted(high, reverse=True)
    low = sorted(low, reverse=True)
    assert sum(high) == sum(low)
    return all(sum(high[:i]) >= sum(low[:i]) for i in range(1, len(high)))


def polynomial_counts(loads, r):
    """Extract u^r z^k in product of [(1+u)^m + uz(1+uz)^m]."""
    coefficient = {(0, 0): 1}
    for m in loads:
        terms = [(j, 0, comb(m, j)) for j in range(m + 1)]
        terms += [(1 + j, 1 + j, comb(m, j)) for j in range(m + 1)]
        next_coefficient = {}
        for (old_r, old_k), weight in coefficient.items():
            for new_r, new_k, c in terms:
                if old_r + new_r > r:
                    continue
                key = old_r + new_r, old_k + new_k
                next_coefficient[key] = next_coefficient.get(key, 0) + weight * c
        coefficient = next_coefficient
    n = len(loads) + sum(loads)
    out = [coefficient.get((r, k), 0) for k in range(n + 1)]
    assert sum(out) == comb(n, r)
    return out


def brute_counts(loads, r):
    """Independent count by enumerating all fixed-size survivor subsets."""
    a = len(loads)
    n = a + sum(loads)
    out = [0] * (n + 1)
    for chosen in combinations(range(n), r):
        survivors = set(chosen)
        count = 0
        offset = a
        for i, b_i in enumerate(loads):
            if i in survivors:
                count += 1
                for j in range(b_i):
                    if offset + j in survivors:
                        count += 1
            offset += b_i
        out[count] += 1
    return out


def falling(n, k):
    ans = 1
    for i in range(k):
        ans *= n - i
    return ans


def q(n, r, k):
    return Fraction(falling(r, k), falling(n, k)) if k <= min(n, r) else Fraction(0)


def variance(hist):
    size = sum(hist)
    mean = Fraction(sum(k * v for k, v in enumerate(hist)), size)
    second = Fraction(sum(k*k*v for k, v in enumerate(hist)), size)
    return second - mean*mean


def stoploss(hist, strike):
    return sum(max(k - strike, 0) * v for k, v in enumerate(hist))


def check():
    dist_checks = 0
    ordered_pairs = 0
    stoploss_checks = 0
    variance_checks = 0
    strict_checks = 0
    for a in range(2, 6):
        for b in range(2, 8):
            N = a + b
            profiles = list(partitions(b, a))
            caches = {}
            for loads in profiles:
                for r in range(N + 1):
                    dp = polynomial_counts(loads, r)
                    enumeration = brute_counts(loads, r)
                    assert dp == enumeration, (a, b, loads, r)
                    caches[loads, r] = dp
                    dist_checks += 1
            for low in profiles:
                for high in profiles:
                    if low == high or not majorizes(high, low):
                        continue
                    ordered_pairs += 1
                    T_low = sum(comb(v, 2) for v in low)
                    T_high = sum(comb(v, 2) for v in high)
                    assert T_high > T_low
                    for r in range(N + 1):
                        x = caches[low, r]
                        y = caches[high, r]
                        assert sum(k*c for k, c in enumerate(x)) == sum(k*c for k, c in enumerate(y))
                        for strike in range(N + 1):
                            assert stoploss(x, strike) <= stoploss(y, strike), (a,b,low,high,r,strike)
                            stoploss_checks += 1
                        vgap = variance(y) - variance(x)
                        expected = 2 * (T_high-T_low) * (q(N,r,3)-q(N,r,4))
                        assert vgap == expected, (a,b,low,high,r,vgap,expected)
                        variance_checks += 1
                        if 3 <= r < N:
                            assert vgap > 0
                            strict_checks += 1
                        else:
                            assert x == y
    assert polynomial_counts((2,1),3) == [1,1,4,4,0,0]
    assert polynomial_counts((3,0),3) == [1,3,0,6,0,0]
    assert variance(polynomial_counts((3,0),3)) - variance(polynomial_counts((2,1),3)) == Fraction(2,5)
    print('PASS exact distribution independently enumerated:',dist_checks)
    print('PASS distinct majorization pairs:',ordered_pairs)
    print('PASS convex stop-loss inequalities:',stoploss_checks)
    print('PASS exact variance-gap identities:',variance_checks)
    print('PASS strict variance gaps at interior stages:',strict_checks)
    print('PASS five-species illustration')


if __name__ == '__main__':
    check()

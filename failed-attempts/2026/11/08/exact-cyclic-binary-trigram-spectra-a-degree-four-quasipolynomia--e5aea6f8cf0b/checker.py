"""Independent checks for binary circular length-three multiset spectra.

Run with Python 3: python checker.py. No external dependencies.
"""
from collections import defaultdict
from fractions import Fraction
from math import comb


def direct_spectra(n):
    """Generate cyclic words, not Euler-flow parameters."""
    out = set()
    for mask in range(1 << n):
        bits = [(mask >> j) & 1 for j in range(n)]
        h = [0] * 8
        for j in range(n):
            h[4 * bits[j] + 2 * bits[(j + 1) % n] + bits[(j + 2) % n]] += 1
        out.add(tuple(h))
    return out


def flow_spectra(n):
    """Independently enumerate nonnegative balanced connected edge profiles."""
    ans = set()
    for a in range(n // 3 + 1):
        for b in range(n + 1):
            for d in range(n // 2 + 1):
                c = a + d - b
                if c < 0:
                    continue
                remain = n - 2*a - 2*b - c - d
                if remain < 0:
                    continue
                for p in range(remain + 1):
                    q = remain - p
                    if a and b:
                        good = True
                    elif a:
                        good = q == 0
                    elif b:
                        good = p == 0
                    else:
                        good = ((p > 0 and q == 0 and d == 0)
                                or (q > 0 and p == 0 and d == 0)
                                or (d > 0 and p == q == 0))
                    if good:
                        ans.add((p,a,c,b,a,d,b,q))
    return ans


def coefficient(n):
    """Evaluate five summands of the asserted rational generating function."""
    if n < 1:
        return 0
    val = 2 + (n % 2 == 0)
    for a in range(1, n // 3 + 1):
        for d in range((n - 3*a) // 2 + 1):
            val += 2
    for a in range(1, n // 3 + 1):
        for d in range((n - 3*a) // 2 + 1):
            for b in range(1, a + d + 1):
                if 3*a + b + 2*d <= n:
                    val += n - 3*a - b - 2*d + 1
    return val


def quasi_formula(n):
    """Independent partial-fraction extraction, valid for n >= 1."""
    poly = (Fraction(4225, 1728) - Fraction(17, 32)*(n+1)
            + Fraction(71, 144)*comb(n+2,2)
            - Fraction(5, 24)*comb(n+3,3)
            + Fraction(1, 12)*comb(n+4,4))
    period3 = Fraction(4,27) * (2 if n % 3 == 0 else -1)
    period4 = Fraction((1 if n%4==0 else (-1 if n%4==2 else 0)), 8)
    period2 = Fraction(19 * (-1 if n%2 else 1), 64)
    return poly + period2 + period3 + period4


def main():
    word_cases = 0
    profiles_checked = 0
    for n in range(1, 18):
        from_words = direct_spectra(n)
        from_flows = flow_spectra(n)
        assert from_words == from_flows, ('flow mismatch', n,
                                           from_words ^ from_flows)
        assert len(from_words) == coefficient(n) == quasi_formula(n), n
        word_cases += 1 << n
        profiles_checked += len(from_words)
    for n in range(18, 85):
        assert coefficient(n) == quasi_formula(n), n
    print('PASS: all cyclic words of lengths 1..17', word_cases)
    print('PASS: flow-profile sets and exact counts', profiles_checked)
    print('PASS: exact quasipolynomial coefficients for lengths 1..84')
    print('Counts for n=1..18:', [coefficient(n) for n in range(1,19)])

if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""Exact finite checks for the reversal-Hamming spectrum of cyclic Sturmian lifts.

All symbolic computations use integers. The rational P/Q is a high-order
Fibonacci convergent of the quadratic irrational rotation, and an independent
Fibonacci substitution language is compared on every reported finite horizon.
The finite tests corroborate, but do not replace, the infinite rotation proof.
"""
from fractions import Fraction

P, Q = 832040, 2178309  # consecutive Fibonacci numbers separated by one index
assert P * 2 < Q  # slope < 1/2

def finite_rotation_language(m, n):
    """Generate all n-letter phase intervals without floating-point arithmetic."""
    period = m * Q
    boundaries = sorted({(j * Q - i * P) % period
                         for i in range(n) for j in range(m)})
    assert len(boundaries) == m * n, (m, n, len(boundaries))
    answer = set()
    for k, left in enumerate(boundaries):
        right = boundaries[(k + 1) % len(boundaries)]
        if k + 1 == len(boundaries):
            right += period
        theta_twice = left + right
        word = tuple(((theta_twice + 2 * i * P) // (2 * Q)) % m
                     for i in range(n))
        answer.add(word)
    assert len(answer) == m * n, (m, n, len(answer))
    return answer

def fibonacci_word(length):
    word = '0'
    while len(word) < length:
        word = ''.join('01' if c == '0' else '0' for c in word)
    return word

FIB = fibonacci_word(20000)

def independent_substitution_language(m, n):
    factors = {FIB[i:i + n - 1] for i in range(len(FIB) - n + 1)}
    assert len(factors) == n, (n, len(factors))
    result = set()
    for factor in factors:
        for initial in range(m):
            word = [initial]
            for letter in factor:
                word.append((word[-1] + int(letter)) % m)
            result.add(tuple(word))
    return result

def brute_distance(language):
    reversed_words = [w[::-1] for w in language]
    return min(sum(a != b for a, b in zip(w, v))
               for w in language for v in reversed_words)

def periodic_tent(c, m):
    """Triangular measure of the agreement set, using exact Fraction values."""
    val = Fraction(0)
    for j in range(m):
        center = 2*j + 1
        for k in range(-2, 3):
            d = abs(c - center - k*m)
            if d < 1:
                val += 1-d
    return val

def direct_overlap(c, m):
    """Independent exact interval intersection length for each matching cell."""
    out = Fraction(0)
    for j in range(m):
        for k in range(-2, 3):
            # t lies simultaneously in [j,j+1] and
            # [c-(j+1)-km, c-j-km], up to endpoints of zero measure.
            lower = max(Fraction(j), c-(j+1)-k*m)
            upper = min(Fraction(j+1), c-j-k*m)
            if upper > lower:
                out += upper-lower
    return out

def run():
    checks = 0
    for m in range(2, 11):
        for a in range(0, 2*m*13 + 1):
            c = Fraction(a, 13)
            overlap = direct_overlap(c, m)
            triangles = periodic_tent(c, m)
            assert overlap == triangles, (m, c, overlap, triangles)
            if m % 2:
                assert overlap == 1, (m, c, overlap)
            else:
                dist_to_even = min(abs(c-2*k) for k in range(-2, m + 3))
                assert overlap == 2*dist_to_even, (m, c, overlap)
            checks += 1
    print('Exact circle-intersection and parity identities:', checks)

    comparisons = 0
    distances = []
    for m in range(2, 9):
        for n in range(1, 37):
            phase_lang = finite_rotation_language(m, n)
            sub_lang = independent_substitution_language(m, n)
            assert phase_lang == sub_lang, (m, n)
            comparisons += 1
            if n in (8, 16, 24, 36):
                delta = brute_distance(phase_lang)
                target = Fraction(m-1, m) if m % 2 else Fraction(m-2, m)
                # Simple finite discrepancy estimate, not an infinite proof.
                assert abs(Fraction(delta, n)-target) < Fraction(7, 20), (m,n,delta)
                distances.append((m, n, delta, float(target)))
    print('Independent rotation/substitution language comparisons:', comparisons)
    print('Exact brute-force reversal-distance checks:', len(distances))
    for m,n,d,c in distances:
        if n==36: print('m=%d, n=%d, min Hamming=%d, proportion=%.6f, limit=%.6f'
                        % (m,n,d,d/n,c))
    print('PASS: finite checks only; no infinite claim inferred from enumeration.')

if __name__ == '__main__': run()

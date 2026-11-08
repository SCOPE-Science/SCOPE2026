#!/usr/bin/env python3
"""Independent finite checks for exact bounded-range subsequence spectra.

Run: python3 periodic_span_verify.py
No nonstandard dependencies.
"""
from collections import Counter, defaultdict
from itertools import product
from itertools import groupby


def greedy_periodic_span(a, b, pattern):
    """Reference: try every starting phase, scanning the periodic text."""
    period = '0' * a + '1' * b
    L = len(period)
    best = None
    for start in range(L):
        cursor = start
        for letter in pattern:
            while period[cursor % L] != letter:
                cursor += 1
            cursor += 1
        span = cursor - start
        best = span if best is None else min(best, span)
    return best


def run_formula(a, b, pattern):
    L = a + b
    terms = []
    for symbol, it in groupby(pattern):
        length = sum(1 for _ in it)
        capacity = a if symbol == '0' else b
        q, remainder0 = divmod(length - 1, capacity)
        terms.append((q, remainder0 + 1, capacity))
    assert terms
    if len(terms) == 1:
        q, remainder, _ = terms[0]
        return q * L + remainder
    return (sum(q * L for q, _, _ in terms)
            + terms[0][1] + terms[-1][1]
            + sum(c for _, _, c in terms[1:-1]))


def sharp_threshold(a, b, k):
    assert a > 0 and b > 0 and k > 0
    L, m, M = a + b, min(a, b), max(a, b)
    if m == 1:
        return 1 + (k - 1) * L
    if k == 1:
        return 1
    t = k // 2
    if k % 2 == 0:
        return (t - 1) * L + 2
    if m == 2:
        return t * L + 1
    return (t - 1) * L + M + 2


def endpoint_and_internal_series(capacity, L, k_limit):
    """Truncated F_c and G_c coefficients as (length, span): multiplicity."""
    F, G = Counter(), Counter()
    for ell in range(1, k_limit + 1):
        q, rr = divmod(ell - 1, capacity)
        F[ell, q * L + rr + 1] += 1
        G[ell, q * L + capacity] += 1
    return F, G


def multiply(A, B, limit):
    C = Counter()
    for (n, p), multiplicity in A.items():
        for (m, q), other in B.items():
            if n + m <= limit:
                C[n + m, p + q] += multiplicity * other
    return C


def rational_series_coefficients(a, b, max_len):
    """Expand F0+F1+(2F0F1+F0^2G1+F1^2G0)/(1-G0G1)."""
    L = a + b
    F0, G0 = endpoint_and_internal_series(a, L, max_len)
    F1, G1 = endpoint_and_internal_series(b, L, max_len)
    poly = F0 + F1
    geometric = Counter({(0, 0): 1})
    block = multiply(G0, G1, max_len)
    while geometric:
        pair = multiply(F0, F1, max_len)
        odd0 = multiply(multiply(F0, F0, max_len), G1, max_len)
        odd1 = multiply(multiply(F1, F1, max_len), G0, max_len)
        combined = Counter()
        for (n, p), v in pair.items():
            combined[n, p] += 2*v
        combined.update(odd0)
        combined.update(odd1)
        poly.update(multiply(combined, geometric, max_len))
        geometric = multiply(geometric, block, max_len)
    return poly


def main():
    checks_formula = checks_threshold = checks_series = 0
    for a in range(1, 7):
        for b in range(1, 7):
            for k in range(1, 10):
                spans = []
                for bits in product('01', repeat=k):
                    u = ''.join(bits)
                    direct = greedy_periodic_span(a, b, u)
                    predicted = run_formula(a, b, u)
                    assert direct == predicted, (a, b, u, direct, predicted)
                    checks_formula += 1
                    spans.append(direct)
                actual = max(spans)
                expected = sharp_threshold(a, b, k)
                assert actual == expected, (a, b, k, actual, expected)
                checks_threshold += 1
    for a in range(1, 5):
        for b in range(1, 5):
            kmax = 7
            coefficients = rational_series_coefficients(a, b, kmax)
            for k in range(1, kmax+1):
                freq = Counter(greedy_periodic_span(a, b, ''.join(bits))
                               for bits in product('01', repeat=k))
                for span in set(freq) | {p for (length, p) in coefficients if length == k}:
                    got = coefficients.get((k, span), 0)
                    assert got == freq.get(span, 0), (a, b, k, span, got, freq.get(span, 0))
                    checks_series += 1
                assert sum(coefficients.get((k, p), 0) for p in range(1, (a+b)*k+1)) == 2**k
    print(f'PASS: {checks_formula} exact reference-span comparisons; '
          f'{checks_threshold} sharp-threshold comparisons; '
          f'{checks_series} coefficient comparisons; '
          f'all polynomial coefficient mass totals equal 2^k.')


if __name__ == '__main__':
    main()

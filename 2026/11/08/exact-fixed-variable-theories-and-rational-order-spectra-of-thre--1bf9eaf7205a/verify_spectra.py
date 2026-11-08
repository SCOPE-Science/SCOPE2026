#!/usr/bin/env python3
"""Check the minimum-model and exact-order spectra by independent enumeration.

Enumerates every binary creation word through order 12 (not k-variable
formulas). Compares direct canonical signatures to the rational generating
functions obtained by counting alternating canonical peeling blocks.
"""
from itertools import product
from collections import defaultdict
import json


def signature(code, k):
    """Creation word is read chronologically; peel the final monochrome runs."""
    if not code:
        return (("singleton", 1),)
    symbols = [code[0]] + list(code)
    # The first coded bit and the base vertex form one canonical last run.
    runs = []
    for bit in reversed(symbols):
        if runs and runs[-1][0] == bit:
            runs[-1][1] += 1
        else:
            runs.append([bit, 1])
    assert runs[-1][1] >= 2
    return tuple(("U" if b else "I", min(count, k)) for b, count in runs)


def convolution_coefficients(max_n, max_part):
    """1 / (1 - z - z^2 - ... - z^max_part)."""
    a = [0] * (max_n + 1)
    a[0] = 1
    for n in range(1, max_n + 1):
        a[n] = sum(a[n-j] for j in range(1, max_part+1) if n >= j)
    return a


def minimum_spectrum(k, max_n):
    a = convolution_coefficients(max_n, k)
    out = [0] * (max_n + 1)
    out[1] = 1
    for n in range(2, max_n + 1):
        out[n] = 2 * sum(a[n-j] for j in range(2, k + 1) if n >= j)
    return out


def exact_spectrum(k, max_n):
    # Only a layer of truncated size k permits arbitrarily enlarging its class.
    all_min = minimum_spectrum(k, max_n)
    unsaturated = minimum_spectrum(k - 1, max_n) if k >= 3 else [0] * (max_n + 1)
    if k == 2:
        unsaturated[1] = 1
    return [unsaturated[n] + sum(all_min[j] - unsaturated[j] for j in range(n+1))
            for n in range(max_n + 1)]


def main():
    max_n = 12
    results = []
    for k in range(2, 7):
        first = {}
        exact_by_order = defaultdict(set)
        for n in range(1, max_n + 1):
            for code in product((0, 1), repeat=n-1):
                sig = signature(code, k)
                exact_by_order[n].add(sig)
                first.setdefault(sig, n)
        direct_min = [sum(1 for v in first.values() if v == n) for n in range(max_n + 1)]
        direct_exact = [len(exact_by_order[n]) for n in range(max_n + 1)]
        expected_min = minimum_spectrum(k, max_n)
        expected_exact = exact_spectrum(k, max_n)
        assert direct_min == expected_min, (k, 'minimum spectrum', direct_min, expected_min)
        assert direct_exact == expected_exact, (k, 'exact-order spectrum', direct_exact, expected_exact)
        results.append({"k": k, "max_order": max_n, "distinct_minimum_theories": len(first),
                        "minimum_counts_1_to_12": direct_min[1:],
                        "exact_order_counts_1_to_12": direct_exact[1:],
                        "result": "PASS"})
    print(json.dumps({"method": "binary_word_enumeration_vs_rational_spectra",
                      "checks": results, "result": "PASS"}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

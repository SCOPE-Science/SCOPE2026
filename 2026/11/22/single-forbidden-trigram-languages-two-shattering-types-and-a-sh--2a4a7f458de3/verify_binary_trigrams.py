#!/usr/bin/env python3
"""Exhaustive, independent coordinate-trace test for single forbidden binary trigrams.
All indexing is zero-based, leftmost character first.
"""
from collections import Counter
from math import comb

def predicted(n, pattern):
    q = int(pattern, 2)
    # Class B: one adjacent equal pair and one distinct symbol.
    b = pattern in ('001', '011', '100', '110')
    if b:
        return {k: (1 if k == 0 else n if k == 1 else
                     comb(n-k+2, k) if n-k+2 >= k else 0)
                for k in range(n+1)}
    else:
        out = Counter()
        for mask in range(1 << n):
            bits = ''.join(str(mask >> j & 1) for j in range(n))
            if '111' not in bits:
                out[mask.bit_count()] += 1
        return {k: out[k] for k in range(n+1)}

def enumerate_language(n, pattern):
    return [mask for mask in range(1 << n)
            if pattern not in ''.join(str(mask >> j & 1) for j in range(n))]

def structurally_shattered(n, pattern, mask):
    sites = [j for j in range(n) if (mask >> j) & 1]
    if pattern in ('000', '010', '101', '111'):
        return all(not all((mask >> (j+r)) & 1 for r in range(3)) for j in range(n-2))
    if pattern in ('100', '011'):
        return not any(i < j for i in sites for j in sites if j + 1 in sites)
    else:
        return not any(i + 1 < j for i in sites if i + 1 in sites for j in sites)

def main():
    for n in range(0, 10):
        for q in range(8):
            pat = ''.join(str(q >> j & 1) for j in range(3))
            language = enumerate_language(n, pat)
            coeff = Counter()
            for mask in range(1 << n):
                traces = {c & mask for c in language}
                actual = len(traces) == 1 << mask.bit_count()
                predicted_face = structurally_shattered(n, pat, mask)
                assert actual == predicted_face, (n, pat, mask, actual)
                if actual:
                    coeff[mask.bit_count()] += 1
            assert all(coeff[k] == v for k, v in predicted(n, pat).items()), (n, pat, coeff)
            # Independently test the extremality classification for each n.
            is_extremal = sum(coeff.values()) == len(language)
            assert is_extremal == (n <= 3 or pat not in ('010', '101')), (n, pat, is_extremal)
        print('n=%d: all eight patterns, all supports, traces, coefficients, extremality PASS' % n)
    print('PYTHON_CHECK_PASS')
if __name__ == '__main__':
    main()

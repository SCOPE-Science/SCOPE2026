"""Step E: full Kh differentials + homology (bigraded) for 10_124 over Q.
Uses Fractions for exactness. Largest matrix 5352x4512 -- Fraction elimination
may be slow; use modular rank (prime) + spot-check exactness: compute ranks mod
p=10^9+7 for nullity, then verify Euler characteristic vs Jones. For CLAIM we
need exact Q ranks: modular rank equals Q rank unless p divides a minor; we
take two primes and require agreement (certificate of generic equality).
"""
import json
from collections import defaultdict
from kh_stepD import parse_pd, smoothing_data, build

def edge_kind(pd, mask, k):
    r0, lab0 = smoothing_data(pd, mask)
    r1, lab1 = smoothing_data(pd, mask | (1 << k))
    c0, c1 = len(r0), len(r1)
    if c1 == c0 - 1:
        return 'merge'
    elif c1 == c0 + 1:
        return 'split'
    else:
        return 'other(%d->%d)' % (c0, c1)

if __name__ == '__main__':
    d = json.load(open('output/artifacts/pd_codes.json'))
    pd = parse_pd(d['10_124']['pd'])
    n = len(pd)
    from collections import Counter
    kinds = Counter()
    for mask in range(1 << n):
        for k in range(n):
            if not (mask >> k) & 1:
                kinds[edge_kind(pd, mask, k)] += 1
    print('edge kinds:', dict(kinds))

#!/usr/bin/env python3
"""Exact checks for four-point shattering by two length-r disjoint windows.

Use: python3 verify_two_windows.py
Python 3 standard library only. Every enumerated mask is produced independently
from two start positions; four-traces are extracted by direct integer bit tests.
"""
from itertools import combinations

# For increasing query positions (1,r,2r+1,2r+2), pattern bit i labels
# query i. These are the affine start-pair witnesses of the theorem.
WITNESS_AFFINE = [
    ((1, 1), (2, 3)), ((0, 0), (1, 1)),
    ((1, 0), (2, 3)), ((0, 0), (1, 0)),
    ((1, 2), (2, 3)), ((0, 0), (1, 2)),
    ((0, 2), (1, 2)), ((0, 1), (1, 2)),
    ((1, 1), (2, 2)), ((0, 0), (2, 2)),
    ((1, 0), (2, 2)), ((0, 1), (2, 2)),
    ((1, 1), (2, 1)), ((0, 0), (2, 1)),
    ((1, 0), (2, 1)), ((0, 1), (2, 1)),
]

def trace(mask, support):
    return sum(((mask >> j) & 1) << i for i, j in enumerate(support))

def mask_of(n, r, p, q):
    assert 0 <= p and p + r <= q and q + r <= n
    return (((1 << r) - 1) << p) | (((1 << r) - 1) << q)

def concepts(n, r):
    return {mask_of(n, r, p, q)
            for p in range(n-r+1)
            for q in range(p+r, n-r+1)}

def shattered(concepts_, support):
    bits = 0
    target = (1 << (1 << len(support))) - 1
    for mask in concepts_:
        bits |= 1 << trace(mask, support)
        if bits == target:
            return True
    return bits == target

def predicted_at_threshold(n, r):
    assert n == 3*r + 3
    a = (1, r, 2*r+1, 2*r+2)
    b = tuple(n-1-x for x in reversed(a))
    return {a, b}

def main():
    witness_tests = 0
    for r in range(2, 1001):
        n = 3*r + 3
        support = (1, r, 2*r+1, 2*r+2)
        for pattern, ((ap,bp),(aq,bq)) in enumerate(WITNESS_AFFINE):
            p, q = ap*r+bp, aq*r+bq
            assert trace(mask_of(n,r,p,q),support) == pattern, (r,pattern,p,q)
            witness_tests += 1
    print('WITNESS_AFFINE_PASS', witness_tests, 'r_range_2_1000')

    # Exhaust every four-element support, not a sample, at every tested size.
    examined = 0
    critical_counts = []
    for r in range(2, 8):
        for n in range(2*r+1, 3*r+4):
            C = concepts(n, r)
            actual = {S for S in combinations(range(n),4) if shattered(C,S)}
            examined += sum(1 for _ in combinations(range(n),4))
            expected = predicted_at_threshold(n,r) if n == 3*r+3 else set()
            assert actual == expected, (r,n,len(actual),list(actual)[:5],expected)
            if n == 3*r+3:
                critical_counts.append((r,n,len(actual)))
    print('EXHAUSTIVE_FOUR_SUPPORT_PASS', examined,
          'r_range_2_7', 'critical_counts', critical_counts)

    # Distinct implementation of cardinality and admissibility of concepts.
    for r in range(2,6):
        for n in range(2*r+1, 3*r+4):
            C=concepts(n,r)
            expected=((n-2*r+1)*(n-2*r+2))//2
            assert len(C)==expected, (r,n,len(C),expected)
            for w in C:
                runs = []
                left = None
                for i in range(n+1):
                    bit = (w>>i)&1 if i<n else 0
                    if bit and left is None:left=i
                    if not bit and left is not None:
                        runs.append((left,i-left));left=None
                assert ((len(runs)==1 and runs[0][1]==2*r) or
                        (len(runs)==2 and runs[0][1]==runs[1][1]==r
                         and runs[0][0]+r<runs[1][0]))
    print('INDEPENDENT_RUN_SHAPE_PASS')

if __name__=='__main__':
    main()

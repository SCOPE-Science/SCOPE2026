#!/usr/bin/env python3
"""Recompute finite Pascal nondivisibility-gap histograms with integer modular Pascal rows."""
from collections import Counter
from math import comb

def predicted(p, r):
    A = p * (p + 1) // 2
    B = p * (p - 1) // 2
    result = Counter()
    for d in range(1, p ** (r - 1) + 1):
        i0 = 0
        while p ** i0 < d:
            i0 += 1
        result[d] = B * (A ** (r - i0) - 1) // (A - 1)
        assert B * (A ** (r - i0) - 1) % (A - 1) == 0
    return result

def observed(p, r):
    limit = p ** r
    row = [1]
    gaps = Counter()
    for n in range(limit):
        valid = [k for k, value in enumerate(row) if value % p]
        assert valid[0] == 0 and valid[-1] == n
        gaps.update(y - x for x, y in zip(valid, valid[1:]))
        if n < 160:
            assert valid == [k for k in range(n+1) if comb(n,k)%p]
        row = [1] + [(row[j-1] + row[j]) % p for j in range(1,len(row))] + [1]
    return gaps

def run():
    cases = [(2, i) for i in range(1, 10)] + [(3,i) for i in range(1,7)] + [(5,i) for i in range(1,5)] + [(7,i) for i in range(1,4)] + [(11,i) for i in range(1,4)]
    for p,r in cases:
        a = observed(p,r)
        b = predicted(p,r)
        assert a == b, (p,r,a-b,b-a)
        A = p * (p+1) // 2
        assert sum(a.values()) == A**r - p**r
        assert sum(d*c for d,c in a.items()) == p**r*(p**r-1)//2
        for j in range(r):
            assert sum(c for d,c in a.items() if d>p**j) == sum(b[d] for d in b if d>p**j)
        print(f'p={p}, r={r}, gaps={sum(a.values())}, kinds={len(a)}, OK')
    print('CHECK_OK')
if __name__=='__main__':run()

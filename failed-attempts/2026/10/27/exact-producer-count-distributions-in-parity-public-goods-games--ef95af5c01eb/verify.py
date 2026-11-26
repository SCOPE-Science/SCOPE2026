#!/usr/bin/env python3
"""Reproduce producer-count distributions for binary even-neighbor public-goods equilibria.

Run: python3 verify.py
Uses only Python 3 standard library; no external data.
"""
from collections import Counter
from itertools import product
from math import comb


def predicted(m, n):
    """Theorem's claimed production-count histogram for an m-by-n rook network."""
    ans = Counter()
    if m % 2 == 0 and n % 2 == 0:
        ans[m*n] = 1
    elif m % 2 == 0:
        for a in range(1, m+1, 2):
            ans[n*a] += comb(m, a)
    elif n % 2 == 0:
        for b in range(1, n+1, 2):
            ans[m*b] += comb(n, b)
    else:
        for a in range(1, m+1, 2):
            for b in range(1, n+1, 2):
                ans[a*b+(m-a)*(n-b)] += comb(m, a)*comb(n, b)
    return ans


def brute(m, n):
    """Independently evaluate every best-response condition on each binary profile."""
    out = Counter()
    for bits in product((0, 1), repeat=m*n):
        rows = [sum(bits[i*n:(i+1)*n]) for i in range(m)]
        cols = [sum(bits[i*n+j] for i in range(m)) for j in range(n)]
        if all(bits[i*n+j] == int((rows[i] + cols[j] - 2*bits[i*n+j]) % 2 == 0)
               for i in range(m) for j in range(n)):
            out[sum(bits)] += 1
    return out


def gf2_rank(m, n):
    """Compute the rank of I+adjacency over F2 with exact bit operations."""
    q = m*n
    rows = []
    for i in range(m):
        for j in range(n):
            mask = 0
            for a in range(m):
                for b in range(n):
                    if a == i or b == j:
                        mask ^= 1 << (a*n+b)
            rows.append(mask)
    pivots = {}
    for mask in rows:
        while mask:
            bit = mask.bit_length()-1
            if bit not in pivots:
                pivots[bit] = mask
                break
            mask ^= pivots[bit]
    return len(pivots)


def expected_minimum(m,n):
    if m%2==0 and n%2==0:
        return m*n,1
    if m%2==0:
        return n,m
    if n%2==0:
        return m,n
    return (m,n) if m<n else ((n,m) if n<m else (m,2*m))


def main():
    cases = 0
    exhaustive = 0
    total_profiles = 0
    for m in range(2, 11):
        for n in range(2, 11):
            h = predicted(m,n)
            assert sum(h.values()) == (1 if m%2==0 and n%2==0 else
                                     2**(m-1) if m%2==0 else
                                     2**(n-1) if n%2==0 else 2**(m+n-2))
            assert gf2_rank(m,n) == m*n - (sum(h.values()).bit_length()-1)
            k = min(h)
            assert (k,h[k]) == expected_minimum(m,n), (m,n,k,h[k])
            cases += 1
            if m*n <=16:
                observed = brute(m,n)
                assert observed == h, (m,n,observed,h)
                exhaustive +=1
                total_profiles += 2**(m*n)
    assert predicted(3,5)==Counter({3:5,5:3,7:30,9:25,15:1})
    print(f'VERIFY_OK parameter_cases={cases} fully_enumerated_boards={exhaustive} profiles_tested={total_profiles}')
    print('RECTANGLE_3x5', dict(sorted(predicted(3,5).items())))

if __name__ == '__main__':
    main()

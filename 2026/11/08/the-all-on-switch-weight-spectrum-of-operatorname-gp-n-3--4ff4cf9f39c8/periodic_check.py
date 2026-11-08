#!/usr/bin/env python3
"""Verify the all-on strategy weight census for GP(n,3) using its reversible recurrence.
Python 3, standard library only. Graph vertices are u_i,v_i with i mod n.
"""
from collections import Counter
from math import gcd

EXPECTED = {
    1: {1: 2},
    2: {2: 4},
    4: {2: 4, 4: 8, 6: 4},
    5: {3: 10, 5: 12, 7: 10},
    10: {6: 10, 10: 44, 14: 10},
    20: {10: 4, 12: 10, 18: 60, 20: 108,
         22: 60, 28: 10, 30: 4},
}

def all_period20():
    patterns = []
    for start in range(256):
        a = [(start >> i) & 1 for i in range(8)]
        for i in range(20):
            a.append(a[i] ^ a[i+1] ^ a[i+2] ^ a[i+3]
                     ^ a[i+5] ^ a[i+6] ^ a[i+7])
        assert a[20:28] == a[:8]
        seq = tuple(a[:20])
        assert all(sum(seq[(i+j) % 20]
                       for j in (-4,-3,-2,-1,1,2,3,4)) % 2 == 0
                   for i in range(20))
        patterns.append(seq)
    assert len(set(patterns)) == 256
    return patterns

def enumerate_period(g, patterns):
    cnt = Counter()
    for a20 in patterns:
        if any(a20[i] != a20[i % g] for i in range(20)):
            continue
        a = a20[:g]
        b = [1 ^ a[(i-1) % g] ^ a[i] ^ a[(i+1) % g]
             for i in range(g)]
        assert all((a[(i-1)%g] ^ a[i] ^ a[(i+1)%g] ^ b[i]) == 1
                   for i in range(g))
        assert all((a[i] ^ b[(i-3)%g] ^ b[i] ^ b[(i+3)%g]) == 1
                   for i in range(g))
        cnt[sum(a) + sum(b)] += 1
    return dict(sorted(cnt.items()))

def census_for_n(n, patterns):
    g = gcd(n, 20)
    tab = enumerate_period(g, patterns)
    return {w * n // g: count for w, count in tab.items()}

def main():
    patterns = all_period20()
    for g, expected in EXPECTED.items():
        result = enumerate_period(g, patterns)
        assert result == expected, (g, result, expected)
        print(f'period_g={g} solutions={sum(result.values())} weight_counts={result}')
    for n in range(7, 401):
        result = census_for_n(n, patterns)
        assert sum(result.values()) == sum(EXPECTED[gcd(n,20)].values())
        if n % 4 == 0:
            assert min(result) == n // 2 and result[n//2] == 4
        elif n % 5 == 0:
            assert min(result) == 3*n//5 and result[3*n//5] == 10
        else:
            assert min(result) == n
    print('PERIODIC_CHECK_PASS: all six residue classes and n=7..400')

if __name__ == '__main__':
    main()

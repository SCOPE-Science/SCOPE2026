#!/usr/bin/env python3
"""Finite exhaustive test for MCS cut density; Python 3 standard library only."""
from collections import defaultdict

TARGET = '00101110100011'
EXPECTED = (1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8)  # n=2,...,14


def closed(v):
    if len(v) == 1:
        return True
    # An arbitrary witnessing border is sufficient; uniqueness is not assumed.
    for t in range(1, len(v)):
        u = v[:t]
        if v[-t:] == u and sum(v[i:i+t] == u for i in range(len(v)-t+1)) == 2:
            return True
    return False


def crossing_intervals(s, cut):
    n = len(s)
    out = []
    for i in range(n):
        for j in range(i+1,n):
            if not i <= cut < j: continue
            if (closed(s[i:j+1]) and (i == 0 or not closed(s[i-1:j+1]))
                    and (j == n-1 or not closed(s[i:j+2]))):
                out.append((i+1,j+1))
    return out


def main():
    found = []
    for n in range(2,15):
        best = 0
        for mask in range(1<<n):
            s = format(mask, '0%db' % n)
            # Compute intrinsic closedness only once per interval, not per cut.
            c = [[False]*n for _ in range(n)]
            for i in range(n):
                for j in range(i,n):
                    c[i][j] = closed(s[i:j+1])
            by_cut = [0]*(n-1)
            for i in range(n):
                for j in range(i+1,n):
                    if c[i][j] and (i==0 or not c[i-1][j]) and (j==n-1 or not c[i][j+1]):
                        for cut in range(i,j):
                            by_cut[cut] += 1
            for cut,value in enumerate(by_cut):
                if value > best: best = value
                if n == 14 and value >= 8: found.append((s,cut+1))
        assert best == EXPECTED[n-2], (n,best)
        print('n=%d max_crossings=%d' % (n,best))
    want = sorted([('00101110100011', 8), ('00111010001011',6),
                   ('11000101110100',6),('11010001011100',8)])
    assert sorted(found) == want, found
    iv = crossing_intervals(TARGET, 7)
    assert iv == [(1,11),(1,13),(2,10),(3,9),(4,14),(6,14),(7,10),(8,13)]
    print('length14_superhalf_pairs=',found)
    print('witness_1based_cut=8 intervals=',iv)
    print('DIRECT_PASS')

if __name__ == '__main__': main()

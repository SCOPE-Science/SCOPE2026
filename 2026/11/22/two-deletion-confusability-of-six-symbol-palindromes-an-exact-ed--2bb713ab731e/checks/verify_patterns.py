#!/usr/bin/env python3
"""Exact equality-template proof for length-six palindromic two-deletion conflicts.
All templates are restricted-growth set partitions of six variable slots.
No symbolic algebra or third-party dependencies are required.
"""
from collections import Counter
from itertools import combinations

def partitions(n):
    def extend(a, maximum):
        if len(a) == n:
            yield tuple(a)
        else:
            for j in range(maximum + 2):
                yield from extend(a + [j], max(maximum, j))
    yield from extend([0], 0)

def lcs(a, b):
    old = [0] * (len(b) + 1)
    for x in a:
        new = [0] * (len(b) + 1)
        for j, y in enumerate(b, 1):
            new[j] = old[j-1]+1 if x==y else max(old[j],new[j-1])
        old = new
    return old[-1]

def conflict(a,b):
    return a != b and lcs(a+a[::-1],b+b[::-1]) >= 4

def run():
    cc = Counter()
    num = 0
    for p in partitions(6):
        num += 1
        if conflict(p[:3],p[3:]):
            cc[max(p)+1] += 1
    assert num == 203, num
    assert dict(cc) == {2:20,3:37,4:9}, cc
    for q in range(1,21):
        falling = lambda k: __import__('math').prod(q-j for j in range(k))
        e = sum(v*falling(k) for k,v in cc.items())//2
        assert 2*e == q*q*(q-1)*(9*q-8)
    print('PATTERN_OK 203 templates, conflicting counts r=2:20 r=3:37 r=4:9')

if __name__ == '__main__':
    run()

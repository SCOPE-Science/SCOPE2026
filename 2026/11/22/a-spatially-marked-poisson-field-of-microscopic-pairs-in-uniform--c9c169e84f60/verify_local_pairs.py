#!/usr/bin/env python3
"""Finite checks for displacement-marked close pairs in uniform permutations.
Run with Python 3 standard library: python verify_local_pairs.py
"""
from itertools import permutations
from fractions import Fraction
from math import factorial


def marks_for(p, H=3, K=3):
    n = len(p)
    out = {}
    for h in range(1, min(H, n-1)+1):
        for k in range(1, min(K, n-1)+1):
            for s in (-1, 1):
                out[(h,k,s)] = sum(p[i+h]-p[i] == s*k for i in range(n-h))
    return out


def falling(n, k):
    ans = 1
    for j in range(k):
        ans *= n-j
    return ans


def valid_maps(n, mark, i):
    h,k,s = mark
    if i+h >= n:
        return
    for a in range(1, n+1):
        b = a+s*k
        if 1 <= b <= n:
            yield {i:a,i+h:b}


def direct_two_event_moment(n, mark1, mark2):
    h1,_,_ = mark1
    h2,_,_ = mark2
    val = Fraction(0)
    for i in range(n-h1):
        for j in range(n-h2):
            if mark1 == mark2 and i == j:
                continue  # ordered falling factorial, not ordinary square
            positions = len({i,i+h1,j,j+h2})
            denom = falling(n,positions)
            for a in valid_maps(n,mark1,i):
                for b in valid_maps(n,mark2,j):
                    if any(v != b[x] for x,v in a.items() if x in b):
                        continue
                    merged = dict(a)
                    merged.update(b)
                    if len(set(merged.values())) != len(merged):
                        continue
                    val += Fraction(1,denom)
    return val


def finite_checks():
    num = 0
    moment_pairs = [
        ((1,1,1),(1,1,1)),
        ((1,1,1),(1,1,-1)),
        ((1,1,1),(2,1,1)),
        ((1,1,1),(1,2,-1)),
        ((2,1,1),(2,2,-1)),
    ]
    for n in range(3,9):
        kinds = [(h,k,s) for h in range(1,min(n,4)) for k in range(1,min(n,4)) for s in (-1,1)]
        sums = {m:0 for m in kinds}
        seconds = {pair:0 for pair in moment_pairs if all(m in kinds for m in pair)}
        zero = 0
        total = factorial(n)
        for p in permutations(range(1,n+1)):
            counts = marks_for(p)
            for m in kinds:
                sums[m] += counts[m]
            for (a,b) in seconds:
                seconds[(a,b)] += counts[a]*(counts[b]-(a==b))
            if all(counts[m] == 0 for m in [(1,1,1),(1,1,-1)]):
                zero += 1
        for h,k,s in kinds:
            got = Fraction(sums[(h,k,s)], total)
            expected = Fraction((n-h)*(n-k),n*(n-1))
            assert got == expected,(n,h,k,s,got,expected)
            num += 1
        for pair, counted in seconds.items():
            expected = direct_two_event_moment(n,*pair)
            got = Fraction(counted,total)
            assert got == expected,(n,pair,got,expected)
            num += 1
        assert 0 <= zero < total
        if n >= 4:
            assert zero > 0
        num += 1
    # For any fixed mark, expected count tends to one, with explicit boundary correction.
    for n in (20,100,1000,10000):
        for h,k in [(1,1),(1,2),(2,1),(2,2),(3,5)]:
            v = Fraction((n-h)*(n-k),n*(n-1))
            assert abs(v-1) <= Fraction(h+k+2,n)
            num += 1
    # Independent-Poisson consequences, checked as finite integer set identities.
    for d in range(1,11):
        manhattan = {(h,k) for h in range(1,d+1) for k in range(1,d+1) if h+k<=d+1}
        assert len(manhattan) == d*(d+1)//2
        num += 1
        for r in range(1,11):
            box={(h,k) for h in range(1,r+1) for k in range(1,r+1)}
            intersection = sum(max(0,min(r,d+1-h)) for h in range(1,r+1))
            assert len(manhattan & box)==intersection
            assert len(manhattan | box)==d*(d+1)//2+r*r-intersection
            num += 2
    print(f"PASS: {num} finite exact checks, exhaustive permutations through n=8")

if __name__ == '__main__':
    finite_checks()

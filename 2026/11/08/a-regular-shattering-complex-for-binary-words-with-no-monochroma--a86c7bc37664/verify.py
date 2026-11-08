#!/usr/bin/env python3
"""Exhaustive checks for no-monochromatic-triple trace supports.
Python >=3.9, standard library only. No external files required.
"""
from itertools import product
from collections import Counter


def admissible(word):
    return not any(word[i] == word[i+1] == word[i+2] for i in range(len(word)-2))


def valid_mask(mask, n):
    bits = [(mask >> i) & 1 for i in range(n)]
    if any(bits[i:i+3] == [1, 1, 1] for i in range(n-2)):
        return False
    last_11 = -1
    last_00 = -1
    for i in range(n-1):
        if bits[i] == bits[i+1] == 0:
            last_00 = i
        if bits[i] == bits[i+1] == 1:
            if last_11 >= 0 and last_00 <= last_11:
                return False
            last_11 = i
    return True


def recurrence(n):
    # Coefficient tuples for (1 + tz - t^2 z + t^2 z^2)/(1-t-2t^2 z+t^3 z).
    base = [(1,), (1, 1), (1, 2, 1)]
    if n < 3:
        return base[n]
    for j in range(3, n+1):
        q = [0]*(max(len(base[-1]),len(base[-2])+1,len(base[-3])+1))
        for i,c in enumerate(base[-1]): q[i] += c
        for i,c in enumerate(base[-2]): q[i+1] += 2*c
        for i,c in enumerate(base[-3]): q[i+1] -= c
        while q and q[-1] == 0: q.pop()
        base.append(tuple(q))
    return base[n]


def trace_set(words, mask):
    return {w & mask for w in words}


def verify():
    # Independently compare each proposed support with all admissible words, n<=15.
    for n in range(0, 16):
        words = [sum(bit << i for i,bit in enumerate(seq))
                 for seq in product((0,1), repeat=n) if admissible(seq)]
        counts = Counter()
        for mask in range(1 << n):
            shatters = len(trace_set(words, mask)) == 1 << mask.bit_count()
            if shatters != valid_mask(mask, n):
                raise AssertionError((n, mask, shatters, valid_mask(mask,n)))
            if shatters:
                counts[mask.bit_count()] += 1
        poly = tuple(counts.get(k,0) for k in range(n+1))
        poly = poly[:max(1,max((k+1 for k,c in enumerate(poly) if c),default=0))]
        assert poly == recurrence(n), (n, poly, recurrence(n))
        if n:
            assert max(counts) == n//2+1, (n,max(counts))
        print('TRACE', n, 'supports',sum(counts.values()),'degree',max(counts),'PASS')
    # Two free bridge coordinates, every four fixed boundary bits.
    for a,b,c,d in product((0,1),repeat=4):
        assert any(admissible((a,b,x,y,c,d)) for x,y in product((0,1),repeat=2))
    print('BRIDGE_16_BOUNDARY_CASES_PASS')
    # Independent test of static-background free positions for n<=10.
    for n in range(3, 11):
        best = 0
        for mask in range(1 << n):
            if all(sum(mask>>j&1 for j in range(i,i+3)) <= 1 for i in range(n-2)):
                best = max(best,mask.bit_count())
        assert best == (n+2)//3,(n,best)
    print('FIXED_BACKGROUND_BOUND_PASS')
    print('NO_MONOCHROMATIC_TRIPLE_SHATTERING_PASS')

if __name__ == '__main__':
    verify()

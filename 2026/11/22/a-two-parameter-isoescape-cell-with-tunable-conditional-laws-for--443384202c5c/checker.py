#!/usr/bin/env python3
"""Exact-rational tests of an asymmetric negative-doubling open system.

Run with Python 3: python checker.py
The proof for arbitrary parameters and times is in RESULT.md; this finite
checker is an independent consistency test, not an exhaustive proof.
"""
from fractions import Fraction as Q


def clipped(intervals, allowed):
    out = []
    for a,b in intervals:
        for c,d in allowed:
            lo,hi=max(a,c),min(b,d)
            if lo<hi: out.append((lo,hi))
    return out


def coalesce(intervals):
    a=sorted(intervals)
    if not a:return []
    out=[a[0]]
    for x,y in a[1:]:
        if x<=out[-1][1]:out[-1]=(out[-1][0],max(y,out[-1][1]))
        else:out.append((x,y))
    return out


def length(intervals):
    return sum((y-x for x,y in intervals),Q(0))


def preimage_next(intervals,a,b):
    # First branch T(x)=1-2x on [0,1/2]; second T(x)=2-2x on [1/2,1].
    raw = []
    for u,v in intervals:
        raw += [((1-v)/2,(1-u)/2),((2-v)/2,(2-u)/2)]
    return coalesce(clipped(raw,[(Q(0),a),(b,Q(1))]))


def predicted(a,b,n):
    # Survives visits j=0,...,n, inclusive.
    return (a+1-b+n*(3*(a-b)+1)) / (2**n)


def test(a,b):
    assert Q(1,3)<a<Q(2,5) and Q(3,5)<b<Q(2,3)
    intervals=[(Q(0),a),(b,Q(1))]
    for n in range(11):
        actual=length(intervals)
        expected=predicted(a,b,n)
        assert actual==expected,(a,b,n,actual,expected)
        intervals=preimage_next(intervals,a,b)


def main():
    a_values=[Q(17,50),Q(7,20),Q(9,25),Q(11,30),Q(3,8),Q(23,60),Q(39,100)]
    b_values=[Q(61,100),Q(37,60),Q(5,8),Q(19,30),Q(16,25),Q(13,20)]
    count=0
    for a in a_values:
        for b in b_values:
            test(a,b)
            count+=1
    # Equal hole widths but unequal terminal channel weights.
    x=(Q(9,25),Q(61,100))
    y=(Q(19,50),Q(63,100))
    assert x[1]-x[0] == y[1]-y[0] == Q(1,4)
    weights=[]
    for a,b in (x,y):
        delta=3*(a-b)+1
        weights.append((3*a-1)/delta)
    assert weights==[Q(8,25),Q(14,25)]
    for n in range(15):
        assert predicted(*x,n)==predicted(*y,n)
    print('PASS: %d parameter pairs x 11 finite horizons, exact interval recursion' % count)
    print('PASS: equal-width holes produce identical escape sequence, unequal terminal weights 8/25 and 14/25')

if __name__=='__main__': main()

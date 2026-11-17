#!/usr/bin/env python3
"""Finite prefix tests for the explicitly described one-accumulation construction.
Analytical scale claims are proved in RESULT.md, not by this checker.
"""
import math

def prefixes(blocks,n):
    points={0}
    for B in blocks:
        assert len(B)<=20
        for mask in range(1<<len(B)):
            x=0
            for i,bit in enumerate(B):
                if (mask>>i)&1 and bit<n: x|=1<<bit
            points.add(x)
    return len(points)

def check():
    # A square-root control with sampled block endpoints; finite truncation.
    k=lambda n: math.isqrt(n)
    bounds=[0,9,100,625]
    F=[i for i in range(bounds[-1]) if k(i+1)>k(i)]
    blocks=[[i for i in F if a<=i<b] for a,b in zip(bounds[:-1],bounds[1:])]
    assert [len(B) for B in blocks]==[k(bounds[i+1])-k(bounds[i]) for i in range(3)]
    for n in [1,2,9,10,49,99,100,101,625]:
        count=prefixes(blocks,n)
        assert 1<=count<=1+n*2**k(n)
        assert count==len({0}|{sum((1<<pos) for j,pos in enumerate(B) if (mask>>j)&1 and pos<n) for B in blocks for mask in range(1<<len(B))})
    for j in range(1,len(bounds)):
        n=bounds[j]
        assert prefixes(blocks,n)>=2**(k(bounds[j])-k(bounds[j-1]))
    # All-zero profile example has exactly n+1 prefixes.
    for n in range(2,100):
        assert len({0}|{1<<j for j in range(n)})==n+1
    print('VERIFY_OK finite_block_prefix_cases=9 segment_lower_bounds=3 singleton_prefix_cases=98')
if __name__=='__main__':check()

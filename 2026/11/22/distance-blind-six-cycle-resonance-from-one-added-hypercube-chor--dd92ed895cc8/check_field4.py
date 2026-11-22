#!/usr/bin/env python3
"""Direct q=4 state-space verification in dimension three.

A fixed F_2-basis identifies F_4 with F_2^2 for adjacency-only updates.
"""
from collections import Counter
from check_chord import matrix


def check(r):
    B = matrix(3,r)
    masks = B
    def once(bits):
        return sum((((bits & row).bit_count() & 1)<<i) for i,row in enumerate(masks))
    period_counts=Counter()
    for low in range(256):
        for high in range(256):
            a,b=low,high
            t=0
            while True:
                a,b=once(a),once(b)
                t+=1
                if (a,b)==(low,high):
                    period_counts[t]+=1
                    break
                assert t<7
    q=4;N=8
    expected={1:q**(N//2-2),2:q**(N-4)-q**(N//2-2),3:q**(N//2)-q**(N//2-2),6:q**N-q**(N-4)-q**(N//2)+q**(N//2-2)}
    assert period_counts==expected,(period_counts,expected)
    print('F4 d=3 distance',r,'PASS',dict(period_counts))

if __name__=='__main__':
    for r in (2,3):check(r)

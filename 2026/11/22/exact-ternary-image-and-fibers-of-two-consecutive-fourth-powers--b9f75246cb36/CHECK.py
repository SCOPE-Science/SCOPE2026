#!/usr/bin/env python3
"""Independent exhaustive fiber verifier for consecutive fourth powers modulo 3^k."""
from collections import Counter

def square_roots_histogram(k):
    m=3**k
    return Counter((s*s)%m for s in range(m))

def expected_fiber(y,k):
    m=3**k
    # 8 and 4 are units modulo m
    c=pow(8,-1,m)
    if y%3==1: return 2
    if y%3==0: return 0
    if k<=3: return 3**(k-1) if y==c else 0
    diff=(y-c)%m
    if diff%27: return 0
    z=(4*(diff//27))%(3**(k-3))
    return 9*square_roots_histogram(k-3)[z]

def check():
    for k in range(1,10):
        mod=3**k
        got=Counter((x**4+(x+1)**4)%mod for x in range(mod))
        ref=dict((y,expected_fiber(y,k)) for y in range(mod))
        for y in range(mod):
            assert got[y]==ref[y], (k,y,got[y],ref[y])
        nk=max(k-3,0)
        sq=sum(1 for v in square_roots_histogram(nk).values() if v)
        predicted=3**(k-1)+sq
        assert len(got)==predicted, (k,len(got),predicted)
        print(f'k={k:2} modulus={mod:6} image={len(got):5} count OK')
    print('PASS: all values and full fibers for k=1..9')

if __name__=='__main__': check()

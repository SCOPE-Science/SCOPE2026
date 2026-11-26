#!/usr/bin/env python3
"""Independent finite checks of Rudin–Shapiro subsequence universality."""
from itertools import product

MORPH = {'A':'AB','B':'AD','C':'CD','D':'CB'}
BIT = {'A':0,'B':0,'C':1,'D':1}
STATES = (None,0,1)

def binary_parity(n):
    return ((n & (n >> 1)).bit_count() & 1)

def morph_word(k, letter='A'):
    x = letter
    for _ in range(k):
        x = ''.join(MORPH[c] for c in x)
    return [BIT[c] for c in x]

def scan(w, pending=None):
    count=0
    for x in w:
        if pending is None:
            pending=x
        elif pending!=x:
            count+=1
            pending=None
    return count, pending

def check_small_subsequences(w):
    index=scan(w)[0]
    for k in range(index+2):
        covers = all(is_subsequence(w, p) for p in product((0,1), repeat=k))
        assert covers==(k<=index), (w, k, index, covers)

def is_subsequence(w, p):
    j=0
    for x in w:
        if j<len(p) and x==p[j]:
            j+=1
    return j==len(p)

def level_formula(k):
    return 5*(1 << (k-4))-(k%2==0)

def block_expected(k, letter, pending):
    e = (k%2==0)
    a = level_formula(k)
    b = a+(1 if e else -1)
    base = a if letter in 'AC' else b
    first=0 if letter in 'AB' else 1
    extra=(pending is not None and pending!=first)
    end=e if letter in 'AD' else 1-e
    return base+int(extra), int(end)

def main():
    for k in range(1,17):
        w=morph_word(k)
        assert w==[binary_parity(i) for i in range(1<<k)]
        if k>=4:
            assert scan(w)[0]==level_formula(k), (k,scan(w),level_formula(k))
        if k<=4:
            for n in range(1,min(len(w),16)+1):
                check_small_subsequences(w[:n])
    for k in range(4,12):
        for c in MORPH:
            w=morph_word(k,c)
            for p in STATES:
                assert scan(w,p)==block_expected(k,c,p), (k,c,p,scan(w,p),block_expected(k,c,p))
    n=1<<17
    w=[binary_parity(i) for i in range(n)]
    ct=0; pending=None
    for i,v in enumerate(w,1):
        if pending is None: pending=v
        elif pending!=v: ct+=1; pending=None
        if i<16: check_small_subsequences(w[:i])
        assert abs(ct-5*i/16)<=i.bit_length()+16, (i,ct)
    print('VERIFY_OK: 16 dyadic levels, four-block transfer identities through level 11, all prefixes through 131072, direct subsequence checks')

if __name__=='__main__': main()

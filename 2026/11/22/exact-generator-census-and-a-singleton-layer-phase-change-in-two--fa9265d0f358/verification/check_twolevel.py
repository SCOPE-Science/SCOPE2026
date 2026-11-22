#!/usr/bin/env python3
"""Reproducible finite checks for generator counts in two-level Heyting algebras."""
from itertools import product
from math import comb

def upsets(a, b):
    upper = ((1 << b) - 1) << a
    return [s for s in range(1 << (a + b)) if not(s & ((1 << a) - 1)) or s & upper == upper]

def implication(u, v, a, b):
    # Direct finite Kripke implication: p belongs iff all its successors in u lie in v.
    out = 0
    for p in range(a + b):
        successors = (1 << p) | (((1 << b) - 1) << a if p < a else 0)
        if not (successors & u & ~v):
            out |= 1 << p
    return out

def generated_size(generators, a, b):
    s = set(generators) | {0, (1 << (a + b)) - 1}
    while True:
        grown = set(s)
        for u in s:
            for v in s:
                grown.update((u | v, u & v, implication(u,v,a,b)))
        if grown == s:
            return len(s)
        s = grown

def colour_condition(generators, a, b):
    colours = [sum(((g >> p) & 1) << j for j,g in enumerate(generators)) for p in range(a + b)]
    low,high = colours[:a],colours[a:]
    return len(set(low)) == a and len(set(high)) == b and (b > 1 or high[0] not in low)

def falling(n,r):
    p = 1
    for i in range(r): p *= n - i
    return p

def stirling_signed_first(n):
    c = [1]
    for m in range(n):
        nxt = [0] * (len(c)+1)
        for j,t in enumerate(c): nxt[j] -= m*t; nxt[j+1] += t
        c=nxt
    return c

def census(a,b,k):
    if b == 1:
        return sum(comb(k,c)*falling((1 << c)-1,a) for c in range(k+1))
    sign = stirling_signed_first(b)
    return sum(comb(k,c)*falling(1 << c,a) *
               sum(sign[j]*((1 << j)-1)**(k-c) for j in range(1,b+1))
               for c in range(k+1))

def bound(a,b):
    cl = (a-1).bit_length()
    return ((a).bit_length() if b==1 else cl+(b-1).bit_length())

def run():
    checks=0
    configs=[(1,1,0),(1,1,1),(1,1,2),(2,1,1),(2,1,2),(3,1,2),
             (1,2,1),(1,2,2),(1,3,2),(1,4,2),(2,2,1),(2,2,2),
             (3,2,2),(2,3,2),(3,3,2),(2,2,3),(2,3,3),(3,2,3)]
    for a,b,k in configs:
        h=upsets(a,b)
        ntrue=0
        for gs in product(h, repeat=k):
            truth=generated_size(gs,a,b)==len(h)
            pred=colour_condition(gs,a,b)
            assert truth==pred,(a,b,k,gs,truth,pred)
            ntrue+=truth
            checks+=1
        assert ntrue==census(a,b,k),(a,b,k,ntrue,census(a,b,k))
        if k==bound(a,b):
            assert ntrue>0,(a,b,k)
        if k<bound(a,b):
            assert ntrue==0,(a,b,k)
    # Independent row-injectivity and column-inclusion count up to alphabet size four.
    for a in range(1,5):
        for b in range(1,5):
            for k in range(4):
                if (a+b)*k>16:continue
                brute=sum(colour_condition(gs,a,b) for gs in product(upsets(a,b),repeat=k))
                assert brute==census(a,b,k),(a,b,k,brute,census(a,b,k))
    print('VERIFY_OK',checks)
if __name__ == '__main__':run()

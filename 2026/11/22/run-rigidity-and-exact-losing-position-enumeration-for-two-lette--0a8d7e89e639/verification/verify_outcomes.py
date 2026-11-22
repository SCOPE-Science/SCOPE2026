#!/usr/bin/env python3
"""Finite reproducibility verification of the two-sided prefix/suffix game.

Move: remove a prefix ending in 'ab' or a suffix beginning in 'ba'.
The computation recursively enumerates actual options, independently of
both the proposed regular-language classification and the counting formula.
"""
from functools import lru_cache
from itertools import product
import re

@lru_cache(None)
def grundy(w):
    options=set()
    for i in range(len(w)-1):
        if w[i:i+2]=='ab':
            options.add(grundy(w[i+2:]))
        if w[i:i+2]=='ba':
            options.add(grundy(w[:i]))
    g=0
    while g in options:
        g+=1
    return g

p_language=re.compile(r'(?:b*|a+(?:b{2,}a+)*)\Z')

def canonical_winning_move(w):
    if not w or p_language.fullmatch(w):
        return None
    if w[0]=='b':
        first_a=w.index('a')
        assert w[first_a-1:first_a+1]=='ba'
        return w[:first_a-1]
    if w[-1]=='b':
        last_a=w.rindex('a')
        assert w[last_a:last_a+2]=='ab'
        return w[last_a+2:]
    # Starts and ends in a: locate leftmost maximal singleton b-run.
    for i in range(1,len(w)-1):
        if w[i]=='b' and w[i-1]==w[i+1]=='a':
            assert w[i:i+2]=='ba'
            return w[:i]
    raise AssertionError(('missing singleton run',w))
counts=[]
for n in range(18):
    losing=0
    maximum=0
    for letters in product('ab',repeat=n):
        w=''.join(letters)
        g=grundy(w)
        if (g==0)!=bool(p_language.fullmatch(w)):
            raise AssertionError(('classification',w,g))
        chosen=canonical_winning_move(w)
        if g==0:
            assert chosen is None
        else:
            assert chosen is not None
            assert grundy(chosen)==0,('bad canonical reply',w,chosen)
        if g>n//2:
            raise AssertionError(('sharp-bound',w,g))
        losing+=(g==0)
        maximum=max(maximum,g)
    if maximum!=n//2:
        raise AssertionError(('attainment',n,maximum))
    counts.append(losing)
print('exhaustive length range: 0..17')
print('positions checked:',sum(2**n for n in range(18)))
print('P counts:',counts)
print('max Grundy by length:',[n//2 for n in range(18)])
print('classification, constructive winning move, upper bound and attainment: PASS')

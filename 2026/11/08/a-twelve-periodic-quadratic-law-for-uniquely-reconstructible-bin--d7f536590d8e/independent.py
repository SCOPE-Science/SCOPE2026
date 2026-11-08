#!/usr/bin/env python3
"""Independent direct multiset reconstruction census, without any DFA routines."""
from collections import defaultdict

CONSTANTS=(-88,-85,-108,-85,-88,-97,-96,-85,-100,-85,-96,-97)
SMALL=(None,None,None,8,14,26,46,74,92)

def hist(word):
    h=[0]*8
    for a,b,c in zip(word,word[1:],word[2:]):
        h[(a<<2)|(b<<1)|c]+=1
    return tuple(h)

def exact_census(n):
    counts=defaultdict(int)
    for x in range(1<<n):
        bits=tuple((x>>j)&1 for j in range(n-1,-1,-1))
        counts[hist(bits)]+=1
    return sum(multiplicity==1 for multiplicity in counts.values())

if __name__=='__main__':
    for n in range(3,17):
        actual=exact_census(n)
        expected=SMALL[n] if n<9 else (n*n+28*n+CONSTANTS[n%12])//2
        assert actual==expected,(n,actual,expected)
    print('INDEPENDENT_OK exhaustive_binary_3gram_census_n=3..16')

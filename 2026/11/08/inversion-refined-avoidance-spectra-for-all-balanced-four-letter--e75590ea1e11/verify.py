#!/usr/bin/env python3
"""Exhaustive independently implemented verification of six balanced-pattern spectra."""
from itertools import product
from collections import defaultdict

PATTERNS=('0011','0101','0110','1001','1010','1100')


def contains_scattered(word,pat):
    step=0
    for symbol in word:
        if symbol==pat[step]:
            step+=1
            if step==len(pat):return True
    return False


def predicted(A,B,C,p):
    if p in ('0110','1001'):
        return 1
    if p=='0101':
        return 1 if C==0 else sum(C%d==0 and C//d<=B for d in range(1,A+1))
    if p=='1010':
        return predicted(A,B,A*B-C,'0101')
    if p=='0011':
        lower=max(2,C-B+1)
        upper=min(A,C)
        return int(C<=B)+max(0,upper-lower+1)
    if p=='1100':
        return predicted(A,B,A*B-C,'0011')
    raise AssertionError(p)


def verify():
    tests=0
    for n in range(15):
        counts=defaultdict(int)
        for word in product('01',repeat=n):
            A=word.count('0')
            B=n-A
            zeros_seen=0
            C=0
            for letter in word:
                if letter=='0': zeros_seen+=1
                else: C+=zeros_seen
            for p in PATTERNS:
                if not contains_scattered(word,p):
                    counts[A,B,C,p]+=1
        for A in range(n+1):
            B=n-A
            for C in range(A*B+1):
                for p in PATTERNS:
                    got=counts[A,B,C,p]
                    want=predicted(A,B,C,p)
                    assert got==want,(n,A,B,C,p,got,want)
                    tests+=1
    for A in range(26):
        for B in range(26):
            for p in PATTERNS:
                histogram=[predicted(A,B,C,p) for C in range(A*B+1)]
                assert sum(histogram)==A*B+1
            for p,numerator,denominator in (
                ('0110',A*B*(A*B+1),2),
                ('0101',A*B*(A+1)*(B+1),4),
                ('0011',A*B*(A+B),2)):
                moment=sum(C*predicted(A,B,C,p) for C in range(A*B+1))
                assert denominator*moment==numerator
    print('BALANCED_PATTERN_VERIFY_OK', tests, 'coefficients', 26*26, 'moment_grids')

if __name__=='__main__': verify()

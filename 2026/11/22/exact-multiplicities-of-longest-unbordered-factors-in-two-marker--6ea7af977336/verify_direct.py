#!/usr/bin/env python3
"""Exhaustively verify longest-unbordered-factor occurrence theorem via KMP border tables."""
from collections import Counter
from math import comb

def direct(w):
    best=0; count=0
    for begin in range(len(w)):
        suffix=w[begin:]
        p=[0]*len(suffix)
        for i in range(1,len(suffix)):
            j=p[i-1]
            while j and suffix[i]!=suffix[j]:j=p[j-1]
            if suffix[i]==suffix[j]:j+=1
            p[i]=j
        for L, border in enumerate(p,1):
            if border==0:
                if L>best: best,count=L,1
                elif L==best: count+=1
    return best,count

def formula(a,b,c):
    m=max(a,c)
    if m>b:
        return b+m+2, int(a==m)+int(c==m)
    if b==0: return 1,2
    return b+1,2+int(a==b)+int(c==b)

all_checked=0
for n in range(2,47):
    qcounts=Counter()
    for a in range(n-1):
        for b in range(n-1-a):
            c=n-a-b-2
            w='0'*a+'1'+'0'*b+'1'+'0'*c
            got=direct(w); expected=formula(a,b,c)
            assert got==expected,(n,a,b,c,got,expected)
            qcounts[got[1]]+=1
            all_checked+=1
    assert sum(qcounts.values())==comb(n,2)
    if n in (2,3,4,5,10,20,30,40,46):
        print('n=',n,'Q-multiplicities=',dict(sorted(qcounts.items())))
print('PASS: raw-string suffix KMP exhaustive',all_checked,'two-one words across n=2..46')

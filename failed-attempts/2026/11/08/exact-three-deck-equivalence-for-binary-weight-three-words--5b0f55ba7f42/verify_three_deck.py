#!/usr/bin/env python3
"""Independent finite checks for ternary-gap classification of binary weight-three 3-decks.
Scientific content only: direct subsequence dynamic programming and independent gap formula.
"""
from collections import defaultdict
from itertools import combinations
from math import comb
import sys

def signature(word):
    # All patterns of length at most 3, lexicographic binary order.
    counts={"": 1}
    for ch in word:
        old=counts.copy()
        for pat,num in old.items():
            if len(pat)<3:
                counts[pat+ch]=counts.get(pat+ch,0)+num
    return tuple(counts.get(format(i, f'0{r}b'),0) for r in (1,2,3) for i in range(1<<r))

def pair_formula(n):
    total=0
    for d in range(1,(n-3)//4+1):
        m=n-3-4*d
        for z in range(m//2+1):
            total+=m-2*z+1
    return total

def word_from_gap(g):
    x,y,z,t=g
    return '0'*x+'1'+'0'*y+'1'+'0'*z+'1'+'0'*t

def partner(g):
    x,y,z,t=g
    if (y-z)%3: return None
    d=(y-z)//3
    if d==0:return None
    h=(x+d,z,y,t-d)
    if min(h)<0:return None
    return h

def check(upto=30):
    checked_words=0
    checked_pairs=0
    for n in range(3,upto+1):
        bysig=defaultdict(list)
        for ps in combinations(range(n),3):
            arr=['0']*n
            for p in ps: arr[p]='1'
            s=''.join(arr)
            bysig[signature(s)].append(s)
            checked_words+=1
        observed_pairs=0
        for members in bysig.values():
            assert len(members)<=2,(n,members)
            if len(members)==2:
                observed_pairs+=1
                g=[]
                for s in members:
                    a,b,c=s.index('1'),s.index('1',s.index('1')+1),s.rindex('1')
                    g.append((a,b-a-1,c-b-1,n-c-1))
                assert partner(g[0])==g[1] and partner(g[1])==g[0],(n,g)
        expected=pair_formula(n)
        assert observed_pairs==expected,(n,observed_pairs,expected)
        assert len(bysig)==comb(n,3)-expected,(n,len(bysig),expected)
        checked_pairs+=observed_pairs
    print(f'VERIFY_OK n=3..{upto} words={checked_words} pairs={checked_pairs}')

if __name__=='__main__':
    check(int(sys.argv[1]) if len(sys.argv)>1 else 30)

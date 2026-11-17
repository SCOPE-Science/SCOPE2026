#!/usr/bin/env python3
"""Reproducibility checks for scattered-palindrome spectrum in cyclic words."""
from collections import Counter
from itertools import product
from math import comb

def predicted(q,n,l):
    r = l//2
    if l % 2:
        upper=r
    else:
        if r==0:return 0
        upper=r-1
    return sum(comb(upper,e)*(q-1)**(upper-e)
               for a in range(q) for e in range(upper+1)
               if a+1+q*(r+e)<=n)

def brute_profile(q,n):
    word=tuple(i%q for i in range(n))
    allsub={tuple()}
    for sym in word:
        # Independently enumerate distinct subsequences without palindrome assumptions.
        allsub |= {v+(sym,) for v in tuple(allsub)}
    result=Counter(len(v) for v in allsub if v and v==v[::-1])
    return {i:result.get(i,0) for i in range(1,n+1)}

def check_greedy(q,depth=9):
    tests=0
    for l in range(1,depth+1):
        for u in product(range(q),repeat=(l+1)//2):
            pal=u+((u[:-1] if l%2 else u)[::-1])
            pos=-1
            for sym in pal:
                pos+=1
                while pos%q!=sym:pos+=1
            last=pos+1
            r=l//2
            first_half=pal[:r+1] if l%2 else pal[:r]
            e=sum(first_half[i]==first_half[i+1] for i in range(len(first_half)-1))
            expected=pal[0]+1+q*(r+e)
            assert last==expected,(q,pal,last,expected)
            tests+=1
    return tests

if __name__ == '__main__':
    tests=0
    for q,nmax in [(2,17),(3,15),(4,13),(5,11)]:
        for n in range(1,nmax+1):
            actual=brute_profile(q,n)
            expected={l:predicted(q,n,l) for l in range(1,n+1)}
            assert actual==expected,(q,n,actual,expected)
            tests+=n
    greedy=sum(check_greedy(q,8 if q<=4 else 7) for q in [2,3,4,5])
    print('PASS independent full subsequence-set profiles: 56 host prefixes and',tests,'individual length cells')
    print('PASS independent per-palindrome greedy embedding minima:',greedy,'palindromes')
    for q in (3,4,5):
        for n in (q,2*q,3*q):
            print('sample',q,n,sum(predicted(q,n,l) for l in range(1,n+1)))

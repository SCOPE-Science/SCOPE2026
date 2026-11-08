#!/usr/bin/env python3
"""Finite independent checks of a periodic binary palindrome-pair spectrum.
No external dependencies. Enumeration supplements, but does not replace, the proof.
"""
from collections import Counter

def palindrome_lengths(w):
    n=len(w)
    pal=[[False]*n for _ in range(n)]
    for i in range(n):pal[i][i]=True
    for length in range(2,n+1):
        for i in range(n-length+1):
            j=i+length-1
            pal[i][j]=(w[i]==w[j] and (length<=2 or pal[i+1][j-1]))
    dp=[0]+[n+1]*n
    for j in range(1,n+1):
        for i in range(j):
            if pal[i][j-1]:dp[j]=min(dp[j],dp[i]+1)
    return dp[-1]

def expected(a,b,n):
    L=a+b
    if n<L+2:return 0
    r=n%L
    return 2*sum(i+j==r for i in range(1,a) for j in range(1,b))

def phase_is_three(a,b,start,n):
    L=a+b
    if n<L+2:return False
    end=(start+n)%L
    if start<a:
        return start>0 and a<end<L
    return start>a and 0<end<a

def run():
    configs=phase_tests=words=0
    for a in range(1,10):
      for b in range(1,10):
        L=a+b
        cycle='0'*a+'1'*b
        infinite=cycle*7
        for n in range(1,4*L+1):
            factors=[infinite[s:s+n] for s in range(L)]
            actual=[palindrome_lengths(w) for w in factors]
            c3=actual.count(3)
            assert all(1<=x<=3 for x in actual),(a,b,n,actual)
            assert c3==expected(a,b,n),(a,b,n,c3,expected(a,b,n))
            for s in range(L):
                assert (actual[s]==3)==phase_is_three(a,b,s,n),(a,b,n,s,factors[s],actual[s]);phase_tests+=1
            if n>=L:assert len(set(factors))==L,(a,b,n)
            configs+=1;words+=L
    print('PASS: %s parameters-and-length cases; %s phase equivalences; %s brute-force words' %(configs,phase_tests,words))

if __name__=='__main__':run()

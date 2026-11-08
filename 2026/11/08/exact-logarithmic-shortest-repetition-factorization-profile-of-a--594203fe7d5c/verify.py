#!/usr/bin/env python3
"""Finite checks for the logarithmic run-width theorem; no infinite certification."""
from functools import lru_cache

def letter(n):
    return ((n + 1).bit_length() - 1) & 1

def is_repetition(x):
    m=len(x)
    for p in range(1,m//2+1):
        if all(x[j]==x[j+p] for j in range(m-p)):
            return True
    return False

def exact_width(x):
    m=len(x)
    best=[m+1]*(m+1)
    best[0]=0
    for j in range(1,m+1):
        for i in range(j-1):
            if best[i]<m+1 and is_repetition(x[i:j]):
                best[j]=min(best[j],best[i]+1)
    return 0 if best[-1]>m else best[-1]

def run_width(x):
    runs=[]
    for v in x:
        if not runs or runs[-1][0]!=v:
            runs.append([v,1])
        else:
            runs[-1][1]+=1
    return len(runs) if all(t>=2 for _,t in runs) else 0

def witness(L):
    k=L.bit_length()-1
    if k==1:
        j=(L-1).bit_length()
        return 2**j-1, L
    for j in (1,2):
        middle=sum(1<<h for h in range(j+1,j+k-1))
        r=L-middle
        left=max(2,r-(1<<(j+k-1)))
        right=r-left
        if left <= (1<<j) and 2<=right <= (1<<(j+k-1)):
            start=(1<<j)-1 + (1<<j)-left
            return start,L
    raise AssertionError((L,k))

def main():
    N=4096
    w=''.join(str(letter(i)) for i in range(N))
    assert w.startswith('0'+'1'*2+'0'*4+'1'*8+'0'*16)
    checks=0
    # Direct square check independent of the factorization-width DP.
    for start in range(320):
        for p in range(1,81):
            q=w[start:start+p]
            if q==w[start+p:start+2*p]:
                assert len(set(q))==1,(start,p,q)
            checks+=1
    # Independent O(n^3) dynamic programming for every small factor.
    for start in range(120):
        for L in range(2,39):
            s=w[start:start+L]
            actual=exact_width(s)
            expected=run_width(s)
            assert actual==expected,(start,L,s,actual,expected)
            assert actual <= (L.bit_length()-1)
            checks+=1
    # All exact-length witnesses from the geometric-run construction.
    for L in range(2,1025):
        start,_=witness(L)
        s=w[start:start+L]
        assert len(s)==L
        assert run_width(s)==L.bit_length()-1,(L,start,s[:30])
        checks+=1
    print('VERIFY_OK checks=',checks,'max_length=',1024,'dp_factors=',120*37)

if __name__=='__main__': main()

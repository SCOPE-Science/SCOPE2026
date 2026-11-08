#!/usr/bin/env python3
"""Finite exact checks for block-sum dynamics; analytical statements need the accompanying proof."""
from fractions import Fraction
from itertools import islice

def levels(T):
    s = []
    for t in range(T):
        # exact integer realization: greatest power of two <= log_2(t+4)
        k = (t+4).bit_length()-1
        size=1 << (k.bit_length()-1)
        s.append(size)
    N=[0]
    for v in s:N.append(N[-1]+v)
    return s,N

def phi(j,s,N):
    lo,hi=0,len(s)-2
    while lo<=hi:
        m=(lo+hi)//2
        if N[m]<=j<N[m+1]:
            return N[m+1]+(s[m+1]//s[m])*(j-N[m])
        if j<N[m]:hi=m-1
        else:lo=m+1
    raise ValueError(j)

def checks():
    T=3000
    s,N=levels(T)
    assert s[0]==2 and max(s)<=16
    assert all(s[k+1]//s[k] in (1,2) and s[k+1]%s[k]==0 for k in range(T-1))
    assert all(phi(j+1,s,N)-phi(j,s,N) in (1,2) for j in range(N[260]))
    assert phi(0,s,N)==2
    tests=0
    for t in range(1,120):
        for u in range(s[t]):
            j=N[t]+u
            for n in range(0,12):
                actual=j
                for _ in range(n):actual=phi(actual,s,N)
                expected=N[t+n]+s[t+n]//s[t]*u
                assert actual==expected, (j,n,actual,expected)
                tests+=1
    for n in range(1,150):
        x0=N[n]+1
        x1=N[n]+s[n]//2
        j=1
        for _ in range(n):j=phi(j,s,N)
        assert j==x1
        j=0
        for _ in range(n):j=phi(j,s,N)
        assert j==x0-1
        assert x0<=x1<N[n+1]
        assert s[n]//2<=(n+4).bit_length()
        tests+=6
    # Repeat finite block sum identity on exact rational vectors
    for n in range(1,10):
        for width in range(1,8):
            Y=[Fraction(j-2,7) for j in range(width)]
            output=[]
            # y supported in [0,width); inverse spread into intervals of phi^n
            bounds=[-1]
            for j in range(width):
                b=j
                for _ in range(n): b=phi(b,s,N)
                bounds.append(b)
            spread=[Fraction(0) for _ in range(bounds[-1]+1)]
            for j,y in enumerate(Y):
                aa=bounds[j]+1
                bb=bounds[j+1]+1
                for k in range(aa,bb):spread[k]=y/(bb-aa)
            for j in range(width):
                output.append(sum(spread[bounds[j]+1:bounds[j+1]+1],Fraction(0)))
            assert output==Y
            tests+=len(Y)
    print('PASS exact finite assertions:',tests,'(+ exhaustive adjacent-step checks)')
if __name__=='__main__':checks()

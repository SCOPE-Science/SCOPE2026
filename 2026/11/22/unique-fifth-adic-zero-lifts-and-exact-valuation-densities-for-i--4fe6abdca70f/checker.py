#!/usr/bin/env python3
"""Exact finite regression checks for the fifth-adic involution valuation theorem.
The mathematical proof, not these finite checks, establishes all powers.
"""
from collections import Counter

def involutions_mod(count, modulus):
    out=[1, 1]
    for n in range(2,count):
        out.append((out[-1]+(n-1)*out[-2])%modulus)
    return out[:count]

def v5(n):
    if n==0: return None
    r=0
    while n%5==0:
        n//=5;r+=1
    return r

def main():
    assertions=0
    q=5**7
    N=3*5**6+100
    a=involutions_mod(N,q)
    for k in range(1,7):
        period=5**k
        mod=period
        for n in range(N-period):
            assert (a[n+period]-a[n])%mod==0
            assertions+=1
        zero=[i for i in range(period) if a[i]%mod==0]
        assert len(zero)==1 and zero[0]%5==4
        assertions+=1
        for n in range(4,period,5):
            assert a[n]%5==0
            assertions+=1
        # Nonzero 5-adic targets in the regular image branch have unique indices.
        images=[a[n]%mod for n in range(4,period,5)]
        assert len(set(images))==5**(k-1)
        assert set(images)==set(range(0,mod,5))
        assertions+=2
        print('k=',k,'zero index=',zero[0], 'regular target count=',len(images))
    for r in range(1,6):
        h=5**r
        for n in range(0,500):
            diff=a[n+h]-a[n]
            assert diff%h==0
            c=((a[h]-a[0])//h)%5
            t,j=divmod(n,5)
            expected=((c-t)*[1,1,2,4,0][j]+[0,0,1,2,2][j])%5
            assert (diff//h)%5==expected
            assertions+=2
            if j==4:
                assert (diff//h)%5==2
                assertions+=1
    branches=list(range(4,700,5))
    for i,n in enumerate(branches):
        for m in branches[i+1:]:
            diff=a[n]-a[m]
            assert diff!=0
            assert v5(diff)==v5(m-n)
            assertions+=1
    print('PASS',assertions,'finite exact assertions')

if __name__=='__main__':main()

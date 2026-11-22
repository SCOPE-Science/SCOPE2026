#!/usr/bin/env python3
"""Exact finite checks for the open-chord cut profile in uniform pairings.

These tests are finite consistency checks, not a proof of the asymptotic limit.
Uses only the Python standard library.
"""
from fractions import Fraction
from functools import lru_cache
from collections import Counter

@lru_cache(None)
def matchings(items):
    if not items:
        return ((),)
    a=items[0]; result=[]
    for j in range(1,len(items)):
        b=items[j]
        for rest in matchings(items[1:j]+items[j+1:]):
            result.append(((a,b),)+rest)
    return tuple(result)

def profile(matching, m):
    h=[0]*(m+1)
    for a,b in matching:
        for k in range(a,b): h[k]+=1
    return tuple(h)

def check():
    tests=0
    for n in range(2,7):
        m=2*n
        table=Counter(profile(x,m) for x in matchings(tuple(range(1,m+1))))
        N=sum(table.values())
        assert N==__import__('math').prod(range(1,m,2));tests+=1
        for k in range(m+1):
            mu=Fraction(k*(m-k),m-1)
            empirical=sum(Fraction(freq*h[k],N) for h,freq in table.items())
            assert empirical==mu,(n,k,'mean',empirical,mu);tests+=1
        for k in range(2,m-1):
            var=Fraction(2*k*(k-1)*(m-k)*(m-k-1),(m-3)*(m-1)**2)
            emp=sum(Fraction(freq,N)*(h[k]-Fraction(k*(m-k),m-1))**2 for h,freq in table.items())
            assert emp==var,(n,k,'variance',emp,var);tests+=1
        for k in range(m):
            tally=Counter();down=Counter()
            for h,frequency in table.items():
                tally[h[k]]+=frequency
                if h[k+1]==h[k]-1:down[h[k]]+=frequency
                else:assert h[k+1]==h[k]+1
            for level,qty in tally.items():
                assert Fraction(down[level],qty)==Fraction(level,m-k),(n,k,level)
                tests+=1
        for k in range(m+1):
            assert all(h[k]%2==k%2 for h in table);tests+=1
    print('exact assertions passed:',tests)
    print('max enumerated size: 12 endpoints; 10,395 matchings')

if __name__=='__main__':check()

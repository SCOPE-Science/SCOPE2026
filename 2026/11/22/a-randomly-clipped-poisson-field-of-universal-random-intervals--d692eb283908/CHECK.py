"""Finite combinatorial and numerical checks for the universal-interval limit theorem."""
from __future__ import annotations
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from math import factorial, pi, gamma, exp, sqrt
import random

@lru_cache(None)
def matchings(items):
    if not items:
        return ((),)
    a=items[0]
    out=[]
    for j in range(1,len(items)):
        b=items[j]
        rest=items[1:j]+items[j+1:]
        for z in matchings(rest):
            out.append(((a,b),)+z)
    return tuple(out)

def count_universal(intervals):
    q=min(b for a,b in intervals)
    p=max(a for a,b in intervals)
    k=sum(a<=q and b>=p for a,b in intervals)
    brute=sum(all(a<=s and b>=r for j,(r,s) in enumerate(intervals) if j!=i)
              for i,(a,b) in enumerate(intervals))
    assert k==brute
    return k

def limiting_p(k):
    return Fraction(2**(k+1)*(k+1)*factorial(k+1)**2,factorial(2*k+3))

def main():
    checks=0
    for n in range(2,7):
        ct=Counter(count_universal(m) for m in matchings(tuple(range(2*n))))
        total=sum(ct.values())
        assert total == factorial(2*n)//(2**n*factorial(n)); checks+=1
        assert Fraction(total-ct[0],total)==Fraction(2,3);checks+=1
        assert sum(Fraction(v,total) for v in ct.values()) == 1;checks+=1
        print('n',n,'finite law', [(j,str(Fraction(ct[j],total))) for j in sorted(ct)])
    vals=[float(limiting_p(k)) for k in range(100)]
    assert abs(sum(vals)-1)<2e-14;checks+=1
    mean=sum(k*v for k,v in enumerate(vals))
    assert abs(mean-pi/2)<2e-13;checks+=1
    assert limiting_p(0)==Fraction(1,3);checks+=1
    assert limiting_p(1)==Fraction(4,15);checks+=1
    assert limiting_p(2)==Fraction(6,35);checks+=1
    r=random.Random(17341)
    for n,reps in [(120,20000),(700,14000)]:
        ct=Counter()
        mark_sum_x=mark_sum_y=mark_count=0
        for _ in range(reps):
            intervals=[tuple(sorted((r.random(),r.random()))) for _ in range(n)]
            # O(n) exact geometry via the two global boundaries.
            q=min(b for a,b in intervals)
            p=max(a for a,b in intervals)
            marks=[(a,b) for a,b in intervals if a<=q and b>=p]
            ct[len(marks)] += 1
            for a,b in marks:
                mark_sum_x += a/q
                mark_sum_y += (1-b)/(1-p)
                mark_count += 1
        p0=ct[0]/reps
        mu=sum(k*v for k,v in ct.items())/reps
        assert abs(p0-1/3)<.025;checks+=1
        assert abs(mu-pi/2)<.13;checks+=1
        assert abs(mark_sum_x/mark_count-.5)<.035;checks+=1
        assert abs(mark_sum_y/mark_count-.5)<.035;checks+=1
        print('sample n',n,'P0',p0,'mean',mu,'normalized mean marks',(mark_sum_x/mark_count,mark_sum_y/mark_count))
    print('PASS', checks, 'structural assertions with finite exhaustive enumerations and seeded simulations')
if __name__=='__main__': main()

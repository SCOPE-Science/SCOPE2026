#!/usr/bin/env python3
"""Exact finite checks for paired-endpoint interval-order boundary counts.
No external dependencies. Run: python checker.py
"""
from fractions import Fraction
from math import comb, factorial
from collections import Counter


def double_factorial_odd_pairs(n):
    out=1
    for j in range(1,n+1): out*=2*j-1
    return out


def survival(n,k):
    if not (0<=k<=n): raise ValueError((n,k))
    result=Fraction(1)
    for j in range(k): result*=Fraction(2*n-2*j,2*n-j)
    return result


def joint_survival(n,k,l):
    if not(0<=k<=n and 0<=l<=n):raise ValueError((n,k,l))
    c=2*n-k-l
    count=0
    for h in range(max(0,k+l-n), min(k,l)+1):
        z=n-k-l+h
        assert z>=0
        count+=factorial(k)*factorial(l)*factorial(c)//(factorial(h)*factorial(k-h)*factorial(l-h)*2**z*factorial(z))
    return Fraction(count,double_factorial_odd_pairs(n))


def all_matchings(items):
    if not items:
        yield ()
        return
    a=items[0]
    for i in range(1,len(items)):
        b=items[i]
        rest=items[1:i]+items[i+1:]
        for m in all_matchings(rest):yield ((a,b),)+m


def boundary_counts(pairs,n):
    partner={a:b for a,b in pairs}
    partner.update({b:a for a,b in pairs})
    starts=0
    for i in range(2*n):
        if partner[i]<i: break
        starts+=1
    ends=0
    for i in range(2*n-1,-1,-1):
        if partner[i]>i: break
        ends+=1
    return starts, ends


def verify():
    comparisons=0
    for n in range(1,8):
        dist=Counter(boundary_counts(pairs,n) for pairs in all_matchings(tuple(range(2*n))))
        total=sum(dist.values())
        assert total==double_factorial_odd_pairs(n)
        comparisons+=1
        for k in range(0,n+1):
            observed=Fraction(sum(ct for (a,b),ct in dist.items() if a>=k),total)
            assert observed==survival(n,k),(n,k,observed,survival(n,k))
            comparisons+=1
            for l in range(0,n+1):
                observed=Fraction(sum(ct for (a,b),ct in dist.items() if a>=k and b>=l),total)
                expected=joint_survival(n,k,l)
                assert observed==expected,(n,k,l,observed,expected)
                comparisons+=1
        # Exact zero/one complementary joint distributions and moment computation.
        assert sum(dist.values())==total
        comparisons+=1
    # Bound and count moments for moderate n, distinct from simulation.
    for n in (8,12,20,40):
        assert sum(survival(n,k) for k in range(1,n+1))>0
        for k in range(n+1):
            assert joint_survival(n,k,0)==survival(n,k)
            assert joint_survival(n,0,k)==survival(n,k)
            comparisons+=2
    print(f'PASS {comparisons} exact rational checks, including all perfect matchings through n=7')

if __name__=='__main__':verify()

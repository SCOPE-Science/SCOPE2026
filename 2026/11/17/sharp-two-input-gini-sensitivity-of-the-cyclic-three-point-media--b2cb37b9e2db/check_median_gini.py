#!/usr/bin/env python3
"""Exact finite verification of the cyclic three-point median Gini modulus."""
from fractions import Fraction
from itertools import permutations

def expected(n):
    if n == 3:
        return Fraction(0)
    if n == 4:
        return Fraction(4, 3)
    return Fraction(3*(n-3), n-1)

def median_selector(x):
    n=len(x)
    return tuple(sorted(((i-1)%n,i,(i+1)%n),key=lambda j:x[j])[1] for i in range(n))

def selector_norm(s):
    n=len(s)
    c=[s.count(i) for i in range(n)]
    best=Fraction(0)
    for mask in range(1,(1<<n)-1):
        k=mask.bit_count()
        t=sum(c[j] for j in range(n) if mask & (1<<j))
        best=max(best,Fraction(t*(n-t),k*(n-k)))
    return best

def cyclic_median(x):
    n=len(x)
    return tuple(sorted((x[(i-1)%n],x[i],x[(i+1)%n]))[1] for i in range(n))

def gini(x):
    return sum(abs(x[i]-x[j]) for i in range(len(x)) for j in range(i+1,len(x)))

if __name__=='__main__':
    perms=0
    for n in range(3,9):
        best=Fraction(0)
        for x in permutations(range(n)):
            best=max(best,selector_norm(median_selector(x)))
            perms+=1
        assert best==expected(n),(n,best,expected(n))
        print('EXHAUSTIVE_STRICT_ORDER_AND_ALL_BINARY_CUTS_PASSED',n,str(best))
    print('EXHAUSTIVE_PERMUTATIONS_TOTAL',perms)
    for n in range(4,111):
        if n==4:
            x=[1,0,2,3]
        else:
            x=[5]*n
            x[0]=1;x[1]=-1;x[2]=3;x[-1]=2;x[-2]=-2
            for j in range(3,n-2): x[j]=10+j
        # All x entries distinct in the decisive three windows.
        eps=Fraction(1,100)
        xx=[Fraction(a) for a in x]
        yy=xx.copy();yy[0]+=eps
        rx=cyclic_median(xx);ry=cyclic_median(yy)
        d=[ry[i]-rx[i] for i in range(n)]
        ratio=Fraction(gini(d),gini([yy[i]-xx[i] for i in range(n)]))
        assert ratio==expected(n),(n,ratio,expected(n))
    print('EXPLICIT_TWO_INPUT_SHARP_WITNESSES_PASSED_4_TO_110')
    for n in range(5,101):
        bound=expected(n)
        for k in range(1,n):
            lo=max(0,n-3*(n-k))
            hi=min(n,3*k)
            for t in range(lo,hi+1):
                assert Fraction(t*(n-t),k*(n-k))<=bound,(n,k,t)
    print('EXACT_CAPACITY_CUT_BOUND_PASSED_5_TO_100')
    print('ALL_MEDIAN_GINI_CHECKS_PASSED')
